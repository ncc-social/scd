frappe.form.link_formatters['Business Authorisation'] = function(value, doc) {
	if(doc && doc.business_name && doc.business_name !== value) {
		return value + ': ' + doc.business_name;
	} else {
		return value;
	}
}