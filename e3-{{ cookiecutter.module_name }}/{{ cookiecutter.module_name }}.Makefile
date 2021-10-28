# Copyright (C) {% now 'local', '%Y' %}  {{ cookiecutter.company }}

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


## The following lines are mandatory, please don't change them.
where_am_I := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
include $(E3_REQUIRE_TOOLS)/driver.makefile
include $(E3_REQUIRE_CONFIG)/DECOUPLE_FLAGS


############################################################################
#
# Add any required modules here that come from startup scripts, etc.
#
############################################################################

# REQUIRED += stream


############################################################################
#
# If you want to exclude any architectures:
#
############################################################################

# EXCLUDE_ARCHS += linux-ppc64e6500


############################################################################
#
# If you want to allow specific architectures only:
#
############################################################################

# ARCH_FILTER += linux-x86_64


############################################################################
#
# Relevant directories to point to files
#
############################################################################

APP:={{ cookiecutter.module_name }}App
#APPDB:=$(APP)/Db
APPSRC:=$(APP)/src
#APPCMDS:=$(APP)/cmds


############################################################################
#
# Add any files that should be copied to $(module)/db
#
############################################################################

# TEMPLATES += $(wildcard $(APPDB)/*.db)
# TEMPLATES += $(wildcard $(APPDB)/*.proto)
# TEMPLATES += $(wildcard $(APPDB)/*.template)

# USR_INCLUDES += -I$(where_am_I)$(APPSRC)


############################################################################
#
# Add any files that need to be compiled (e.g. .c, .cpp, .st, .stt)
#
############################################################################

SOURCES   += $(APPSRC)/{{ cookiecutter.module_name }}Main.cpp


############################################################################
#
# Add any .dbd files that should be included (e.g. from user-defined functions, etc.)
#
############################################################################

#DBDS   += 


############################################################################
#
# Add any header files that should be included in the install (e.g. 
# StreamDevice or asyn header files that are used by other modules)
#
############################################################################

#HEADERS   += 


############################################################################
#
# Add any startup scripts that should be installed in the base directory
#
############################################################################

SCRIPTS += $(wildcard iocsh/*.iocsh)


############################################################################
#
# If you have any .substitution files, and template files, add them here.
#
############################################################################

# SUBS=$(wildcard $(APPDB)/*.substitutions)
# TMPS=$(wildcard $(APPDB)/*.template)

USR_DBFLAGS += -I . -I ..
USR_DBFLAGS += -I $(EPICS_BASE)/db
USR_DBFLAGS += -I $(APPDB)

db: $(SUBS) $(TMPS)

$(SUBS):
	@printf "Inflating database ... %44s >>> %40s \n" "$@" "$(basename $(@)).db"
	@rm -f  $(basename $(@)).db.d  $(basename $(@)).db
	@$(MSI) -D $(USR_DBFLAGS) -o $(basename $(@)).db -S $@  > $(basename $(@)).db.d
	@$(MSI)    $(USR_DBFLAGS) -o $(basename $(@)).db -S $@

$(TMPS):
	@printf "Inflating database ... %44s >>> %40s \n" "$@" "$(basename $(@)).db"
	@rm -f  $(basename $(@)).db.d  $(basename $(@)).db
	@$(MSI) -D $(USR_DBFLAGS) -o $(basename $(@)).db $@  > $(basename $(@)).db.d
	@$(MSI)    $(USR_DBFLAGS) -o $(basename $(@)).db $@

.PHONY: db $(SUBS) $(TMPS)


vlibs:

.PHONY: vlibs
