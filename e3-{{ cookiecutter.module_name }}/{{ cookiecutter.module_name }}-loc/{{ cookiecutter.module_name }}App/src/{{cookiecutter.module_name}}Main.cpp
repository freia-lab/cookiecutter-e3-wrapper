/* {{ cookiecutter.module_name }}Main.cpp */
/* Author:  {{ cookiecutter.full_name }} */
/* Date:    {% now 'local', '%Y-%m-%d' %} */

#include <stddef.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

#include "epicsExit.h"
#include "epicsThread.h"
#include "iocsh.h"

int main(int argc, char *argv[])
{
    if (argc >= 2)
    {
        iocsh(argv[1]);
        epicsThreadSleep(.2);
    }
    iocsh(NULL);
    epicsExit(0);
    return (0);
}
