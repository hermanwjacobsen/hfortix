Package Details
===============

HFortix provides three packages that can be installed individually or together, depending on
your needs. Each package is published separately on PyPI and has its own documentation.

Package Selection Guide
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Package
     - Install When
     - Documentation
   * - ``hfortix``
     - You want the complete suite with all components
     - https://hfortix.readthedocs.io/
   * - ``hfortix-fortios``
     - You need FortiGate/FortiOS automation only
     - https://hfortix-fortios.readthedocs.io/
   * - ``hfortix-core``
     - You're building custom Fortinet integrations
     - https://hfortix-core.readthedocs.io/

hfortix (Meta Package)
----------------------

The meta-package that installs all HFortix components.

**What It Includes:**

* ``hfortix-fortios`` - Complete FortiOS/FortiGate API client
* ``hfortix-core`` - Foundation libraries and infrastructure

**Installation:**

.. code-block:: bash

   pip install hfortix

**Package Info:**

* **PyPI:** https://pypi.org/project/hfortix/
* **Repository:** https://github.com/hermanwjacobsen/hfortix
* **Documentation:** https://hfortix.readthedocs.io/

**When to Use:**

* Starting a new FortiGate automation project
* You want all available components
* Simplest installation - one command gets everything

hfortix-fortios
---------------

Complete FortiOS/FortiGate API client with full type safety and comprehensive endpoint coverage.

**Features:**

* **1,348 FortiOS 7.6.5 Endpoints** - Complete coverage of CMDB, Monitor, Log, and Service APIs
* **Full Type Safety** - Pydantic models and TypedDict definitions for all operations
* **Async/Await Support** - Both synchronous and asynchronous clients included
* **Batch Transactions** - Atomic configuration changes with automatic rollback
* **Rate Limiting** - Built-in rate limiting and retry logic for production use
* **Request Hooks** - Intercept and modify requests/responses for custom workflows
* **Audit Logging** - Enterprise-grade audit logging for compliance (SOC 2, HIPAA, PCI-DSS)

**Installation:**

.. code-block:: bash

   pip install hfortix-fortios

**Package Info:**

* **PyPI:** https://pypi.org/project/hfortix-fortios/
* **Repository:** https://github.com/hermanwjacobsen/hfortix-fortios
* **Documentation:** https://hfortix-fortios.readthedocs.io/

**Dependencies:**

* ``hfortix-core>=0.5.0`` - Foundation libraries
* ``httpx>=0.27.0`` - Modern HTTP client
* ``pydantic>=2.0.0`` - Data validation and type safety

**When to Use:**

* You need FortiOS/FortiGate automation
* You want complete API coverage with type safety
* Production deployments requiring enterprise features

**Example:**

.. code-block:: python

   from hfortix_fortios import FortiOS

   with FortiOS(host="192.168.1.99", token="your-token") as fgt:
       # Create firewall address
       fgt.api.cmdb.firewall.address.post(
           name="web-server",
           subnet="10.0.1.100/32"
       )
       
       # Get all policies
       policies = fgt.api.cmdb.firewall.policy.get()

hfortix-core
------------

Foundation libraries providing HTTP clients, audit logging, debugging, and shared utilities
used across all HFortix packages.

**Features:**

* **HTTP Client Framework** - FortiOS and FortiManager HTTP clients with retry logic and circuit breakers
* **Enterprise Audit Logging** - Syslog, file, and stream handlers with JSON, CEF, and RFC 5424 formats
* **Request Hooks Protocol** - Before/after request hooks for custom request/response handling
* **Exception Hierarchy** - 20+ exception types for granular error handling
* **Structured Logging** - JSON and text formatters for integration with enterprise logging systems
* **Debug Utilities** - Debug sessions, timing decorators, connection stats, and request inspection
* **Type Safety** - Comprehensive TypedDict definitions for all internal structures
* **Caching** - TTL-based cache for readonly reference data

**Installation:**

.. code-block:: bash

   pip install hfortix-core

**Package Info:**

* **PyPI:** https://pypi.org/project/hfortix-core/
* **Repository:** https://github.com/hermanwjacobsen/hfortix-core
* **Documentation:** https://hfortix-core.readthedocs.io/

**Dependencies:**

* ``httpx[http2]>=0.27.0`` - HTTP client with HTTP/2 support
* ``typing_extensions>=4.0.0`` - Enhanced type hints

**When to Use:**

* Building custom Fortinet API clients
* You need infrastructure without the full FortiOS client
* Developing extensions or integrations for HFortix
* You want just the HTTP client and logging capabilities

**Example:**

.. code-block:: python

   from hfortix_core.http import HTTPClient
   from hfortix_core.audit import SyslogHandler
   
   # Create custom FortiOS client
   client = HTTPClient(
       url="https://192.168.1.99",
       token="your-token",
       verify=True,
       max_retries=3
   )
   
   # Add audit logging
   client.audit_handler = SyslogHandler("siem.company.com:514")
   
   # Make API requests
   response = client.get("cmdb", "/api/v2/cmdb/system/global")

Dependency Chain
----------------

Understanding the dependency relationships:

.. code-block:: text

   hfortix (meta-package)
   ├── hfortix-fortios
   │   ├── hfortix-core
   │   │   ├── httpx[http2]>=0.27.0
   │   │   └── typing_extensions>=4.0.0
   │   ├── httpx>=0.27.0
   │   └── pydantic>=2.0.0
   └── hfortix-core (same as above)

**Key Points:**

* ``hfortix-core`` has minimal dependencies and can be used standalone
* ``hfortix-fortios`` requires ``hfortix-core`` for its HTTP client and utilities
* ``hfortix`` installs all components for a complete automation platform

Version Compatibility
---------------------

All HFortix packages use synchronized versioning. When installing, ensure version compatibility:

.. code-block:: bash

   # Install specific version across all packages
   pip install hfortix==0.5.156
   
   # Or install compatible versions individually
   pip install hfortix-core==0.5.156 hfortix-fortios==0.5.156

**Compatibility Matrix:**

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - hfortix
     - hfortix-fortios
     - hfortix-core
     - Python
   * - 0.5.156
     - 0.5.156
     - 0.5.156
     - 3.10+
   * - 0.5.x
     - 0.5.x
     - 0.5.x
     - 3.10+

   hfortix (meta)
   └── hfortix-fortios
       └── hfortix-core
           └── httpx[http2]
           └── typing-extensions

Installing ``hfortix-fortios`` automatically installs ``hfortix-core``.
Installing ``hfortix`` automatically installs both component packages.
