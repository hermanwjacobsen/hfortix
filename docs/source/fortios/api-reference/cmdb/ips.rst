Ips
===

Configure IPS custom signature configuration and management.

Overview
--------

The ``cmdb.ips`` category provides configuration management for:

- :ref:`Custom <ips-custom>` - Configure IPS custom signature.
- :ref:`Decoder <ips-decoder>` - Configure IPS decoder.
- :ref:`Global <ips-global>` - Configure IPS global parameter.
- :ref:`Rule <ips-rule>` - Configure IPS rules.
- :ref:`Rule Settings <ips-rule-settings>` - Configure IPS rule setting.
- :ref:`Sensor <ips-sensor>` - Configure IPS sensor.
- :ref:`Settings <ips-settings>` - Configure IPS VDOM parameter.
- :ref:`View Map <ips-view-map>` - Configure IPS view-map.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.ips

Available Endpoints
-------------------

.. _ips-custom:

custom
~~~~~~

Configure IPS custom signature.

**Python attribute:** ``custom``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.custom.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.custom.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.custom.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.custom.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.custom.delete(mkey='item-name')

.. _ips-decoder:

decoder
~~~~~~~

Configure IPS decoder.

**Python attribute:** ``decoder``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.decoder.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.decoder.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.decoder.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.decoder.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.decoder.delete(mkey='item-name')

.. _ips-global:

global
~~~~~~

Configure IPS global parameter.

**Python attribute:** ``global``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.global.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.global.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.global.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.global.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.global.delete(mkey='item-name')

.. _ips-rule:

rule
~~~~

Configure IPS rules.

**Python attribute:** ``rule``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.rule.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.rule.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.rule.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.rule.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.rule.delete(mkey='item-name')

.. _ips-rule-settings:

rule-settings
~~~~~~~~~~~~~

Configure IPS rule setting.

**Python attribute:** ``rule_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.rule_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.rule_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.rule_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.rule_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.rule_settings.delete(mkey='item-name')

.. _ips-sensor:

sensor
~~~~~~

Configure IPS sensor.

**Python attribute:** ``sensor``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.sensor.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.sensor.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.sensor.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.sensor.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.sensor.delete(mkey='item-name')

.. _ips-settings:

settings
~~~~~~~~

Configure IPS VDOM parameter.

**Python attribute:** ``settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.settings.delete(mkey='item-name')

.. _ips-view-map:

view-map
~~~~~~~~

Configure IPS view-map.

**Python attribute:** ``view_map``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.ips.view_map.get()
   
   # Get specific item
   item = fgt.api.cmdb.ips.view_map.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.ips.view_map.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.ips.view_map.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.ips.view_map.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.ips.custom.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.ips.custom.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.ips.custom.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.ips.custom.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.ips.custom.delete(mkey='config-name')

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
