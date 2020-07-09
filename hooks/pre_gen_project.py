import re
import sys

MODULE_NAME_REGEX = r"^[A-Za-z_][A-Za-z0-9_]*$"

module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_NAME_REGEX, module_name):
    print(
        'ERROR: "{}" is not a valid module name! It should match "^[A-Za-z_][A-Za-z0-9_]*$"'.format(
            module_name
        )
    )
    sys.exit(1)
