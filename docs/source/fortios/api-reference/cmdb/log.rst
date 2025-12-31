Log
===

Configure filters for local disk logging configuration and management.

Overview
--------

The ``cmdb.log`` category provides configuration management for:

- **Custom Field** - Configure custom log fields.
- **Eventfilter** - Configure log event filters.
- **Gui Display** - Configure how log messages are displayed on the GUI.
- **Setting** - Configure general log settings.
- **Threat Weight** - Configure threat weight settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.log

Available Endpoints
-------------------

**custom-field**
   Configure custom log fields.
   
   .. code-block:: python
   
      # List all custom-field
      items = fgt.api.cmdb.log.custom_field.get()
      
      # Get specific custom-field
      item = fgt.api.cmdb.log.custom_field.get(mkey='name')

**eventfilter**
   Configure log event filters.
   
   .. code-block:: python
   
      # List all eventfilter
      items = fgt.api.cmdb.log.eventfilter.get()
      
      # Get specific eventfilter
      item = fgt.api.cmdb.log.eventfilter.get(mkey='name')

**gui-display**
   Configure how log messages are displayed on the GUI.
   
   .. code-block:: python
   
      # List all gui-display
      items = fgt.api.cmdb.log.gui_display.get()
      
      # Get specific gui-display
      item = fgt.api.cmdb.log.gui_display.get(mkey='name')

**setting**
   Configure general log settings.
   
   .. code-block:: python
   
      # List all setting
      items = fgt.api.cmdb.log.setting.get()
      
      # Get specific setting
      item = fgt.api.cmdb.log.setting.get(mkey='name')

**threat-weight**
   Configure threat weight settings.
   
   .. code-block:: python
   
      # List all threat-weight
      items = fgt.api.cmdb.log.threat_weight.get()
      
      # Get specific threat-weight
      item = fgt.api.cmdb.log.threat_weight.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.log.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.log.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.log.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.log.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.log.{endpoint}.delete(mkey='config-name')

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
