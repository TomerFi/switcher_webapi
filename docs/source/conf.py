"""Configuration file for Sphinx Documentation Generator."""

import os
import sys

sys.path.insert(0, os.path.abspath('../../pyscripts'))

with open("../../VERSION", "r") as version_file:
    version = version_file.readline()

project = "Switcher Webapi"
copyright = "2019, Tomer Figenblat"
author = "Tomer Figenblat"
release = version
extensions = [
  "sphinx.ext.autodoc",
  "sphinx.ext.napoleon",
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
