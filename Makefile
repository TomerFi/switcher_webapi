########################################################################
# .env_vars file contains following keys, example:                     #
# -------------------------------------------------------------------- #
# (Optional)                                                           #
# EXPOSED_PORT=8000                                                    #
# CONF_THROTTLE=5.0                                                    #
#                                                     					       #
# (Mandatory)                                                          #
# CONF_DEVICE_IP_ADDR=192.168.100.157                                  #
# CONF_PHONE_ID=1234                                                   #
# CONF_DEVICE_ID=ab1c2d                                                #
# CONF_DEVICE_PASSWORD=12345678                                        #
#																																	     #
# change the source file name by passing env_vars=another_file to make #
########################################################################

EXPOSED_PORT ?= 8000
CONF_THROTTLE ?= 5.0

env_vars ?= .env_vars
include $(env_vars)
export $(shell sed 's/=.*//' $(env_vars))

default: help

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

IMAGE_NAME = tomerfi/switcher_webapi

CONTAINER_NAME = switcher_webapi

GIT_COMMIT = $(strip $(shell git rev-parse --short HEAD))

CURRENT_DATE = $(strip $(shell date -u +"%Y-%m-%dT%H:%M:%SZ"))

CODE_VERSION = $(strip $(shell cat VERSION))

ifndef CODE_VERSION
$(error You need to create a VERSION file to build the image.)
endif

FULL_IMAGE_NAME = $(strip $(IMAGE_NAME):$(CODE_VERSION))

docker-build: ## build image from Dockerfile.
	docker build \
	--build-arg VCS_REF=$(GIT_COMMIT) \
  --build-arg BUILD_DATE=$(CURRENT_DATE) \
  --build-arg VERSION=$(CODE_VERSION) \
  -t $(FULL_IMAGE_NAME) .

docker-build-no-cache: ## build image from Dockerfile with no caching.
	docker build --no-cache \
	--build-arg VCS_REF=$(GIT_COMMIT) \
  --build-arg BUILD_DATE=$(CURRENT_DATE) \
  --build-arg VERSION=$(CODE_VERSION) \
  -t $(FULL_IMAGE_NAME) .

docker-tag-latest: ## add latest tag before pushing the latest version
	docker tag FULL_IMAGE_NAME IMAGE_NAME:latest

docker-run: ## run the built image as a container (must be built first).
docker-run:	verify-environment-file
	docker run -d -p $(EXPOSED_PORT):8000 \
	-e CONF_DEVICE_IP_ADDR=$(CONF_DEVICE_IP_ADDR) \
  -e CONF_PHONE_ID=$(CONF_PHONE_ID) \
  -e CONF_DEVICE_ID=$(CONF_DEVICE_ID) \
  -e CONF_DEVICE_PASSWORD=$(CONF_DEVICE_PASSWORD) \
  -e CONF_THROTTLE=$(CONF_THROTTLE) \
  --name $(CONTAINER_NAME) $(FULL_IMAGE_NAME)

docker-build-and-run: ## build image from Dockerfile and run as container.
docker-build-and-run: docker-build docker-run

docker-build-no-cache-and-run: ## build image from Dockerfile with no caching and run as container.
docker-build-no-cache-and-run: docker-build-no-cache docker-run

push-description: ## push the relative README.md file as full description to docker hub, requires username and password arguments
	bash shellscripts/push-docker-description.sh $(strip $(username)) $(strip $(password)) $(strip $(IMAGE_NAME))

verify-environment-file: ## verify the existence of the required environment variables file.
ifndef CONF_DEVICE_IP_ADDR
	$(error Mandatory configuration value CONF_DEVICE_IP_ADDR was not provided, can't run container.)
endif
ifndef CONF_PHONE_ID
	$(error Mandatory configuration value CONF_PHONE_ID was not provided, can't run container.)
endif
ifndef CONF_DEVICE_ID
	$(error Mandatory configuration value CONF_DEVICE_ID was not provided, can't run container.)
endif
ifndef CONF_DEVICE_PASSWORD
	$(error Mandatory configuration value CONF_DEVICE_PASSWORD was not provided, can't run container.)
endif
	$(info Safe to run image (assuming the provided information is infact correct).)

######################################################################
######################################################################