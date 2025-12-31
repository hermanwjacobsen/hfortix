Fortianalyzer
=============

Fortianalyzer log query operations.

Overview
--------

The ``log.fortianalyzer`` category provides log query access for:

- :doc:`Fortianalyzer_Virus_Archive <fortianalyzer-virus-archive>` - Return a description of the quarantined virus file.
- :doc:`Fortianalyzer_{Type}_Archive <fortianalyzer-{type}-archive>` - Return a list of archived items for the desired type. :type can be app-ctrl or ips
- :doc:`Fortianalyzer_{Type}_Archive Download <fortianalyzer-{type}-archive-download>` - Download an archived file.
- :doc:`Fortianalyzer_{Type}_Raw <fortianalyzer-{type}-raw>` - Log data for the given log type in raw format.
- :doc:`Fortianalyzer_Traffic_{Subtype}_Raw <fortianalyzer-traffic-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Fortianalyzer_Event_{Subtype}_Raw <fortianalyzer-event-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Fortianalyzer_{Type} <fortianalyzer-{type}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Fortianalyzer_Traffic_{Subtype} <fortianalyzer-traffic-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Fortianalyzer_Event_{Subtype} <fortianalyzer-event-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.log.fortianalyzer.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   fortianalyzer-event-{subtype}
   fortianalyzer-event-{subtype}-raw
   fortianalyzer-traffic-{subtype}
   fortianalyzer-traffic-{subtype}-raw
   fortianalyzer-virus-archive
   fortianalyzer-{type}
   fortianalyzer-{type}-archive
   fortianalyzer-{type}-archive-download
   fortianalyzer-{type}-raw

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
