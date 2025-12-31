Ftp Proxy
=========

Configure explicit FTP proxy settings configuration and management.

Overview
--------

The ``cmdb.ftp-proxy`` category provides configuration management for:

- :doc:`Explicit <explicit>` - Configure explicit FTP proxy settings.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.ftp-proxy.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   explicit

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
