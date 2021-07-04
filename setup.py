#!/usr/bin/env python

# Copyright Tomer Figenblat.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Home Automation",
    ],
    license="Apache-2.0",
)
