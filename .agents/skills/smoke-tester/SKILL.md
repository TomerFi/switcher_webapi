---
name: smoke-tester
description: |
  Run E2E smoke tests on the switcher_webapi container image.
  Build the image, run the container, poll /health, and report results.
---

## What I do

- Build the container image
- Run it as a background container
- Poll the /health endpoint on localhost:8000 (12 attempts, 5s interval)
- Report pass/fail, show container logs, clean up

## When to use me

Use this when you need to verify a container build runs and responds
to health checks.

## Steps

1. Build:

```bash
podman build -t switcher_webapi:local .
```

2. Run container:

```bash
podman run -d --name smoke-test -p 8000:8000 switcher_webapi:local
```

3. Poll health:

```bash
for i in {1..12}; do
  response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health || true)
  [ "$response" = "200" ] && break
  echo "Attempt $i: status $response, retrying in 5s..."
  sleep 5
done
```

4. If healthy (else report failure):

```bash
podman logs smoke-test
podman stop smoke-test
podman rm smoke-test
```

## Expected Output

`/health` should return `{"status": "healthy"}`.
