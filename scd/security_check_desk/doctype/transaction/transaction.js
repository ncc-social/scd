// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt



frappe.ui.form.on('Transaction', {
	refresh: function(frm) {
		cur_frm.add_fetch('exporter','exporter_name','exporter_name');
		cur_frm.add_fetch('forwarder','forwarder_name','forwarder_name');
		cur_frm.add_fetch('consignee','consignee_name','consignee_name');
		cur_frm.add_fetch('consignee','consignee_country','consignee_country');
	}
});
