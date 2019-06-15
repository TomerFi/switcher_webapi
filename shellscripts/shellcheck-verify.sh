#!/bin/bash

# "shellcheck-verify.sh"
#
# The script verifies the existence of shellcheck (https://github.com/koalaman/shellcheck).
# If exists the script will run the shellcheck against the path passed in the first argument.
# The script does not install anything on your behalf, for using it, please manually install shellcheck.

display_no_shellcheck() {
    echo -e "### !!!SKIPPING TEST!!! ###\n"
    echo -e "shellcheck is not installed.\n"
    echo "please consider installing shellcheck for linting your shell scripts."
}

display_usage() {
    echo -e "please provide the exact path of the shellscripts as the first and only argument.\n"
    echo "usage: $0 /absolute/or/relative/path/my-script.sh"
    echo "usage: $0 /absolute/or/relative/path/*.sh"
}

if command -v shellcheck > /dev/null
then
    if [ -z "$1" ]
    then
        display_usage
        exit 1
    else
        echo "shellcheck is present, running shellcheck"
        if [ -z "$2" ]
        then
            shellcheck "$1"
        else
            shellcheck "$1"/*."$2"
        fi
    fi
else
    display_no_shellcheck
    exit 0
fi
