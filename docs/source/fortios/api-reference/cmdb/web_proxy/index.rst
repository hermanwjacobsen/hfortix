Web Proxy
=========

Overview
--------

The ``cmdb.web_proxy`` namespace provides configuration management for:

- :doc:`Debug Url <debug_url>` - Debug Url configuration endpoint.
- :doc:`Explicit <explicit>` - Explicit configuration endpoint.
- :doc:`Fast Fallback <fast_fallback>` - Fast Fallback configuration endpoint.
- :doc:`Forward Server <forward_server>` - Forward Server configuration endpoint.
- :doc:`Forward Server Group <forward_server_group>` - Forward Server Group configuration endpoint.
- :doc:`Global <global_>` - Global configuration endpoint.
- :doc:`Isolator Server <isolator_server>` - Isolator Server configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.
- :doc:`Url Match <url_match>` - Url Match configuration endpoint.
- :doc:`Wisp <wisp>` - Wisp configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.web_proxy.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   debug_url
   explicit
   fast_fallback
   forward_server
   forward_server_group
   global_
   isolator_server
   profile
   url_match
   wisp

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
