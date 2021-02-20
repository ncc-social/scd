// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Examination', {
	refresh: function(frm) {
		frm.set_query("examination_officer_id", function(frm, cdt, cdn) {
			// var a = locals[cdt][cdn];
			var d = new Date;
			return {
				filters: [
					["designation", "=", "Officer"],
				]
			}
		});
	}
});

frappe.ui.form.on('Examination', {
	refresh: function(frm) {
		frm.add_fetch('officer','officer_name','officer_name');
		// frm.add_fetch('exporter','phone_number','phone_number');
		// frm.add_fetch('exporter','exporter_photo','exporter_photo');
		// frm.add_fetch('forwarder','forwarder_name','forwarder_name');
		// frm.add_fetch('consignee','consignee_name','consignee_name');
		// frm.add_fetch('consignee','consignee_country','consignee_country');
		// frm.add_fetch('business','business_name','business_name');
	}
});
