Log Disk
========

Query logs stored on local disk storage.

Overview
--------

The ``log.disk`` category provides access to all log types stored on the FortiGate's local disk:

- Traffic logs
- Event logs  
- Virus logs
- IPS logs
- Web filter logs
- Application control logs
- DLP logs
- Email filter logs
- And more...

Endpoint
--------

.. code-block:: python

   fgt.api.log.disk

Methods
-------

**.get()**
   Query disk logs with filtering

   .. code-block:: python
   
      # Get recent traffic logs
      logs = fgt.api.log.disk.traffic.get(rows=100)
      
      # Filter by source IP
      logs = fgt.api.log.disk.traffic.get(
          filter='srcip==192.168.1.100',
          rows=50
      )
      
      # Get event logs
      events = fgt.api.log.disk.event.get(rows=100)

Parameters
----------

**rows** (int, optional)
   Maximum number of log entries to return. Default: 100

**filter** (str, optional)
   Filter expression to limit results. See :doc:`/fortios/guides/filtering` for syntax

**start** (int, optional)
   Starting row number for pagination

Log Types Available
-------------------

**traffic**
   Traffic logs - packet forwarding decisions

**event**
   System event logs - configuration changes, admin actions

**virus**
   Antivirus detection logs

**ips**
   Intrusion prevention logs

**webfilter**
   Web filtering logs

**app-ctrl**
   Application control logs

**dlp**
   Data loss prevention logs

**emailfilter**
   Email filtering logs

**anomaly**
   Anomaly detection logs

**voip**
   VoIP logs

**gtp**
   GTP protocol logs

**dns**
   DNS query logs

**ssh**
   SSH connection logs

**ssl**
   SSL/TLS inspection logs

**cifs**
   CIFS/SMB file transfer logs

**file-filter**
   File filtering logs

**waf**
   Web application firewall logs

Usage Examples
--------------

Query Traffic Logs
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Get last 100 traffic logs
   logs = fgt.api.log.disk.traffic.get(rows=100)
   
   for log in logs['results']:
       print(f"{log['srcip']} -> {log['dstip']} : {log['action']}")

Filter by Criteria
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Filter by source IP
   logs = fgt.api.log.disk.traffic.get(
       filter='srcip==192.168.1.100',
       rows=50
   )
   
   # Filter by destination port
   logs = fgt.api.log.disk.traffic.get(
       filter='dstport==443',
       rows=50
   )
   
   # Multiple filters
   logs = fgt.api.log.disk.traffic.get(
       filter='srcip==192.168.1.100&dstport==443',
       rows=50
   )

Query Event Logs
^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get system events
   events = fgt.api.log.disk.event.get(rows=50)
   
   for event in events['results']:
       print(f"{event['logdesc']}: {event['msg']}")

Pagination
^^^^^^^^^^

.. code-block:: python

   # Get first page
   page1 = fgt.api.log.disk.traffic.get(rows=100, start=0)
   
   # Get second page
   page2 = fgt.api.log.disk.traffic.get(rows=100, start=100)

Response Format
---------------

.. code-block:: python

   {
       'results': [
           {
               'srcip': '192.168.1.100',
               'dstip': '8.8.8.8',
               'srcport': 54321,
               'dstport': 53,
               'action': 'accept',
               'policyid': 1,
               'service': 'dns',
               'sentbyte': 74,
               'rcvdbyte': 146,
               'logid': '0000000013',
               'type': 'traffic',
               # ... more fields
           },
           # ... more log entries
       ],
       'serial': 'FGVMXXXXXXXXX',
       'vdom': 'root'
   }

See Also
--------

- :doc:`/fortios/guides/filtering` - Log filtering guide
- :doc:`memory` - Memory logs
- :doc:`fortianalyzer` - FortiAnalyzer logs
- :doc:`forticloud` - FortiCloud logs
