FortiAnalyzer
=============

FortiAnalyzer log query operations - query logs sent to FortiAnalyzer.

Overview
--------

The ``log.fortianalyzer`` category provides access to logs sent to a FortiAnalyzer device for centralized logging and analysis.

Python Usage
------------

**Log Queries:**

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query traffic logs
   traffic = fgt.api.log.fortianalyzer.traffic.get(rows=100)
   
   # Query event logs
   events = fgt.api.log.fortianalyzer.event.get(rows=100)
   
   # Query with filters
   filtered = fgt.api.log.fortianalyzer.traffic.get(
       filter='srcip==192.168.1.100',
       rows=50
   )

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/guides/filtering` - Filtering guide
