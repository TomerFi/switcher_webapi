#!/bin/bash

# push-docker-description.sh
#
# Script to push the content of README.md as Description to Docker Hub using Docker Registry HTTP API V2.
# Pass docker-hub user name as first argument,
# Pass docker-hub password as second argument.
# Pass image name including namespace but with no tags as the third and final argument.

display_usage() {
    echo "please provide username, password and image name as arguments."
    echo -e "please note, there is no need for any image tags, just the namespace and name.\n"
    echo "usage: $0 dockhub_username dockhub_password namespace/image_name"
}


if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]
then
    display_usage
    exit 1
fi

token=$(curl -s -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "'"$1"'", "password": "'"$2"'"}' \
    https://hub.docker.com/v2/users/login/ | jq -r .token)

if [ -z "$token" ]
then
  echo "Failed retrieving token from the registry api, please check username and password."
  exit 1
else
  echo "Got token."
fi

code=$(jq -n --arg msg "$(<README.md)" \
  '{"registry":"registry-1.docker.io","full_description": $msg }' | \
      curl -s -o /dev/null  -L -w "%{http_code}" \
         https://cloud.docker.com/v2/repositories/"$3"/ \
         -d @- -X PATCH \
         -H "Content-Type: application/json" \
         -H "Authorization: JWT ${token}")

if [[ "${code}" = "200" ]]
then
  echo "Description updated successful."
  exit 0
else
  echo "Failed updating the description, response code: %s\n" "${code}"
  exit 1
fi
