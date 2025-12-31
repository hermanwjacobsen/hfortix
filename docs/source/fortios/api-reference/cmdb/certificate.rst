Certificate
===========

CA certificate configuration and management.

Overview
--------

The ``cmdb.certificate`` category provides configuration management for:

- :ref:`Ca <certificate-ca>` - CA certificate.
- :ref:`Crl <certificate-crl>` - Certificate Revocation List as a PEM file.
- :ref:`Hsm Local <certificate-hsm-local>` - Local certificates whose keys are stored on HSM.
- :ref:`Local <certificate-local>` - Local keys and certificates.
- :ref:`Remote <certificate-remote>` - Remote certificate as a PEM file.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.certificate

Available Endpoints
-------------------

.. _certificate-ca:

ca
~~

CA certificate.

**Python attribute:** ``ca``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.certificate.ca.get()
   
   # Get specific item
   item = fgt.api.cmdb.certificate.ca.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.certificate.ca.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.certificate.ca.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.certificate.ca.delete(mkey='item-name')

.. _certificate-crl:

crl
~~~

Certificate Revocation List as a PEM file.

**Python attribute:** ``crl``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.certificate.crl.get()
   
   # Get specific item
   item = fgt.api.cmdb.certificate.crl.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.certificate.crl.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.certificate.crl.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.certificate.crl.delete(mkey='item-name')

.. _certificate-hsm-local:

hsm-local
~~~~~~~~~

Local certificates whose keys are stored on HSM.

**Python attribute:** ``hsm_local``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.certificate.hsm_local.get()
   
   # Get specific item
   item = fgt.api.cmdb.certificate.hsm_local.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.certificate.hsm_local.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.certificate.hsm_local.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.certificate.hsm_local.delete(mkey='item-name')

.. _certificate-local:

local
~~~~~

Local keys and certificates.

**Python attribute:** ``local``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.certificate.local.get()
   
   # Get specific item
   item = fgt.api.cmdb.certificate.local.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.certificate.local.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.certificate.local.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.certificate.local.delete(mkey='item-name')

.. _certificate-remote:

remote
~~~~~~

Remote certificate as a PEM file.

**Python attribute:** ``remote``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.certificate.remote.get()
   
   # Get specific item
   item = fgt.api.cmdb.certificate.remote.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.certificate.remote.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.certificate.remote.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.certificate.remote.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.certificate.ca.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.certificate.ca.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.certificate.ca.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.certificate.ca.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.certificate.ca.delete(mkey='config-name')

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
