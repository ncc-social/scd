# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"label": _("Transaction Date"),
			"fieldname": "date_of_transaction",
			"fieldtype": "Date",
			"width": 100,
		},
		{
			"label": _("Exporter"),
			"fieldname": "exporter_name",
			"fieldtype": "Data",
			"width": 200
		},
        {
			"label": _("Forwarder"),
			"fieldname": "forwarder_name",
			"fieldtype": "Data",
			"width": 200
		},
        {
			"label": _("Consignee"),
			"fieldname": "consignee_name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname":"quantity",
			"label": _("Quantity"),
			"fieldtype": "Int",
			"width": 80
		},
		{
			"fieldname":"weight",
			"label": _("Weight"),
			"fieldtype": "Float",
			"width": 100
		},
		{
			"label": _("Cargo Description"),
			"fieldname": "cargo_description",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Country"),
			"fieldname": "country",
			"fieldtype": "Data",
			"width": 100
		}
		
	]
	return columns

def get_data(filters):
	return frappe.db.sql("""
		SELECT
			date_of_transaction,
			exporter_name,
			forwarder_name,
			consignee_name,
			quantity,
			weight,
			cargo_description,
			consignee_country
		FROM
			tabTransaction
		WHERE
			1 = 1 {conditions}""".format(conditions=get_conditions(filters)), filters, as_dict=1)

def get_conditions(filters) :
	conditions = []

	if filters.get("exporter_name"):
		conditions.append(" and and exporter_name LIKE %(exporter_name)s")
    
	if filters.get("forwarder_name"):
		conditions.append(" and and exporter_name LIKE %(forwarder_name)s")
	
	if filters.get("consignee_name"):
		conditions.append(" and and exporter_name LIKE %(consignee_name)s")

	return " ".join(conditions) if conditions else ""