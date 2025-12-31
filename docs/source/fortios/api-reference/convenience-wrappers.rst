Convenience Wrappers
====================

High-level wrappers that simplify common FortiOS operations.

.. note::
   **New users should start here!** Convenience wrappers provide a simpler,
   more intuitive interface compared to the low-level API methods.

Overview
--------

Convenience wrappers are accessed through the ``firewall`` namespace:

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access wrappers through fgt.firewall
   fgt.firewall.policy.create(...)
   fgt.firewall.schedule_recurring.create(...)
   fgt.firewall.service_custom.create(...)

Firewall Policy
---------------

.. autoclass:: hfortix_fortios.firewall.FirewallPolicy
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
^^^^^^^

.. code-block:: python

   # Create a firewall policy
   policy = fgt.firewall.policy.create(
       name='Allow-Web-Traffic',
       srcintf=['port1'],
       dstintf=['port2'],
       srcaddr=['internal-network'],
       dstaddr=['web-server'],
       service=['HTTP', 'HTTPS'],
       action='accept',
       schedule='always',
       nat=True
   )

   # Check if policy exists
   exists = fgt.firewall.policy.exists(policyid='1')
   
   # Get policy by name
   policy = fgt.firewall.policy.get_by_name('Allow-Web-Traffic')
   
   # Clone policy
   new_policy = fgt.firewall.policy.clone(
       policyid='1',
       new_name='Allow-Web-Traffic-Copy'
   )

Schedule Wrappers
-----------------

Schedule Recurring
^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ScheduleRecurring
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create recurring schedule
   schedule = fgt.firewall.schedule_recurring.create(
       name='business-hours',
       day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
       start='08:00',
       end='18:00'
   )
   
   # Clone and modify
   extended = fgt.firewall.schedule_recurring.clone(
       name='business-hours',
       new_name='extended-hours',
       end='20:00'
   )

Schedule Onetime
^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ScheduleOnetime
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create one-time schedule
   schedule = fgt.firewall.schedule_onetime.create(
       name='maintenance-window',
       start='2025-12-31 22:00',
       end='2026-01-01 02:00'
   )

Schedule Group
^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ScheduleGroup
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create schedule group
   group = fgt.firewall.schedule_group.create(
       name='all-business-hours',
       member=['business-hours', 'extended-hours']
   )

Service Wrappers
----------------

Service Custom
^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ServiceCustom
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create custom service
   service = fgt.firewall.service_custom.create(
       name='custom-app',
       protocol='TCP',
       tcp_portrange='8080-8090',
       comment='Custom application'
   )

Service Group
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ServiceGroup
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create service group
   group = fgt.firewall.service_group.create(
       name='web-services',
       member=['HTTP', 'HTTPS', 'custom-app']
   )

Service Category
^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ServiceCategory
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Traffic Shaper Wrappers
-----------------------

Traffic Shaper
^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.TrafficShaper
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create traffic shaper
   shaper = fgt.firewall.traffic_shaper.create(
       name='bandwidth-limit',
       guaranteed_bandwidth=10000,  # 10 Mbps
       maximum_bandwidth=50000      # 50 Mbps
   )

Shaper Per IP
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ShaperPerIp
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create per-IP shaper
   shaper = fgt.firewall.shaper_per_ip.create(
       name='user-limit',
       max_bandwidth=5000,           # 5 Mbps per user
       max_concurrent_session=100
   )

IP/MAC Binding Wrappers
-----------------------

IP/MAC Binding Setting
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.IPMACBindingSetting
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

IP/MAC Binding Table
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.IPMACBindingTable
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Example
~~~~~~~

.. code-block:: python

   # Create IP/MAC binding entry
   binding = fgt.firewall.ipmac_binding_table.create(
       name='workstation-1',
       ip='192.168.1.100',
       mac='00:11:22:33:44:55',
       status='enable'
   )

Common Patterns
---------------

Error Handling
^^^^^^^^^^^^^^

All wrappers support configurable error handling:

.. code-block:: python

   # Default: raise exceptions
   try:
       fgt.firewall.policy.create(name='test', ...)
   except DuplicateEntryError:
       print("Policy already exists")

   # Return error dict instead
   result = fgt.firewall.policy.create(
       name='test',
       error_mode='return',
       ...
   )
   if result.get('error'):
       print(f"Error: {result['error']}")

Exists/Update Pattern
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Check if exists, create or update
   if fgt.firewall.policy.exists(name='my-policy'):
       fgt.firewall.policy.update(name='my-policy', ...)
   else:
       fgt.firewall.policy.create(name='my-policy', ...)

Clone and Modify
^^^^^^^^^^^^^^^^

.. code-block:: python

   # Clone existing resource with modifications
   new_schedule = fgt.firewall.schedule_recurring.clone(
       name='original-schedule',
       new_name='modified-schedule',
       end='20:00'  # Override specific fields
   )

See Also
--------

- :doc:`../guides/firewall-policies` - Firewall policy guide
- :doc:`../guides/schedules` - Schedule management guide
- :doc:`../guides/services` - Service management guide
- :doc:`../guides/shapers` - Traffic shaping guide
- :doc:`../user-guide/error-handling` - Error handling guide
