Certificate
===========

CA certificate configuration and management.

Overview
--------

The ``cmdb.certificate`` category provides configuration management for:

- **Ca** - CA certificate.
- **Crl** - Certificate Revocation List as a PEM file.
- **Hsm Local** - Local certificates whose keys are stored on HSM.
- **Local** - Local keys and certificates.
- **Remote** - Remote certificate as a PEM file.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.certificate

Available Endpoints
-------------------

**ca**
   CA certificate.
   
   .. code-block:: python
   
      # List all ca
      items = fgt.api.cmdb.certificate.ca.get()
      
      # Get specific ca
      item = fgt.api.cmdb.certificate.ca.get(mkey='name')

**crl**
   Certificate Revocation List as a PEM file.
   
   .. code-block:: python
   
      # List all crl
      items = fgt.api.cmdb.certificate.crl.get()
      
      # Get specific crl
      item = fgt.api.cmdb.certificate.crl.get(mkey='name')

**hsm-local**
   Local certificates whose keys are stored on HSM.
   
   .. code-block:: python
   
      # List all hsm-local
      items = fgt.api.cmdb.certificate.hsm_local.get()
      
      # Get specific hsm-local
      item = fgt.api.cmdb.certificate.hsm_local.get(mkey='name')

**local**
   Local keys and certificates.
   
   .. code-block:: python
   
      # List all local
      items = fgt.api.cmdb.certificate.local.get()
      
      # Get specific local
      item = fgt.api.cmdb.certificate.local.get(mkey='name')

**remote**
   Remote certificate as a PEM file.
   
   .. code-block:: python
   
      # List all remote
      items = fgt.api.cmdb.certificate.remote.get()
      
      # Get specific remote
      item = fgt.api.cmdb.certificate.remote.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.certificate.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.certificate.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.certificate.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.certificate.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.certificate.{endpoint}.delete(mkey='config-name')

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
