# pylint: disable=invalid-name,redefined-builtin

"""Configuration file for Sphinx Documentation Generator."""

project = 'SwitcherDockerizedWbapi'
copyright = "2019, Tomer Figenblat"
author = "Tomer Figenblat"
templates_path = ['_templates']
html_theme = 'alabaster'
html_static_path = ['_static']
language = 'en'

with open('../../VERSION', 'r') as version_file:
    version = version_file.readline()

release = version
