"""Nox sessions."""

import os
import shlex
import shutil
import sys
from pathlib import Path
import tempfile
from textwrap import dedent
from typing import Iterable

import nox
{% if cookiecutter.dependency_manager_tool == "poetry" %}


try:
    from nox_poetry import Session
    from nox_poetry import session
except ImportError:
    message = f"""\
    Nox failed to import the 'nox-poetry' package.

    Please install it using the following command:

    {sys.executable} -m pip install nox-poetry"""
    raise SystemExit(dedent(message)) from None
{% else %}
from nox import Session

{% endif %}

package = "{{cookiecutter.package_name}}"
python_versions = ["3.11", "3.12", "3.13"]
python_versions_for_test = python_versions + ["3.10"]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "pre-commit",
    "mypy",
    "tests",
    "typeguard",
    "xdoctest",
    "docs-build",
)
{% if cookiecutter.dependency_manager_tool == "poetry" %}


def install_poetry_groups(session, groups: Iterable[str]) -> None:
    """Install dependencies from poetry groups.

    This is as workaround until this PR is merged in:
    https://github.com/cjolowicz/nox-poetry/pull/1080
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            *[f"--only={group}" for group in groups],
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )

        session.install("-r", requirements.name)
{% else %}
nox.options.default_venv_backend = "uv"
session = nox.session


def install_with_uv(
    session: Session,
    *,
    all_extras: bool = False,
    locked: bool = True,
    only_groups: None | Iterable[str] = None,
) -> None:
    """Install packages using uv, pinned to uv.lock."""
    cmd = ["uv", "sync"]
    if locked:
        cmd.append("--locked")
    if all_extras:
        cmd.append("--all-extras")
    if only_groups:
        for group in only_groups:
            cmd.extend(["--only-group", group])

    cmd.append(
        f"--python={session.virtualenv.location}"
    )  # Target the nox venv's Python interpreter
    session.run_install(
        *cmd, env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
    )
{% endif %}


def activate_virtualenv_in_precommit_hooks(session: Session) -> None:
    """Activate virtualenv in hooks installed by pre-commit.

    This function patches git hooks installed by pre-commit to activate the
    session's virtual environment. This allows pre-commit to locate hooks in
    that environment when invoked from git.

    Args:
        session: The Session object.
    """
    assert session.bin is not None  # nosec

    # Only patch hooks containing a reference to this session's bindir. Support
    # quoting rules for Python and bash, but strip the outermost quotes so we
    # can detect paths within the bindir, like <bindir>/python.
    bindirs = [
        bindir[1:-1] if bindir[0] in "'\"" else bindir
        for bindir in (repr(session.bin), shlex.quote(session.bin))
    ]

    virtualenv = session.env.get("VIRTUAL_ENV")
    if virtualenv is None:
        return

    headers = {
        # pre-commit < 2.16.0
        "python": f"""\
            import os
            os.environ["VIRTUAL_ENV"] = {virtualenv!r}
            os.environ["PATH"] = os.pathsep.join((
                {session.bin!r},
                os.environ.get("PATH", ""),
            ))
            """,
        # pre-commit >= 2.16.0
        "bash": f"""\
            VIRTUAL_ENV={shlex.quote(virtualenv)}
            PATH={shlex.quote(session.bin)}"{os.pathsep}$PATH"
            """,
        # pre-commit >= 2.17.0 on Windows forces sh shebang
        "/bin/sh": f"""\
            VIRTUAL_ENV={shlex.quote(virtualenv)}
            PATH={shlex.quote(session.bin)}"{os.pathsep}$PATH"
            """,
    }

    hookdir = Path(".git") / "hooks"
    if not hookdir.is_dir():
        return

    for hook in hookdir.iterdir():
        if hook.name.endswith(".sample") or not hook.is_file():
            continue

        if not hook.read_bytes().startswith(b"#!"):
            continue

        text = hook.read_text()

        if not is_bindir_in_text(bindirs, text):
            continue

        lines = text.splitlines()
        hook.write_text(insert_header_in_hook(headers, lines))


def is_bindir_in_text(bindirs: list[str], text: str) -> bool:
    """Helper function to check if bindir is in text."""
    return any(
        Path("A") == Path("a") and bindir.lower() in text.lower() or bindir in text
        for bindir in bindirs
    )


def insert_header_in_hook(header: dict[str, str], lines: list[str]) -> str:
    """Helper function to insert headers in hook's text."""
    for executable, header_text in header.items():
        if executable in lines[0].lower():
            lines.insert(1, dedent(header_text))
            return "\n".join(lines)
    return "\n".join(lines)


@session(name="pre-commit", python=python_versions[0])
def precommit(session: Session) -> None:
    """Lint using pre-commit."""
    args = session.posargs or [
        "run",
        "--all-files",
        "--hook-stage=manual",
        "--show-diff-on-failure",
    ]
{% if cookiecutter.dependency_manager_tool == "poetry" %}
    session.poetry.installroot()
    install_poetry_groups(session, ("dev", "pre-commit"))
{% else %}
    install_with_uv(session, ("dev", "pre-commit"))
{% endif %}
    session.run("pre-commit", *args)
    if args and args[0] == "install":
        activate_virtualenv_in_precommit_hooks(session)


@session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or ["src", "tests"]
{% if cookiecutter.dependency_manager_tool == "poetry" %}
    session.poetry.installroot()
    install_poetry_groups(session, ("dev", "type-stubs"))
{% else %}
    install_with_uv(session, ("dev", "type-stubs"))
{% endif %}
    session.run("mypy", *args)
    if not session.posargs:
        session.run("mypy", f"--python-executable={sys.executable}", "noxfile.py")


@session(python=python_versions_for_test)
def tests(session: Session) -> None:
    """Run the test suite."""
{% if cookiecutter.dependency_manager_tool == "poetry" %}
    session.poetry.installroot()
    install_poetry_groups(session, ("dev",))
{% else %}
    install_with_uv(session)
{% endif %}
    try:
        session.run(
            "coverage",
            "run",
            "--parallel",
            "-m",
            "pytest",
            "-o",
            "pythonpath=",
            *session.posargs,
        )
    finally:
        if session.interactive:
            session.notify("coverage", posargs=[])


@session(python=python_versions[0])
def coverage(session: Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["report", "--skip-empty"]

{% if cookiecutter.dependency_manager_tool == "poetry" %}
    install_poetry_groups(session, ("dev",))
{% else %}
    install_with_uv(session, only_groups=("dev",))
{% endif %}

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)


@session(python=python_versions[0])
def typeguard(session: Session) -> None:
    """Runtime type checking using Typeguard."""
{% if cookiecutter.dependency_manager_tool == "poetry" %}
    session.poetry.installroot()
    install_poetry_groups(session, ("dev", "type-stubs"))
{% else %}
    install_with_uv(session, only_groups=("dev", "type-stubs"))
{% endif %}
    session.run("pytest", f"--typeguard-packages={package}", *session.posargs)


@session(python=python_versions)
def xdoctest(session: Session) -> None:
    """Run examples with xdoctest."""
    if session.posargs:
        args = [package, *session.posargs]
    else:
        args = [f"--modname={package}", "--command=all"]
        if "FORCE_COLOR" in os.environ:
            args.append("--colored=1")

{% if cookiecutter.dependency_manager_tool == "poetry" %}
    session.poetry.installroot()
    install_poetry_groups(session, ("dev",))
{% else %}
    install_with_uv(session, only_groups=("dev",))
{% endif %}
    session.run("python", "-m", "xdoctest", *args)


@session(name="docs-build", python=python_versions[0])
def docs_build(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    if not session.posargs and "FORCE_COLOR" in os.environ:
        args.insert(0, "--color")

{% if cookiecutter.dependency_manager_tool == "poetry" %}
    install_poetry_groups(session, ("dev", "docs"))
{% else %}
    install_with_uv(session, only_groups=("dev", "docs"))
{% endif %}

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-build", *args)


@session(python=python_versions[0])
def docs(session: Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = session.posargs or ["--open-browser", "docs", "docs/_build"]
{% if cookiecutter.dependency_manager_tool == "poetry" %}
    install_poetry_groups(session, ("dev", "docs"))
{% else %}
    install_with_uv(session, only_groups=("dev", "docs"))
{% endif %}

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-autobuild", *args)
