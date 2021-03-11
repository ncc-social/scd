frappe.views.calendar["Exporter"] = {
	options: {
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month'
		}
	},
    field_map: {
		"start": "birthday",
		"end": "birthday",
		"id": "name",
		"title": "exporter_name",
		"allDay": "allDay",
		"eventColor": "red"
	},
	get_events_method: "scd.security_check_desk.doctype.exporter.custom.get_events",
};