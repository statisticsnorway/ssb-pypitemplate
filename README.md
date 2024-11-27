# ssb-pypitemplate

<!-- badges-begin -->

[![Status][status badge]][status badge]
[![Python Version][python version badge]][github page]
[![CalVer][calver badge]][calver]
[![License][license badge]][license]<br>
[![Documentation][ghpages badge]][ghpages page]
[![Tests][github actions badge]][github actions page]
[![Coverage][sonarcov badge]][sonar page]<br>
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Black codestyle][black badge]][black project]
[![Ruff][ruff badge]][ruff project]
[![Contributor Covenant][contributor covenant badge]][code of conduct]

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black project]: https://github.com/psf/black
[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff project]: https://github.com/astral-sh/ruff
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[calver]: https://calver.org/
[code of conduct]: https://github.com/statisticsnorway/ssb-pypitemplate/blob/main/CODE_OF_CONDUCT.md
[sonarcov badge]: https://sonarcloud.io/api/project_badges/measure?project=statisticsnorway_ssb-pypitemplate-instance&metric=coverage
[sonar page]: https://sonarcloud.io/summary/overall?id=statisticsnorway_ssb-pypitemplate-instance
[contributor covenant badge]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[github actions badge]: https://github.com/statisticsnorway/ssb-pypitemplate/workflows/Tests/badge.svg
[github actions page]: https://github.com/statisticsnorway/ssb-pypitemplate/actions?workflow=Tests
[github page]: https://github.com/statisticsnorway/ssb-pypitemplate
[license badge]: https://img.shields.io/github/license/statisticsnorway/ssb-pypitemplate
[license]: https://opensource.org/license/mit/
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/pypi/pyversions/ssb-pypitemplate-instance
[ghpages badge]: https://github.com/statisticsnorway/ssb-pypitemplate/actions/workflows/docs.yml/badge.svg
[ghpages page]: https://statisticsnorway.github.io/ssb-pypitemplate/
[status badge]: https://badgen.net/badge/status/stable/4bc51d

<!-- badges-end -->

<p align="center"><img alt="logo" src="docs/_static/ssb_logo.svg" width="50%" /></p>

[Cookiecutter] template for a Python package based on the
[Hypermodern Python] article series.
This repo is a fork of [cookiecutter-hypermodern-python], and adjusted for use
in [Statistics Norway].

✨📚✨ [Read the full documentation][ghpages page]

- [Quickstart]
- [User Guide]

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[cookiecutter-hypermodern-python]: https://github.com/cjolowicz/cookiecutter-hypermodern-python.git
[statistics norway]: https://www.ssb.no/en
[quickstart]: https://statisticsnorway.github.io/ssb-pypitemplate/quickstart.html
[user guide]: https://statisticsnorway.github.io/ssb-pypitemplate/guide.html

## Usage

Use [Cruft] to create and update an instance of this template.

```console
cruft create https://github.com/statisticsnorway/ssb-pypitemplate.git --checkout=2024.11.27
```

Cruft downloads the template, and asks you a series of questions about project variables,
for example, how you wish your project to be named. Further details and a complete list of
project variables with explanation can be found in the [Creating a project] section of the
user guide.

[creating a project]: https://statisticsnorway.github.io/ssb-pypitemplate/guide.html#creating-a-project

### Update

To check if there are there are template updates and update your instance with
the new updates, run the following commands from the root directory:

```console
cruft check
cruft update
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [Poetry]
- Test automation with [Nox]
- Linting with [pre-commit] and [ruff]
- Continuous integration with [GitHub Actions]
- Documentation with [Sphinx], [MyST], and [GitHub Pages] using the [furo] theme
- Automated uploads to [PyPI] and [TestPyPI]
- Automated release notes with [Release Drafter]
- Automated dependency updates with [Dependabot]
- Code formatting with [Black] and [Prettier]
- Import sorting with [ruff]
- Testing with [pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [SonarCloud]
- Command-line interface with [Click]
- Static type-checking with [mypy]
- Runtime type-checking with [Typeguard]
- Automated Python syntax upgrades with [ruff]
- Security audit with [ruff]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc] and [napoleon]
- Generate command-line reference with [sphinx-click]
- Manage project labels with [GitHub Labeler]

The template supports Python 3.10, 3.10 and 3.12.

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[black]: https://github.com/psf/black
[click]: https://click.palletsprojects.com/
[coverage.py]: https://coverage.readthedocs.io/
[cruft]: https://cruft.github.io/cruft/
[dependabot]: https://github.com/dependabot/dependabot-core
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[github pages]: https://pages.github.com/
[isort]: https://pycqa.github.io/isort/
[mypy]: https://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[release drafter]: https://github.com/release-drafter/release-drafter
[ruff]: https://beta.ruff.rs
[sonarcloud]: https://www.sonarsource.com/products/sonarcloud/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest

<!-- features-end -->
