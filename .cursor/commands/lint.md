---
name: lint
description: Run ruff linter and formatter checks
---

Run linting and format checks:

```bash
ruff check app/
ruff format --check app/
mypy --ignore-missing-imports app/
```

To auto-fix issues:

```bash
ruff check --fix app/
ruff format app/
```
