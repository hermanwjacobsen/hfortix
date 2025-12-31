Disk
====

Disk log query operations.

Overview
--------

The ``log.disk`` category provides log query access for:

- :doc:`Disk_Virus_Archive <disk-virus-archive>` - Return a description of the quarantined virus file.
- :doc:`Disk_{Type}_Archive <disk-{type}-archive>` - Return a list of archived items for the desired type. :type can be app-ctrl or ips
- :doc:`Disk_{Type}_Archive Download <disk-{type}-archive-download>` - Download an archived file.
- :doc:`Disk_{Type}_Raw <disk-{type}-raw>` - Log data for the given log type in raw format.
- :doc:`Disk_Traffic_{Subtype}_Raw <disk-traffic-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Disk_Event_{Subtype}_Raw <disk-event-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Disk_{Type} <disk-{type}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Disk_Traffic_{Subtype} <disk-traffic-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Disk_Event_{Subtype} <disk-event-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.log.disk.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   disk-event-{subtype}
   disk-event-{subtype}-raw
   disk-traffic-{subtype}
   disk-traffic-{subtype}-raw
   disk-virus-archive
   disk-{type}
   disk-{type}-archive
   disk-{type}-archive-download
   disk-{type}-raw

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
