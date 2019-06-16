#!/bin/bash

# container-structure-test-verify.sh
#
# The script verifies the existence of container-structure-test (https://github.com/GoogleContainerTools/container-structure-test).
# If exists the script will run the tool with the configuration file passed as the first argument against the image passed as the second argument.
# The script does not install anything on your behalf, for using it, please manually install container-structure-test.
# Image must be build first.

display_no_container_structure_test() {
    echo -e "### !!!SKIPPING TEST!!! ###\n"
    echo -e "container-structure-test is not installed.\n"
    echo "please consider installing container-structure-test for linting your shell scripts."
}

display_usage() {
    echo "please provide the exact path of the configuration file as the first argument and the image name as the second."
    echo -e "the image must be build before running this tool.\n"
    echo "usage: $0 /absolute/or/relative/path/cst_config.yml namespace/image_name:some_tag"
}

if command -v container-structure-test > /dev/null
then
    if [ -z "$1" ] || [ -z "$2" ]
    then
        display_usage
        exit 1
    else
        echo "container-structure-test is present, running container-structure-test"
        container-structure-test test --force --config "$1" --verbosity info --image "$2"
    fi
else
    display_no_container_structure_test
    exit 0
fi
