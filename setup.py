#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='anybinding',
    version='v2.0.2',
    packages=['anybinding', ],
    license='MIT',
    author="guangrei",
    author_email="myawn@pm.me",
    description="any command line program binding to python.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="command binding",
    url="https://github.com/guangrei/Anypybinding",
)
