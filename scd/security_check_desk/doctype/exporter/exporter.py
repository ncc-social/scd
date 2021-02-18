# -*- coding: utf-8 -*-
# Copyright (c) 2021, NCC and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import getdate, validate_email_address, today, add_years, format_datetime, cstr
from frappe import throw, _, scrub

class Exporter(Document):
	def validate(self):
		self.set_exporter_name()
		self.validate_date()
		self.validate_email()

	def set_exporter_name(self):
		self.exporter_name = ' '.join(filter(lambda x: x, [self.first_name, self.middle_name, self.last_name]))

	def validate_date(self):
		if self.date_of_birth and getdate(self.date_of_birth) >= getdate(today()):
			throw(_("Date of Birth cannot be today or a future date."))
	
	def validate_email(self):
		if self.personal_email:
			validate_email_address(self.personal_email, True)

@frappe.whitelist()
def create_forwarder(docname):
	forwarder_exist = frappe.db.exists("Forwarder", {"exporter_record": docname})
	if forwarder_exist:
		frappe.throw(_("Exporter {0} already exists as a Forwarder").format(exporter))

	exporter_info = frappe.get_doc("Exporter", docname)
	new_forwarder = frappe.new_doc("Forwarder")
	new_forwarder.first_name = exporter_info.first_name
	new_forwarder.middle_name = exporter_info.middle_name
	new_forwarder.last_name = exporter_info.last_name
	new_forwarder.forwarder_photo = exporter_info.exporter_photo
	new_forwarder.date_of_birth = exporter_info.date_of_birth
	new_forwarder.place_of_birth = exporter_info.place_of_birth
	new_forwarder.region_place_of_birth = exporter_info.region_place_of_birth
	new_forwarder.hometown = exporter_info.hometown
	new_forwarder.region_hometown = exporter_info.region_hometown
	new_forwarder.residential_address = exporter_info.residential_address
	new_forwarder.popular_landmark = exporter_info.popular_landmark
	new_forwarder.postal_address = exporter_info.postal_address
	new_forwarder.phone_number = exporter_info.phone_number
	new_forwarder.personal_email = exporter_info.personal_email
	new_forwarder.id_type = exporter_info.id_type
	new_forwarder.id_number = exporter_info.id_number
	new_forwarder.photo_id = exporter_info.photo_id
	new_forwarder.fingerprint_impressions = exporter_info.fingerprint_impressions

    return new_forwarder.as_dict()