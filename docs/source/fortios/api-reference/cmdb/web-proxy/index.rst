Web Proxy
=========

Configure debug URL addresses configuration and management.

Overview
--------

The ``cmdb.web-proxy`` category provides configuration management for:

- :doc:`Debug Url <debug-url>` - Configure debug URL addresses.
- :doc:`Explicit <explicit>` - Configure explicit Web proxy settings.
- :doc:`Fast Fallback <fast-fallback>` - Proxy destination connection fast-fallback.
- :doc:`Forward Server <forward-server>` - Configure forward-server addresses.
- :doc:`Forward Server Group <forward-server-group>` - Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
- :doc:`Global <global>` - Configure Web proxy global settings.
- :doc:`Isolator Server <isolator-server>` - Configure forward-server addresses.
- :doc:`Profile <profile>` - Configure web proxy profiles.
- :doc:`Url Match <url-match>` - Exempt URLs from web proxy forwarding, caching and fast-fallback.
- :doc:`Wisp <wisp>` - Configure Websense Integrated Services Protocol (WISP) servers.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.web-proxy.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   debug-url
   explicit
   fast-fallback
   forward-server
   forward-server-group
   global
   isolator-server
   profile
   url-match
   wisp

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
