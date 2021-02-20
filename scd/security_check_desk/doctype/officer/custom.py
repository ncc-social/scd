from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cstr
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

@frappe.whitelist()
# Define the function to send Officer details to User doc
def create_user(officer, email):
    off = frappe.get_doc("Officer", officer)
    user_exist = frappe.db.exists("User", {"email": email})
    if user_exist:
        frappe.throw(_("Officer {0} already has User credentials").format(off.officer_name))
    # Load current Officer details into variable "off"
    
    # Create a new User
    user = frappe.new_doc("User")
    # Fill the User doc with details fetched from Officer doc
    user.first_name = off.first_name
    user.middle_name = off.middle_name
    user.last_name = off.last_name
    user.email = off.officer_email
    user.enabled = 1
    user.gender = off.gender
    user.phone = off.phone_number
    user.user_image = off.officer_photo
    user.send_welcome_email = 0
    # Details should be sent to officer.js file
    return user