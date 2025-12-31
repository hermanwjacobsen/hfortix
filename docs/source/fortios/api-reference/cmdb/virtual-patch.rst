Virtual Patch
=============

Configure virtual-patch profile configuration and management.

Overview
--------

The ``cmdb.virtual-patch`` category provides configuration management for:

- :ref:`Profile <virtual-patch-profile>` - Configure virtual-patch profile.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.virtual-patch

Available Endpoints
-------------------

.. _virtual-patch-profile:

profile
~~~~~~~

Configure virtual-patch profile.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.virtual-patch.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.virtual-patch.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.virtual-patch.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.virtual-patch.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.virtual-patch.profile.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.virtual-patch.profile.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.virtual-patch.profile.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.virtual-patch.profile.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.virtual-patch.profile.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.virtual-patch.profile.delete(mkey='config-name')

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
