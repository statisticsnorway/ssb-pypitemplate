# SSB PyPI Template

```{toctree}
---
hidden: true
maxdepth: 1
---

Quickstart <quickstart>
guide
contributing
Code of Conduct <codeofconduct>
license
Major changes <changes>
Changelog <https://github.com/statisticsnorway/ssb-pypitemplate/releases>
```

```{include} ../README.md
---
start-after: <!-- badges-begin -->
end-before: <!-- badges-end -->
---
```

[Cookiecutter] template for a Python package
based on the [Hypermodern Python] article series,
and adopted for use in [Statistics Norway].

## Usage

Use [Cruft](https://cruft.github.io/cruft/) to create and update an instance of this template.

```console
cruft create https://github.com/statisticsnorway/ssb-pypitemplate.git --checkout=2023.11.15

# To check if there are there are template updates and update your instance with
# the new updates, run the following commands from the root directory:
cruft check
cruft update
```

## Features

```{include} ../README.md
---
start-after: <!-- features-begin -->
end-before: <!-- features-end -->
---
```

## FAQ

### What is this project about?

The mission of this project is to
enable current best practices
through modern Python tooling.

### What makes this project different from other Python templates?

This is a general-purpose template for Python libraries and applications.

Our goals are:

- Focus on simplicity and minimalism
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- [Poetry][1] for packaging and dependency management
- [Nox][2] for automation of checks and other development tasks
- [GitHub Actions][3] for continuous integration and delivery

[1]: https://python-poetry.org/
[2]: https://nox.thea.codes/
[3]: https://github.com/features/actions
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[hypermodernism]: https://en.wikipedia.org/wiki/Hypermodernism_(chess)
[retrofuturism]: https://en.wikipedia.org/wiki/Retrofuturism
[statistics norway]: https://www.ssb.no/
