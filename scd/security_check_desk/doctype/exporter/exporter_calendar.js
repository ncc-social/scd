frappe.views.calendar["Exporter"] = {
	options: {
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month'
		}
	},
    field_map: {
		"start": "date_of_birth",
		"end": "date_of_birth",
		"id": "name",
		"title": "exporter_name",
		"status": "status",
        "allDay": "allDay"
	}
	// get_events_method: "erpnext.hr.doctype.attendance.attendance.get_events"
};