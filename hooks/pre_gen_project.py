import re
import sys

MODULE_NAME_REGEX = r"^[A-Za-z_][A-Za-z0-9_]*$"

module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_NAME_REGEX, module_name):
    print(
        f'ERROR: "{module_name}" is not a valid module name! It should match "{MODULE_NAME_REGEX}"',
        file=sys.stderr,
    )
    sys.exit(-1)
