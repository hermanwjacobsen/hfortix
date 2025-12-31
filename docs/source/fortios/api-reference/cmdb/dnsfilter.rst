Dnsfilter
=========

Configure DNS domain filters configuration and management.

Overview
--------

The ``cmdb.dnsfilter`` category provides configuration management for:

- **Domain Filter** - Configure DNS domain filters.
- **Profile** - Configure DNS domain filter profile.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.dnsfilter

Available Endpoints
-------------------

**domain-filter**
   Configure DNS domain filters.
   
   .. code-block:: python
   
      # List all domain-filter
      items = fgt.api.cmdb.dnsfilter.domain_filter.get()
      
      # Get specific domain-filter
      item = fgt.api.cmdb.dnsfilter.domain_filter.get(mkey='name')

**profile**
   Configure DNS domain filter profile.
   
   .. code-block:: python
   
      # List all profile
      items = fgt.api.cmdb.dnsfilter.profile.get()
      
      # Get specific profile
      item = fgt.api.cmdb.dnsfilter.profile.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.dnsfilter.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.dnsfilter.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.dnsfilter.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.dnsfilter.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.dnsfilter.{endpoint}.delete(mkey='config-name')

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
