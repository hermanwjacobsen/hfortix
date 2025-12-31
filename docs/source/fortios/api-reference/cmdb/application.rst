Application
===========

Configure custom application signatures configuration and management.

Overview
--------

The ``cmdb.application`` category provides configuration management for:

- :ref:`Custom <application-custom>` - Configure custom application signatures.
- :ref:`Group <application-group>` - Configure firewall application groups.
- :ref:`List <application-list>` - Configure application control lists.
- :ref:`Name <application-name>` - Configure application signatures.
- :ref:`Rule Settings <application-rule-settings>` - Configure application rule settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.application

Available Endpoints
-------------------

.. _application-custom:

custom
~~~~~~

Configure custom application signatures.

**Python attribute:** ``custom``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.application.custom.get()
   
   # Get specific item
   item = fgt.api.cmdb.application.custom.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.application.custom.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.application.custom.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.application.custom.delete(mkey='item-name')

.. _application-group:

group
~~~~~

Configure firewall application groups.

**Python attribute:** ``group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.application.group.get()
   
   # Get specific item
   item = fgt.api.cmdb.application.group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.application.group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.application.group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.application.group.delete(mkey='item-name')

.. _application-list:

list
~~~~

Configure application control lists.

**Python attribute:** ``list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.application.list.get()
   
   # Get specific item
   item = fgt.api.cmdb.application.list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.application.list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.application.list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.application.list.delete(mkey='item-name')

.. _application-name:

name
~~~~

Configure application signatures.

**Python attribute:** ``name``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.application.name.get()
   
   # Get specific item
   item = fgt.api.cmdb.application.name.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.application.name.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.application.name.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.application.name.delete(mkey='item-name')

.. _application-rule-settings:

rule-settings
~~~~~~~~~~~~~

Configure application rule settings.

**Python attribute:** ``rule_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.application.rule_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.application.rule_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.application.rule_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.application.rule_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.application.rule_settings.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.application.custom.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.application.custom.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.application.custom.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.application.custom.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.application.custom.delete(mkey='config-name')

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
