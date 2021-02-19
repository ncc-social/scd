frappe.listview_settings['Cargo Import'] = {
	add_fields: ["status", "awb", "origin", "destination"],
	get_indicator: function(doc) {
		var indicator = [__(doc.status), frappe.utils.guess_colour(doc.status), "status,=," + doc.status];
		indicator[1] = {"Tagged": "red", "Untagged": "blue"}[doc.status];
		return indicator;
	}
};