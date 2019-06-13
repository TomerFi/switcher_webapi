#!/bin/bash

# dockerlint-verify.sh
#
# The script verifies the existence of npm (https://www.npmjs.com/) and the npm package dockerlint (https://www.npmjs.com/package/dockerlint).
# If both exists the script will run the dockerlint linter against the Dockerfile passed as the first argument to the script.
# The script does not install anything on your behalf, for using it, please manually install npm and dockerlint.

display_no_npm() {
    echo -e "### !!!SKIPPING TEST!!! ###\n"
    echo -e "npm is not installed.\n"
    echo "please consider installing npm for use with dockerlint."
}

display_no_dockerlint() {
    echo -e "### !!!SKIPPING TEST!!! ###\n"
    echo -e "dockerlint is not installed.\n"
    echo "please consider installing the dockerlint npm package for linting docker files."
}

display_usage() {
    echo -e "please provide the exact path of the Dockerfile as the first and only argument.\n"
    echo "usage: $0 /absolute/or/relative/path/Dockerfile"
}

if command -v npm > /dev/null
then
    echo "npm is present, checking for dockerlint."
    if npm -g list | grep dockerlint > /dev/null
    then
        echo "dockerlint package is present, running dockerlint"
        if [ -z "$1" ]
        then
            display_usage
            exit 1
        else
            if [ "$1" = "." ]
            then
                dockerlint
            else
                dockerlint -f "$1"
            fi
        fi
    else
        display_no_dockerlint
        exit 0
    fi
else
    display_no_npm
    exit 0
fi
