# -*- coding: utf-8 -*-
# Copyright (c) 2021, NCC and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Transaction(Document):
	pass
	# @frappe.whitelist()
	# def fetch_business(parent, year):
	# 	record = frappe.db.sql("""
	# 		select 
	# 			business 
	# 		from `tabBusiness Authorisation` 
	# 		where parent = %(parent)s and year =%(year)s
	# 	""", {
	# 		"parent": parent,
	# 		"year": "2021"
	# 	}, as_dict=1)
	# 	return record


# @frappe.whitelist()
#     def fetch_business(doctype, txt, searchfield, start, page_len, filters):
#         business = frappe.db.sql("select name,business_name from `tabBusiness Authorisation`")
#         return business