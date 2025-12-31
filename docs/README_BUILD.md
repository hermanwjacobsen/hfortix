# Building the Documentation

This directory contains the Sphinx documentation for HFortix.

## Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Build HTML Documentation

```bash
cd docs
make html
```

The built documentation will be in `build/html/`. Open `build/html/index.html` in your browser.

### Live Rebuild (Development)

For automatic rebuilding while editing:

```bash
cd docs
make livehtml
```

Then open http://127.0.0.1:8000 in your browser. The page will automatically refresh when you save changes.

## Available Build Formats

```bash
make html      # HTML documentation
make pdf       # PDF via LaTeX
make epub      # ePub for e-readers
make linkcheck # Check for broken links
make clean     # Remove build directory
```

## Documentation Structure

```
docs/
├── source/              # Documentation source files
│   ├── conf.py         # Sphinx configuration
│   ├── index.rst       # Main landing page
│   │
│   ├── getting-started/
│   │   ├── installation.md
│   │   ├── quickstart.md
│   │   └── authentication.md
│   │
│   ├── user-guide/
│   │   └── ...
│   │
│   ├── guides/
│   │   └── ...
│   │
│   ├── api-reference/
│   │   ├── core.rst
│   │   └── fortios.rst
│   │
│   ├── examples/
│   │   └── ...
│   │
│   ├── _static/        # Custom CSS, images
│   └── _templates/     # Custom HTML templates
│
├── build/              # Generated documentation (gitignored)
├── requirements.txt    # Sphinx dependencies
└── Makefile           # Build commands
```

## Read the Docs

This documentation is automatically built and hosted on Read the Docs when pushed to GitHub.

Configuration: `.readthedocs.yaml` in project root

- **Public URL**: https://hfortix.readthedocs.io/
- **Builds**: Automatically built on every commit to main branch
- **Versions**: Supports multiple versions (latest, stable, v0.4.0, etc.)

## Writing Documentation

### Adding a New Page

1. Create a `.md` or `.rst` file in the appropriate directory
2. Add it to a `toctree` in the parent `index.rst` or `index.md`
3. Build to verify it appears correctly

### Markdown vs reStructuredText

- **Markdown (`.md`)**: Easier to write, good for narrative content
- **reStructuredText (`.rst`)**: Better for API references, more Sphinx features

Use markdown for guides and RST for API documentation.

### Code Examples

Use code blocks with syntax highlighting:

````markdown
```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token')
```
````

### Cross-References

Link to other pages:

```markdown
See the [Installation Guide](../getting-started/installation.md)
```

Link to API documentation:

```rst
:class:`hfortix_fortios.FortiOS`
:meth:`hfortix_fortios.FortiOS.api`
```

### Admonitions

Use note, warning, tip, etc.:

````markdown
```{note}
This is a note.
```

```{warning}
This is a warning.
```

```{tip}
This is a tip.
```
````

## Troubleshooting

### Import Errors

If you get import errors when building:

```bash
# Make sure packages are installed
pip install -e ../../packages/core
pip install -e ../../packages/fortios
```

### Broken Links

Check for broken links:

```bash
make linkcheck
```

### Build Warnings

Run with warnings as errors to catch issues:

```bash
SPHINXOPTS="-W" make html
```

## Contributing

When adding new features to HFortix:

1. Add docstrings to all public classes and methods
2. Update relevant documentation pages
3. Add examples if appropriate
4. Build docs locally to verify changes
5. Commit documentation with code changes

## Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Parser](https://myst-parser.readthedocs.io/)
- [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/)
- [Read the Docs](https://docs.readthedocs.io/)
