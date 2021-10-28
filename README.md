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
