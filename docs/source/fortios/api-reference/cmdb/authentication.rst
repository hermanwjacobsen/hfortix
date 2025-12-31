Authentication
==============

Configure Authentication Rules configuration and management.

Overview
--------

The ``cmdb.authentication`` category provides configuration management for:

- :ref:`Rule <authentication-rule>` - Configure Authentication Rules.
- :ref:`Scheme <authentication-scheme>` - Configure Authentication Schemes.
- :ref:`Setting <authentication-setting>` - Configure authentication setting.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.authentication

Available Endpoints
-------------------

.. _authentication-rule:

rule
~~~~

Configure Authentication Rules.

**Python attribute:** ``rule``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.authentication.rule.get()
   
   # Get specific item
   item = fgt.api.cmdb.authentication.rule.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.authentication.rule.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.authentication.rule.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.authentication.rule.delete(mkey='item-name')

.. _authentication-scheme:

scheme
~~~~~~

Configure Authentication Schemes.

**Python attribute:** ``scheme``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.authentication.scheme.get()
   
   # Get specific item
   item = fgt.api.cmdb.authentication.scheme.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.authentication.scheme.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.authentication.scheme.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.authentication.scheme.delete(mkey='item-name')

.. _authentication-setting:

setting
~~~~~~~

Configure authentication setting.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.authentication.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.authentication.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.authentication.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.authentication.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.authentication.setting.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.authentication.rule.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.authentication.rule.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.authentication.rule.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.authentication.rule.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.authentication.rule.delete(mkey='config-name')

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
