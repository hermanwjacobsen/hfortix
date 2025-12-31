Ips
===

Configure IPS custom signature configuration and management.

Overview
--------

The ``cmdb.ips`` category provides configuration management for:

- **Custom** - Configure IPS custom signature.
- **Decoder** - Configure IPS decoder.
- **Global** - Configure IPS global parameter.
- **Rule** - Configure IPS rules.
- **Rule Settings** - Configure IPS rule setting.
- **Sensor** - Configure IPS sensor.
- **Settings** - Configure IPS VDOM parameter.
- **View Map** - Configure IPS view-map.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.ips

Available Endpoints
-------------------

**custom**
   Configure IPS custom signature.
   
   .. code-block:: python
   
      # List all custom
      items = fgt.api.cmdb.ips.custom.get()
      
      # Get specific custom
      item = fgt.api.cmdb.ips.custom.get(mkey='name')

**decoder**
   Configure IPS decoder.
   
   .. code-block:: python
   
      # List all decoder
      items = fgt.api.cmdb.ips.decoder.get()
      
      # Get specific decoder
      item = fgt.api.cmdb.ips.decoder.get(mkey='name')

**global**
   Configure IPS global parameter.
   
   .. code-block:: python
   
      # List all global
      items = fgt.api.cmdb.ips.global.get()
      
      # Get specific global
      item = fgt.api.cmdb.ips.global.get(mkey='name')

**rule**
   Configure IPS rules.
   
   .. code-block:: python
   
      # List all rule
      items = fgt.api.cmdb.ips.rule.get()
      
      # Get specific rule
      item = fgt.api.cmdb.ips.rule.get(mkey='name')

**rule-settings**
   Configure IPS rule setting.
   
   .. code-block:: python
   
      # List all rule-settings
      items = fgt.api.cmdb.ips.rule_settings.get()
      
      # Get specific rule-settings
      item = fgt.api.cmdb.ips.rule_settings.get(mkey='name')

**sensor**
   Configure IPS sensor.
   
   .. code-block:: python
   
      # List all sensor
      items = fgt.api.cmdb.ips.sensor.get()
      
      # Get specific sensor
      item = fgt.api.cmdb.ips.sensor.get(mkey='name')

**settings**
   Configure IPS VDOM parameter.
   
   .. code-block:: python
   
      # List all settings
      items = fgt.api.cmdb.ips.settings.get()
      
      # Get specific settings
      item = fgt.api.cmdb.ips.settings.get(mkey='name')

**view-map**
   Configure IPS view-map.
   
   .. code-block:: python
   
      # List all view-map
      items = fgt.api.cmdb.ips.view_map.get()
      
      # Get specific view-map
      item = fgt.api.cmdb.ips.view_map.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.ips.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.ips.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.ips.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.ips.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.ips.{endpoint}.delete(mkey='config-name')

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
