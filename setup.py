"""
Setup configuration for Fortinet Python SDK
"""
from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = []
with open('requirements.txt') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            requirements.append(line)

setup(
    name="fortinet-sdk",
    version="0.1.0",
    author="Herman W. Jacobsen",
    author_email="herman@wjacobsen.fo",
    description="Python client library for Fortinet products (FortiOS, FortiManager, FortiAnalyzer)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermanwjacobsen/fortinet-sdk",
    packages=find_packages(exclude=['X', 'X.*', 'Tests', 'Tests.*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.5.0',
            'python-dotenv>=1.0.0',
        ],
    },
    keywords='fortinet fortigate fortios fortimanager fortianalyzer api sdk firewall security',
    project_urls={
        'Bug Reports': 'https://github.com/hermanwjacobsen/fortinet-sdk/issues',
        'Source': 'https://github.com/hermanwjacobsen/fortinet-sdk',
        'Documentation': 'https://github.com/hermanwjacobsen/fortinet-sdk/blob/main/README.md',
    },
)
