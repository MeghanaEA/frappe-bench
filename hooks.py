app_name = "work_completed"
app_title = "Work Completed"
app_publisher = "Meghana"
app_description = "This helps people to know about the completed work"
app_email = "meghana.ea@negentropysolutions.com"
app_license = "MIT"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/work_completed/css/work_completed.css"
# app_include_js = "/assets/work_completed/js/work_completed.js"

# include js, css files in header of web template
# web_include_css = "/assets/work_completed/css/work_completed.css"
# web_include_js = "/assets/work_completed/js/work_completed.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "work_completed/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "work_completed.utils.jinja_methods",
#	"filters": "work_completed.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "work_completed.install.before_install"
# after_install = "work_completed.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "work_completed.uninstall.before_uninstall"
# after_uninstall = "work_completed.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "work_completed.utils.before_app_install"
# after_app_install = "work_completed.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "work_completed.utils.before_app_uninstall"
# after_app_uninstall = "work_completed.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "work_completed.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"work_completed.tasks.all"
#	],
#	"daily": [
#		"work_completed.tasks.daily"
#	],
#	"hourly": [
#		"work_completed.tasks.hourly"
#	],
#	"weekly": [
#		"work_completed.tasks.weekly"
#	],
#	"monthly": [
#		"work_completed.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "work_completed.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "work_completed.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "work_completed.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["work_completed.utils.before_request"]
# after_request = ["work_completed.utils.after_request"]

# Job Events
# ----------
# before_job = ["work_completed.utils.before_job"]
# after_job = ["work_completed.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"work_completed.auth.validate"
# ]
