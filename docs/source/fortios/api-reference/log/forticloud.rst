Log FortiCloud
==============

Query logs stored in Fortinet's FortiCloud service.

Overview
--------

The ``log.forticloud`` category provides access to logs that have been uploaded to FortiCloud for cloud-based logging and analysis.

Endpoint
--------

.. code-block:: python

   fgt.api.log.forticloud

Methods
-------

**.get()**
   Query FortiCloud logs

   .. code-block:: python
   
      # Get logs from FortiCloud
      logs = fgt.api.log.forticloud.traffic.get(rows=100)

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

- FortiCloud account must be configured
- Logs must be enabled for FortiCloud upload
- Valid FortiCloud subscription
- Internet connectivity

Usage Examples
--------------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query logs from FortiCloud
   logs = fgt.api.log.forticloud.traffic.get(rows=100)
   
   # Filter by criteria
   logs = fgt.api.log.forticloud.event.get(
       filter='logdesc==User login',
       rows=50
   )

See Also
--------

- :doc:`disk` - Local disk logs
- :doc:`fortianalyzer` - FortiAnalyzer logs
