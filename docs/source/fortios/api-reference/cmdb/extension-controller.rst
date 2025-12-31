Extension Controller
====================

FortiExtender dataplan configuration configuration and management.

Overview
--------

The ``cmdb.extension-controller`` category provides configuration management for:

- **Dataplan** - FortiExtender dataplan configuration.
- **Extender** - Extender controller configuration.
- **Extender Profile** - FortiExtender extender profile configuration.
- **Extender Vap** - FortiExtender wifi vap configuration.
- **Fortigate** - FortiGate controller configuration.
- **Fortigate Profile** - FortiGate connector profile configuration.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.extension-controller

Available Endpoints
-------------------

**dataplan**
   FortiExtender dataplan configuration.
   
   .. code-block:: python
   
      # List all dataplan
      items = fgt.api.cmdb.extension-controller.dataplan.get()
      
      # Get specific dataplan
      item = fgt.api.cmdb.extension-controller.dataplan.get(mkey='name')

**extender**
   Extender controller configuration.
   
   .. code-block:: python
   
      # List all extender
      items = fgt.api.cmdb.extension-controller.extender.get()
      
      # Get specific extender
      item = fgt.api.cmdb.extension-controller.extender.get(mkey='name')

**extender-profile**
   FortiExtender extender profile configuration.
   
   .. code-block:: python
   
      # List all extender-profile
      items = fgt.api.cmdb.extension-controller.extender_profile.get()
      
      # Get specific extender-profile
      item = fgt.api.cmdb.extension-controller.extender_profile.get(mkey='name')

**extender-vap**
   FortiExtender wifi vap configuration.
   
   .. code-block:: python
   
      # List all extender-vap
      items = fgt.api.cmdb.extension-controller.extender_vap.get()
      
      # Get specific extender-vap
      item = fgt.api.cmdb.extension-controller.extender_vap.get(mkey='name')

**fortigate**
   FortiGate controller configuration.
   
   .. code-block:: python
   
      # List all fortigate
      items = fgt.api.cmdb.extension-controller.fortigate.get()
      
      # Get specific fortigate
      item = fgt.api.cmdb.extension-controller.fortigate.get(mkey='name')

**fortigate-profile**
   FortiGate connector profile configuration.
   
   .. code-block:: python
   
      # List all fortigate-profile
      items = fgt.api.cmdb.extension-controller.fortigate_profile.get()
      
      # Get specific fortigate-profile
      item = fgt.api.cmdb.extension-controller.fortigate_profile.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.extension-controller.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.extension-controller.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.extension-controller.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.extension-controller.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.extension-controller.{endpoint}.delete(mkey='config-name')

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
