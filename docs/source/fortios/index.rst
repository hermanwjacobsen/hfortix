FortiOS
=======

Complete Python SDK for FortiOS/FortiGate automation with 100% API coverage (750+ endpoints across 77 categories).

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: 🚀 Getting Started
        :link: getting-started/quickstart
        :link-type: doc

        Install and connect to your FortiGate in minutes.

    .. grid-item-card:: 📖 User Guide
        :link: user-guide/index
        :link-type: doc

        Learn core concepts and patterns.

    .. grid-item-card:: 📚 API Documentation
        :link: api-documentation/index
        :link-type: doc

        Convenience wrappers and complete endpoint reference.

    .. grid-item-card:: 📋 Topic Guides
        :link: guides/index
        :link-type: doc

        Advanced topics and patterns.

.. toctree::
   :maxdepth: 1
   :hidden:

   getting-started/quickstart
   getting-started/authentication
   user-guide/index
   api-documentation/index
   guides/index
   examples/index

Quick Example
-------------

.. code-block:: python

    from hfortix_fortios import FortiOS

    # Connect to FortiGate
    fgt = FortiOS(host="192.168.1.99", token="your-api-token")

    # Create firewall address
    fgt.api.cmdb.firewall.address.create(
        name="web-server",
        subnet="10.0.1.100/32",
        comment="Production web server"
    )

    # Create policy with convenience wrapper
    fgt.firewall.policy.create(
        name="Allow-Web-Traffic",
        srcintf=["internal"],
        dstintf=["wan1"],
        srcaddr=["all"],
        dstaddr=["web-server"],
        service=["HTTP", "HTTPS"],
        action="accept",
        nat=True
    )

    # Get system status
    status = fgt.api.monitor.system.status.get()
    print(f"Hostname: {status['hostname']}")
    print(f"Version: {status['version']}")

Key Features
------------

**Complete API Coverage**
    All 750+ FortiOS 7.6.5 API endpoints organized across 77 categories (CMDB, Monitor, Log, Service).

**Dual Interface Patterns**
    Use dict-style or kwargs-style - choose what fits your workflow.

**Full Async Support**
    All endpoints available in async/await with ``_async`` suffix.

**Convenience Wrappers**
    High-level wrappers for common operations: firewall policies, schedules, traffic shapers, IP/MAC bindings.

**Production Ready**
    Circuit breaker pattern, automatic retries, connection pooling, comprehensive validation.

**Developer Friendly**
    100% type hints, extensive documentation, rich error messages, validation framework.

Supported FortiOS Versions
---------------------------

- **FortiOS 7.6.x** - Full support
- **FortiOS 7.4.x** - Compatible
- **FortiOS 7.2.x** - Compatible
- **FortiOS 7.0.x** - Compatible
- **FortiOS 6.x** - Most features work

API Categories
--------------

The FortiOS API is organized into four main types:

**CMDB (Configuration)**
    37 categories for managing firewall configuration: addresses, policies, routes, VPN, system settings, etc.

**Monitor (Status/Stats)**
    32 categories for real-time monitoring: system status, interface stats, routing tables, VPN status, etc.

**Log (Historical Data)**
    Access to historical logs and events.

**Service (Operations)**
    Service operations like backups, restores, and maintenance tasks.

See :doc:`/fortios/api-reference/index` for complete category listing.

Next Steps
----------

1. **Install** - :doc:`/getting-started/installation`
2. **Quick Start** - :doc:`/fortios/getting-started/quickstart`
3. **Authentication** - :doc:`/fortios/getting-started/authentication`
4. **Browse Examples** - :doc:`/fortios/examples/index`
5. **Explore API** - :doc:`/fortios/api-reference/index`
