Application
===========

Configure custom application signatures configuration and management.

Overview
--------

The ``cmdb.application`` category provides configuration management for:

- **Custom** - Configure custom application signatures.
- **Group** - Configure firewall application groups.
- **List** - Configure application control lists.
- **Name** - Configure application signatures.
- **Rule Settings** - Configure application rule settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.application

Available Endpoints
-------------------

**custom**
   Configure custom application signatures.
   
   .. code-block:: python
   
      # List all custom
      items = fgt.api.cmdb.application.custom.get()
      
      # Get specific custom
      item = fgt.api.cmdb.application.custom.get(mkey='name')

**group**
   Configure firewall application groups.
   
   .. code-block:: python
   
      # List all group
      items = fgt.api.cmdb.application.group.get()
      
      # Get specific group
      item = fgt.api.cmdb.application.group.get(mkey='name')

**list**
   Configure application control lists.
   
   .. code-block:: python
   
      # List all list
      items = fgt.api.cmdb.application.list.get()
      
      # Get specific list
      item = fgt.api.cmdb.application.list.get(mkey='name')

**name**
   Configure application signatures.
   
   .. code-block:: python
   
      # List all name
      items = fgt.api.cmdb.application.name.get()
      
      # Get specific name
      item = fgt.api.cmdb.application.name.get(mkey='name')

**rule-settings**
   Configure application rule settings.
   
   .. code-block:: python
   
      # List all rule-settings
      items = fgt.api.cmdb.application.rule_settings.get()
      
      # Get specific rule-settings
      item = fgt.api.cmdb.application.rule_settings.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.application.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.application.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.application.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.application.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.application.{endpoint}.delete(mkey='config-name')

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
