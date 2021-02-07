// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Forwarder", "refresh", function(frm) {
	frappe.ui.form.on("Business Authorisation", {
			"business": function(frm) {
			frm.add_fetch("business", "business_name", "business_name");
			frm.add_fetch("business", "phone_number", "phone_number");
			frm.refresh_field("business");

		}
	});

});
