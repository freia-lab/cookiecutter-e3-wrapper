# e3 NFS module wrapper cookiecutter template

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for e3 NFS module wrappers.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```
$ pip install cookiecutter
```

Generate an EPICS/E3 module:

```
$ cookiecutter git+https://gitlab.esss.lu.se/ics-cookiecutter/cookiecutter-e3-wrapper.git
```

As this is not easy to remember, you can add an alias in your `~/.bash_profile`:

```
alias e3-wrapper='cookiecutter git+https://gitlab.esss.lu.se/ics-cookiecutter/cookiecutter-e3-wrapper.git'
```

## Usage notes

This cookiecutter recipe is based on [e3TemplateGenerator](https://github.com/icshwi/e3-tools). You will be prompted for the following information:

* Company
* Module name
* Summary
* Name
* email address
* EPICS base version/location
* Require version
* Git repository to include as submodule

If the git repository that you provide exists and is found on the ESS gitlab server, then it will add it as a submodule. Otherwise, it will simply add a local module within the E3 wrapper.