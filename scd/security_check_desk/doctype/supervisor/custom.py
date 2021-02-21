from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cstr
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

@frappe.whitelist()
# Define the function to send supervisor details to User doc
def create_user(supervisor, email):
    # Load current supervisor details into variable "sup"sup = frappe.get_doc("supervisor", supervisor)
    user_exist = frappe.db.exists("User", {"email": email})
    if user_exist:
        frappe.throw(_("Supervisor {0} already has User credentials").format(sup.supervisor_name))
    
    # Create a new User
    user = frappe.new_doc("User")
    # Fill the User doc with details fetched from supervisor doc
    user.first_name = sup.first_name
    user.middle_name = sup.middle_name
    user.last_name = sup.last_name
    user.email = sup.supervisor_email
    user.enabled = 1
    user.gender = sup.gender
    user.phone = sup.phone_number
    user.user_image = sup.supervisor_photo
    user.send_welcome_email = 0
    # Details should be sent to supervisor.js file
    return user