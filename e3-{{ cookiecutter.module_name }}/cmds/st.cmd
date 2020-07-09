# This should be a test startup script
require {{ cookiecutter.module_name }}, master

iocshLoad("$({{ cookiecutter.module_name }}_DIR)/{{ cookiecutter.module_name }}.iocsh")
