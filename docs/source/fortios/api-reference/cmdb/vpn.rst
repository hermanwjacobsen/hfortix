Vpn
===

CA certificate configuration and management.

Overview
--------

The ``cmdb.vpn`` category provides configuration management for:

- **Kmip Server** - KMIP server entry configuration.
- **L2Tp** - Configure L2TP.
- **Pptp** - Configure PPTP.
- **Qkd** - Configure Quantum Key Distribution servers


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.vpn

Available Endpoints
-------------------

**kmip-server**
   KMIP server entry configuration.
   
   .. code-block:: python
   
      # List all kmip-server
      items = fgt.api.cmdb.vpn.kmip_server.get()
      
      # Get specific kmip-server
      item = fgt.api.cmdb.vpn.kmip_server.get(mkey='name')

**l2tp**
   Configure L2TP.
   
   .. code-block:: python
   
      # List all l2tp
      items = fgt.api.cmdb.vpn.l2tp.get()
      
      # Get specific l2tp
      item = fgt.api.cmdb.vpn.l2tp.get(mkey='name')

**pptp**
   Configure PPTP.
   
   .. code-block:: python
   
      # List all pptp
      items = fgt.api.cmdb.vpn.pptp.get()
      
      # Get specific pptp
      item = fgt.api.cmdb.vpn.pptp.get(mkey='name')

**qkd**
   Configure Quantum Key Distribution servers
   
   .. code-block:: python
   
      # List all qkd
      items = fgt.api.cmdb.vpn.qkd.get()
      
      # Get specific qkd
      item = fgt.api.cmdb.vpn.qkd.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.vpn.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.vpn.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.vpn.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.vpn.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.vpn.{endpoint}.delete(mkey='config-name')

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
