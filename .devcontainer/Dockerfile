# Base image is is python's image
FROM python:3.8.6

# Set shell with pipline fail return
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set environment variables
ENV SHELL=/bin/bash \
    PATH=$PATH:/opt/gopath/bin:/opt/go/bin

# Install linux packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends git-lfs \
    && apt-get install -y --no-install-recommends nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install nodejs (includes npm)
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install golang
WORKDIR /opt/go
RUN curl -sOL https://dl.google.com/go/go1.14.4.linux-amd64.tar.gz \
    && tar -C /opt -xf go1.14.4.linux-amd64.tar.gz \
    && rm go1.14.4.linux-amd64.tar.gz \
    && bin/go env -w GOPATH=/opt/gopath GO111MODULE=on

# Install hadolint
RUN curl -sL https://github.com/hadolint/hadolint/releases/download/v1.18.0/hadolint-Linux-x86_64 \
        -o /usr/local/bin/hadolint \
    && chmod +x /usr/local/bin/hadolint

# Copy stuff from host to container
COPY requirements.txt ./

# Install modules, requirements, dependencies, packages, libraries etc.
RUN \
    # Install node modules
    npm install -g \
        markdownlint-cli@0.23.2 \
        @commitlint/cli@9.0.1 \
        @commitlint/config-conventional@9.0.1 \
    # Install golang modules
    && go get -u github.com/client9/misspell/cmd/misspell@v0.3.4 \
    # Install python dependencies
    && pip install --no-cache-dir -r requirements.txt
