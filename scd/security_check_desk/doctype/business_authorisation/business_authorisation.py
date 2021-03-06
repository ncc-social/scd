# -*- coding: utf-8 -*-
# Copyright (c) 2021, NCC and contributors
# For license information, please see license.txt

import frappe, re
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class BusinessAuthorisation(Document):
	def autoname(self):
		self.name = self.business_name + "(" + "hash" + ")"


