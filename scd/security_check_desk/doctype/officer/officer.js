// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Officer", {
	refresh: function(frm) {
        if(frm.doc.docstatus == 0) {
            frm.add_custom_button(__('As User'), function() {
                frm.events.create_user(frm);
            }, __('Create'));
            frm.page.set_inner_btn_group_as_primary(__('Create'));
            // cur_frm.add_custom_button(__("Create User Access"), function() {
            //     frm.events.create_user(frm);
            // });
        }
    },
	create_user: function(frm) {
		frappe.call({
			method: "scd.security_check_desk.doctype.officer.custom.create_user",
			args: {
                 officer: frm.doc.name, email: frm.doc.officer_email
            },
			callback: function(r){
                var doc = frappe.model.sync(r.message);
                frappe.set_route('Form', 'User', r.message.name);
            }
		});
	}
});