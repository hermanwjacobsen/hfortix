Icap
====

Configure ICAP profiles configuration and management.

Overview
--------

The ``cmdb.icap`` category provides configuration management for:

- :ref:`Profile <icap-profile>` - Configure ICAP profiles.
- :ref:`Server <icap-server>` - Configure ICAP servers.
- :ref:`Server Group <icap-server-group>` - Configure an ICAP server group consisting of multiple forward servers. Supports failover and load balancing.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.icap

Available Endpoints
-------------------

.. _icap-profile:

profile
~~~~~~~

Configure ICAP profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.icap.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.icap.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.icap.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.icap.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.icap.profile.delete(mkey='item-name')

.. _icap-server:

server
~~~~~~

Configure ICAP servers.

**Python attribute:** ``server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.icap.server.get()
   
   # Get specific item
   item = fgt.api.cmdb.icap.server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.icap.server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.icap.server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.icap.server.delete(mkey='item-name')

.. _icap-server-group:

server-group
~~~~~~~~~~~~

Configure an ICAP server group consisting of multiple forward servers. Supports failover and load balancing.

**Python attribute:** ``server_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.icap.server_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.icap.server_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.icap.server_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.icap.server_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.icap.server_group.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.icap.profile.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.icap.profile.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.icap.profile.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.icap.profile.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.icap.profile.delete(mkey='config-name')

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
