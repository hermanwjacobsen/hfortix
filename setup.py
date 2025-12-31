"""Setup configuration for HFortix - Meta-package for Fortinet Products.

This is a meta-package that installs all HFortix components.
The actual implementation is in the modular packages:
- hfortix-core: Core exceptions and HTTP framework
- hfortix-fortios: FortiOS/FortiGate client
"""

from pathlib import Path

from setuptools import setup

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="hfortix",
    version="0.4.0.dev1",
    author="Herman W. Jacobsen",
    author_email="herman@wjacobsen.fo",
    description=(
        "Meta-package for HFortix - Python SDK for Fortinet products "
        "(FortiOS, FortiManager, FortiAnalyzer)"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermanwjacobsen/hfortix",
    # Meta-package: no code, just dependencies
    packages=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.10",
    # Meta-package just depends on the actual packages
    install_requires=[
        "hfortix-core>=0.4.0.dev1",
        "hfortix-fortios>=0.4.0.dev1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "python-dotenv>=1.0.0",
        ],
    },
    keywords=(
        "hfortix fortinet fortigate fortios fortimanager fortianalyzer "
        "api sdk firewall security"
    ),
    project_urls={
        "Bug Reports": "https://github.com/hermanwjacobsen/hfortix/issues",
        "Source": "https://github.com/hermanwjacobsen/hfortix",
        "Documentation": (
            "https://github.com/hermanwjacobsen/hfortix/blob/main/README.md"
        ),
    },
)
