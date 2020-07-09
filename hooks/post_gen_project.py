import sys
import shutil
import os
import subprocess


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
    if repo:
        pass
    return False


def clone_repo(repo):
    print("Cloning repository:")
    subprocess.call(["git", "clone", "--recursive", repo])


def main():
    module_name = "{{ cookiecutter.module_name }}"
    repo = "{{ cookiecutter.git_repository }}"

    if check_git_repo(repo):
        remove_dir(module_name + "-loc")
        clone_repo(repo)


if __name__ == "__main__":
    main()
