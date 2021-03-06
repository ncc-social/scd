// Copyright (c) 2016, NCC and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Transaction Report"] = {
	"filters": [
		{
			"fieldname":"exporter_name",
			"label": __("Exporter"),
			"fieldtype": "Data"
		},
        {
			"fieldname":"forwarder_name",
			"label": __("Forwarder"),
			"fieldtype": "Data"
		},
        {
			"fieldname":"consignee_name",
			"label": __("Consignee"),
			"fieldtype": "Data"
		}
	]
};
