import re
import sys

module_name_regex = r"^[A-Za-z_][A-Za-z0-9_]*$"
module_name = "{{ cookiecutter.module_name }}"

if not re.match(module_name_regex, module_name):
    print(
        f'ERROR: "{module_name}" is not a valid module name! It should match "{module_name_regex}"',
        file=sys.stderr,
    )
    sys.exit(-1)
