Diameter Filter
===============

Configure Diameter filter profiles configuration and management.

Overview
--------

The ``cmdb.diameter-filter`` category provides configuration management for:

- :ref:`Profile <diameter-filter-profile>` - Configure Diameter filter profiles.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.diameter-filter

Available Endpoints
-------------------

.. _diameter-filter-profile:

profile
~~~~~~~

Configure Diameter filter profiles.

**Python attribute:** ``profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.diameter-filter.profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.diameter-filter.profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.diameter-filter.profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.diameter-filter.profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.diameter-filter.profile.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.diameter-filter.profile.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.diameter-filter.profile.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.diameter-filter.profile.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.diameter-filter.profile.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.diameter-filter.profile.delete(mkey='config-name')

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
