# -*- coding: utf-8 -*-
# Copyright (c) 2021, NCC and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import getdate, validate_email_address, today, add_years, format_datetime, cstr
from frappe import throw, _, scrub

class Officer(Document):
	def validate(self):
		self.officer_name = ' '.join(filter(lambda x: x, [self.first_name, self.middle_name, self.last_name]))