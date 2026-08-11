---
name: add-endpoint
description: Step-by-step guide for adding a new API endpoint to switcher_webapi. Covers defining endpoint constants, creating async handlers, adding tests, updating docs, and running tests.
---

## What I do

- Define endpoint path constants in `app/webapp.py`
- Create async handler functions with the standard pattern
- Add pytest-asyncio tests using the `api_client` fixture
- Update MkDocs endpoint documentation
- Guide through running tests and verifying coverage

## When to use me

Use this when adding a new API endpoint to switcher_webapi, such as:
- Adding new device control functionality
- Exposing new aioswitcher API methods
- Creating new query endpoints

## Use the standard handler pattern

All endpoint handlers follow this structure:

1. Extract `device_type`, `ip`, `id`, and optional `login_key` from query params
2. Open `SwitcherApi` async context manager
3. Call the appropriate aioswitcher method
4. Serialize and return the result as JSON

## Steps to add an endpoint

### Step 1: Define Endpoint Constant

In `app/webapp.py`, add the endpoint path constant (around line 54-71):

```python
ENDPOINT_YOUR_ENDPOINT = "/switcher/your_endpoint"
```

### Step 2: Create Handler Function

Add the async handler with the appropriate decorator:

```python
@routes.get(ENDPOINT_YOUR_ENDPOINT)  # or .post, .patch, .delete
async def your_endpoint(request: web.Request) -> web.Response:
    """Describe what this endpoint does."""
    device_type = DEVICES[request.query[KEY_TYPE]]
    if KEY_LOGIN_KEY in request.query:
        login_key = request.query[KEY_LOGIN_KEY]
    else:
        login_key = "00"
    async with SwitcherApi(
        device_type, request.query[KEY_IP], request.query[KEY_ID], login_key
    ) as swapi:
        result = await swapi.your_method()
        return web.json_response(_serialize_object(result))
```

### Step 3: Add Tests

In `app/tests/test_web_app.py`, add test cases:

```python
@mark.parametrize(
    "url",
    [
        "/switcher/your_endpoint?type=plug&id=ab1c2d&ip=1.2.3.4",
        "/switcher/your_endpoint?type=plug&id=ab1c2d&ip=1.2.3.4&key=18",
    ],
)
async def test_successful_your_endpoint_get_request(api_client, url):
    with patch("app.webapp.SwitcherApi") as mock_api:
        mock_api.return_value.__aenter__.return_value.your_method = AsyncMock(
            return_value=expected_response
        )
        resp = await api_client.get(url)
        assert resp.status == 200
```

### Step 4: Update Documentation

Create or update the relevant docs file in `docs/`:
- Add endpoint to the appropriate `endpoints_*.md` file
- Include method, path, description, and query parameters

### Step 5: Run Tests

Run `ruff` for linting and `pytest` with coverage to verify the changes.

## Reference

Look at existing endpoints for patterns:
- `get_state` — Simple GET returning device state
- `turn_on` — POST with optional body parameters
- `control_breeze_device` — PATCH with complex body handling
