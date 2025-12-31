Log API Reference
==================

Log query and retrieval functionality.

Overview
--------

The Log API provides access to FortiGate log data across 5 categories:

- :doc:`Disk <disk/index>` - Logs stored on local disk - traffic, event, virus, IPS, web filter, and more
- :doc:`Memory <memory/index>` - Logs stored in device memory for quick access
- :doc:`FortiAnalyzer <fortianalyzer/index>` - Logs sent to FortiAnalyzer for centralized management
- :doc:`FortiCloud <forticloud/index>` - Logs stored in Fortinet's FortiCloud service
- :doc:`Search <search/index>` - Advanced log search and query operations

.. toctree::
   :maxdepth: 2
   :caption: Log Categories

   disk/index
   memory/index
   fortianalyzer/index
   forticloud/index
   search/index

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
