from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cstr
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

@frappe.whitelist()
def create_forwarder(docname):
    forwarder_exist = frappe.db.exists("Forwarder", {"exporter_record": docname})
    if forwarder_exist:
        frappe.throw(_("Exporter already exists as a Forwarder"))

    exporter_info = frappe.get_doc("Exporter", docname)
    new_forwarder = frappe.new_doc("Forwarder")
    new_forwarder.first_name = exporter_info.first_name
    new_forwarder.middle_name = exporter_info.middle_name
    new_forwarder.last_name = exporter_info.last_name
    new_forwarder.forwarder_photo = exporter_info.exporter_photo
    new_forwarder.exporter_record = exporter_info.name
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

@frappe.whitelist()
def get_events(start, end, filters=None):
	"""Returns events for Gantt / Calendar view rendering.
	:param start: Start date-time.
	:param end: End date-time.
	:param filters: Filters (JSON).
	"""
	# from frappe.desk.calendar import get_event_conditions
	# conditions = get_event_conditions("Workshop", filters)

	data = frappe.db.sql("""select name, exporter_name, 
        concat(year(curdate()),"-", DATE_FORMAT(date_of_birth,'%m-%d')) as birthday 
        from tabExporter"""), as_dict=True)

	return data