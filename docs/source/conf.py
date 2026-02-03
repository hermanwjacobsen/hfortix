# Configuration file for the Sphinx documentation builder.
# For hfortix meta-package

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'HFortix'
copyright = f'{datetime.now().year}, Herman W. Jacobsen'
author = 'Herman W. Jacobsen'

# The full version, including alpha/beta/rc tags
release = '0.5.156'
version = '0.5'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
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

suppress_warnings = ['myst.header']
toctree_maxdepth = 3

# Performance optimizations
import multiprocessing

# Use all available cores for parallel processing
num_cores = multiprocessing.cpu_count()
parallel_read = num_cores
parallel_write = num_cores

# Reduce memory usage
keep_warnings = 10  # Only keep last 10 warnings

# Disable slow features for ReadTheDocs builds
if os.environ.get('READTHEDOCS') == 'True':
    # Skip intersphinx inventory loading (slow)
    intersphinx_timeout = 5
    # Optimize navigation
    html_theme_options = {
        'navigation_depth': 4,
        'collapse_navigation': False,  # Keep expanded
        'sticky_navigation': True,
        'includehidden': True,
        'titles_only': False,
    }
else:
    html_theme_options = {
        'navigation_depth': 4,
        'collapse_navigation': False,
        'sticky_navigation': True,
        'includehidden': True,
        'titles_only': False,
    }

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# html_theme_options defined above based on environment

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
napoleon_include_init_with_doc = True
