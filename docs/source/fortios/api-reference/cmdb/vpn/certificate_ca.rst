CertificateCa
=============

Configuration endpoint for vpn/certificate_ca.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.certificate_ca

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
   items = fgt.api.cmdb.vpn.certificate_ca.get()

   # Get specific item by name
   item = fgt.api.cmdb.vpn.certificate_ca.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.vpn.certificate_ca.post(
       nkey='value',  # optional
       name='value',  # optional
       ca='value',  # optional
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
       ca=None,
       range=None,
       source=None,
       ssl_inspection_trusted=None,
       scep_url=None,
       est_url=None,
       auto_update_days=None,
       auto_update_days_warning=None,
       source_ip=None,
       ca_identifier=None,
       obsolete=None,
       fabric_ca=None,
       # ... more parameters
   )

Create object(s) in this table.

