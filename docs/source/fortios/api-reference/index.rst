API Reference
=============

Complete low-level API documentation for all 750+ FortiOS endpoints organized by category.
These endpoints use HTTP methods (GET, POST, PUT, DELETE) for direct API access.

CMDB API (Configuration)
-------------------------

.. toctree::
   :maxdepth: 1

   cmdb/index

Monitor API (Status & Statistics)
----------------------------------

.. toctree::
   :maxdepth: 1

   monitor/index

Log API (Historical Data)
--------------------------

.. toctree::
   :maxdepth: 1

   log/index

Service API (Operations)
-------------------------

.. toctree::
   :maxdepth: 1

   service/index

Overview
--------

The FortiOS API is organized into four main categories:

CMDB API - Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Configuration Management Database (CMDB)** API provides access to all FortiOS configuration settings.
This includes 37 categories covering:

- **Firewall**: Addresses, policies, services, VIPs, schedules
- **System**: Global settings, interfaces, routing, admin users
- **VPN**: IPsec, SSL VPN, certificates
- **Wireless**: WiFi controllers, APs, SSIDs
- **Security**: IPS, antivirus, web filtering, application control
- **Network**: Routing (static, BGP, OSPF), DNS, DHCP
- **And much more...**

See :doc:`/fortios/api-reference/cmdb/index` for the complete list of 37 CMDB categories.

Monitor API - Status & Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Monitor** API provides real-time status information and statistics. This includes 32 categories covering:

- **System**: Status, resources, performance
- **Firewall**: Active sessions, policy stats
- **Router**: Routing tables, neighbor status
- **VPN**: Tunnel status, connection stats
- **WiFi**: Client status, AP performance
- **UTM**: IPS stats, AV activity, web filter logs
- **And much more...**

See :doc:`/fortios/api-reference/monitor/index` for the complete list of 32 Monitor categories.

Log API - Historical Data
^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Log** API provides access to historical log data:

- Traffic logs
- Security event logs
- System logs
- UTM logs
- Application logs

See :doc:`/fortios/api-reference/log/index` for log query capabilities.

Service API - Operations
^^^^^^^^^^^^^^^^^^^^^^^^^

The **Service** API provides operational commands:

- Backup and restore
- System reboot
- Configuration validation
- License management
- And more...

See :doc:`/fortios/api-reference/service/index` for available service operations.

API Patterns
------------

All FortiOS endpoints follow consistent patterns:

**CMDB Endpoints** (Configuration)

.. code-block:: python

   # List all objects
   fgt.api.cmdb.firewall.address.get()

   # Get specific object
   fgt.api.cmdb.firewall.address.get(name="web-server")

   # Create object
   fgt.api.cmdb.firewall.address.create(
       name="web-server",
       subnet="10.0.1.100/32"
   )

   # Update object
   fgt.api.cmdb.firewall.address.update(
       name="web-server",
       comment="Updated comment"
   )

   # Delete object
   fgt.api.cmdb.firewall.address.delete(name="web-server")

**Monitor Endpoints** (Status)

.. code-block:: python

   # Get status (no parameters)
   fgt.api.monitor.system.status.get()

   # Get status with filters
   fgt.api.monitor.firewall.session.get(
       ip_version="ipv4",
       count=100
   )

**Log Endpoints** (Historical Data)

.. code-block:: python

   # Query logs
   fgt.api.log.disk.traffic.get(
       rows=100,
       start=0,
       filter="srcip==10.0.1.100"
   )

**Service Endpoints** (Operations)

.. code-block:: python

   # Execute service operation
   fgt.api.service.system.backup.create(
       scope="global",
       password="backup-password"
   )

Async Support
-------------

All endpoints support async/await by adding ``_async`` suffix:

.. code-block:: python

   import asyncio

   async def get_status():
       status = await fgt.api.monitor.system.status.get_async()
       return status

   asyncio.run(get_status())

Convenience Wrappers
--------------------

For common tasks, use the convenience wrappers which provide simplified interfaces:

.. code-block:: python

   # Firewall policy wrapper
   fgt.firewall.policy.create(
       name="Allow-Web",
       srcintf=["internal"],
       dstintf=["wan1"],
       srcaddr=["all"],
       dstaddr=["web-server"],
       service=["HTTP", "HTTPS"],
       action="accept"
   )

   # Schedule wrapper
   fgt.firewall.schedule.recurring.create(
       name="business-hours",
       day=["monday", "tuesday", "wednesday", "thursday", "friday"],
       start="08:00",
       end="18:00"
   )

See :doc:`/fortios/api-reference/convenience-wrappers` for all available wrappers.

Navigation
----------

Use the sidebar to navigate to specific API categories, or start with these popular ones:

**Popular CMDB Categories:**

- :doc:`/fortios/api-reference/cmdb/firewall` - Firewall configuration
- :doc:`/fortios/api-reference/cmdb/system` - System settings
- :doc:`/fortios/api-reference/cmdb/router` - Routing configuration
- :doc:`/fortios/api-reference/cmdb/vpn` - VPN configuration

**Popular Monitor Categories:**

- :doc:`/fortios/api-reference/monitor/system` - System status
- :doc:`/fortios/api-reference/monitor/firewall` - Firewall statistics
- :doc:`/fortios/api-reference/monitor/router` - Routing information
- :doc:`/fortios/api-reference/monitor/vpn` - VPN status
