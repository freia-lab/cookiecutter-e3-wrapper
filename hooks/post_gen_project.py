from __future__ import print_function
import sys
import shutil
import os
import subprocess
from cookiecutter.main import cookiecutter

try:
    from urllib import request
    from urllib.parse import quote
    import urllib.error
except ImportError:
    print("Warning: urllib is not installed.", file=sys.stderr)
    request = None


def remove_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("ERROR: file '{}' can not be deleted.".format(filename))
        sys.exit(1)


def remove_dir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
    else:
        print("ERROR: directory '{}' can not be deleted.".format(dirname))
        sys.exit(1)


def git_api_call(path, api_url, quote_path=False):
    # Fall through in case urllib did not import correctly.
    if request is None:
        return False

    if quote_path:
        path = quote(path, safe="")
    try:
        response = request.urlopen("{}/{}".format(api_url, path))
    except urllib.error.HTTPError:
        return False
    return True


def check_git_repo(repo):
    gitlab_url = "https://gitlab.esss.lu.se/"
    github_url = "https://github.com/"

    if repo and repo.startswith(gitlab_url):
        path = repo[len(gitlab_url) :]
        if path.endswith(".git"):
            path = path[:-4]

        # URL Encode the path
        return git_api_call(
            path, "{}api/v4/projects".format(gitlab_url), quote_path=True
        )

    elif repo and repo.startswith(github_url):
        path = repo[len(github_url) :]
        if path.endswith(".git"):
            path = path[:-4]

        return git_api_call(path, "https://api.github.com/repos")

    return False


def git(*args):
    try:
        subprocess.call(["git"] + list(args))
    except OSError:
        return False
    return True


def create_default_repo(repo):
    if repo:
        print(">>>> The repository '{}' was not found.".format(repo))
        print(
            ">>>> Please check that the repository is public, and then re-run 'git submodule add {}'.".format(
                repo
            )
        )
        print(">>>> A template module has been included in the meantime.")

    # Create project from the cookiecutter-pypackage.git repo template
    cookiecutter(
        "https://gitlab.esss.lu.se/ics-cookiecutter/cookiecutter-e3-module.git",
        None,
        True,
        {
            "company": "{{ cookiecutter.company}}",
            "module_name": "{{ cookiecutter.module_name }}",
            "summary": "{{ cookiecutter.summary }}",
            "full_name": "{{ cookiecutter.full_name }}",
            "email": "{{ cookiecutter.email }}",
            "keep_epics_base_makefiles": "Y",
        },
    )

    # For now, we should remove the Makefile.E3 file in the module, since that is for the conda version.
    remove_file("{{ cookiecutter.module_name }}/Makefile.E3")

    if sys.platform == "darwin":
        subprocess.call(
            [
                "sed",
                "-i",
                "",
                "-e",
                "s/^EPICS_MODULE_TAG/# EPICS_MODULE_TAG/",
                "configure/CONFIG_MODULE",
            ]
        )
    elif sys.platform == "linux":
        subprocess.call(
            [
                "sed",
                "-i",
                "s/^EPICS_MODULE_TAG/# EPICS_MODULE_TAG/",
                "configure/CONFIG_MODULE",
            ]
        )


def main():
    module_name = "{{ cookiecutter.module_name }}".strip()
    repo = "{{ cookiecutter.git_repository }}".strip()

    if git("init"):
        print(">>>> git repository has been initialized.")
        if check_git_repo(repo):
            git("submodule", "add", repo)
        else:
            create_default_repo(repo)
    else:
        print(">>>> git is not installed correctly on your machine.")


if __name__ == "__main__":
    main()
