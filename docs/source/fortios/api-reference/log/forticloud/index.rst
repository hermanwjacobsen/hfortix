FortiCloud
==========

FortiCloud log query operations - query logs stored in Fortinet's cloud service.

Overview
--------

The ``log.forticloud`` category provides access to logs stored in Fortinet's FortiCloud service for cloud-based logging and analysis.

Python Usage
------------

**Log Queries:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query traffic logs
   traffic = fgt.api.log.forticloud.traffic.get(rows=100)
   
   # Query event logs
   events = fgt.api.log.forticloud.event.get(rows=100)
   
   # Query with filters
   filtered = fgt.api.log.forticloud.traffic.get(
       filter='srcip==192.168.1.100',
       rows=50
   )

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/guides/filtering` - Filtering guide
