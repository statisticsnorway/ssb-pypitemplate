# Quickstart Guide

## Requirements

Install [pipx]:

```console
$ python -m pip install --user pipx
$ python -m pipx ensurepath
```

Install [cruft]:

```console
$ pipx install cruft[pyproject]
```

Install [Poetry]:

```console
$ pipx install poetry
```

Install [Nox] and [nox-poetry]:

```console
$ pipx install nox
$ pipx inject nox nox-poetry
```

[pipx] is preferred, but you can also install with `pip install --user`.

It is recommended to set up Python 3.8, 3.9, 3.10 and 3.11 using [pyenv].

## Creating a project

Generate a Python project:

```console
cruft create https://github.com/statisticsnorway/ssb-pypitemplate.git --checkout=2023.2.24
```

Change to the root directory of your new project,
and create a Git repository:

```console
$ git init
$ git add .
$ git commit
```

## Running

Run the command-line interface from the source tree:

```console
$ poetry install
$ poetry run <project>
```

Run an interactive Python session:

```console
$ poetry install
$ poetry run python
```

## Testing

Run the full test suite:

```console
$ nox
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

Install the pre-commit hooks:

```console
$ nox -s pre-commit -- install
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

### Codecov

1. Sign up at [Codecov].
2. Install their GitHub app.

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
4. Choose Analysis Method: _With GitHub Actions_.
5. Follow the description to add a GitHub repository secret for the `SONAR_TOKEN`.
6. That's it. The next time code are pushed to a branch or merged to main on GitHub,
   the code will be analysed by SonarCloud.

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

[codecov]: https://about.codecov.io/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cruft]: https://cruft.github.io/cruft/
[github]: https://github.com/
[github pages]: https://docs.github.com/en/pages
[install-poetry.py]: https://install.python-poetry.org/
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/
[pipx]: https://pypa.github.io/pipx/
[poetry]: https://python-poetry.org/
[poetry version]: https://python-poetry.org/docs/cli/#version
[pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.org/
[read the docs]: https://readthedocs.org/
[sonarcloud]: https://www.sonarsource.com/products/sonarcloud/
[testpypi]: https://test.pypi.org/
[trusted publisher]: https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/
