frappe.query_reports["Transaction"] = {
	"filters": [
		{
			"fieldname":"exporter",
			"label": __("Exporter"),
			"fieldtype": "Link",
			"options": "Exporter"
		},
        {
			"fieldname":"forwarder",
			"label": __("Forwarder"),
			"fieldtype": "Link",
			"options": "Forwarder"
		},
        {
			"fieldname":"consignee",
			"label": __("Consignee"),
			"fieldtype": "Link",
			"options": "Consignee"
		}
	]
}