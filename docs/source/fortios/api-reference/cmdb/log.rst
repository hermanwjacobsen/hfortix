Log
===

Configure filters for local disk logging configuration and management.

Overview
--------

The ``cmdb.log`` category provides configuration management for:

- :ref:`Custom Field <log-custom-field>` - Configure custom log fields.
- :ref:`Eventfilter <log-eventfilter>` - Configure log event filters.
- :ref:`Gui Display <log-gui-display>` - Configure how log messages are displayed on the GUI.
- :ref:`Setting <log-setting>` - Configure general log settings.
- :ref:`Threat Weight <log-threat-weight>` - Configure threat weight settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.log

Available Endpoints
-------------------

.. _log-custom-field:

custom-field
~~~~~~~~~~~~

Configure custom log fields.

**Python attribute:** ``custom_field``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.log.custom_field.get()
   
   # Get specific item
   item = fgt.api.cmdb.log.custom_field.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.log.custom_field.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.log.custom_field.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.log.custom_field.delete(mkey='item-name')

.. _log-eventfilter:

eventfilter
~~~~~~~~~~~

Configure log event filters.

**Python attribute:** ``eventfilter``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.log.eventfilter.get()
   
   # Get specific item
   item = fgt.api.cmdb.log.eventfilter.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.log.eventfilter.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.log.eventfilter.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.log.eventfilter.delete(mkey='item-name')

.. _log-gui-display:

gui-display
~~~~~~~~~~~

Configure how log messages are displayed on the GUI.

**Python attribute:** ``gui_display``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.log.gui_display.get()
   
   # Get specific item
   item = fgt.api.cmdb.log.gui_display.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.log.gui_display.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.log.gui_display.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.log.gui_display.delete(mkey='item-name')

.. _log-setting:

setting
~~~~~~~

Configure general log settings.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.log.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.log.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.log.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.log.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.log.setting.delete(mkey='item-name')

.. _log-threat-weight:

threat-weight
~~~~~~~~~~~~~

Configure threat weight settings.

**Python attribute:** ``threat_weight``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.log.threat_weight.get()
   
   # Get specific item
   item = fgt.api.cmdb.log.threat_weight.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.log.threat_weight.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.log.threat_weight.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.log.threat_weight.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.log.custom_field.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.log.custom_field.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.log.custom_field.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.log.custom_field.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.log.custom_field.delete(mkey='config-name')

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
