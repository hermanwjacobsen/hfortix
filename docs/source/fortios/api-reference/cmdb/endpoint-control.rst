Endpoint Control
================

Configure FortiClient Enterprise Management Server (EMS) entries configuration and management.

Overview
--------

The ``cmdb.endpoint-control`` category provides configuration management for:

- :ref:`Fctems <endpoint-control-fctems>` - Configure FortiClient Enterprise Management Server (EMS) entries.
- :ref:`Fctems Override <endpoint-control-fctems-override>` - Configure FortiClient Enterprise Management Server (EMS) entries.
- :ref:`Settings <endpoint-control-settings>` - Configure endpoint control settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.endpoint-control

Available Endpoints
-------------------

.. _endpoint-control-fctems:

fctems
~~~~~~

Configure FortiClient Enterprise Management Server (EMS) entries.

**Python attribute:** ``fctems``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.endpoint-control.fctems.get()
   
   # Get specific item
   item = fgt.api.cmdb.endpoint-control.fctems.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.endpoint-control.fctems.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.endpoint-control.fctems.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.endpoint-control.fctems.delete(mkey='item-name')

.. _endpoint-control-fctems-override:

fctems-override
~~~~~~~~~~~~~~~

Configure FortiClient Enterprise Management Server (EMS) entries.

**Python attribute:** ``fctems_override``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.endpoint-control.fctems_override.get()
   
   # Get specific item
   item = fgt.api.cmdb.endpoint-control.fctems_override.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.endpoint-control.fctems_override.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.endpoint-control.fctems_override.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.endpoint-control.fctems_override.delete(mkey='item-name')

.. _endpoint-control-settings:

settings
~~~~~~~~

Configure endpoint control settings.

**Python attribute:** ``settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.endpoint-control.settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.endpoint-control.settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.endpoint-control.settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.endpoint-control.settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.endpoint-control.settings.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.endpoint-control.fctems.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.endpoint-control.fctems.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.endpoint-control.fctems.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.endpoint-control.fctems.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.endpoint-control.fctems.delete(mkey='config-name')

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
