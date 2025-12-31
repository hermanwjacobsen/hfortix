Traffic Shaping
===============

High-level wrappers for managing FortiOS traffic shapers.

Overview
--------

Traffic shaping wrappers provide an intuitive interface for controlling bandwidth
and managing traffic with per-IP shapers and traffic shapers.

Shaper Types
------------

FortiOS supports two types of shapers:

1. **Traffic Shapers** - Control overall traffic bandwidth
2. **Per-IP Shapers** - Control bandwidth per IP address

Traffic Shaper
--------------

Create traffic shapers to control overall bandwidth limits.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create traffic shaper
   shaper = fgt.firewall.traffic_shaper.create(
       name='bandwidth-limit-10mb',
       guaranteed_bandwidth=5000,  # 5 Mbps guaranteed
       maximum_bandwidth=10000,    # 10 Mbps maximum
       bandwidth_unit='kbps',
       priority='high'
   )
   
   # List all traffic shapers
   shapers = fgt.firewall.traffic_shaper.list()
   
   # Clone and modify
   new_shaper = fgt.firewall.traffic_shaper.clone(
       name='bandwidth-limit-10mb',
       new_name='bandwidth-limit-20mb',
       maximum_bandwidth=20000
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.TrafficShaper
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Per-IP Shaper
-------------

Create per-IP shapers to control bandwidth on a per-IP-address basis.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   # Create per-IP shaper
   per_ip = fgt.firewall.shaper_per_ip.create(
       name='per-ip-5mb',
       max_bandwidth=5000,        # 5 Mbps per IP
       max_concurrent_session=100
   )
   
   # List all per-IP shapers
   shapers = fgt.firewall.shaper_per_ip.list()

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ShaperPerIp
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

See Also
--------

- :doc:`/fortios/guides/shapers` - Complete traffic shaping guide with examples
- :doc:`/fortios/api-reference/cmdb/firewall` - Low-level firewall API
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
