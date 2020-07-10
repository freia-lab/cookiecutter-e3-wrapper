# This should be a test startup script
require {{ cookiecutter.module_name }}

iocshLoad("$({{ cookiecutter.module_name }}_DIR)/{{ cookiecutter.module_name }}.iocsh")
