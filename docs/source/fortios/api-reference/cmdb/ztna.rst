Ztna
====

Configure ZTNA Reverse-Connector configuration and management.

Overview
--------

The ``cmdb.ztna`` category provides configuration management for:

- **Reverse Connector** - Configure ZTNA Reverse-Connector.
- **Traffic Forward Proxy** - Configure ZTNA traffic forward proxy.
- **Web Portal** - Configure ztna web-portal.
- **Web Portal Bookmark** - Configure ztna web-portal bookmark.
- **Web Proxy** - Configure ZTNA web-proxy.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.ztna

Available Endpoints
-------------------

**reverse-connector**
   Configure ZTNA Reverse-Connector.
   
   .. code-block:: python
   
      # List all reverse-connector
      items = fgt.api.cmdb.ztna.reverse_connector.get()
      
      # Get specific reverse-connector
      item = fgt.api.cmdb.ztna.reverse_connector.get(mkey='name')

**traffic-forward-proxy**
   Configure ZTNA traffic forward proxy.
   
   .. code-block:: python
   
      # List all traffic-forward-proxy
      items = fgt.api.cmdb.ztna.traffic_forward_proxy.get()
      
      # Get specific traffic-forward-proxy
      item = fgt.api.cmdb.ztna.traffic_forward_proxy.get(mkey='name')

**web-portal**
   Configure ztna web-portal.
   
   .. code-block:: python
   
      # List all web-portal
      items = fgt.api.cmdb.ztna.web_portal.get()
      
      # Get specific web-portal
      item = fgt.api.cmdb.ztna.web_portal.get(mkey='name')

**web-portal-bookmark**
   Configure ztna web-portal bookmark.
   
   .. code-block:: python
   
      # List all web-portal-bookmark
      items = fgt.api.cmdb.ztna.web_portal_bookmark.get()
      
      # Get specific web-portal-bookmark
      item = fgt.api.cmdb.ztna.web_portal_bookmark.get(mkey='name')

**web-proxy**
   Configure ZTNA web-proxy.
   
   .. code-block:: python
   
      # List all web-proxy
      items = fgt.api.cmdb.ztna.web_proxy.get()
      
      # Get specific web-proxy
      item = fgt.api.cmdb.ztna.web_proxy.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.ztna.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.ztna.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.ztna.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.ztna.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.ztna.{endpoint}.delete(mkey='config-name')

HTTP Methods
------------

All CMDB endpoints support standard HTTP methods:

**.get()**
   HTTP GET - Retrieve configuration(s)

**.post()**
   HTTP POST - Create new configuration

**.put()**
   HTTP PUT - Update existing configuration

**.delete()**
   HTTP DELETE - Remove configuration

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
