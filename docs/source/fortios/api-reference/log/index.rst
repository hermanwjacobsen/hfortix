Log API Reference
==================

Log query and retrieval functionality.

Overview
--------

The Log API provides access to FortiGate log data across 5 categories:

:doc:`disk` - **Disk Logs** (``log.disk``)
   Logs stored on local disk - traffic, event, virus, IPS, web filter, and more. Persistent storage with large capacity.

:doc:`memory` - **Memory Logs** (``log.memory``)
   Logs stored in device memory for quick access. Fast queries but limited capacity and lost on reboot.

:doc:`fortianalyzer` - **FortiAnalyzer Logs** (``log.fortianalyzer``)
   Logs sent to FortiAnalyzer for centralized management and analysis across multiple FortiGate devices.

:doc:`forticloud` - **FortiCloud Logs** (``log.forticloud``)
   Logs stored in Fortinet's FortiCloud service for cloud-based logging and analysis.

:doc:`search` - **Log Search** (``log.search``)
   Advanced log search and query operations across all log types and storage locations.

.. toctree::
   :maxdepth: 1
   :hidden:

   disk
   memory
   fortianalyzer
   forticloud
   search

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
