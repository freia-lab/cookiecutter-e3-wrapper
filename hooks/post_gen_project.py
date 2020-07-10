import sys
import shutil
import os
import subprocess
from urllib import request
from urllib.parse import quote
import urllib.error


def remove_file(filename: str):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("ERROR: file '{}' can not be deleted.".format(filename))
        sys.exit(1)


def remove_dir(dirname: str):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
    else:
        print("ERROR: directory '{}' can not be deleted.".format(dirname))
        sys.exit(1)


def check_git_repo(repo: str):
    git_url = "https://gitlab.esss.lu.se/"

    if repo and repo.startswith(git_url):
        path = repo[len(git_url) :]
        if path.endswith(".git"):
            path = path[:-4]

        # URL Encode the path
        path = quote(path, safe="")

        try:
            response = request.urlopen(f"{git_url}api/v4/projects/{path}")
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


def main():
    module_name = "{{ cookiecutter.module_name }}".strip()
    repo = "{{ cookiecutter.git_repository }}".strip()

    if git("init"):
        if check_git_repo(repo):
            remove_dir(module_name + "-loc")
            git("submodule", "add", repo)
        else:
            print(f">>>> The repository '{repo}' was not found on gitlab.")
            print(
                f">>>> Please check that the repository is public, and then re-run 'git submodule add {repo}'."
            )
            print(">>>> A template module has been included in the meantime.")
    else:
        print(">>>> git is not installed correctly on your machine.")


if __name__ == "__main__":
    main()
