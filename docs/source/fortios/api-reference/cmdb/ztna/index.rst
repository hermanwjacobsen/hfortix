Ztna
====

Configure ZTNA Reverse-Connector configuration and management.

Overview
--------

The ``cmdb.ztna`` category provides configuration management for:

- :doc:`Reverse Connector <reverse-connector>` - Configure ZTNA Reverse-Connector.
- :doc:`Traffic Forward Proxy <traffic-forward-proxy>` - Configure ZTNA traffic forward proxy.
- :doc:`Web Portal <web-portal>` - Configure ztna web-portal.
- :doc:`Web Portal Bookmark <web-portal-bookmark>` - Configure ztna web-portal bookmark.
- :doc:`Web Proxy <web-proxy>` - Configure ZTNA web-proxy.


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
   
   reverse-connector
   traffic-forward-proxy
   web-portal
   web-portal-bookmark
   web-proxy

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
