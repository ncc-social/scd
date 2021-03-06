# -*- coding: utf-8 -*-
# Copyright (c) 2021, NCC and contributors
# For license information, please see license.txt

import frappe, re
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class BusinessAuthorisation(Document):
	def autoname(self):
		prefix = re.sub('-+', '-', self.business_name.replace(' ', '-'))
		self.name = make_autoname(prefix + '-.###')


