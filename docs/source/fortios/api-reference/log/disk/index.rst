DiskDisk

========



Disk log query operations - query logs stored on local disk storage.Disk log query operations.



OverviewOverview

----------------



The ``log.disk`` category provides access to logs stored on the FortiGate's local disk, including traffic, events, virus, IPS, and more.The ``log.disk`` category provides log query access for:



**Log Types with Archive Support:**- :doc:`Disk_Virus_Archive <disk-virus-archive>` - Return a description of the quarantined virus file.

- :doc:`Disk_{Type}_Archive <disk-{type}-archive>` - Return a list of archived items for the desired type. :type can be app-ctrl or ips

- ``ips`` - Intrusion Prevention System logs with packet capture archives- :doc:`Disk_{Type}_Archive Download <disk-{type}-archive-download>` - Download an archived file.

- ``app_ctrl`` - Application Control logs with packet capture archives- :doc:`Disk_{Type}_Raw <disk-{type}-raw>` - Log data for the given log type in raw format.

- :doc:`Disk_Traffic_{Subtype}_Raw <disk-traffic-{subtype}-raw>` - Log data for the given log type in raw format.

**Special Virus Archive:**- :doc:`Disk_Event_{Subtype}_Raw <disk-event-{subtype}-raw>` - Log data for the given log type in raw format.

- :doc:`Disk_{Type} <disk-{type}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.

- ``virus_archive`` - Quarantined virus file metadata- :doc:`Disk_Traffic_{Subtype} <disk-traffic-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.

- :doc:`Disk_Event_{Subtype} <disk-event-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.

**Standard Log Types:**



- ``traffic`` - Network traffic logs (with event/forward/local/multicast subtypes)Quick Start

- ``event`` - System events (with system/user/router/ha/wireless/switch subtypes)-----------

- ``webfilter`` - Web filtering logs

- ``waf`` - Web Application Firewall logs.. code-block:: python

- ``anomaly`` - Anomaly detection logs

- ``emailfilter`` - Email filtering logs   from hfortix_fortios import FortiOS

- ``dlp`` - Data Loss Prevention logs   

- ``voip`` - VoIP logs   fgt = FortiOS(host='192.168.1.99', token='your-token')

- ``gtp`` - GTP (mobile network) logs   

- ``dns`` - DNS query logs   # Access endpoints via:

- ``ssh`` - SSH session logs   fgt.api.log.disk.<endpoint>

- ``ssl`` - SSL/TLS inspection logs

- ``file_filter`` - File filtering logsAvailable Endpoints

- ``ztna`` - Zero Trust Network Access logs-------------------



Python Usage.. toctree::

------------   :maxdepth: 1

   

**Archive Downloads (IPS and App-Ctrl):**   disk-event-{subtype}

   disk-event-{subtype}-raw

.. code-block:: python   disk-traffic-{subtype}

   disk-traffic-{subtype}-raw

   from hfortix_fortios import FortiOS   disk-virus-archive

      disk-{type}

   fgt = FortiOS(host='192.168.1.99', token='your-token')   disk-{type}-archive

      disk-{type}-archive-download

   # List IPS archives   disk-{type}-raw

   archives = fgt.api.log.disk.ips.archive.get()

   See Also

   # Download specific IPS archive--------

   pcap_data = fgt.api.log.disk.ips.archive_download.get(mkey=123)

   - :doc:`/fortios/api-reference/log/index` - Log API overview

   # List App-Ctrl archives- :doc:`/fortios/user-guide/client` - FortiOS client reference

   archives = fgt.api.log.disk.app_ctrl.archive.get()- :doc:`/fortios/guides/filtering` - Filtering guide

   
   # Download specific App-Ctrl archive
   pcap_data = fgt.api.log.disk.app_ctrl.archive_download.get(mkey=456)

**Virus Archive:**

.. code-block:: python

   # List all quarantined viruses
   viruses = fgt.api.log.disk.virus_archive.get()
   
   # Get specific virus by checksum
   virus = fgt.api.log.disk.virus_archive.get(mkey=12345678)

**Standard Log Queries:**

.. code-block:: python

   # Query traffic logs
   traffic = fgt.api.log.disk.traffic.get(rows=100)
   
   # Query traffic logs with specific subtype
   forward_traffic = fgt.api.log.disk.traffic.forward.get(rows=50)
   
   # Query event logs
   events = fgt.api.log.disk.event.get(rows=100)
   
   # Query system events specifically
   system_events = fgt.api.log.disk.event.system.get(rows=50)
   
   # Query web filter logs
   webfilter = fgt.api.log.disk.webfilter.get(
       rows=100,
       filter='action==blocked'
   )

Log Filtering
-------------

All log queries support filtering using the ``filter`` parameter:

.. code-block:: python

   # Filter by source IP
   logs = fgt.api.log.disk.traffic.get(
       filter='srcip==192.168.1.100',
       rows=100
   )
   
   # Multiple filters (AND logic)
   logs = fgt.api.log.disk.traffic.get(
       filter=['srcip==192.168.1.100', 'dstport==443'],
       rows=100
   )
   
   # Time range filter
   logs = fgt.api.log.disk.event.get(
       filter='logid==32001&time>2024-01-01',
       rows=50
   )

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
