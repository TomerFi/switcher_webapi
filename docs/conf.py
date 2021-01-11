"""Configuration file for Sphinx Documentation Generator."""

from os import path as os_path
from sys import path as sys_path

sys_path.insert(0, os_path.abspath("../pyscripts"))

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
    "asynctest",
    "bs4",
    "pytest",
    "sanic",
]
