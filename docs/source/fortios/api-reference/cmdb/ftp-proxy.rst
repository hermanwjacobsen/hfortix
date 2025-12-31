Ftp Proxy
=========

Configure explicit FTP proxy settings configuration and management.

Overview
--------

The ``cmdb.ftp-proxy`` category provides configuration management for:

- **Explicit** - Configure explicit FTP proxy settings.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.ftp-proxy

Available Endpoints
-------------------

**explicit**
   Configure explicit FTP proxy settings.
   
   .. code-block:: python
   
      # List all explicit
      items = fgt.api.cmdb.ftp-proxy.explicit.get()
      
      # Get specific explicit
      item = fgt.api.cmdb.ftp-proxy.explicit.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.ftp-proxy.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.ftp-proxy.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.ftp-proxy.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.ftp-proxy.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.ftp-proxy.{endpoint}.delete(mkey='config-name')

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
