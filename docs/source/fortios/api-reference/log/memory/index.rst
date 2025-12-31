Memory
======

Memory log query operations - query logs stored in device RAM.

Overview
--------

The ``log.memory`` category provides access to logs stored in the FortiGate's memory. These logs are fast to query but have limited capacity and are lost on reboot.

Python Usage
------------

**Log Queries:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query traffic logs
   traffic = fgt.api.log.memory.traffic.get(rows=100)
   
   # Query event logs
   events = fgt.api.log.memory.event.get(rows=100)
   
   # Query with filters
   filtered = fgt.api.log.memory.traffic.get(
       filter='srcip==192.168.1.100',
       rows=50
   )

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/api-reference/log/disk/index` - Disk logs (persistent)
- :doc:`/fortios/guides/filtering` - Filtering guide
