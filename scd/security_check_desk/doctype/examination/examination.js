// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Examination', {
	
});

frappe.ui.form.on('Examination', {
	refresh: function(frm) {
		frm.set_query("import", function(frm, cdt, cdn) {
			return {
				filters: [
					["status", "=", "Tagged"]
				]
			}
		});
	}
});


frappe.ui.form.on('Examination', {
	refresh: function(frm) {
		frm.add_fetch('officer','officer_name','officer_name');
		frm.add_fetch('supervisor','supervisor_name','supervisor_name');
		frm.add_fetch('Cargo Import','flight_number','flight_number');
		frm.add_fetch('Cargo Import','flight_date','flight_date');
		frm.add_fetch('Cargo Import','awb','awb');
		frm.add_fetch('Cargo Import','weight','weight');
		frm.add_fetch('Cargo Import','description','description');
		frm.add_fetch('Cargo Import','arrival_date','arrival_date');
		// frm.add_fetch('exporter','phone_number','phone_number');
		// frm.add_fetch('exporter','exporter_photo','exporter_photo');
		frm.add_fetch('forwarder','forwarder_name','forwarder_name');
		// frm.add_fetch('consignee','consignee_name','consignee_name');
		// frm.add_fetch('consignee','consignee_country','consignee_country');
		// frm.add_fetch('business','business_name','business_name');
	}
});
