// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Exporter', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on("Exporter", "refresh", function(frm) {
	frappe.ui.form.on("Company Authorisation", {
			"company": function(frm) {
			frm.add_fetch("company", "company", "company_name");
			frm.add_fetch("company", "phone_number", "phone_number");
			frm.refresh_field("company");

		}
	});

});
