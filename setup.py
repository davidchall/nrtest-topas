#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# extensions
entry_points = {
    'nrtest.compare': [
        'topas binned=nrtest_topas:topas_binned_compare',
        'topas ntuple=nrtest_topas:topas_ntuple_compare',
    ]
}

setup(
    name='nrtest-topas',
    version='0.1.0',
    description="TOPAS extensions for nrtest",
    author="David Hall",
    author_email='dhcrawley@gmail.com',
    url='https://github.com/davidchall/nrtest-topas',
    packages=[
        'nrtest_topas',
    ],
    entry_points=entry_points,
    include_package_data=True,
    install_requires=[
        'nrtest>=0.2.0',
        'numpy>=1.6.0',
        'topas2numpy',
    ]
)
