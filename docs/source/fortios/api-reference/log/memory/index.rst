Memory
======

Memory log query operations.

Overview
--------

The ``log.memory`` category provides log query access for:

- :doc:`Memory_Virus_Archive <memory-virus-archive>` - Return a description of the quarantined virus file.
- :doc:`Memory_{Type}_Archive <memory-{type}-archive>` - Return a list of archived items for the desired type. :type can be app-ctrl or ips
- :doc:`Memory_{Type}_Archive Download <memory-{type}-archive-download>` - Download an archived file.
- :doc:`Memory_{Type}_Raw <memory-{type}-raw>` - Log data for the given log type in raw format.
- :doc:`Memory_Traffic_{Subtype}_Raw <memory-traffic-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Memory_Event_{Subtype}_Raw <memory-event-{subtype}-raw>` - Log data for the given log type in raw format.
- :doc:`Memory_{Type} <memory-{type}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Memory_Traffic_{Subtype} <memory-traffic-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.
- :doc:`Memory_Event_{Subtype} <memory-event-{subtype}>` - Log data for the given log type (and subtype). Append '/raw' to retrieve in raw format.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.log.memory.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   memory-event-{subtype}
   memory-event-{subtype}-raw
   memory-traffic-{subtype}
   memory-traffic-{subtype}-raw
   memory-virus-archive
   memory-{type}
   memory-{type}-archive
   memory-{type}-archive-download
   memory-{type}-raw

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
