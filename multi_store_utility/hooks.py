app_name = "multi_store_utility"
app_title = "Multi Store Utility"
app_publisher = "efeone Pvt Ltd"
app_description = "Frappe App for Handling multi store with ERPNext"
app_email = "info@efeone.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/multi_store_utility/css/multi_store_utility.css"
# app_include_js = "/assets/multi_store_utility/js/multi_store_utility.js"

# include js, css files in header of web template
# web_include_css = "/assets/multi_store_utility/css/multi_store_utility.css"
# web_include_js = "/assets/multi_store_utility/js/multi_store_utility.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "multi_store_utility/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "multi_store_utility/public/icons.svg"

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
#	"methods": "multi_store_utility.utils.jinja_methods",
#	"filters": "multi_store_utility.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "multi_store_utility.install.before_install"
# after_install = "multi_store_utility.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "multi_store_utility.uninstall.before_uninstall"
# after_uninstall = "multi_store_utility.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "multi_store_utility.utils.before_app_install"
# after_app_install = "multi_store_utility.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "multi_store_utility.utils.before_app_uninstall"
# after_app_uninstall = "multi_store_utility.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "multi_store_utility.notifications.get_notification_config"

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
#		"multi_store_utility.tasks.all"
#	],
#	"daily": [
#		"multi_store_utility.tasks.daily"
#	],
#	"hourly": [
#		"multi_store_utility.tasks.hourly"
#	],
#	"weekly": [
#		"multi_store_utility.tasks.weekly"
#	],
#	"monthly": [
#		"multi_store_utility.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "multi_store_utility.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"erpnext.accounts.doctype.accounting_dimension.accounting_dimension.get_dimensions": "multi_store_utility.multi_store_utility.doc_events.accounting_dimension.get_dimensions"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "multi_store_utility.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["multi_store_utility.utils.before_request"]
# after_request = ["multi_store_utility.utils.after_request"]

# Job Events
# ----------
# before_job = ["multi_store_utility.utils.before_job"]
# after_job = ["multi_store_utility.utils.after_job"]

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
#	"multi_store_utility.auth.validate"
# ]
