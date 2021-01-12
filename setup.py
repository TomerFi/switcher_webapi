#!/usr/bin/env python

"""Module setup file.

This project is not to be distributed as a library, but as a docker image.
Please do not deploy this package,
this setup.py file was basically created to for testing purposes.
"""

from distutils.core import setup
from os import path

version = open(path.realpath("VERSION")).read().strip()

setup(
    name="switcher_webapi",
    version=version,
    author="Tomer Figenblat",
    author_email="tomer.figenblat@gmail.com",
    description="Switcher Water Heater Unofficial REST API",
    url="https://github.com/TomerFi/switcher_webapi",
    data_files=[(".", ["VERSION"])],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Home Automation",
    ],
    license="MIT",
)
