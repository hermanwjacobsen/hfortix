Web Proxy
=========

Configure debug URL addresses configuration and management.

Overview
--------

The ``cmdb.web-proxy`` category provides configuration management for:

- :ref:`Debug Url <web-proxy-debug-url>` - Configure debug URL addresses.
- :ref:`Explicit <web-proxy-explicit>` - Configure explicit Web proxy settings.
- :ref:`Fast Fallback <web-proxy-fast-fallback>` - Proxy destination connection fast-fallback.
- :ref:`Forward Server <web-proxy-forward-server>` - Configure forward-server addresses.
- :ref:`Forward Server Group <web-proxy-forward-server-group>` - Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.
- :ref:`Global <web-proxy-global>` - Configure Web proxy global settings.
- :ref:`Isolator Server <web-proxy-isolator-server>` - Configure forward-server addresses.
- :ref:`Profile <web-proxy-profile>` - Configure web proxy profiles.
- :ref:`Url Match <web-proxy-url-match>` - Exempt URLs from web proxy forwarding, caching and fast-fallback.
- :ref:`Wisp <web-proxy-wisp>` - Configure Websense Integrated Services Protocol (WISP) servers.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.web-proxy

Available Endpoints
-------------------

.. _web-proxy-debug-url:

debug-url
~~~~~~~~~

Configure debug URL addresses.

**Python attribute:** ``debug_url``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.debug_url.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.debug_url.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.debug_url.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.debug_url.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.debug_url.delete(mkey='item-name')

.. _web-proxy-explicit:

explicit
~~~~~~~~

Configure explicit Web proxy settings.

**Python attribute:** ``explicit``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.explicit.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.explicit.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.explicit.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.explicit.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.explicit.delete(mkey='item-name')

.. _web-proxy-fast-fallback:

fast-fallback
~~~~~~~~~~~~~

Proxy destination connection fast-fallback.

**Python attribute:** ``fast_fallback``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.fast_fallback.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.fast_fallback.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.fast_fallback.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.fast_fallback.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.fast_fallback.delete(mkey='item-name')

.. _web-proxy-forward-server:

forward-server
~~~~~~~~~~~~~~

Configure forward-server addresses.

**Python attribute:** ``forward_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.forward_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.forward_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.forward_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.forward_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.forward_server.delete(mkey='item-name')

.. _web-proxy-forward-server-group:

forward-server-group
~~~~~~~~~~~~~~~~~~~~

Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.

**Python attribute:** ``forward_server_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.forward_server_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.forward_server_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.forward_server_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.forward_server_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.forward_server_group.delete(mkey='item-name')

.. _web-proxy-global:

global
~~~~~~

Configure Web proxy global settings.

**Python attribute:** ``global``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.global.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.global.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.global.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.global.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.global.delete(mkey='item-name')

.. _web-proxy-isolator-server:

isolator-server
~~~~~~~~~~~~~~~

Configure forward-server addresses.

**Python attribute:** ``isolator_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.isolator_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.isolator_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.isolator_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.isolator_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.isolator_server.delete(mkey='item-name')

.. _web-proxy-profile:

profile
~~~~~~~

Configure web proxy profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.profile.delete(mkey='item-name')

.. _web-proxy-url-match:

url-match
~~~~~~~~~

Exempt URLs from web proxy forwarding, caching and fast-fallback.

**Python attribute:** ``url_match``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.url_match.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.url_match.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.url_match.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.url_match.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.url_match.delete(mkey='item-name')

.. _web-proxy-wisp:

wisp
~~~~

Configure Websense Integrated Services Protocol (WISP) servers.

**Python attribute:** ``wisp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.web-proxy.wisp.get()
   
   # Get specific item
   item = fgt.api.cmdb.web-proxy.wisp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.web-proxy.wisp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.web-proxy.wisp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.web-proxy.wisp.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.web-proxy.debug_url.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.web-proxy.debug_url.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.web-proxy.debug_url.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.web-proxy.debug_url.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.web-proxy.debug_url.delete(mkey='config-name')

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
