Emailfilter
===========

Configure anti-spam block/allow list configuration and management.

Overview
--------

The ``cmdb.emailfilter`` category provides configuration management for:

- **Block Allow List** - Configure anti-spam block/allow list.
- **Bword** - Configure AntiSpam banned word list.
- **Dnsbl** - Configure AntiSpam DNSBL/ORBL.
- **Fortishield** - Configure FortiGuard - AntiSpam.
- **Iptrust** - Configure AntiSpam IP trust.
- **Mheader** - Configure AntiSpam MIME header.
- **Options** - Configure AntiSpam options.
- **Profile** - Configure Email Filter profiles.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.emailfilter

Available Endpoints
-------------------

**block-allow-list**
   Configure anti-spam block/allow list.
   
   .. code-block:: python
   
      # List all block-allow-list
      items = fgt.api.cmdb.emailfilter.block_allow_list.get()
      
      # Get specific block-allow-list
      item = fgt.api.cmdb.emailfilter.block_allow_list.get(mkey='name')

**bword**
   Configure AntiSpam banned word list.
   
   .. code-block:: python
   
      # List all bword
      items = fgt.api.cmdb.emailfilter.bword.get()
      
      # Get specific bword
      item = fgt.api.cmdb.emailfilter.bword.get(mkey='name')

**dnsbl**
   Configure AntiSpam DNSBL/ORBL.
   
   .. code-block:: python
   
      # List all dnsbl
      items = fgt.api.cmdb.emailfilter.dnsbl.get()
      
      # Get specific dnsbl
      item = fgt.api.cmdb.emailfilter.dnsbl.get(mkey='name')

**fortishield**
   Configure FortiGuard - AntiSpam.
   
   .. code-block:: python
   
      # List all fortishield
      items = fgt.api.cmdb.emailfilter.fortishield.get()
      
      # Get specific fortishield
      item = fgt.api.cmdb.emailfilter.fortishield.get(mkey='name')

**iptrust**
   Configure AntiSpam IP trust.
   
   .. code-block:: python
   
      # List all iptrust
      items = fgt.api.cmdb.emailfilter.iptrust.get()
      
      # Get specific iptrust
      item = fgt.api.cmdb.emailfilter.iptrust.get(mkey='name')

**mheader**
   Configure AntiSpam MIME header.
   
   .. code-block:: python
   
      # List all mheader
      items = fgt.api.cmdb.emailfilter.mheader.get()
      
      # Get specific mheader
      item = fgt.api.cmdb.emailfilter.mheader.get(mkey='name')

**options**
   Configure AntiSpam options.
   
   .. code-block:: python
   
      # List all options
      items = fgt.api.cmdb.emailfilter.options.get()
      
      # Get specific options
      item = fgt.api.cmdb.emailfilter.options.get(mkey='name')

**profile**
   Configure Email Filter profiles.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.emailfilter.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.emailfilter.profile.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.emailfilter.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.emailfilter.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.emailfilter.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.emailfilter.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.emailfilter.{endpoint}.delete(mkey='config-name')

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
