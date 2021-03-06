# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_transactions(filters)

	return columns, data

def get_columns():
	return [
		_("Transaction Date") + ":Date:100",
        _("Exporter") + ":Data:200",
        _("Forwarder") + ":Data:200",
        _("Consignee") + ":Data:200",
        _("Quantity") + ":Data:100",
        _("Weight")+ ":Float:100",
		_("Cargo Description") + ":Data:200",
        _("Country") + ":Data:100"
	]

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

def get_transactions(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select date_of_transaction, exporter_name, forwarder_name, consignee_name,
	quantity, weight, cargo_description,
	consignee_country from tabTransaction where 1 = 1 %s""" % conditions, filters)

def get_conditions(filters):
	conditions = ""
	if filters.get("exporter_name"):
		conditions += " and exporter_name LIKE '%%s%%'" % filters["exporter_name"]
	
	if filters.get("forwarder_name"):
		conditions += " and forwarder_name LIKE '%%s%%'" % filters["forwarder_name"]

	if filters.get("consignee_name"):
		conditions += " and consignee_name LIKE '%%s%%'" % filters["consignee_name"]
	
	# if filters.get("month"):
	# 	month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
	# 		"Dec"].index(filters["month"]) + 1
	# 	conditions += " and month(date_of_birth) = '%s'" % month

	# if filters.get("company"): conditions += " and company = '%s'" % \
	# 	filters["company"].replace("'", "\\'")

	return conditions