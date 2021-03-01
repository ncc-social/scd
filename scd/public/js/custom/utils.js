frappe.form.link_formatters['Forwarder'] = function(value, doc) {
	if(doc && doc.forwarder_name && doc.forwarder_name !== value) {
		return value + ': ' + doc.forwarder_name;
	} else {
		return value;
	}
}