import pytest
from playwright.sync_api import expect

from pages import realtime_pages as pages


@pytest.mark.positive
def test_login_page_allows_valid_sign_in(page, base_url):
    login = pages.LOGIN.create(page, base_url)
    login.open()
    login.expect_heading()
    login.expect_primary_action_enabled()


@pytest.mark.negative
def test_login_page_blocks_blank_password(page, base_url):
    login = pages.LOGIN.create(page, base_url)
    login.open_with_query([("email", "qa@example.com"), ("password", "")])
    login.expect_heading()
    login.expect_primary_action_disabled()


@pytest.mark.positive
def test_signup_page_supports_onboarding(page, base_url):
    signup = pages.SIGNUP.create(page, base_url)
    signup.open()
    signup.expect_heading()
    signup.expect_primary_action_enabled()


@pytest.mark.negative
def test_signup_page_rejects_weak_password(page, base_url):
    signup = pages.SIGNUP.create(page, base_url)
    signup.open_with_query([("passwordStrength", "weak")])
    signup.expect_heading()
    signup.expect_primary_action_disabled()


@pytest.mark.negative
def test_forgot_password_requires_valid_email(page, base_url):
    forgot = pages.FORGOT_PASSWORD.create(page, base_url)
    forgot.open_with_query([("email", "not-an-email")])
    forgot.expect_heading()
    forgot.expect_primary_action_disabled()


@pytest.mark.positive
def test_dashboard_loads_realtime_insights(page, base_url):
    dashboard = pages.DASHBOARD.create(page, base_url)
    dashboard.open()
    dashboard.expect_heading()
    dashboard.expect_realtime_widget()


@pytest.mark.negative
def test_live_feed_handles_paused_stream(page, base_url):
    feed = pages.LIVE_FEED.create(page, base_url)
    feed.open_with_query([("state", "paused")])
    feed.expect_heading()
    feed.expect_primary_action_enabled()


@pytest.mark.positive
def test_notifications_support_bulk_mark_read(page, base_url):
    notifications = pages.NOTIFICATIONS.create(page, base_url)
    notifications.open()
    notifications.expect_heading()
    notifications.expect_primary_action_enabled()


@pytest.mark.positive
def test_reports_can_generate_snapshot(page, base_url):
    reports = pages.REPORTS.create(page, base_url)
    reports.open()
    reports.expect_heading()
    reports.expect_primary_action_enabled()


@pytest.mark.positive
def test_analytics_allows_run(page, base_url):
    analytics = pages.ANALYTICS.create(page, base_url)
    analytics.open()
    analytics.expect_heading()
    analytics.expect_primary_action_enabled()


@pytest.mark.negative
def test_users_prevent_duplicate_invite(page, base_url):
    users = pages.USERS.create(page, base_url)
    users.open_with_query([("inviteEmail", "duplicate@example.com")])
    users.expect_heading()
    users.expect_primary_action_disabled()


@pytest.mark.positive
def test_roles_page_supports_creation(page, base_url):
    roles = pages.ROLES.create(page, base_url)
    roles.open()
    roles.expect_heading()
    roles.expect_primary_action_enabled()


@pytest.mark.negative
def test_permissions_block_invalid_policy(page, base_url):
    permissions = pages.PERMISSIONS.create(page, base_url)
    permissions.open_with_query([("policyState", "invalid")])
    permissions.expect_heading()
    permissions.expect_primary_action_disabled()


@pytest.mark.positive
def test_audit_logs_export_ready(page, base_url):
    logs = pages.AUDIT_LOGS.create(page, base_url)
    logs.open()
    logs.expect_heading()
    logs.expect_primary_action_enabled()


@pytest.mark.positive
def test_integrations_connect_supported_provider(page, base_url):
    integrations = pages.INTEGRATIONS.create(page, base_url)
    integrations.open()
    integrations.expect_heading()
    integrations.expect_primary_action_enabled()


@pytest.mark.negative
def test_webhooks_reject_insecure_endpoint(page, base_url):
    webhooks = pages.WEBHOOKS.create(page, base_url)
    webhooks.open_with_query([("target", "http://insecure")])
    webhooks.expect_heading()
    webhooks.expect_primary_action_disabled()


@pytest.mark.positive
def test_api_keys_generate_token(page, base_url):
    api_keys = pages.API_KEYS.create(page, base_url)
    api_keys.open()
    api_keys.expect_heading()
    api_keys.expect_primary_action_enabled()


@pytest.mark.negative
def test_billing_blocks_expired_card(page, base_url):
    billing = pages.BILLING.create(page, base_url)
    billing.open_with_query([("cardStatus", "expired")])
    billing.expect_heading()
    billing.expect_primary_action_disabled()


@pytest.mark.positive
def test_invoices_download_available(page, base_url):
    invoices = pages.INVOICES.create(page, base_url)
    invoices.open()
    invoices.expect_heading()
    invoices.expect_primary_action_enabled()


@pytest.mark.positive
def test_subscription_change_plan(page, base_url):
    subscription = pages.SUBSCRIPTION.create(page, base_url)
    subscription.open()
    subscription.expect_heading()
    subscription.expect_primary_action_enabled()


@pytest.mark.negative
def test_settings_prevent_invalid_timezone(page, base_url):
    settings = pages.SETTINGS.create(page, base_url)
    settings.open_with_query([("timezone", "Invalid/Zone")])
    settings.expect_heading()
    settings.expect_primary_action_disabled()


@pytest.mark.positive
def test_profile_updates_are_available(page, base_url):
    profile = pages.PROFILE.create(page, base_url)
    profile.open()
    profile.expect_heading()
    profile.expect_primary_action_enabled()


@pytest.mark.positive
def test_support_ticket_creation_flow(page, base_url):
    support = pages.SUPPORT.create(page, base_url)
    support.open()
    support.expect_heading()
    support.expect_primary_action_enabled()


@pytest.mark.negative
def test_incidents_require_summary(page, base_url):
    incidents = pages.INCIDENTS.create(page, base_url)
    incidents.open_with_query([("summary", "")])
    incidents.expect_heading()
    incidents.expect_primary_action_disabled()


@pytest.mark.api
@pytest.mark.positive
def test_api_health_check(request, api_base_url):
    response = request.get(f"{api_base_url}/health")
    assert response.status == 200


@pytest.mark.api
@pytest.mark.negative
def test_api_rejects_missing_token(request, api_base_url):
    response = request.post(f"{api_base_url}/v1/events", data={"type": "heartbeat"})
    assert response.status in {401, 403}


@pytest.mark.api
@pytest.mark.positive
def test_api_creates_event_and_returns_id(request, api_base_url):
    response = request.post(
        f"{api_base_url}/v1/events",
        headers={"Authorization": "Bearer valid-token"},
        data={"type": "alert", "payload": "latency spike"},
    )
    assert response.status == 201
    data = response.json()
    assert "id" in data


@pytest.mark.api
@pytest.mark.negative
def test_api_validates_event_schema(request, api_base_url):
    response = request.post(
        f"{api_base_url}/v1/events",
        headers={"Authorization": "Bearer valid-token"},
        data={"payload": "missing type"},
    )
    assert response.status == 422


@pytest.mark.api
@pytest.mark.complex
@pytest.mark.positive
def test_api_bulk_import_with_rate_limit(request, api_base_url):
    response = request.post(
        f"{api_base_url}/v1/imports",
        headers={"Authorization": "Bearer valid-token"},
        data={"batch": "large"},
    )
    assert response.status in {201, 202}
    expect_header = response.headers.get("x-rate-limit-remaining")
    assert expect_header is None or int(expect_header) >= 0


@pytest.mark.complex
@pytest.mark.positive
def test_complex_incident_triage_flow(page, base_url, request, api_base_url):
    incident = request.post(
        f"{api_base_url}/v1/incidents",
        headers={"Authorization": "Bearer valid-token"},
        data={"summary": "Spike in errors", "severity": "high"},
    )
    assert incident.status == 201
    incident_id = incident.json().get("id")

    incidents_page = pages.INCIDENTS.create(page, base_url)
    incidents_page.open_with_query([("highlight", str(incident_id))])
    incidents_page.expect_heading()
    incidents_page.expect_primary_action_enabled()
    expect(page.get_by_text("Spike in errors")).to_be_visible()
