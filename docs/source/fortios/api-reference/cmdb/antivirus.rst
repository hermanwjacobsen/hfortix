Antivirus
=========

Configure a list of hashes to be exempt from AV scanning configuration and management.

Overview
--------

The ``cmdb.antivirus`` category provides configuration management for:

- **Exempt List** - Configure a list of hashes to be exempt from AV scanning.
- **Profile** - Configure AntiVirus profiles.
- **Quarantine** - Configure quarantine options.
- **Settings** - Configure AntiVirus settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.antivirus

Available Endpoints
-------------------

**exempt-list**
   Configure a list of hashes to be exempt from AV scanning.
   
   .. code-block:: python
   
      # List all exempt-list
      items = fgt.api.cmdb.antivirus.exempt_list.get()
      
      # Get specific exempt-list
      item = fgt.api.cmdb.antivirus.exempt_list.get(mkey='name')

**profile**
   Configure AntiVirus profiles.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.antivirus.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.antivirus.profile.get(mkey='name')

**quarantine**
   Configure quarantine options.
   
   .. code-block:: python
   
      # List all quarantine
      items = fgt.api.cmdb.antivirus.quarantine.get()
      
      # Get specific quarantine
      item = fgt.api.cmdb.antivirus.quarantine.get(mkey='name')

**settings**
   Configure AntiVirus settings.
   
   .. code-block:: python
   
      # List all settings
      items = fgt.api.cmdb.antivirus.settings.get()
      
      # Get specific settings
      item = fgt.api.cmdb.antivirus.settings.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.antivirus.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.antivirus.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.antivirus.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.antivirus.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.antivirus.{endpoint}.delete(mkey='config-name')

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
