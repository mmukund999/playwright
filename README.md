# Realtime QA POM Suite (Playwright Python)

This repository provides a Playwright + Pytest POM-based QA suite for a real-time domain application. It includes **30 page objects** and **30 test cases** (positive/negative coverage, API testing, and complex flows).

## Structure

- `pages/`
  - `base_page.py`: Shared POM helpers and a `PageSpec` definition.
  - `realtime_pages.py`: 30 real-time app pages modeled as POM specs.
- `tests/`
  - `test_realtime_suite.py`: 30 test cases (UI + API + complex flows).
  - `conftest.py`: base URL configuration.
- `pytest.ini`: marker definitions.

## Pages Covered

1. Login
2. Signup
3. Forgot Password
4. Dashboard
5. Live Feed
6. Notifications
7. Reports
8. Analytics
9. Users
10. Roles
11. Permissions
12. Audit Logs
13. Integrations
14. Webhooks
15. API Keys
16. Billing
17. Invoices
18. Subscription
19. Settings
20. Profile
21. Support
22. Status
23. Incidents
24. Uptime
25. Devices
26. Device Detail
27. Alerts
28. Rules
29. Metrics
30. Exports
31. Feature Flags
32. Data Pipelines
33. SLA
34. Compliance
35. Queue

## Configuration

Set the base URLs to target your environment:

```bash
export REALTIME_BASE_URL="https://your-realtime-app.test"
export REALTIME_API_BASE_URL="https://api.your-realtime-app.test"
```

## Run Tests

```bash
pytest
```

## Notes

- UI tests use the POM classes defined in `pages/realtime_pages.py`.
- API tests use the `request` fixture from `pytest-playwright`.
- Complex coverage includes multi-step API + UI validation (incident triage flow).
