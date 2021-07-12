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

help:
	@echo usage: make [target]
	@echo --------------------
	@echo targets:
	@echo ********
	@echo docker-build
	@echo docker-build-no-cache
	@echo docker-remove-image
	@echo docker-run
	@echo docker-build-and-run
	@echo docker-build-no-cache-and-run
	@echo docker-tag-latest


IMAGE_NAME = tomerfi/switcher_webapi

CONTAINER_NAME = switcher_webapi

GIT_COMMIT = $(strip $(shell git rev-parse --short HEAD))

CURRENT_DATE = $(strip $(shell date -u +"%Y-%m-%dT%H:%M:%SZ"))

CODE_VERSION = $(strip $(shell cat VERSION))

ifndef CODE_VERSION
$(error You need to create a VERSION file to build the image.)
endif

FULL_IMAGE_NAME = $(strip $(IMAGE_NAME):$(CODE_VERSION))

ifeq ($(shell docker info -f '{{json .OSType}}'),"linux")
	arch = $(shell docker info -f '{{json .Architecture}}')
	ifeq ($(arch),"x86_64")
		BASE_IMAGE = python:3.9.6-slim
	else ifeq ($(arch),"armv7l")
		BASE_IMAGE = arm32v7/python:3.9.6
	endif
endif

ifndef BASE_IMAGE
$(error Operating system or Architecture is not supported.)
endif

docker-build:
	docker build \
	--build-arg BASE_IMAGE=$(BASE_IMAGE) \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=$(CODE_VERSION) \
	-t $(FULL_IMAGE_NAME) .

docker-build-no-cache:
	docker build --no-cache \
	--build-arg BASE_IMAGE=$(BASE_IMAGE) \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=$(CODE_VERSION) \
	-t $(FULL_IMAGE_NAME) .

docker-remove-image:
	docker image rm $(FULL_IMAGE_NAME)

docker-run:
	docker run -d -p :8000 --name $(CONTAINER_NAME) $(FULL_IMAGE_NAME)

docker-build-and-run:
	docker-build docker-run

docker-build-no-cache-and-run:
	docker-build-no-cache docker-run

docker-tag-latest:
	docker tag $(FULL_IMAGE_NAME) $(IMAGE_NAME):latest
