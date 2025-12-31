Videofilter
===========

Overview
--------

The ``cmdb.videofilter`` namespace provides configuration management for:

- :doc:`Keyword <keyword>` - Keyword configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Youtube Key <youtube_key>` - Youtube Key configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.videofilter.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   keyword
   profile
   youtube_key

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
