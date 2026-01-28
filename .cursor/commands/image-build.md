---
name: image-build
description: Build container image locally for testing (uses podman if available)
---

Build single-platform image for local testing:

```bash
CONTAINER_CMD=$(command -v podman 2>/dev/null || echo docker)
$CONTAINER_CMD build -t switcher_webapi:local .
```

Run the container:

```bash
CONTAINER_CMD=$(command -v podman 2>/dev/null || echo docker)
$CONTAINER_CMD run -d -p 8000:8000 --name switcher_webapi switcher_webapi:local
```

Test it's running:

```bash
curl http://localhost:8000/health
```

Stop and remove:

```bash
CONTAINER_CMD=$(command -v podman 2>/dev/null || echo docker)
$CONTAINER_CMD stop switcher_webapi && $CONTAINER_CMD rm switcher_webapi
```
