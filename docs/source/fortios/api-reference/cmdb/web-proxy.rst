Web Proxy
=========

Configure debug URL addresses configuration and management.

Overview
--------

The ``cmdb.web-proxy`` category provides configuration management for:

- **Debug Url** - Configure debug URL addresses.
- **Explicit** - Configure explicit Web proxy settings.
- **Fast Fallback** - Proxy destination connection fast-fallback.
- **Forward Server** - Configure forward-server addresses.
- **Forward Server Group** - Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
- **Global** - Configure Web proxy global settings.
- **Isolator Server** - Configure forward-server addresses.
- **Profile** - Configure web proxy profiles.
- **Url Match** - Exempt URLs from web proxy forwarding, caching and fast-fallback.
- **Wisp** - Configure Websense Integrated Services Protocol (WISP) servers.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.web-proxy

Available Endpoints
-------------------

**debug-url**
   Configure debug URL addresses.
   
   .. code-block:: python
   
      # List all debug-url
      items = fgt.api.cmdb.web-proxy.debug_url.get()
      
      # Get specific debug-url
      item = fgt.api.cmdb.web-proxy.debug_url.get(mkey='name')

**explicit**
   Configure explicit Web proxy settings.
   
   .. code-block:: python
   
      # List all explicit
      items = fgt.api.cmdb.web-proxy.explicit.get()
      
      # Get specific explicit
      item = fgt.api.cmdb.web-proxy.explicit.get(mkey='name')

**fast-fallback**
   Proxy destination connection fast-fallback.
   
   .. code-block:: python
   
      # List all fast-fallback
      items = fgt.api.cmdb.web-proxy.fast_fallback.get()
      
      # Get specific fast-fallback
      item = fgt.api.cmdb.web-proxy.fast_fallback.get(mkey='name')

**forward-server**
   Configure forward-server addresses.
   
   .. code-block:: python
   
      # List all forward-server
      items = fgt.api.cmdb.web-proxy.forward_server.get()
      
      # Get specific forward-server
      item = fgt.api.cmdb.web-proxy.forward_server.get(mkey='name')

**forward-server-group**
   Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
   
   .. code-block:: python
   
      # List all forward-server-group
      items = fgt.api.cmdb.web-proxy.forward_server_group.get()
      
      # Get specific forward-server-group
      item = fgt.api.cmdb.web-proxy.forward_server_group.get(mkey='name')

**global**
   Configure Web proxy global settings.
   
   .. code-block:: python
   
      # List all global
      items = fgt.api.cmdb.web-proxy.global.get()
      
      # Get specific global
      item = fgt.api.cmdb.web-proxy.global.get(mkey='name')

**isolator-server**
   Configure forward-server addresses.
   
   .. code-block:: python
   
      # List all isolator-server
      items = fgt.api.cmdb.web-proxy.isolator_server.get()
      
      # Get specific isolator-server
      item = fgt.api.cmdb.web-proxy.isolator_server.get(mkey='name')

**profile**
   Configure web proxy profiles.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.web-proxy.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.web-proxy.profile.get(mkey='name')

**url-match**
   Exempt URLs from web proxy forwarding, caching and fast-fallback.
   
   .. code-block:: python
   
      # List all url-match
      items = fgt.api.cmdb.web-proxy.url_match.get()
      
      # Get specific url-match
      item = fgt.api.cmdb.web-proxy.url_match.get(mkey='name')

**wisp**
   Configure Websense Integrated Services Protocol (WISP) servers.
   
   .. code-block:: python
   
      # List all wisp
      items = fgt.api.cmdb.web-proxy.wisp.get()
      
      # Get specific wisp
      item = fgt.api.cmdb.web-proxy.wisp.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.web-proxy.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.web-proxy.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.web-proxy.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.web-proxy.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.web-proxy.{endpoint}.delete(mkey='config-name')

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
