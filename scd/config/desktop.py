# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		# Security Check Desk
		{
			"module_name": "Security Check Desk",
			"category": "Modules",
			"label": _("Security Check Desk"),
			"color": "#589494",
			"reverse": 1,
			"icon": "octicon octicon-briefcase",
			"type": "module",
			"description": "Managing Security Check Desk"
		},
	]
