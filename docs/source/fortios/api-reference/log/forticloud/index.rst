Forticloud
==========

Forticloud log query operations.

Overview
--------

The ``log.forticloud`` category provides log query access for:

- :doc:`Forticloud_Virus_Archive <forticloud-virus-archive>` - Return a description of the quarantined virus file.
- :doc:`Forticloud_{Type}_Archive <forticloud-{type}-archive>` - Return a list of archived items for the desired type. :type can be app-ctrl or ips
- :doc:`Forticloud_{Type}_Archive Download <forticloud-{type}-archive-download>` - Download an archived file.
- :doc:`Forticloud_{Type}_Raw <forticloud-{type}-raw>` - Log data for the given log type in raw format.
- :doc:`Forticloud_Traffic_{Subtype}_Raw <forticloud-traffic-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Forticloud_Event_{Subtype}_Raw <forticloud-event-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Forticloud_{Type} <forticloud-{type}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Forticloud_Traffic_{Subtype} <forticloud-traffic-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Forticloud_Event_{Subtype} <forticloud-event-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.log.forticloud.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   forticloud-event-{subtype}
   forticloud-event-{subtype}-raw
   forticloud-traffic-{subtype}
   forticloud-traffic-{subtype}-raw
   forticloud-virus-archive
   forticloud-{type}
   forticloud-{type}-archive
   forticloud-{type}-archive-download
   forticloud-{type}-raw

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
