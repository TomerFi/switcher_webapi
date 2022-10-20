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

build: enable-multiarch
	docker buildx build \
	--build-arg VCS_REF=$(GIT_COMMIT) \
	--build-arg BUILD_DATE=$(CURRENT_DATE) \
	--build-arg VERSION=$(CODE_VERSION) \
	--platform $(PLATFORMS) \
	--tag $(FULL_IMAGE_NAME) \
	--tag $(IMAGE_NAME):latest .

dockerfile-lint:
	npx dockerfilelint Dockerfile

enable-multiarch:
	docker run --rm --privileged multiarch/qemu-user-static --reset -p yes

.PHONY: build dockerfile-lint enable-multiarch
