SdnVpn
======

Configuration endpoint for system/sdn_vpn.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.sdn_vpn

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
   items = fgt.api.cmdb.system.sdn_vpn.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.sdn_vpn.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.sdn_vpn.post(
       nkey='value',  # optional
       name='value',  # optional
       sdn='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.sdn_vpn.put(
       name='updated-value',
       sdn='updated-value',
       remote_type='updated-value',
       routing_type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.sdn_vpn.delete(name='item-name')


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
       sdn=None,
       remote_type=None,
       routing_type=None,
       vgw_id=None,
       tgw_id=None,
       subnet_id=None,
       bgp_as=None,
       cgw_gateway=None,
       nat_traversal=None,
       tunnel_interface=None,
       internal_interface=None,
       local_cidr=None,
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
       sdn=None,
       remote_type=None,
       routing_type=None,
       vgw_id=None,
       tgw_id=None,
       subnet_id=None,
       bgp_as=None,
       cgw_gateway=None,
       nat_traversal=None,
       tunnel_interface=None,
       internal_interface=None,
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

