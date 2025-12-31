Endpoint Control
================

Configure FortiClient Enterprise Management Server (EMS) entries configuration and management.

Overview
--------

The ``cmdb.endpoint-control`` category provides configuration management for:

- **Fctems** - Configure FortiClient Enterprise Management Server (EMS) entries.
- **Fctems Override** - Configure FortiClient Enterprise Management Server (EMS) entries.
- **Settings** - Configure endpoint control settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.endpoint-control

Available Endpoints
-------------------

**fctems**
   Configure FortiClient Enterprise Management Server (EMS) entries.
   
   .. code-block:: python
   
      # List all fctems
      items = fgt.api.cmdb.endpoint-control.fctems.get()
      
      # Get specific fctems
      item = fgt.api.cmdb.endpoint-control.fctems.get(mkey='name')

**fctems-override**
   Configure FortiClient Enterprise Management Server (EMS) entries.
   
   .. code-block:: python
   
      # List all fctems-override
      items = fgt.api.cmdb.endpoint-control.fctems_override.get()
      
      # Get specific fctems-override
      item = fgt.api.cmdb.endpoint-control.fctems_override.get(mkey='name')

**settings**
   Configure endpoint control settings.
   
   .. code-block:: python
   
      # List all settings
      items = fgt.api.cmdb.endpoint-control.settings.get()
      
      # Get specific settings
      item = fgt.api.cmdb.endpoint-control.settings.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.endpoint-control.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.endpoint-control.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.endpoint-control.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.endpoint-control.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.endpoint-control.{endpoint}.delete(mkey='config-name')

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
