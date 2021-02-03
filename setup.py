# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in scd/__init__.py
from scd import __version__ as version

setup(
	name='scd',
	version=version,
	description='Managing Security Check Desk',
	author='NCC',
	author_email='social@ncc.gov.gh',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
