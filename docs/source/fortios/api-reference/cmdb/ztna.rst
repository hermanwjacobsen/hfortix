Ztna
====

Configure ZTNA Reverse-Connector configuration and management.

Overview
--------

The ``cmdb.ztna`` category provides configuration management for:

- :ref:`Reverse Connector <ztna-reverse-connector>` - Configure ZTNA Reverse-Connector.
- :ref:`Traffic Forward Proxy <ztna-traffic-forward-proxy>` - Configure ZTNA traffic forward proxy.
- :ref:`Web Portal <ztna-web-portal>` - Configure ztna web-portal.
- :ref:`Web Portal Bookmark <ztna-web-portal-bookmark>` - Configure ztna web-portal bookmark.
- :ref:`Web Proxy <ztna-web-proxy>` - Configure ZTNA web-proxy.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.ztna

Available Endpoints
-------------------

.. _ztna-reverse-connector:

reverse-connector
~~~~~~~~~~~~~~~~~

Configure ZTNA Reverse-Connector.

**Python attribute:** ``reverse_connector``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ztna.reverse_connector.get()
   
   # Get specific item
   item = fgt.api.cmdb.ztna.reverse_connector.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ztna.reverse_connector.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ztna.reverse_connector.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ztna.reverse_connector.delete(mkey='item-name')

.. _ztna-traffic-forward-proxy:

traffic-forward-proxy
~~~~~~~~~~~~~~~~~~~~~

Configure ZTNA traffic forward proxy.

**Python attribute:** ``traffic_forward_proxy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ztna.traffic_forward_proxy.get()
   
   # Get specific item
   item = fgt.api.cmdb.ztna.traffic_forward_proxy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ztna.traffic_forward_proxy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ztna.traffic_forward_proxy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ztna.traffic_forward_proxy.delete(mkey='item-name')

.. _ztna-web-portal:

web-portal
~~~~~~~~~~

Configure ztna web-portal.

**Python attribute:** ``web_portal``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ztna.web_portal.get()
   
   # Get specific item
   item = fgt.api.cmdb.ztna.web_portal.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ztna.web_portal.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ztna.web_portal.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ztna.web_portal.delete(mkey='item-name')

.. _ztna-web-portal-bookmark:

web-portal-bookmark
~~~~~~~~~~~~~~~~~~~

Configure ztna web-portal bookmark.

**Python attribute:** ``web_portal_bookmark``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ztna.web_portal_bookmark.get()
   
   # Get specific item
   item = fgt.api.cmdb.ztna.web_portal_bookmark.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ztna.web_portal_bookmark.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ztna.web_portal_bookmark.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ztna.web_portal_bookmark.delete(mkey='item-name')

.. _ztna-web-proxy:

web-proxy
~~~~~~~~~

Configure ZTNA web-proxy.

**Python attribute:** ``web_proxy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ztna.web_proxy.get()
   
   # Get specific item
   item = fgt.api.cmdb.ztna.web_proxy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ztna.web_proxy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ztna.web_proxy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ztna.web_proxy.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.ztna.reverse_connector.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.ztna.reverse_connector.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.ztna.reverse_connector.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.ztna.reverse_connector.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.ztna.reverse_connector.delete(mkey='config-name')

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
