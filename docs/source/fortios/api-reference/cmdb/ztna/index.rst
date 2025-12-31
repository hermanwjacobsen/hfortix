ZTNA
====

Overview
--------

The ``cmdb.ztna`` namespace provides configuration management for:

- :doc:`Reverse Connector <reverse_connector>` - Reverse Connector configuration endpoint.
- :doc:`Traffic Forward Proxy <traffic_forward_proxy>` - Traffic Forward Proxy configuration endpoint.
- :doc:`Web Portal <web_portal>` - Web Portal configuration endpoint.
- :doc:`Web Portal Bookmark <web_portal_bookmark>` - Web Portal Bookmark configuration endpoint.
- :doc:`Web Proxy <web_proxy>` - Web Proxy configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.ztna.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   reverse_connector
   traffic_forward_proxy
   web_portal
   web_portal_bookmark
   web_proxy

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
