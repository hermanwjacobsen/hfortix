HFortix - Python SDK for Fortinet Products
===========================================

.. image:: https://badge.fury.io/py/hfortix.svg
   :target: https://pypi.org/project/hfortix/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.10+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.10+

.. image:: https://img.shields.io/badge/typing-typed-green.svg
   :target: https://peps.python.org/pep-0561/
   :alt: Typing: Typed

**HFortix** is a modern, fully-typed Python SDK ecosystem for Fortinet products.

This meta package installs all available HFortix packages for easy setup.

Quick Installation
------------------

.. code-block:: bash

   # Install all available packages
   pip install hfortix
   
   # Or install specific packages
   pip install hfortix-fortios  # FortiOS/FortiGate
   pip install hfortix-core     # Core framework only

Available Packages
------------------

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 🔥 HFortix-FortiOS
      :link: https://hfortix-fortios.readthedocs.io
      :link-type: url

      Complete FortiOS/FortiGate API client with 1,348 endpoints.
      
      **Status:** v0.5.154 Beta
      
      **📚 Documentation:** https://hfortix-fortios.readthedocs.io

   .. grid-item-card:: ⚙️ HFortix-Core
      :link: https://hfortix-core.readthedocs.io
      :link-type: url

      Foundation HTTP client and shared utilities.
      
      **Status:** v0.5.154 Beta
      
      **📚 Documentation:** https://hfortix-core.readthedocs.io

Key Features
------------

✨ **Complete API Coverage**
   100% coverage of FortiOS 7.6.5 API (1,348 endpoints)

🎯 **Fully Typed**
   Complete type hints with .pyi stubs for excellent IDE support

⚡ **Modern & Fast**
   Async/await support with httpx, HTTP/2, connection pooling

🛡️ **Production Ready**
   Comprehensive error handling, validation, retry logic, rate limiting

Quick Example - FortiOS
-----------------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect with context manager (automatic cleanup)
   with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
       # Create firewall address
       fgt.api.cmdb.firewall.address.post(
           name="web-server",
           subnet="10.0.1.100/32",
           comment="Production web server"
       )

       # Create firewall policy - simple list format (auto-converted)
       fgt.api.cmdb.firewall.policy.post(
           name="Allow-Web-Traffic",
           srcintf=["internal"],
           dstintf=["wan1"],
           srcaddr=["all"],
           dstaddr=["web-server"],
           service=["HTTP", "HTTPS"],
           action="accept",
           nat="enable"
       )

For more examples, see the `FortiOS documentation <https://hfortix-fortios.readthedocs.io>`_.

Package Documentation
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Package
     - Version
     - Documentation
   * - ``hfortix`` (meta)
     - 0.5.154
     - This page
   * - ``hfortix-core``
     - 0.5.154
     - https://hfortix-core.readthedocs.io
   * - ``hfortix-fortios``
     - 0.5.154
     - https://hfortix-fortios.readthedocs.io

Community & Support
-------------------

- **GitHub**: https://github.com/hermanwjacobsen/hfortix
- **Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **PyPI**: https://pypi.org/project/hfortix/

License
-------

Proprietary license. All rights reserved.
