# Major changes

This repo is a fork of [hypermodern python cookiecutter] and the major changes compared
to the hypermodern python cookiecutter are described on this page.

- Use [cruft] instead of [cookiecutter] to create instances of the template.
  _Cruft supports updating instances when the template is updated._
- Adopt template for use in Statistics Norway.
  - _Template variables updated to support github_organization and copyright_owner._
  - _Replace all references to cjolowicz-repos with ssb-pypitemplate._
- Support running `pytest` directly from the command line, without using `nox`.
- Add library function example.
  _The original template only had a command line tool example._
- Document generation works out of the box.
  _Use `make html` in the docs directory._
- Fix warnings in GitHub Actions.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cruft]: https://cruft.github.io/cruft/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
