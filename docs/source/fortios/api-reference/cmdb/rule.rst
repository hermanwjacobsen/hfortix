Rule
====

Show FMWP signatures configuration and management.

Overview
--------

The ``cmdb.rule`` category provides configuration management for:

- :ref:`Fmwp <rule-fmwp>` - Show FMWP signatures.
- :ref:`Iotd <rule-iotd>` - Show IOT detection signatures.
- :ref:`Otdt <rule-otdt>` - Show OT detection signatures.
- :ref:`Otvp <rule-otvp>` - Show OT patch signatures.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.rule

Available Endpoints
-------------------

.. _rule-fmwp:

fmwp
~~~~

Show FMWP signatures.

**Python attribute:** ``fmwp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.rule.fmwp.get()
   
   # Get specific item
   item = fgt.api.cmdb.rule.fmwp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.rule.fmwp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.rule.fmwp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.rule.fmwp.delete(mkey='item-name')

.. _rule-iotd:

iotd
~~~~

Show IOT detection signatures.

**Python attribute:** ``iotd``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.rule.iotd.get()
   
   # Get specific item
   item = fgt.api.cmdb.rule.iotd.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.rule.iotd.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.rule.iotd.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.rule.iotd.delete(mkey='item-name')

.. _rule-otdt:

otdt
~~~~

Show OT detection signatures.

**Python attribute:** ``otdt``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.rule.otdt.get()
   
   # Get specific item
   item = fgt.api.cmdb.rule.otdt.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.rule.otdt.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.rule.otdt.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.rule.otdt.delete(mkey='item-name')

.. _rule-otvp:

otvp
~~~~

Show OT patch signatures.

**Python attribute:** ``otvp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.rule.otvp.get()
   
   # Get specific item
   item = fgt.api.cmdb.rule.otvp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.rule.otvp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.rule.otvp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.rule.otvp.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.rule.fmwp.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.rule.fmwp.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.rule.fmwp.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.rule.fmwp.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.rule.fmwp.delete(mkey='config-name')

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
