#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    README = None

setup(
    name='django-registration-templates',
    version='0.1',
    description='Default templates for django-registation and django.contrib.auth templates, including context variables passed to each and internationalization of strings.',
    long_description=README,
    author='Mathijs de Bruin',
    author_email='mathijs@mathijsfietst.nl',
    url='http://github.com/dokterbob/django-registration-templates',
    packages = find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
