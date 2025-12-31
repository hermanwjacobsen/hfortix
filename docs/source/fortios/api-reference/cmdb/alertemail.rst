Alertemail
==========

Configure alert email settings configuration and management.

Overview
--------

The ``cmdb.alertemail`` category provides configuration management for:

- :ref:`Setting <alertemail-setting>` - Configure alert email settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.alertemail

Available Endpoints
-------------------

.. _alertemail-setting:

setting
~~~~~~~

Configure alert email settings.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.alertemail.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.alertemail.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.alertemail.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.alertemail.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.alertemail.setting.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.alertemail.setting.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.alertemail.setting.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.alertemail.setting.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.alertemail.setting.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.alertemail.setting.delete(mkey='config-name')

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
