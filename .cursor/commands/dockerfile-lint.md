---
name: dockerfile-lint
description: Lint Dockerfile with hadolint
---

Run hadolint on Dockerfile:

```bash
CONTAINER_CMD=$(command -v podman 2>/dev/null || echo docker)
$CONTAINER_CMD run --rm -i hadolint/hadolint:v2.14.0 < Dockerfile
```

Or if hadolint is installed locally:

```bash
hadolint Dockerfile
```

Note: Some warnings are expected until security fixes are applied (e.g., DL3002 for non-root user).
