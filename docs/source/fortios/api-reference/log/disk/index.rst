DiskDiskDisk

====

========

Disk log query operations - query logs stored on local disk storage.



Overview

--------Disk log query operations - query logs stored on local disk storage.Disk log query operations.



The ``log.disk`` category provides access to logs stored on the FortiGate's local disk, including traffic, events, virus, IPS, and more.



**Log Types with Archive Support:**OverviewOverview



- ``ips`` - Intrusion Prevention System logs with packet capture archives----------------

- ``app_ctrl`` - Application Control logs with packet capture archives



**Special Virus Archive:**

The ``log.disk`` category provides access to logs stored on the FortiGate's local disk, including traffic, events, virus, IPS, and more.The ``log.disk`` category provides log query access for:

- ``virus_archive`` - Quarantined virus file metadata



**Standard Log Types:**

**Log Types with Archive Support:**- :doc:`Disk_Virus_Archive <disk-virus-archive>` - Return a description of the quarantined virus file.

- ``traffic`` - Network traffic logs with subtypes (forward, local, multicast, sniffer, fortiview, threat)

- ``event`` - System events with subtypes (system, user, router, ha, wireless, vpn, wad, endpoint, etc.)- :doc:`Disk_{Type}_Archive <disk-{type}-archive>` - Return a list of archived items for the desired type. :type can be app-ctrl or ips

- ``webfilter`` - Web filtering logs

- ``waf`` - Web Application Firewall logs- ``ips`` - Intrusion Prevention System logs with packet capture archives- :doc:`Disk_{Type}_Archive Download <disk-{type}-archive-download>` - Download an archived file.

- ``anomaly`` - Anomaly detection logs

- ``emailfilter`` - Email filtering logs- ``app_ctrl`` - Application Control logs with packet capture archives- :doc:`Disk_{Type}_Raw <disk-{type}-raw>` - Log data for the given log type in raw format.

- ``dlp`` - Data Loss Prevention logs

- ``voip`` - VoIP logs- :doc:`Disk_Traffic_{Subtype}_Raw <disk-traffic-{subtype}-raw>` - Log data for the given log type in raw format.

- ``gtp`` - GTP (mobile network) logs

- ``dns`` - DNS query logs**Special Virus Archive:**- :doc:`Disk_Event_{Subtype}_Raw <disk-event-{subtype}-raw>` - Log data for the given log type in raw format.

- ``ssh`` - SSH session logs

- ``ssl`` - SSL/TLS inspection logs- :doc:`Disk_{Type} <disk-{type}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.

- ``file_filter`` - File filtering logs

- ``cifs`` - CIFS logs- ``virus_archive`` - Quarantined virus file metadata- :doc:`Disk_Traffic_{Subtype} <disk-traffic-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.



Python Usage- :doc:`Disk_Event_{Subtype} <disk-event-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.

------------

**Standard Log Types:**

**Archive Downloads (IPS and App-Ctrl):**



.. code-block:: python

- ``traffic`` - Network traffic logs (with event/forward/local/multicast subtypes)Quick Start

   from hfortix_fortios import FortiOS

   - ``event`` - System events (with system/user/router/ha/wireless/switch subtypes)-----------

   fgt = FortiOS(host='192.168.1.99', token='your-token')

   - ``webfilter`` - Web filtering logs

   # List IPS archives

   archives = fgt.api.log.disk.ips.archive.get()- ``waf`` - Web Application Firewall logs.. code-block:: python

   

   # Download specific IPS archive- ``anomaly`` - Anomaly detection logs

   pcap_data = fgt.api.log.disk.ips.archive_download.get(mkey=123)

   - ``emailfilter`` - Email filtering logs   from hfortix_fortios import FortiOS

   # List App-Ctrl archives

   archives = fgt.api.log.disk.app_ctrl.archive.get()- ``dlp`` - Data Loss Prevention logs   

   

   # Download specific App-Ctrl archive- ``voip`` - VoIP logs   fgt = FortiOS(host='192.168.1.99', token='your-token')

   pcap_data = fgt.api.log.disk.app_ctrl.archive_download.get(mkey=456)

- ``gtp`` - GTP (mobile network) logs   

**Virus Archive:**

- ``dns`` - DNS query logs   # Access endpoints via:

.. code-block:: python

- ``ssh`` - SSH session logs   fgt.api.log.disk.<endpoint>

   # List all quarantined viruses

   viruses = fgt.api.log.disk.virus_archive.get()- ``ssl`` - SSL/TLS inspection logs

   

   # Get specific virus by checksum- ``file_filter`` - File filtering logsAvailable Endpoints

   virus = fgt.api.log.disk.virus_archive.get(mkey=12345678)

- ``ztna`` - Zero Trust Network Access logs-------------------

**Standard Log Queries:**



.. code-block:: python

Python Usage.. toctree::

   # Query traffic logs (has subtypes: forward, local, multicast, sniffer, fortiview, threat)

   traffic = fgt.api.log.disk.traffic.forward.get(rows=100)------------   :maxdepth: 1

   

   # Query all traffic subtypes   

   local_traffic = fgt.api.log.disk.traffic.local.get(rows=50)

   multicast = fgt.api.log.disk.traffic.multicast.get(rows=50)**Archive Downloads (IPS and App-Ctrl):**   disk-event-{subtype}

   

   # Query event logs (has subtypes: system, user, router, ha, wireless, etc.)   disk-event-{subtype}-raw

   system_events = fgt.api.log.disk.event.system.get(rows=100)

   user_events = fgt.api.log.disk.event.user.get(rows=50).. code-block:: python   disk-traffic-{subtype}

   vpn_events = fgt.api.log.disk.event.vpn.get(rows=50)

      disk-traffic-{subtype}-raw

   # Query web filter logs (no subtypes)

   webfilter = fgt.api.log.disk.webfilter.get(   from hfortix_fortios import FortiOS   disk-virus-archive

       rows=100,

       filter='action==blocked'      disk-{type}

   )

      fgt = FortiOS(host='192.168.1.99', token='your-token')   disk-{type}-archive

   # Other log types (no subtypes)

   waf_logs = fgt.api.log.disk.waf.get(rows=100)      disk-{type}-archive-download

   dns_logs = fgt.api.log.disk.dns.get(rows=100)

   ssh_logs = fgt.api.log.disk.ssh.get(rows=100)   # List IPS archives   disk-{type}-raw



Log Filtering   archives = fgt.api.log.disk.ips.archive.get()

-------------

   See Also

All log queries support filtering using the ``filter`` parameter:

   # Download specific IPS archive--------

.. code-block:: python

   pcap_data = fgt.api.log.disk.ips.archive_download.get(mkey=123)

   # Filter by source IP

   logs = fgt.api.log.disk.traffic.forward.get(   - :doc:`/fortios/api-reference/log/index` - Log API overview

       filter='srcip==192.168.1.100',

       rows=100   # List App-Ctrl archives- :doc:`/fortios/user-guide/client` - FortiOS client reference

   )

      archives = fgt.api.log.disk.app_ctrl.archive.get()- :doc:`/fortios/guides/filtering` - Filtering guide

   # Multiple filters (AND logic)

   logs = fgt.api.log.disk.traffic.forward.get(   

       filter=['srcip==192.168.1.100', 'dstport==443'],   # Download specific App-Ctrl archive

       rows=100   pcap_data = fgt.api.log.disk.app_ctrl.archive_download.get(mkey=456)

   )

   **Virus Archive:**

   # Time range filter

   logs = fgt.api.log.disk.event.system.get(.. code-block:: python

       filter='logid==32001&time>2024-01-01',

       rows=50   # List all quarantined viruses

   )   viruses = fgt.api.log.disk.virus_archive.get()

   

Available Log Types   # Get specific virus by checksum

-------------------   virus = fgt.api.log.disk.virus_archive.get(mkey=12345678)



**Traffic Subtypes** (accessed via ``fgt.api.log.disk.traffic.<subtype>``)**Standard Log Queries:**



- ``forward`` - Forwarded traffic.. code-block:: python

- ``local`` - Local traffic

- ``multicast`` - Multicast traffic   # Query traffic logs (has subtypes: forward, local, multicast, sniffer, fortiview, threat)

- ``sniffer`` - Packet capture traffic   traffic = fgt.api.log.disk.traffic.forward.get(rows=100)

- ``fortiview`` - FortiView statistics   

- ``threat`` - Threat traffic   # Query all traffic subtypes

   local_traffic = fgt.api.log.disk.traffic.local.get(rows=50)

**Event Subtypes** (accessed via ``fgt.api.log.disk.event.<subtype>``)   multicast = fgt.api.log.disk.traffic.multicast.get(rows=50)

   

- ``system`` - System events   # Query event logs (has subtypes: system, user, router, ha, wireless, etc.)

- ``user`` - User events   system_events = fgt.api.log.disk.event.system.get(rows=100)

- ``router`` - Router events   user_events = fgt.api.log.disk.event.user.get(rows=50)

- ``ha`` - High Availability events   vpn_events = fgt.api.log.disk.event.vpn.get(rows=50)

- ``wireless`` - Wireless events   

- ``vpn`` - VPN events   # Query web filter logs (no subtypes)

- ``wad`` - Web Application Delivery events   webfilter = fgt.api.log.disk.webfilter.get(

- ``endpoint`` - Endpoint events       rows=100,

- ``compliance_check`` - Compliance events       filter='action==blocked'

- ``security_rating`` - Security rating events   )

- ``fortiextender`` - FortiExtender events   

- ``connector`` - Connector events   # Other log types (no subtypes)

   waf_logs = fgt.api.log.disk.waf.get(rows=100)

**Direct Log Types** (accessed via ``fgt.api.log.disk.<type>``)   dns_logs = fgt.api.log.disk.dns.get(rows=100)

   ssh_logs = fgt.api.log.disk.ssh.get(rows=100)

- ``webfilter``, ``waf``, ``anomaly``, ``emailfilter``, ``dlp``

- ``voip``, ``gtp``, ``dns``, ``ssh``, ``ssl``Log Filtering

- ``file_filter``, ``cifs``-------------



See AlsoAll log queries support filtering using the ``filter`` parameter:

--------

.. code-block:: python

- :doc:`/fortios/api-reference/log/index` - Log API overview

- :doc:`/fortios/user-guide/client` - FortiOS client reference   # Filter by source IP

- :doc:`/fortios/guides/filtering` - Filtering guide   logs = fgt.api.log.disk.traffic.get(

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
