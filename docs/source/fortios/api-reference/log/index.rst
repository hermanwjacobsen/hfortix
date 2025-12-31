Log API Reference
==================

Log query and retrieval functionality.

Overview
--------

The Log API provides access to FortiGate log data across 5 categories:

**Disk Logs** (``log.disk``)
   Logs stored on local disk - traffic, event, virus, IPS, web filter, etc.

**Memory Logs** (``log.memory``)
   Logs stored in device memory for quick access

**FortiAnalyzer Logs** (``log.fortianalyzer``)
   Logs sent to FortiAnalyzer for centralized management

**FortiCloud Logs** (``log.forticloud``)
   Logs stored in FortiCloud service

**Search** (``log.search``)
   Log search and query operations

Usage Example
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query traffic logs
   logs = fgt.api.log.disk.traffic.list(
       filter='srcip==192.168.1.100',
       rows=100
   )
   
   # Query system event logs
   events = fgt.api.log.disk.event.list(rows=50)

See Also
--------

- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/filtering` - Log filtering guide
