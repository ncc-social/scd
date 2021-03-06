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
		_("Transaction Date") + ":Date:120",
        _("Exporter") + ":Data:150",
        _("Forwarder") + ":Data:150",
        _("Consignee") + ":Data:150",
        _("Quantity") + ":Int:50",
        _("Weight")+ ":Float:50",
		_("Cargo Description") + ":Data:200",
        _("Country") + ":Link/Country:120"
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
	consignee_country from tabTransaction where docstatus = 0 %s""" % conditions, as_list=1)

def get_conditions(filters):
	conditions = ""
	if filters.get("exporter_name"):
		conditions += " and exporter_name = '%s'"
	
	if filters.get("forwarder_name"):
		conditions += " and forwarder_name = '%s'"

	if filters.get("consignee_name"):
		conditions += " and consignee_name = '%s'"
	
	# if filters.get("month"):
	# 	month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
	# 		"Dec"].index(filters["month"]) + 1
	# 	conditions += " and month(date_of_birth) = '%s'" % month

	# if filters.get("company"): conditions += " and company = '%s'" % \
	# 	filters["company"].replace("'", "\\'")

	return conditions