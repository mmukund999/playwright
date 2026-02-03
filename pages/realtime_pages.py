from __future__ import annotations

from dataclasses import dataclass

from .base_page import BasePage, PageSpec


@dataclass(frozen=True)
class RealtimePage:
    spec: PageSpec

    def create(self, page, base_url: str) -> BasePage:
        return BasePage(page, base_url, self.spec)


LOGIN = RealtimePage(
    PageSpec("Login", "/login", "Sign in to Realtime", "Sign in", has_realtime_widget=False)
)
SIGNUP = RealtimePage(
    PageSpec("Signup", "/signup", "Create your account", "Create account", has_realtime_widget=False)
)
FORGOT_PASSWORD = RealtimePage(
    PageSpec("Forgot Password", "/forgot-password", "Reset password", "Send reset link", False)
)
DASHBOARD = RealtimePage(
    PageSpec("Dashboard", "/dashboard", "Realtime overview", "Refresh insights")
)
LIVE_FEED = RealtimePage(PageSpec("Live Feed", "/live-feed", "Live events", "Pause stream"))
NOTIFICATIONS = RealtimePage(
    PageSpec("Notifications", "/notifications", "Notifications", "Mark all read")
)
REPORTS = RealtimePage(PageSpec("Reports", "/reports", "Reports", "Generate report"))
ANALYTICS = RealtimePage(PageSpec("Analytics", "/analytics", "Analytics", "Run analysis"))
USERS = RealtimePage(PageSpec("Users", "/users", "User directory", "Invite user"))
ROLES = RealtimePage(PageSpec("Roles", "/roles", "Roles", "Create role"))
PERMISSIONS = RealtimePage(
    PageSpec("Permissions", "/permissions", "Permissions", "Create policy")
)
AUDIT_LOGS = RealtimePage(PageSpec("Audit Logs", "/audit-logs", "Audit logs", "Export logs"))
INTEGRATIONS = RealtimePage(
    PageSpec("Integrations", "/integrations", "Integrations", "Connect provider")
)
WEBHOOKS = RealtimePage(PageSpec("Webhooks", "/webhooks", "Webhooks", "Add webhook"))
API_KEYS = RealtimePage(PageSpec("API Keys", "/api-keys", "API keys", "Generate key"))
BILLING = RealtimePage(PageSpec("Billing", "/billing", "Billing", "Update payment"))
INVOICES = RealtimePage(PageSpec("Invoices", "/invoices", "Invoices", "Download invoice"))
SUBSCRIPTION = RealtimePage(
    PageSpec("Subscription", "/subscription", "Subscription", "Change plan")
)
SETTINGS = RealtimePage(PageSpec("Settings", "/settings", "Settings", "Save settings"))
PROFILE = RealtimePage(PageSpec("Profile", "/profile", "Your profile", "Update profile"))
SUPPORT = RealtimePage(PageSpec("Support", "/support", "Support", "Create ticket"))
STATUS = RealtimePage(PageSpec("Status", "/status", "System status", "Refresh status"))
INCIDENTS = RealtimePage(PageSpec("Incidents", "/incidents", "Incidents", "Declare incident"))
UPTIME = RealtimePage(PageSpec("Uptime", "/uptime", "Uptime", "Export uptime"))
DEVICES = RealtimePage(PageSpec("Devices", "/devices", "Devices", "Register device"))
DEVICE_DETAILS = RealtimePage(
    PageSpec("Device Detail", "/devices/12345", "Device 12345", "Reboot device")
)
ALERTS = RealtimePage(PageSpec("Alerts", "/alerts", "Alerts", "Create alert"))
RULES = RealtimePage(PageSpec("Rules", "/rules", "Rules", "Create rule"))
METRICS = RealtimePage(PageSpec("Metrics", "/metrics", "Metrics", "Export metrics"))
EXPORTS = RealtimePage(PageSpec("Exports", "/exports", "Exports", "Start export"))
FEATURE_FLAGS = RealtimePage(
    PageSpec("Feature Flags", "/feature-flags", "Feature flags", "Create flag")
)
DATA_PIPELINES = RealtimePage(
    PageSpec("Data Pipelines", "/data-pipelines", "Data pipelines", "Create pipeline")
)
SLA = RealtimePage(PageSpec("SLA", "/sla", "Service level", "Create SLA"))
COMPLIANCE = RealtimePage(
    PageSpec("Compliance", "/compliance", "Compliance center", "Export evidence")
)
QUEUE = RealtimePage(PageSpec("Queue", "/queue", "Processing queue", "Retry failed"))
SEGMENTS = RealtimePage(PageSpec("Segments", "/segments", "Segments", "Create segment"))
REGIONS = RealtimePage(PageSpec("Regions", "/regions", "Regions", "Add region"))
TAGS = RealtimePage(PageSpec("Tags", "/tags", "Tags", "Create tag"))
ENVIRONMENTS = RealtimePage(
    PageSpec("Environments", "/environments", "Environments", "Add environment")
)
PLAYBOOKS = RealtimePage(PageSpec("Playbooks", "/playbooks", "Playbooks", "Create playbook"))

ALL_PAGES = [
    LOGIN,
    SIGNUP,
    FORGOT_PASSWORD,
    DASHBOARD,
    LIVE_FEED,
    NOTIFICATIONS,
    REPORTS,
    ANALYTICS,
    USERS,
    ROLES,
    PERMISSIONS,
    AUDIT_LOGS,
    INTEGRATIONS,
    WEBHOOKS,
    API_KEYS,
    BILLING,
    INVOICES,
    SUBSCRIPTION,
    SETTINGS,
    PROFILE,
    SUPPORT,
    STATUS,
    INCIDENTS,
    UPTIME,
    DEVICES,
    DEVICE_DETAILS,
    ALERTS,
    RULES,
    METRICS,
    EXPORTS,
    FEATURE_FLAGS,
    DATA_PIPELINES,
    SLA,
    COMPLIANCE,
    QUEUE,
    SEGMENTS,
    REGIONS,
    TAGS,
    ENVIRONMENTS,
    PLAYBOOKS,
]
