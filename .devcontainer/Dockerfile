# Start from python image
FROM python:3.8.2

# Install prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl=7.64.0-4+deb10u1 bash=5.0-4 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set shell with pipline fail return
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Copy stuff from host to container
COPY requirements.txt ./

# Install nodejs (includes npm)
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y --no-install-recommends nodejs=14.2.0-1nodesource1

# Install golang (note the gopath custom folder and the PATH env var)
RUN curl -sL https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz -o golang.tar.gz \
    && tar -C /usr/local -xzf golang.tar.gz \
    && /usr/local/go/bin/go env -w GOPATH=/usr/local/gopath \
    && /usr/local/go/bin/go env -w GO111MODULE=on

# Install binaries
RUN curl -sL https://github.com/hadolint/hadolint/releases/download/v1.17.6/hadolint-Linux-x86_64 \
        -o /usr/local/bin/hadolint \
    && chmod +x /usr/local/bin/hadolint \
    && curl -sL https://storage.googleapis.com/container-structure-test/v1.8.0/container-structure-test-linux-amd64 \
        -o /usr/local/bin/container-structure-test \
    && chmod +x /usr/local/bin/container-structure-test

# Install node modules
RUN npm install -g markdownlint-cli@0.23.1

# Install golang modules
RUN /usr/local/go/bin/go get -u github.com/client9/misspell/cmd/misspell@v0.3.4

# Install python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV SHELL=/bin/bash \
    PATH=$PATH:/usr/local/gopath/bin:/usr/local/go/bin
