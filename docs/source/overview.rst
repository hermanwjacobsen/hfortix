Overview
========

**HFortix** is the complete suite of Python SDKs for Fortinet automation. This meta-package provides
a unified installation of all HFortix components, making it simple to get started with FortiGate,
FortiManager, and FortiAnalyzer automation.

Key Features
------------

**Complete API Coverage**
   Access to 1,348+ FortiOS endpoints with full type hints and IDE autocomplete support.

**Fully Typed**
   Complete type safety with Pydantic models, TypedDict definitions, and comprehensive type hints
   for all API operations and responses.

**Modern & Fast**
   Built on modern async/await patterns with HTTP/2 support, connection pooling, and optimized
   performance for high-throughput scenarios.

**Production Ready**
   Enterprise-grade error handling, retry logic, circuit breakers, audit logging, and comprehensive
   debugging tools for production deployments.

**Simplified Syntax**
   Pythonic API with automatic conversion to FortiOS format - use underscores instead of hyphens,
   pass dictionaries instead of JSON strings.

**Batch Transactions**
   Atomic configuration changes with automatic rollback on errors, perfect for complex multi-step
   deployments.

What's Included
---------------

When you install ``hfortix``, you get access to:

**hfortix-fortios**
   Complete FortiOS/FortiGate API client with support for all CMDB, monitor, log, and service
   endpoints. Includes both synchronous and asynchronous clients.

**hfortix-core**
   Foundation libraries providing HTTP clients, audit logging, request hooks, exception handling,
   debugging utilities, and shared infrastructure used across all HFortix packages.

Architecture
------------

HFortix follows a modular architecture where each component can be used independently or together:

.. code-block:: text

   hfortix (meta-package)
   ├── hfortix-fortios (FortiOS/FortiGate client)
   │   └── hfortix-core (foundation)
   ├── hfortix-fortimanager (coming soon)
   │   └── hfortix-core
   └── hfortix-fortianalyzer (coming soon)
       └── hfortix-core

This design allows you to:

* Install only what you need (e.g., just ``hfortix-fortios``)
* Use ``hfortix-core`` for custom integrations
* Get everything with a single ``pip install hfortix``

Quick Example
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect to FortiGate
   with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
       # Get system status
       status = fgt.api.monitor.system.status.get()
       print(f"Hostname: {status['hostname']}")
       
       # Create firewall address
       fgt.api.cmdb.firewall.address.post(
           name="web-server",
           subnet="10.0.1.100/32"
       )

Component Documentation
-----------------------

For detailed documentation on each component, visit:

* `HFortix-FortiOS Documentation <https://hfortix-fortios.readthedocs.io/>`_ - Complete FortiGate API reference
* `HFortix-Core Documentation <https://hfortix-core.readthedocs.io/>`_ - Foundation library reference

Use Cases
---------

**Network Automation**
   Automate FortiGate configuration changes, policy updates, and firewall management across
   hundreds of devices.

**Security Compliance**
   Audit firewall configurations, enforce security policies, and generate compliance reports
   with comprehensive audit logging.

**Infrastructure as Code**
   Define FortiGate configurations in code with type-safe APIs, version control, and automated
   deployment pipelines.

**Monitoring & Analytics**
   Collect real-time statistics, monitor system health, and integrate FortiGate data into
   your observability platforms.

**Multi-Device Management**
   Manage large FortiGate deployments with batch operations, parallel execution, and centralized
   error handling.

Getting Started
---------------

1. **Install HFortix:**

   .. code-block:: bash

      pip install hfortix

2. **Generate an API Token:**

   On your FortiGate, create an API user with appropriate permissions:

   .. code-block:: text

      config system api-user
          edit "automation"
              set api-key <your-token>
              set accprofile "super_admin"
              config trusthost
                  edit 1
                      set ipv4-trusthost 192.168.1.0/24
                  next
              end
          next
      end

3. **Start Automating:**

   See the `HFortix-FortiOS Documentation <https://hfortix-fortios.readthedocs.io/>`_ for
   comprehensive examples and API reference.

Community & Support
-------------------

* **Documentation:** https://hfortix.readthedocs.io/
* **PyPI:** https://pypi.org/project/hfortix/
* **Issues:** https://github.com/hermanwjacobsen/hfortix/issues
* **Source Code:** https://github.com/hermanwjacobsen/hfortix
