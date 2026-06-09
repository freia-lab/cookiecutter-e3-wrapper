import os
import subprocess
import sys


def set_local_mode():
    os.mkdir("{{ cookiecutter.module_name }}")
    if sys.platform == "darwin":
        subprocess.call(
            [
                "sed",
                "-i",
                "",
                "-e",
                "/^EPICS_MODULE_TAG/d",
                "configure/CONFIG_MODULE",
            ]
        )
    elif sys.platform == "linux":
        subprocess.call(
            [
                "sed",
                "-i",
                "/^EPICS_MODULE_TAG/d",
                "configure/CONFIG_MODULE",
            ]
        )


def main():
    repo = "{{ cookiecutter.git_repository }}".strip()

    try:
        subprocess.check_call(["git", "init"])
        subprocess.check_call(["git", "checkout", "-b", "main"])
    except subprocess.CalledProcessError:
        sys.exit(-1)

    try:
        # We ignore possible error output since we are "duck-typing"
        subprocess.check_call(
            ["git", "submodule", "add", repo], stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        print(
            f"{'No' if not repo else f'The remote {repo} is not a'} valid submodule - local mode used."
        )
        set_local_mode()

    print(
        """
Your wrapper has been created.

Create the repository on your Git repository manager (e.g. https://github.com)
and add that remote:

    $ cd e3-{{ cookiecutter.module_name }}
    $ git remote add origin path/to/your/remote
    $ git add .
    $ git commit -m "Initial commit"
    $ git push -u origin main
"""
    )


if __name__ == "__main__":
    main()
