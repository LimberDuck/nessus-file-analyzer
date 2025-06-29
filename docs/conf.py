# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'nessus file analyzer (NFA)'
copyright = '2018-2025, Damian Krawczyk'
author = 'Damian Krawczyk'

# The full version, including alpha/beta/rc tags
release = '0.6.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    # "sphinxcontrib.mermaid",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

rst_prolog = """
.. nessus-file-analyzer:
.. |nfa| replace:: :abbr:`nfa (nessus-file-analyzer by Limberduck)`
.. _nessus-file-analyzer: https://github.com/LimberDuck/nessus-file-analyzer
.. _nessus-file-analyzer doc: https://nessus-file-analyzer.readthedocs.io

.. nessus-file-reader:
.. |nfr| replace:: :abbr:`nfr (nessus-file-reader by Limberduck)`
.. _nessus-file-reader: https://github.com/LimberDuck/nessus-file-reader
.. _nessus-file-reader doc: https://nessus-file-reader.readthedocs.io

.. Technology:
.. |OS| replace:: :abbr:`OS (Operating System)`
.. |RMB| replace:: :abbr:`RMB (Right Mouse Button)`
.. |FQDN| replace:: :abbr:`FQDN (Fully Qualified Domain Name)`
.. |IP| replace:: :abbr:`IP (Intrnet Protocol Address)`

.. Security:
.. |CVE| replace:: :abbr:`CVE (Common Vulnerabilities and Exposures)`

"""