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
healthy=0
for i in {1..12}; do
  response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health || true)
  if [ "$response" = "200" ]; then
    healthy=1
    break
  fi
  echo "Attempt $i: status $response, retrying in 5s..."
  sleep 5
done

if [ "$healthy" != "1" ]; then
  echo "Health check failed after 12 attempts!"
  podman logs smoke-test || true
  podman stop smoke-test || true
  podman rm smoke-test || true
  exit 1
fi
```

4. Show logs and clean up:

```bash
podman logs smoke-test
podman stop smoke-test
podman rm smoke-test
```

## Expected Output

`/health` should return `{"status": "healthy"}`.
