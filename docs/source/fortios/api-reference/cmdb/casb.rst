Casb
====

Configure CASB attribute match rule configuration and management.

Overview
--------

The ``cmdb.casb`` category provides configuration management for:

- **Attribute Match** - Configure CASB attribute match rule.
- **Profile** - Configure CASB profile.
- **Saas Application** - Configure CASB SaaS application.
- **User Activity** - Configure CASB user activity.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.casb

Available Endpoints
-------------------

**attribute-match**
   Configure CASB attribute match rule.
   
   .. code-block:: python
   
      # List all attribute-match
      items = fgt.api.cmdb.casb.attribute_match.get()
      
      # Get specific attribute-match
      item = fgt.api.cmdb.casb.attribute_match.get(mkey='name')

**profile**
   Configure CASB profile.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.casb.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.casb.profile.get(mkey='name')

**saas-application**
   Configure CASB SaaS application.
   
   .. code-block:: python
   
      # List all saas-application
      items = fgt.api.cmdb.casb.saas_application.get()
      
      # Get specific saas-application
      item = fgt.api.cmdb.casb.saas_application.get(mkey='name')

**user-activity**
   Configure CASB user activity.
   
   .. code-block:: python
   
      # List all user-activity
      items = fgt.api.cmdb.casb.user_activity.get()
      
      # Get specific user-activity
      item = fgt.api.cmdb.casb.user_activity.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.casb.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.casb.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.casb.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.casb.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.casb.{endpoint}.delete(mkey='config-name')

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
