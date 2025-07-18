# Quickstart Guide

## Requirements

When you create a project, you are asked if you want to use [poetry] or [uv] as a
dependency manager tool. You only need to install one of them.

Install [pipx]:

```console
python -m pip install --user pipx
python -m pipx ensurepath
```

Install [cruft]:

```console
pipx install cruft[pyproject]
```

Install [Nox]:

```console
pipx install nox
```

Install [Poetry] and [nox-poetry]:

```console
pipx install poetry
pipx inject poetry poetry-plugin-export
pipx inject nox nox-poetry
```

Install [uv]:

```console
pipx install uv
```

[pipx] is preferred, but you can also install with `pip install --user`.

It is recommended to set up Python 3.11, 3.12 and 3.13 using [pyenv].

## Creating a project

Generate a Python project:

```console
cruft create https://github.com/statisticsnorway/ssb-pypitemplate.git --checkout=2025.7.18
```

Cruft downloads the template and asks you a series of questions about project variables.
Further details can be found in the [Creating a project] section of the user guide.

Change to the root directory of your new project,
and create a Git repository:

```console
git init
git add .
git commit
```

### Install the environment and create a lock-file

Install the virtual environment using the command:

If using [poetry]:

```console
poetry update
git add poetry.lock
git commit
```

If using [uv]:

```console
uv sync
git add uv.lock
git commit
```

## Testing

Run the full test suite:

```console
nox
```

List the available Nox sessions:

```console
nox --list-sessions
```

Install the pre-commit hooks:

```console
nox -s pre-commit -- install
```

If you want to run the tests with a non-default python version:

```console
nox --force-python 3.11
```

## Continuous Integration

### GitHub

1. Sign up at [GitHub].
2. Create an empty repository for your project.
3. Follow the instructions to push an existing repository from the command line.

### PyPI

1. Sign up at [PyPI].
2. Go to the Account Settings on PyPI, select Publishing,
   and set up a new pending publisher as described on
   [Creating a PyPI Project with a Trusted Publisher][trusted publisher].
3. Use the following information for the new pending publisher:
   - PyPI Project name: Name of the GitHub repo.
   - Owner: GitHub organization name or GitHub username that owns the repository.
   - Repository name: Name of the GitHub repo.
   - Workflow name: `release.yml`
   - Environment: Leave empty.

### TestPyPI

1. Sign up at [TestPyPI].
2. Go to the Account Settings on TestPyPI, select Publishing,
   and set up a new pending publisher as described on
   [Creating a PyPI Project with a Trusted Publisher][trusted publisher].
3. Use the following information for the new pending publisher:
   - PyPI Project name: Name of the GitHub repo.
   - Owner: GitHub organization name or GitHub username that owns the repository.
   - Repository name: Name of the GitHub repo.
   - Workflow name: `release.yml`
   - Environment: Leave empty.

### GitHub Pages

1. Log in to [GitHub].
2. Select Settings, Pages and set Source to "GitHub Actions" below the
   Build and Deployment heading.

[GitHub Pages] should then work out of the box. The pages are deployed to<br>
`<github username>.github.io/<repo name>` or <br>
`<github organization>.github.io/<repo name>`.

### SonarCloud

1. Log in to [SonarCloud] with your GitHub account.
2. Click the plus-sign at upper right and select _Analyze new project_,
   select your organization and the new repo to analyze, and then click
   the _Set Up_ button.
3. Set _new code_ to be based on _Number of days_ and 60 days (suggestion).
   And then click the _Create project_ button.
4. Select _Administration_, _Analysis Method_ and choose method: _With GitHub Actions_.
5. Follow the description to add a GitHub repository secret for the `SONAR_TOKEN`.
6. That's it. The next time a pull request is opened or a branch or merged to main
   on GitHub, the code will be analysed by SonarCloud.

## Releasing

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using [poetry version].
3. Commit and push to GitHub.
4. Open a pull request.
5. Merge the pull request.

The Release workflow performs the following automated steps:

- Build and upload the package to PyPI.
- Apply a version tag to the repository.
- Publish a GitHub Release.

Release notes are populated with the titles and authors of merged pull requests.
You can group the pull requests into separate sections
by applying labels to them, like this:

<!-- table-release-drafter-sections-begin -->

| Pull Request Label | Section in Release Notes     |
| ------------------ | ---------------------------- |
| `breaking`         | 💥 Breaking Changes          |
| `enhancement`      | 🚀 Features                  |
| `removal`          | 🔥 Removals and Deprecations |
| `bug`              | 🐞 Fixes                     |
| `performance`      | 🐎 Performance               |
| `testing`          | 🚨 Testing                   |
| `ci`               | 👷 Continuous Integration    |
| `documentation`    | 📚 Documentation             |
| `refactoring`      | 🔨 Refactoring               |
| `style`            | 💄 Style                     |
| `dependencies`     | 📦 Dependencies              |

<!-- table-release-drafter-sections-end -->

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[creating a project]: https://statisticsnorway.github.io/ssb-pypitemplate/guide.html#creating-a-project
[cruft]: https://cruft.github.io/cruft/
[github]: https://github.com/
[github pages]: https://docs.github.com/en/pages
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/
[pipx]: https://pipx.pypa.io/
[poetry]: https://python-poetry.org/
[poetry version]: https://python-poetry.org/docs/cli/#version
[pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.org/
[sonarcloud]: https://www.sonarsource.com/products/sonarcloud/
[testpypi]: https://test.pypi.org/
[trusted publisher]: https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/
[uv]: https://docs.astral.sh/uv/
