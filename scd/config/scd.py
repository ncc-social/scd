from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Security Check Desk"),
			"icon": "octicon octicon-book",
			"items": [
				{
					"type": "doctype",
					"name": "Exporter",
					"label": _("Exporter"),
					"description": _("Manage Exporters"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Forwarder",
					"label": _("Forwarder"),
					"description": _("Manage Forwarders"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Consignee",
					"label": _("Consignee"),
					"description": _("Manage Consignees"),
					"onboard": 1,
				},
			]
        },
	] 