FortiOS Client
==============

The main FortiOS client class for connecting to FortiGate devices.

Client Class
------------

.. autoclass:: hfortix_fortios.FortiOS
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Usage
-----

Basic Connection
^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   # Connect with API token (recommended)
   fgt = FortiOS(
       host='192.168.1.99',
       token='your-api-token',
       verify=False  # Use True in production
   )

   # Connect with username/password (FortiOS ≤7.4 only)
   fgt = FortiOS(
       host='192.168.1.99',
       username='admin',
       password='password',
       verify=False
   )

Optimized Settings
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # For high-performance scenarios
   fgt = FortiOS(
       host='192.168.1.99',
       token='your-token',
       max_connections=60,
       max_keepalive_connections=30,
       connect_timeout=10.0,
       read_timeout=300.0
   )

API Namespaces
--------------

The FortiOS client provides access to all API categories through organized namespaces.

API Namespace
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.api.API
   :members:
   :undoc-members:
   :show-inheritance:

The ``api`` namespace provides access to:

- ``api.cmdb`` - Configuration Management Database (37 categories)
- ``api.monitor`` - Monitoring and status (34 categories)  
- ``api.log`` - Log queries (5 categories)
- ``api.service`` - System services (3 categories)

Firewall Namespace
^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.client.FirewallNamespace
   :members:
   :undoc-members:
   :show-inheritance:

The ``firewall`` namespace provides convenience wrappers:

- ``firewall.policy`` - Firewall policies
- ``firewall.schedule_recurring`` - Recurring schedules
- ``firewall.schedule_onetime`` - One-time schedules
- ``firewall.schedule_group`` - Schedule groups
- ``firewall.service_custom`` - Custom services
- ``firewall.service_group`` - Service groups
- ``firewall.service_category`` - Service categories
- ``firewall.traffic_shaper`` - Traffic shapers
- ``firewall.shaper_per_ip`` - Per-IP shapers
- ``firewall.ipmac_binding_setting`` - IP/MAC binding settings
- ``firewall.ipmac_binding_table`` - IP/MAC binding table

Examples
--------

Using CMDB API
^^^^^^^^^^^^^^

.. code-block:: python

   # List firewall addresses
   addresses = fgt.api.cmdb.firewall.address.list()

   # Create firewall address
   fgt.api.cmdb.firewall.address.create(
       name='web-server',
       subnet='10.0.1.100/32'
   )

   # Update firewall address
   fgt.api.cmdb.firewall.address.update(
       name='web-server',
       comment='Production server'
   )

   # Delete firewall address
   fgt.api.cmdb.firewall.address.delete(name='web-server')

Using Monitor API
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get system status
   status = fgt.api.monitor.system.status.get()

   # Get firewall sessions
   sessions = fgt.api.monitor.firewall.session.list()

   # Get interface statistics
   stats = fgt.api.monitor.system.interface.list()

Using Convenience Wrappers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Create firewall policy (simplified)
   policy = fgt.firewall.policy.create(
       name='Allow-Web',
       srcintf=['internal'],
       dstintf=['wan1'],
       srcaddr=['all'],
       dstaddr=['web-server'],
       service=['HTTP', 'HTTPS'],
       action='accept'
   )

   # Check if policy exists
   if fgt.firewall.policy.exists(policyid='1'):
       print("Policy exists!")

See Also
--------

- :doc:`convenience-wrappers` - High-level convenience wrappers
- :doc:`cmdb/index` - CMDB API reference
- :doc:`monitor/index` - Monitor API reference
- :doc:`../user-guide/fortios-overview` - User guide
- :doc:`../getting-started/quickstart` - Quick start guide
