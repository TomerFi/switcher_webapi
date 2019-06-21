---
name: Bug report
about: Create a report to help us improve
labels: Bug

---

**Describe the bug**
A clear and concise Description of what the bug is.

**Docker image version**
The image version used:

> **Note:** If you're using the `latest` tag,
> you can get the version from the designated label like so:
>
> ```shell
> docker image inspect tomerfi/switcher_webapi:latest \
> -f '{{ index .Config.Labels "org.label-schema.version" }}'
> ```

**Runtine environment information**
Detailed information about the runtime environment for docker.

**Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Additional context**
Add any other context about the problem here.
