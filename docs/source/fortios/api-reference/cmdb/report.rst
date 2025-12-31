Report
======

Report layout configuration configuration and management.

Overview
--------

The ``cmdb.report`` category provides configuration management for:

- **Layout** - Report layout configuration.
- **Setting** - Report setting configuration.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.report

Available Endpoints
-------------------

**layout**
   Report layout configuration.
   
   .. code-block:: python
   
      # List all layout
      items = fgt.api.cmdb.report.layout.get()
      
      # Get specific layout
      item = fgt.api.cmdb.report.layout.get(mkey='name')

**setting**
   Report setting configuration.
   
   .. code-block:: python
   
      # List all setting
      items = fgt.api.cmdb.report.setting.get()
      
      # Get specific setting
      item = fgt.api.cmdb.report.setting.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.report.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.report.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.report.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.report.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.report.{endpoint}.delete(mkey='config-name')

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
