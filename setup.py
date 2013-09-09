#!/usr/bin/env python

from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
]

setup(
    name='django-shop-ceca',
    version="0.1.0",
    author='Jose Sanchez Moreno',
    author_email='jose@o2w.es',
    maintainer="Jose Sanchez Moreno",
    maintainer_email="jose@o2w.es",
    url='http://github.com/josesanch/django-shop-ceca',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating ceca tpv Payments',
    packages=find_packages(),
    include_package_data=True,
    long_description=open(os.path.join(os.path.dirname(__file__), 'readme.md')).read(),
    classifiers=CLASSIFIERS
)
