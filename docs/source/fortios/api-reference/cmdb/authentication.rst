Authentication
==============

Configure Authentication Rules configuration and management.

Overview
--------

The ``cmdb.authentication`` category provides configuration management for:

- **Rule** - Configure Authentication Rules.
- **Scheme** - Configure Authentication Schemes.
- **Setting** - Configure authentication setting.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.authentication

Available Endpoints
-------------------

**rule**
   Configure Authentication Rules.
   
   .. code-block:: python
   
      # List all rule
      items = fgt.api.cmdb.authentication.rule.get()
      
      # Get specific rule
      item = fgt.api.cmdb.authentication.rule.get(mkey='name')

**scheme**
   Configure Authentication Schemes.
   
   .. code-block:: python
   
      # List all scheme
      items = fgt.api.cmdb.authentication.scheme.get()
      
      # Get specific scheme
      item = fgt.api.cmdb.authentication.scheme.get(mkey='name')

**setting**
   Configure authentication setting.
   
   .. code-block:: python
   
      # List all setting
      items = fgt.api.cmdb.authentication.setting.get()
      
      # Get specific setting
      item = fgt.api.cmdb.authentication.setting.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.authentication.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.authentication.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.authentication.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.authentication.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.authentication.{endpoint}.delete(mkey='config-name')

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
