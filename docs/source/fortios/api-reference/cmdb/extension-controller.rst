Extension Controller
====================

FortiExtender dataplan configuration configuration and management.

Overview
--------

The ``cmdb.extension-controller`` category provides configuration management for:

- :ref:`Dataplan <extension-controller-dataplan>` - FortiExtender dataplan configuration.
- :ref:`Extender <extension-controller-extender>` - Extender controller configuration.
- :ref:`Extender Profile <extension-controller-extender-profile>` - FortiExtender extender profile configuration.
- :ref:`Extender Vap <extension-controller-extender-vap>` - FortiExtender wifi vap configuration.
- :ref:`Fortigate <extension-controller-fortigate>` - FortiGate controller configuration.
- :ref:`Fortigate Profile <extension-controller-fortigate-profile>` - FortiGate connector profile configuration.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.extension-controller

Available Endpoints
-------------------

.. _extension-controller-dataplan:

dataplan
~~~~~~~~

FortiExtender dataplan configuration.

**Python attribute:** ``dataplan``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.extension-controller.dataplan.get()
   
   # Get specific item
   item = fgt.api.cmdb.extension-controller.dataplan.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.extension-controller.dataplan.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.extension-controller.dataplan.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.extension-controller.dataplan.delete(mkey='item-name')

.. _extension-controller-extender:

extender
~~~~~~~~

Extender controller configuration.

**Python attribute:** ``extender``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.extension-controller.extender.get()
   
   # Get specific item
   item = fgt.api.cmdb.extension-controller.extender.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.extension-controller.extender.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.extension-controller.extender.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.extension-controller.extender.delete(mkey='item-name')

.. _extension-controller-extender-profile:

extender-profile
~~~~~~~~~~~~~~~~

FortiExtender extender profile configuration.

**Python attribute:** ``extender_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.extension-controller.extender_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.extension-controller.extender_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.extension-controller.extender_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.extension-controller.extender_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.extension-controller.extender_profile.delete(mkey='item-name')

.. _extension-controller-extender-vap:

extender-vap
~~~~~~~~~~~~

FortiExtender wifi vap configuration.

**Python attribute:** ``extender_vap``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.extension-controller.extender_vap.get()
   
   # Get specific item
   item = fgt.api.cmdb.extension-controller.extender_vap.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.extension-controller.extender_vap.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.extension-controller.extender_vap.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.extension-controller.extender_vap.delete(mkey='item-name')

.. _extension-controller-fortigate:

fortigate
~~~~~~~~~

FortiGate controller configuration.

**Python attribute:** ``fortigate``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.extension-controller.fortigate.get()
   
   # Get specific item
   item = fgt.api.cmdb.extension-controller.fortigate.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.extension-controller.fortigate.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.extension-controller.fortigate.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.extension-controller.fortigate.delete(mkey='item-name')

.. _extension-controller-fortigate-profile:

fortigate-profile
~~~~~~~~~~~~~~~~~

FortiGate connector profile configuration.

**Python attribute:** ``fortigate_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.extension-controller.fortigate_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.extension-controller.fortigate_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.extension-controller.fortigate_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.extension-controller.fortigate_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.extension-controller.fortigate_profile.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.extension-controller.dataplan.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.extension-controller.dataplan.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.extension-controller.dataplan.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.extension-controller.dataplan.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.extension-controller.dataplan.delete(mkey='config-name')

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
