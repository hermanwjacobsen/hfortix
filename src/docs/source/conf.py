# Configuration file for the Sphinx documentation builder.
# For hfortix (meta package)

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'HFortix'
copyright = f'{datetime.now().year}, Herman W. Jacobsen'
author = 'Herman W. Jacobsen'

try:
    from hfortix import __version__
    release = __version__
    version = '.'.join(__version__.split('.')[:2])
except ImportError:
    release = '0.5.154-beta'
    version = '0.5'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'navigation_depth': 2,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

html_context = {
    'display_github': True,
    'github_user': 'hermanwjacobsen',
    'github_repo': 'hfortix',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'hfortix-core': ('https://hfortix-core.readthedocs.io/en/latest/', None),
    'hfortix-fortios': ('https://hfortix-fortios.readthedocs.io/en/latest/', None),
}

# -- Napoleon settings -------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True
