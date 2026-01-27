---
name: lint
description: Run ruff linter and formatter checks
---

Run linting and format checks:

```bash
ruff check .
ruff format --check .
mypy --ignore-missing-imports app/
```

To auto-fix issues:

```bash
ruff check --fix .
ruff format .
```
