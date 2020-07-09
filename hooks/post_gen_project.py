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


def main():
    # First, see if the git repository listed in the cookiecutter is a real git repository.
    # If it is, delete the template directory and clone it.
    # Otherwise, leave it be.
    if "{{ cookiecutter.keep_epics_base_makefiles }}" == "N":
        remove_dir("configure")
        remove_file("Makefile")
        remove_file(os.path.join("{{ cookiecutter.module_name }}App", "Makefile"))
        remove_file(os.path.join("{{ cookiecutter.module_name }}App", "Db", "Makefile"))
        remove_file(
            os.path.join("{{ cookiecutter.module_name }}App", "src", "Makefile")
        )


if __name__ == "__main__":
    main()
