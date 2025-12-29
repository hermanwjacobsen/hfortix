"""Setup configuration for HFortix - Python SDK for Fortinet Products."""

from pathlib import Path

from setuptools import find_packages, setup

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = []
with open("requirements.txt") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            requirements.append(line)

setup(
    name="hfortix",
    version="0.3.38",
    author="Herman W. Jacobsen",
    author_email="herman@wjacobsen.fo",
    description=(
        "HFortix - Python SDK for Fortinet products "
        "(FortiOS, FortiManager, FortiAnalyzer)"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermanwjacobsen/hfortix",
    packages=find_packages(exclude=["X", "X.*", "Tests", "Tests.*"]),
    # The project is packaged as the canonical `hfortix` namespace package.
    # No legacy top-level modules are shipped.
    package_data={
        "hfortix": ["py.typed"],
    },
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
        "Typing :: Typed",  # Indicate type hints are available
    ],
    python_requires=">=3.10",
    install_requires=requirements,
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
