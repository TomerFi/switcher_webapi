"""Configuration file for Sphinx Documentation Generator."""

from os import path as os_path
from sys import path as sys_path

sys_path.insert(0, os_path.abspath("../../pyscripts"))

with open("../../VERSION", "r") as version_file:
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
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = None
exclude_patterns = ["_build"]
pygments_style = "sphinx"
# html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
language = "en"

# autodoc configuration
autodoc_mock_imports = [
    "aiohttp",
    "aioswitcher",
    "asyncio_throttle",
    "asynctest",
    "bs4",
    "pytest",
    "sanic",
    "uvloop",
]
