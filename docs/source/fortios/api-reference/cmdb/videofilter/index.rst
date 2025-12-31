Videofilter
===========

Configure video filter keywords configuration and management.

Overview
--------

The ``cmdb.videofilter`` category provides configuration management for:

- :doc:`Keyword <keyword>` - Configure video filter keywords.
- :doc:`Profile <profile>` - Configure VideoFilter profile.
- :doc:`Youtube Key <youtube-key>` - Configure YouTube API keys.


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
   youtube-key

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
