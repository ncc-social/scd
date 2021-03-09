// Copyright (c) 2016, NCC and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Transaction Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("Date From"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"to_date",
			"label": __("Date To"),
			"fieldtype": "Date"
		}
	]
};
