---
name: test
description: Run pytest with coverage
---

Run all tests:

```bash
pytest -v
```

Run with coverage:

```bash
pytest -v --cov --cov-report term-missing
```

Run specific test:

```bash
pytest -v -k "test_name_here"
```

Generate HTML coverage report:

```bash
pytest -v --cov --cov-report=html
```
