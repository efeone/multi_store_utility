// Copyright (c) 2024, efeone Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Outlet", {
	refresh: function(frm) {
		if (!frm.doc.__islocal) {
        frappe.contacts.render_address_and_contact(frm);
    } else {
        frappe.contacts.clear_address_and_contact(frm);
    }
	},
});

frappe.ui.form.on("Serial Number", {
	letter_head: function(frm, cdt, cdn) {
		if(!frm.doc.letter_head) {
			erpnext.utils.copy_value_in_all_rows(frm.doc, cdt, cdn, "serial_numbers", "letter_head");
		}
	}
});
