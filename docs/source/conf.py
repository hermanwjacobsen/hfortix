# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

# Add the packages to the Python path so autodoc can import them
sys.path.insert(0, os.path.abspath('../../packages/core'))
sys.path.insert(0, os.path.abspath('../../packages/fortios'))
sys.path.insert(0, os.path.abspath('../../packages/meta'))

# -- Project information -----------------------------------------------------
project = 'HFortix'
copyright = f'{datetime.now().year}, Herman W. Jacobsen'
author = 'Herman W. Jacobsen'

# The full version, including alpha/beta/rc tags
# Auto-detect version from package
try:
    from hfortix_fortios import __version__
    release = __version__  # Full version (e.g., 0.4.0)
    version = '.'.join(__version__.split('.')[:2])  # Short version (e.g., 0.4)
except ImportError:
    # Fallback if package not installed
    release = '0.4.0'
    version = '0.4'

# -- General configuration ---------------------------------------------------

extensions = [
    # Sphinx built-in extensions
    'sphinx.ext.autodoc',           # Auto-generate docs from docstrings
    'sphinx.ext.autosummary',       # Generate summary tables
    'sphinx.ext.napoleon',          # Support Google/NumPy docstring styles
    'sphinx.ext.viewcode',          # Add [source] links
    'sphinx.ext.intersphinx',       # Link to other project docs
    'sphinx.ext.todo',              # Support TODO directives
    'sphinx.ext.coverage',          # Check documentation coverage
    
    # Third-party extensions
    'myst_parser',                  # Markdown support
    'sphinx_copybutton',            # Copy button for code blocks
    'sphinx_design',                # Beautiful UI components
    'sphinx_autodoc_typehints',     # ⭐ CRITICAL - Type hints support
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# ⭐ Suppress warnings for specific patterns
suppress_warnings = [
    'myst.header',  # Suppress MyST header warnings
]

# Maximum depth for toctree
toctree_maxdepth = 3

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'pydata_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_url": "https://github.com/hermanwjacobsen/hfortix",
    "logo": {
        "text": "HFortix",
        "alt_text": "HFortix - Python SDK for Fortinet",
    },
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links", "theme-switcher"],
    "navbar_persistent": ["search-button"],
    "show_prev_next": True,
    "show_toc_level": 2,
    "navigation_with_keys": True,  # ✅ Accessibility: keyboard navigation
    "collapse_navigation": False,  # ✅ Accessibility: keep navigation expanded
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "use_edit_page_button": True,  # ✅ Show "Edit on GitHub" button
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom CSS files
html_css_files = [
    'custom.css',
]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs. This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "_static/favicon.ico"

# If true, "Created using Sphinx" is shown in the HTML footer.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer.
html_show_copyright = True

# -- SEO and GitHub Integration ----------------------------------------------

# Base URL for sitemap generation
html_baseurl = 'https://hfortix.readthedocs.io/'

# GitHub integration
html_context = {
    'display_github': True,
    'github_user': 'hermanwjacobsen',
    'github_repo': 'hfortix',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

# -- Options for autodoc -----------------------------------------------------

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
    'show-inheritance': True,
}

# Don't show type hints in signatures (they clutter the docs)
autodoc_typehints = 'description'

# Document __init__ methods
autoclass_content = 'both'

# ⭐ CRITICAL - Mock imports for packages that aren't installed during doc build
autodoc_mock_imports = []

# Preserve signature defaults
autodoc_preserve_defaults = True

# Don't skip __init__ docstrings
autodoc_class_signature = 'separated'

# -- Options for sphinx-autodoc-typehints ------------------------------------

# ⭐ CRITICAL - Type hints configuration
typehints_fully_qualified = False  # Use short names (FortiOS instead of hfortix_fortios.client.FortiOS)
always_document_param_types = True  # Always document parameter types
typehints_document_rtype = True  # Document return types
typehints_defaults = 'comma'  # Show defaults with commas
simplify_optional_unions = True  # Show Optional[str] instead of Union[str, None]

# -- Options for autosummary -------------------------------------------------

autosummary_generate = True  # ⭐ CRITICAL - auto-generates API docs
autosummary_generate_overwrite = True  # Overwrite existing generated files
autosummary_imported_members = False  # Don't document imported members
autosummary_ignore_module_all = False  # Respect __all__ in modules

# Generate stub pages for modules
autosummary_mock_imports = []

# -- Options for napoleon ----------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'requests': ('https://requests.readthedocs.io/en/latest/', None),
    'httpx': ('https://www.python-httpx.org/', None),
}

# -- Options for MyST parser -------------------------------------------------

myst_enable_extensions = [
    "colon_fence",      # ::: fences
    "deflist",          # Definition lists
    "fieldlist",        # Field lists
    "html_admonition",  # HTML admonitions
    "html_image",       # HTML images
    "linkify",          # Auto-detect URLs
    "replacements",     # Text replacements
    "smartquotes",      # Smart quotes
    "strikethrough",    # ~~strikethrough~~
    "substitution",     # Variable substitution
    "tasklist",         # Task lists
]

myst_heading_anchors = 3  # Auto-generate anchors for headings

# -- Options for todo extension ----------------------------------------------

todo_include_todos = True
