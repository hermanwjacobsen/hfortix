CertificateRemote
=================

Configuration endpoint for vpn/certificate_remote.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.certificate_remote

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
   items = fgt.api.cmdb.vpn.certificate_remote.get()

   # Get specific item by name
   item = fgt.api.cmdb.vpn.certificate_remote.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.vpn.certificate_remote.post(
       nkey='value',  # optional
       name='value',  # optional
       remote='value',  # optional
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
       remote=None,
       range=None,
       source=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.

