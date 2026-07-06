Package Details
===============

HFortix is a family of packages that can be installed individually or together, depending
on your needs. Each published package lives on PyPI and has its own documentation.

Package Selection Guide
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Package
     - Status
     - Install When
   * - ``hfortix``
     - Stable
     - You want the common suite (core + fortios; extras add the cloud services)
   * - ``hfortix-fortios``
     - Stable
     - You need FortiGate/FortiOS automation only
   * - ``hfortix-core``
     - Stable
     - You're building custom Fortinet integrations
   * - ``hfortix-forticare``
     - Stable
     - You need FortiCare asset management (registration, licensing, contracts)
   * - ``hfortix-fortiztp``
     - Stable
     - You need FortiZTP zero-touch provisioning
   * - ``hfortix-fortimanager``
     - Alpha (0.1.0)
     - You want an early preview of the FortiManager JSON-RPC client
   * - ``hfortix-fortianalyzer``
     - Coming soon
     - FortiAnalyzer JSON-RPC client — not yet published to PyPI

hfortix (Meta Package)
----------------------

The meta-package that installs the common HFortix components.

**What It Includes (base install):**

* ``hfortix-fortios`` - Complete FortiOS/FortiGate API client
* ``hfortix-core`` - Foundation libraries and infrastructure

**Optional Extras:**

* ``hfortix[fortios]`` - explicit FortiOS extra (same as the base install)
* ``hfortix[forticare]`` - adds ``hfortix-forticare`` (FortiCare asset management)
* ``hfortix[fortiztp]`` - adds ``hfortix-fortiztp`` (FortiZTP provisioning)
* ``hfortix[all]`` - adds fortios, forticare, and fortiztp
* ``hfortix[docs]`` - Sphinx toolchain for building this documentation

**Installation:**

.. code-block:: bash

   pip install hfortix           # core + fortios
   pip install "hfortix[all]"    # + forticare + fortiztp

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

hfortix-forticare
-----------------

FortiCare Asset Management REST API client (FortiCloud OAuth2).

**Features:**

* Product registration, licensing, contracts, and folder management
* OAuth2 authentication via ``api_id``/``password``, a pre-obtained token,
  or a shared ``CloudSession``
* Shares one FortiCloud login with ``hfortix-fortiztp`` through
  ``hfortix_core.session.CloudSession``

**Installation:**

.. code-block:: bash

   pip install hfortix-forticare
   # or as an extra of the meta package:
   pip install "hfortix[forticare]"

**Example:**

.. code-block:: python

   from hfortix_forticare import FortiCare

   fcc = FortiCare(api_id="your_api_id", password="your_password")
   products = fcc.api.products.list.post(serial_number="FGT*")

**Package Info:**

* **PyPI:** https://pypi.org/project/hfortix-forticare/

hfortix-fortiztp
----------------

FortiZTP Zero Touch Provisioning cloud API client (FortiCloud OAuth2).

**Features:**

* Device provisioning status and lifecycle management
* Pre-run CLI script management
* FortiManager integration settings
* Same authentication options as ``hfortix-forticare`` (credentials, token,
  or shared ``CloudSession``)

**Installation:**

.. code-block:: bash

   pip install hfortix-fortiztp
   # or as an extra of the meta package:
   pip install "hfortix[fortiztp]"

**Example:**

.. code-block:: python

   from hfortix_fortiztp import FortiZTP

   client = FortiZTP(api_id="your_api_id", password="your_password")
   devices = client.devices.get()
   status = client.system.system_get()

**Package Info:**

* **PyPI:** https://pypi.org/project/hfortix-fortiztp/

hfortix-fortimanager (Alpha)
----------------------------

FortiManager JSON-RPC API client. Published to PyPI as an **alpha preview**
(0.1.0) — the API surface may still change between releases.

**Features:**

* Generated endpoints from FortiManager 7.6.6 Swagger specs
* Hierarchical dot-navigation with full ``.pyi`` type stubs
* Session (username/password) or API-key authentication

**Installation:**

.. code-block:: bash

   pip install hfortix-fortimanager

**Example:**

.. code-block:: python

   from hfortix_fortimanager import FortiManager

   with FortiManager(host="fmg.example.com", username="admin", password="pw") as fmg:
       addresses = fmg.api.pm.config.adom.obj.firewall.address.get(adom="root")

**Package Info:**

* **PyPI:** https://pypi.org/project/hfortix-fortimanager/

hfortix-fortianalyzer (Coming Soon)
-----------------------------------

FortiAnalyzer JSON-RPC API client — the sibling of ``hfortix-fortimanager``,
built on the same shared JSON-RPC client from ``hfortix-core``. It is **not yet
published to PyPI**.

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
   ├── hfortix-core (same as above)
   ├── [forticare] → hfortix-forticare → hfortix-core
   └── [fortiztp]  → hfortix-fortiztp  → hfortix-core

**Key Points:**

* ``hfortix-core`` has minimal dependencies and can be used standalone
* Every other package requires ``hfortix-core`` for its HTTP client and utilities
* ``hfortix`` installs the common components; extras add the FortiCloud services
* ``hfortix-fortimanager`` / ``hfortix-fortianalyzer`` are installed separately
  (not pulled in by the meta package)

Version Compatibility
---------------------

The stable packages (``hfortix``, ``hfortix-core``, ``hfortix-fortios``,
``hfortix-forticare``, ``hfortix-fortiztp``) use synchronized ``0.5.x``
versioning, and the meta package declares minimum compatible versions of its
dependencies. In general, simply install the latest release:

.. code-block:: bash

   pip install --upgrade hfortix

   # Or upgrade individual packages together
   pip install --upgrade hfortix-core hfortix-fortios

``hfortix-fortimanager`` versions independently (``0.1.x`` alpha) and only
requires a compatible ``hfortix-core``.

Installing ``hfortix-fortios`` automatically installs ``hfortix-core``.
Installing ``hfortix`` automatically installs both, plus any extras you select.
