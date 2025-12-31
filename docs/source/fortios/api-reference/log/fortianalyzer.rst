Log FortiAnalyzer
=================

Query logs sent to FortiAnalyzer for centralized management.

Overview
--------

The ``log.fortianalyzer`` category provides access to logs that have been sent to a FortiAnalyzer device for centralized logging and analysis.

Endpoint
--------

.. code-block:: python

   fgt.api.log.fortianalyzer

Methods
-------

**.get()**
   Query FortiAnalyzer logs

   .. code-block:: python
   
      # Get logs from FortiAnalyzer
      logs = fgt.api.log.fortianalyzer.traffic.get(rows=100)

Parameters
----------

**rows** (int, optional)
   Maximum number of log entries to return

**filter** (str, optional)
   Filter expression to limit results

**start** (int, optional)
   Starting row number for pagination

Prerequisites
-------------

- FortiAnalyzer must be configured in FortiGate
- Logs must be enabled for sending to FortiAnalyzer
- FortiGate must have connectivity to FortiAnalyzer

Usage Examples
--------------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query logs from FortiAnalyzer
   logs = fgt.api.log.fortianalyzer.traffic.get(rows=100)
   
   # Filter by source IP
   logs = fgt.api.log.fortianalyzer.traffic.get(
       filter='srcip==192.168.1.100',
       rows=50
   )

See Also
--------

- :doc:`disk` - Local disk logs
- :doc:`forticloud` - FortiCloud logs
