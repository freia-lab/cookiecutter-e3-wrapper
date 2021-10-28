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

As this is not easy to remember, you can add an alias in your `~/.bash_profile`:

```
alias e3-wrapper='cookiecutter git+https://gitlab.esss.lu.se/ics-cookiecutter/cookiecutter-e3-wrapper.git'
```

## Usage notes

You will be prompted for the following information:

* Company
* Module name
* Module version (N.B.! do not use the default `master`)
* Summary/description
* EPICS base version/location
* Require version
* Git repository to include as submodule

If you define a git repository to include as a submodule then it will add it as a git submodule. Otherwise it is recommended to use a utility like `makeBaseApp`.

To set up your wrapper, consult [e3 pages](https://e3.pages.esss.lu.se).

Once you have finished setting up your wrapper, make sure to remove all template comments as well as empty files and directories.
