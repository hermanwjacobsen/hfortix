CertificateLocal
================

Configuration endpoint for vpn/certificate_local.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.certificate_local

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.vpn.certificate_local.get()

   # Get specific item by name
   item = fgt.api.cmdb.vpn.certificate_local.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.vpn.certificate_local.post(
       nkey='value',  # optional
       name='value',  # optional
       password='value',  # optional
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       name=None,
       password=None,
       comments=None,
       private_key=None,
       certificate=None,
       csr=None,
       state=None,
       scep_url=None,
       range=None,
       source=None,
       auto_regenerate_days=None,
       auto_regenerate_days_warning=None,
       scep_password=None,
       # ... more parameters
   )

Create object(s) in this table.

