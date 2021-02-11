// Copyright (c) 2021, NCC and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Transaction", "onload", function(frm) {
//     cur_frm.set_query("business", function(doc) {
//         return {
//             "filters": [
// 				["Business Authorisation", "parent", "=", doc.forwarder],
// 				["Business Authorisation", "year", ">", "2016"]
// 			]
//         };
//     });
// });


frappe.ui.form.on('Transaction', {
	refresh: function(frm) {
		frm.set_query("business", function(frm, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				query: 'scd.security_check_desk.doctype.transaction.query.fetch_business',
				filters: [
					["Business Authorisation", "parent", "=", frm.forwarder],
					["Business Authorisation", "year", "=", "2016"]
				]
			}
		});
	}
});

// Link formatter sample from Employee
// frappe.form.link_formatters['Exporter'] = function(value, doc) {
//     if(doc.exporter_name && doc.exporter_name !== value) {
//         return value + ':/ ' + doc.exporter_name;
//     } else {
//         return value;
//     }
// }

// frappe.ui.form.on("Transaction", "refresh", function(frm) {
// 	cur_frm.fields_dict['Business'].grid.get_field('business_name').get_query = function(doc, cdt, cdn) {
// 		return {
// 			"filters": [
// 				["Business Authorisation", "parent", "=", doc.forwarder],
// 				["Business Authorisation", "year", ">", "2016"]
// 			]
// 		}
// 	}
// });



// cur_frm.fields_dict.business.get_query = function(doc) {
// 	return {
// 		filters: [
// 			["Business Authorisation", "parent", "=", doc.forwarder],
// 			["Business Authorisation", "year", "=", "2021"]
// 		]
// 	}
// }

frappe.ui.form.on('Transaction', {
	refresh: function(frm) {
		frm.add_fetch('exporter','exporter_name','exporter_name');
		frm.add_fetch('exporter','phone_number','phone_number');
		frm.add_fetch('forwarder','forwarder_name','forwarder_name');
		frm.add_fetch('consignee','consignee_name','consignee_name');
		frm.add_fetch('consignee','consignee_country','consignee_country');
		frm.add_fetch('business','business_name','business_name');
	}
});

// cur_frm.set_query("business", function(doc) {
// 	return {
// 		query: "scd.security_check_desk.doctype.transaction.transaction.fetch_business",
// 		"filters": [
// 			["Business Authorisation", "parent", "=", doc.forwarder],
// 			["Business Authorisation", "year", "=", "2021"]
// 		]
// 	}
// });
