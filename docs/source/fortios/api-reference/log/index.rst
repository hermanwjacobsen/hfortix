Log API Reference
==================

Log query and retrieval functionality.

.. automodule:: hfortix_fortios.api.v2.log
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

Overview
--------

The Log API provides access to FortiGate log data across multiple log types:

- **Disk Logs**: Logs stored on disk
- **Memory Logs**: Logs in memory
- **FortiAnalyzer Logs**: Logs sent to FortiAnalyzer
- **FortiCloud Logs**: Logs in FortiCloud
- **Syslog Logs**: Syslog configuration

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
