import sys
import shutil
import os
import subprocess
from cookiecutter.main import cookiecutter

try:
    from urllib import request
except ImportError:
    print("urllib.request is not installed.")
    exit(1)
try:
    from urllib.parse import quote
except ImportError:
    print("urllib.parse.quote is not installed")
    exit(1)
try:
    import urllib.error
except ImportError:
    print("urllib.error is not installed")
    exit(1)


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


def check_git_repo(repo):
    git_url = "https://gitlab.esss.lu.se/"

    if repo and repo.startswith(git_url):
        path = repo[len(git_url) :]
        if path.endswith(".git"):
            path = path[:-4]

        # URL Encode the path
        path = quote(path, safe="")

        try:
            response = request.urlopen("{}api/v4/projects/{}".format(git_url, path))
        except urllib.error.HTTPError:
            return False
        return True
    return False


def git(*args):
    try:
        subprocess.call(["git"] + list(args))
    except OSError:
        return False
    return True


def create_default_repo(repo):
    if repo:
        print(">>>> The repository '{}' was not found on gitlab.".format(repo))
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


def main():
    module_name = "{{ cookiecutter.module_name }}".strip()
    repo = "{{ cookiecutter.git_repository }}".strip()

    if git("init"):
        print(">>>> git repository has been initialized.")
        if check_git_repo(repo):
            remove_dir(module_name + "-loc")
            git("submodule", "add", repo)
        else:
            create_default_repo(repo)
    else:
        print(">>>> git is not installed correctly on your machine.")


if __name__ == "__main__":
    main()
