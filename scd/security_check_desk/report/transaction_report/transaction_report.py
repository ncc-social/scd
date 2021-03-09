# # Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# # For license information, please see license.txt

# from __future__ import unicode_literals
# from frappe import _
# import frappe

# def execute(filters=None):
# 	if not filters: filters = {}
	
# 	columns = get_columns(filters)
# 	data = get_data(filters)
# 	return columns, data

# def get_columns(filters):
# 	columns = [
# 		{
# 			"label": _("Transaction"),
# 			"fieldname": "name",
# 			"fieldtype": "Link",
# 			"options": "Transaction",
# 			"width": 100
# 		},
# 		{
# 			"label": _("Transaction Date"),
# 			"fieldname": "date_of_transaction",
# 			"fieldtype": "Date",
# 			"width": 100,
# 		},
# 		{
# 			"label": _("Exporter"),
# 			"fieldname": "exporter_name",
# 			"fieldtype": "Data",
# 			"width": 200
# 		},
#         {
# 			"label": _("Forwarder"),
# 			"fieldname": "forwarder_name",
# 			"fieldtype": "Data",
# 			"width": 200
# 		},
#         {
# 			"label": _("Consignee"),
# 			"fieldname": "consignee_name",
# 			"fieldtype": "Data",
# 			"width": 200
# 		},
# 		{
# 			"fieldname":"quantity",
# 			"label": _("Quantity"),
# 			"fieldtype": "Int",
# 			"width": 80
# 		},
# 		{
# 			"fieldname":"weight",
# 			"label": _("Weight"),
# 			"fieldtype": "Float",
# 			"width": 100,
# 			"precision": 2
# 		},
# 		{
# 			"label": _("Cargo Description"),
# 			"fieldname": "cargo_description",
# 			"fieldtype": "Data",
# 			"width": 200
# 		},
# 		{
# 			"label": _("Country"),
# 			"fieldname": "country",
# 			"fieldtype": "Data",
# 			"width": 100
# 		}
		
# 	]
# 	return columns

# def get_data(filters):
# 	conditions = get_conditions(filters)
# 	data = frappe.db.sql("""
# 		SELECT
# 			name,
# 			date_of_transaction,
# 			exporter_name,
# 			forwarder_name,
# 			consignee_name,
# 			quantity,
# 			weight,
# 			cargo_description,
# 			consignee_country
# 		FROM
# 			tabTransaction 
# 		WHERE
# 			1 = 1 {0}""".format(conditions), filters, as_dict=1)
# 	return data

# def get_conditions(filters):
# 	# conditions = []

# 	# if filters.get("exporter_name"):
# 	# 	conditions.append(" and exporter_name LIKE %(exporter_name)s")
    
# 	# if filters.get("forwarder_name"):
# 	# 	conditions.append(" and exporter_name LIKE %(forwarder_name)s")
	
# 	# if filters.get("consignee_name"):
# 	# 	conditions.append(" and exporter_name LIKE %(consignee_name)s")

# 	# return " ".join(conditions) if conditions else ""

# 	conditions = ""
# 	if filters.get("exporter_name"):
# 		conditions += " and exporter_name = %(exporter_name)s%"

# 	if filters.get("forwarder_name"):
# 		conditions += " and exporter_name LIKE %(forwarder_name)s%"

# 	if filters.get("consignee_name"):
# 		conditions += " and exporter_name LIKE %(consignee_name)s"

# 	return conditions

# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	if filters.to_date < filters.from_date:
		frappe.throw(_('"Date From" can not be greater than "Date To"'))

	columns = get_columns()
	data = get_data(filters)

	return columns, data

	# if not filters: filters = {}

	# columns = get_columns()
	# data = get_transactions(filters)

	# return columns, data

def get_columns():
	columns = [
		_("Transaction Date") + ":Date:100",
        _("Exporter") + ":Data:200",
        _("Forwarder") + ":Data:200",
        _("Consignee") + ":Data:200",
        _("Quantity") + ":Data:80",
        _("Weight")+ ":Float:100",
		_("Cargo Description") + ":Data:200",
        _("Country") + ":Data:100"
	]

	return columns

    # columns = [
    #     _("Transaction") + “:date:90”,
    #     _(“Remarks”) + “::200”,
    #     _(“Against Account”) + “::200”,
    #     _(“Amount”) + “:Float:100”,
    # ]
    # if filters.get("exporter"):
    #     columns += [
    #         _("Forwarder") + ":Data:200",
    #         _("Consignee")+ ":Data:100"
    #     ]
    #     columns += [
    #         _(“Voucher Type”) + “::120”
    #     ]
    # return columns

def get_data(filters):
	conditions = get_conditions(filters)

	records = frappe.db.sql("""select name, date_of_transaction, exporter_name, forwarder_name, 
	consignee_name, quantity, weight, cargo_description, consignee_country 
	from tabTransaction where date_of_transaction <= %(from_date)s AND date_of_transaction => %(to_date)s
	""", {
		"from_date": from_date,
		"to_date": to_date
	}, as_dict=1)
	
	return records

	
	# return frappe.db.sql("""select name, date_of_transaction, exporter_name, forwarder_name, consignee_name,
	# quantity, weight, cargo_description,
	# consignee_country from tabTransaction where 1 = 1 %s""" % conditions, as_list=1)


def get_conditions(filters):
	# conditions = ""
	# if filters.get("exporter_name"):
	# 	conditions += " and exporter_name LIKE '%%s%%'" % filters["exporter_name"]
	
	# if filters.get("forwarder_name"):
	# 	conditions += " and forwarder_name LIKE '%%s%%'" % filters["forwarder_name"]

	# if filters.get("consignee_name"):
	# 	conditions += " and consignee_name LIKE '%%s%%'" % filters["consignee_name"]
	
# def get_conditions(filters) :
# 	conditions = []

# 	if filters.get("territory"):
# 		conditions.append(" and `tabLead`.territory=%(territory)s")

# 	if filters.get("status"):
# 		conditions.append(" and `tabLead`.status=%(status)s")
	
# 	return " ".join(conditions) if conditions else ""
	
	# if filters.get("month"):
	# 	month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
	# 		"Dec"].index(filters["month"]) + 1
	# 	conditions += " and month(date_of_birth) = '%s'" % month

	# if filters.get("company"): conditions += " and company = '%s'" % \
	# 	filters["company"].replace("'", "\\'")
	conditions = []
	if filters.get('from_date'):
		conditions['from_date'] = filters.get('from_date')
	if filters.get('to_date'):
		conditions['to_date'] = filters.get('to_date')
	return conditions