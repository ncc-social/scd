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
		"allDay": "allDay"
	}
	// get_events_method: "frappe.desk.calendar.get_events",
};