frappe.views.calendar["Forwarder"] = {
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
		"title": "forwarder_name",
		"allDay": "allDay"
	},
	gantt: { // The values set here will override the values set in the object just for Gantt View
        order_by: "birthday",
    },
	get_events_method: "scd.security_check_desk.doctype.forwarder.custom.get_events",
};