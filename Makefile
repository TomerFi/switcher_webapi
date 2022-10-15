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

default: build

IMAGE_NAME = tomerfi/switcher_webapi
GIT_COMMIT = $(strip $(shell git rev-parse --short HEAD))
CURRENT_DATE = $(strip $(shell date -u +"%Y-%m-%dT%H:%M:%SZ"))
CODE_VERSION = $(strip $(shell cat VERSION))
FULL_IMAGE_NAME = $(strip $(IMAGE_NAME):$(CODE_VERSION))

PLATFORMS = linux/amd64,linux/arm/v7

ifndef CODE_VERSION
$(error You need to create a VERSION file to build the image.)
endif

build:
	docker buildx build \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=$(CODE_VERSION) \
	--platform $(PLATFORMS) \
	--tag $(FULL_IMAGE_NAME) \
	--tag $(IMAGE_NAME):latest .

dockerfile-lint:
	npx dockerfilelint Dockerfile

verify-license-headers: # requires deno (https://deno.land/#installation)
	deno run --unstable --allow-read https://deno.land/x/license_checker@v3.1.3/main.ts

.PHONY: build dockerfile-lint verify-license-headers
