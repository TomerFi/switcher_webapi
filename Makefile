# Copyright Tomer Figenblat.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

docker-build: ## build the image from Dockerfile.
	docker build \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=$(CODE_VERSION) \
	-t $(FULL_IMAGE_NAME) .

docker-build-testing-image: ## build the image from Dockerfile using a testing tag.
	docker build \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=testing \
	-t $(strip $(IMAGE_NAME)):testing .

docker-remove-testing-image: ## remove the testing image (must be built first).
	docker image rm $(strip $(IMAGE_NAME)):testing

docker-build-no-cache: ## build the image from Dockerfile with no caching.
	docker build --no-cache \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=$(CODE_VERSION) \
	-t $(FULL_IMAGE_NAME) .

structure-test: ## run the container-structure-test tool against the built testing image (must be built first) using the relative container_structure.yml file
	container-structure-test test --force --config container_structure.yml --verbosity info --image $(strip $(IMAGE_NAME)):testing

docker-build-structure-test: ## build the image and test the container structure
docker-build-structure-test: docker-build structure-test

docker-build-no-cache-structure-test: ## build the image with no caching and test the container structure
docker-build-no-cache-structure-test: docker-build-no-cache structure-test

docker-full-structure-testing: ## build the image with the testing tag and remove after structure test
docker-full-structure-testing: docker-build-testing-image structure-test docker-remove-testing-image

docker-tag-latest: ## add the latest tag before pushing the latest version
	docker tag $(FULL_IMAGE_NAME) $(IMAGE_NAME):latest

docker-run: ## run the the built image as a container (must be built first).
	docker run -d -p :8000 --name $(CONTAINER_NAME) $(FULL_IMAGE_NAME)

docker-build-and-run: ## build the image from Dockerfile and run it as a container.
docker-build-and-run: docker-build docker-run

docker-build-no-cache-and-run: ## build the image from Dockerfile with no caching and run it as a container.
docker-build-no-cache-and-run: docker-build-no-cache docker-run
