HFortix - Python SDK for Fortinet Products
===========================================

.. image:: https://badge.fury.io/py/hfortix.svg
   :target: https://pypi.org/project/hfortix/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.10+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.10+

.. image:: https://img.shields.io/badge/License-Proprietary-blue.svg
   :target: https://github.com/hermanwjacobsen/hfortix/blob/main/LICENSE
   :alt: License

.. image:: https://img.shields.io/badge/typing-typed-green.svg
   :target: https://peps.python.org/pep-0561/
   :alt: Typing: Typed

**HFortix** is a modern, fully-typed Python SDK ecosystem for Fortinet products.

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 🔥 FortiOS/FortiGate
      :link: fortios/index
      :link-type: doc

      Complete FortiOS API client with 750+ endpoints.
      **Available Now** - v0.4.0 Beta

   .. grid-item-card:: ⚙️ Core Framework
      :link: core/index
      :link-type: doc

      Foundation HTTP client and exception handling.
      **Available Now** - v0.4.0 Beta

.. warning::
   **BETA STATUS - Version 0.4.0**
   
   All implementations are functional but in **BETA**. APIs work correctly but may have incomplete
   parameter coverage or undiscovered edge cases. All packages remain in beta until version 1.0.0
   with comprehensive unit test coverage.

Key Features
------------

✨ **Complete API Coverage**
   100% coverage of FortiOS 7.6.5 API (750+ endpoints across 77 categories)

🎯 **Fully Typed**
   Complete type hints for excellent IDE support and type safety

⚡ **Modern & Fast**
   Async/await support with httpx, connection pooling, and circuit breakers

🛡️ **Production Ready**
   Comprehensive error handling, validation, retry logic, and logging

🔄 **Flexible Interface**
   Dual-pattern syntax supporting both dictionary and keyword arguments

🎨 **Convenience Wrappers**
   High-level wrappers for common tasks (firewall policies, schedules, services)

Quick Example - FortiOS
-----------------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect to FortiGate
   fgt = FortiOS("192.168.1.99", token="your_token_here")

   # Create firewall address
   fgt.api.cmdb.firewall.address.create(
       name='web-server',
       subnet='192.0.2.100/32',
       comment='Production web server'
   )

   # Use convenience wrapper for policy
   fgt.firewall.policy.create(
       name='Allow-Web',
       srcintf=['internal'],
       dstintf=['wan1'],
       srcaddr=['all'],
       dstaddr=['web-server'],
       service=['HTTPS'],
       action='accept',
       nat=True
   )

See :doc:`/fortios/getting-started/quickstart` for more examples.

Installation
------------

.. code-block:: bash

   # Install all available packages
   pip install hfortix
   
   # Or install specific packages
   pip install hfortix-fortios  # FortiOS/FortiGate
   pip install hfortix-core     # Core framework only

See :doc:`/getting-started/installation` for detailed instructions.

Documentation
-------------

.. toctree::
   :maxdepth: 2

   getting-started/overview
   getting-started/installation
   core/index
   fortios/index

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   changelog
   security
   license

Coverage Status
---------------

**FortiOS 7.6.5 API Coverage (December 2025)**

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: CMDB API
      :class-header: bg-success text-white

      37 of 37 categories
      ^^^
      **100% coverage** - 500+ endpoints
      
      🔷 Beta Status

   .. grid-item-card:: Monitor API
      :class-header: bg-success text-white

      32 of 32 categories
      ^^^
      **100% coverage** - 200+ endpoints
      
      🔷 Beta Status

   .. grid-item-card:: Log API
      :class-header: bg-success text-white

      5 of 5 categories
      ^^^
      **100% coverage** - Log reading functionality
      
      🔷 Beta Status

   .. grid-item-card:: Service API
      :class-header: bg-success text-white

      3 of 3 categories
      ^^^
      **100% coverage** - 21 methods
      
      🔷 Beta Status

**Overall: 77 of 77 categories (100% coverage) - 750+ API methods** 🎉

Package Status
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 15 15 40

   * - Package
     - Version
     - Status
     - Description
   * - ``hfortix`` (meta)
     - 0.4.0
     - Beta
     - Meta package - installs all available packages
   * - ``hfortix-core``
     - 0.4.0
     - Beta
     - Core HTTP client and exception framework
   * - ``hfortix-fortios``
     - 0.4.0
     - Beta
     - FortiOS/FortiGate API client (750+ endpoints)

Community & Support
-------------------

- **GitHub**: https://github.com/hermanwjacobsen/hfortix
- **Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **PyPI**: https://pypi.org/project/hfortix/

License
-------

Proprietary license. See the :doc:`/license` page for details.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
