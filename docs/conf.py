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

"""Configuration file for Sphinx Documentation Generator."""

from os import path as os_path
from sys import path as sys_path

sys_path.insert(0, os_path.abspath("../src"))
sys_path.insert(0, os_path.abspath("../tests"))

with open("../VERSION", "r") as version_file:
    version = version_file.readline()

project = "Switcher Webapi"
copyright = "2019, Tomer Figenblat"
author = "Tomer Figenblat"
release = version
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
exclude_patterns = ["_build"]
pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
language = "en"
show_authors = False
linkcheck_anchors = True

# sphinx.ext.todo configuration
todo_include_todos = True

# autodoc configuration
autodoc_mock_imports = [
    "aiohttp",
    "aioswitcher",
    "asyncio_throttle",
    "bs4",
    "pytest",
    "sanic",
]
