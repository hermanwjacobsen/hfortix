IpsecManualkeyInterface
=======================

Configuration endpoint for vpn/ipsec_manualkey_interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.ipsec_manualkey_interface

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.vpn.ipsec_manualkey_interface.get()

   # Get specific item by name
   item = fgt.api.cmdb.vpn.ipsec_manualkey_interface.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.vpn.ipsec_manualkey_interface.post(
       nkey='value',  # optional
       name='value',  # optional
       interface='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.vpn.ipsec_manualkey_interface.put(
       name='updated-value',
       interface='updated-value',
       ip_version='updated-value',
       addr_type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.vpn.ipsec_manualkey_interface.delete(name='item-name')


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
       interface=None,
       ip_version=None,
       addr_type=None,
       remote_gw=None,
       remote_gw6=None,
       local_gw=None,
       local_gw6=None,
       auth_alg=None,
       enc_alg=None,
       auth_key=None,
       enc_key=None,
       local_spi=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       interface=None,
       ip_version=None,
       addr_type=None,
       remote_gw=None,
       remote_gw6=None,
       local_gw=None,
       local_gw6=None,
       auth_alg=None,
       enc_alg=None,
       auth_key=None,
       enc_key=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

