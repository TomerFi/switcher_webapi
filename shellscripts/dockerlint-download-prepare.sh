#!/bin/bash

# dockerlint-download-prepare.sh
#
# The script downloads the source code for dockerlint from github, extracts it and prepare it for use.
# The script uses sudo, so if you're not entitled for that usage, you cannont run this script.
# The script uses wget for the download and npm and coffeescript for the build.
# To use the dockerlint js file after build, you need nodejs.

display_usage() {
    echo -e "please provide desired version as the first and only argument.\n"
    echo "usage: $0 0.3.11"
}

if [ -z "$1" ]
then
    display_usage
    exit 1
fi

if [ -d "dockerlint-$1" ]
then
  echo "dockerlint-$1 found." 
  exit 0
else
  echo "dockerlint-$1 was not found, downloading and preparing." 
  sudo apt-get update
  sudo apt-get install coffeescript --no-install-recommends -y
  wget -v --https-only https://github.com/RedCoolBeans/dockerlint/archive/$1.tar.gz
  tar xzf $1.tar.gz
  cd dockerlint-$1
  make clean js
  rm -r "!(bin|lib)"
  echo "dockerlint-$1 created."
  exit 0
fi
