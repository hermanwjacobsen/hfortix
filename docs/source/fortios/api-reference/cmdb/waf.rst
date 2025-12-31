Waf
===

Hidden table for datasource configuration and management.

Overview
--------

The ``cmdb.waf`` category provides configuration management for:

- **Main Class** - Hidden table for datasource.
- **Profile** - Configure Web application firewall configuration.
- **Signature** - Hidden table for datasource.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.waf

Available Endpoints
-------------------

**main-class**
   Hidden table for datasource.
   
   .. code-block:: python
   
      # List all main-class
      items = fgt.api.cmdb.waf.main_class.get()
      
      # Get specific main-class
      item = fgt.api.cmdb.waf.main_class.get(mkey='name')

**profile**
   Configure Web application firewall configuration.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.waf.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.waf.profile.get(mkey='name')

**signature**
   Hidden table for datasource.
   
   .. code-block:: python
   
      # List all signature
      items = fgt.api.cmdb.waf.signature.get()
      
      # Get specific signature
      item = fgt.api.cmdb.waf.signature.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.waf.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.waf.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.waf.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.waf.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.waf.{endpoint}.delete(mkey='config-name')

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
