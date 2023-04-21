# e3 wrapper cookiecutter template

Cookiecutter template for e3 wrappers.

## Prerequisites

- Python3.6+
- [`cookiecutter`](https://github.com/audreyr/cookiecutter)

## Quickstart

Generate an e3 wrapper:

```sh
$ cookiecutter git+https://gitlab.esss.lu.se/ics-cookiecutter/cookiecutter-e3-wrapper.git
```

## Usage notes

You will be prompted for the following information:

* Company/author
* Module name
* Module version (N.B.! do not use the default `master`)
* Summary/description
* EPICS base version/location
* *require* version
* Git repository to include as submodule

If you define a git repository to include as a submodule then it will add it as a git submodule.

If you are building a new module it is recommended to use a utility like `makeBaseApp.pl` from EPICS base or `makeSupport.pl` from asyn.

To configure your wrapper, consult [e3 pages](https://e3.pages.esss.lu.se).

Once you have finished setting up your wrapper, make sure to remove all template comments as well as empty files and directories.

## pre-commit hooks

The pre-commit is a tool that helps run automated actions that run before a code commit to catch errors, enforce standards, and ensure consistency.
You can find more information on the [documentation](https://pre-commit.com/). The template comes with a ``.pre-commit-config.yml`` with some hooks
configured you could use. You can also find a list of hooks in this on this [page](https://pre-commit.com/hooks.html). Following are the description
of the hooks on the template.

### Black
[Black](https://github.com/psf/black) is a Python code formatter that enforces a consistent coding style. Its hook in the pre-commit configuration ensures that all Python code is formatted consistently.

### Pre-commit-hooks
[Pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) is a collection of hooks for pre-commit that check for common issues. The hooks used in the pre-commit configuration are:
- **End-of-file-fixer**: Adds a newline to the end of files that do not have one.
- **Trailing-whitespace**: Removes trailing whitespace from files.
- **Check-yaml**: Checks YAML files for syntax errors.

### Doc8
[Doc8](https://github.com/myint/doc8) is a tool that checks documentation in Markdown and reStructuredText formats. Its hook in the pre-commit configuration ensures that all documentation is properly formatted.

### Clang-format
[Clang-format](https://github.com/pre-commit/mirrors-clang-format) is a C/C++ code formatter that uses the Clang tooling infrastructure to automatically format code. Its hook in the pre-commit configuration ensures that all C/C++ code is formatted consistently.

### dbformat
[dbformat](https://gitlab.esss.lu.se/e3/dbformat) is a utility to auto-format EPICS database files (in-place) according to [ESS database style guidelines](https://confluence.esss.lu.se/x/2PLPFg).
