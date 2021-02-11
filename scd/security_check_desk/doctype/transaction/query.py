from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

# @frappe.whitelist()
# def fetch_business(doctype, txt, searchfield, start, page_lan, filters):
# 	business = filters.get('business')
# 	result = frappe.db.sql("""
# 		SELECT
# 			a.business_name
# 		FROM
# 			`tabBusiness Authorisation` a
# 		WHERE
# 			a.parent = '{0}'
# 		""".format(forwarder))
# 	return result


@frappe.whitelist()
def fetch_business(doctype, txt, searchfield, start, page_len, filters):
	cond = "1=1"
	if filters.get('Buiness Authorisation'):
		cond += " and business = '{}'".format(filters.get('business'))
	# if filters.get('inspection_type'):
	# 	cond += " and inspection_type = '{}'".format(filters.get('inspection_type'))
	return frappe.db.sql("""select business_name  from `tabBusiness Authorisation` 
			where  {cond}""".format(cond=cond))