# Copyright (c) 2024, efeone Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)


class Outlet(Document):
	def onload(self):
		load_address_and_contact(self)

	def on_trash(self):
		delete_contact_and_address("Outlet", self.name)

	def on_update(self):
		for user in self.users:
			if not frappe.db.exists('User Permission', {'user':user.user,'allow':self.doctype,'for_value':self.name}):
				user_permission = frappe.new_doc('User Permission')
				user_permission.user = user.user
				user_permission.allow = self.doctype
				user_permission.for_value = self.name
				user_permission.save()
