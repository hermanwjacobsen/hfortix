Vpn
===

CA certificate configuration and management.

Overview
--------

The ``cmdb.vpn`` category provides configuration management for:

- :ref:`Kmip Server <vpn-kmip-server>` - KMIP server entry configuration.
- :ref:`L2Tp <vpn-l2tp>` - Configure L2TP.
- :ref:`Pptp <vpn-pptp>` - Configure PPTP.
- :ref:`Qkd <vpn-qkd>` - Configure Quantum Key Distribution servers


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.vpn

Available Endpoints
-------------------

.. _vpn-kmip-server:

kmip-server
~~~~~~~~~~~

KMIP server entry configuration.

**Python attribute:** ``kmip_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.vpn.kmip_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.vpn.kmip_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.vpn.kmip_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.vpn.kmip_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.vpn.kmip_server.delete(mkey='item-name')

.. _vpn-l2tp:

l2tp
~~~~

Configure L2TP.

**Python attribute:** ``l2tp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.vpn.l2tp.get()
   
   # Get specific item
   item = fgt.api.cmdb.vpn.l2tp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.vpn.l2tp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.vpn.l2tp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.vpn.l2tp.delete(mkey='item-name')

.. _vpn-pptp:

pptp
~~~~

Configure PPTP.

**Python attribute:** ``pptp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.vpn.pptp.get()
   
   # Get specific item
   item = fgt.api.cmdb.vpn.pptp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.vpn.pptp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.vpn.pptp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.vpn.pptp.delete(mkey='item-name')

.. _vpn-qkd:

qkd
~~~

Configure Quantum Key Distribution servers

**Python attribute:** ``qkd``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.vpn.qkd.get()
   
   # Get specific item
   item = fgt.api.cmdb.vpn.qkd.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.vpn.qkd.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.vpn.qkd.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.vpn.qkd.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.vpn.kmip_server.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.vpn.kmip_server.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.vpn.kmip_server.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.vpn.kmip_server.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.vpn.kmip_server.delete(mkey='config-name')

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
