FabricVpn
=========

Configuration endpoint for system/fabric_vpn.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.fabric_vpn

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.fabric_vpn.get()


   # Update existing item
   result = fgt.api.cmdb.system.fabric_vpn.put(
       status='updated-value',
       sync_mode='updated-value',
       branch_name='updated-value',
       policy_rule='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       sync_mode=None,
       branch_name=None,
       policy_rule=None,
       vpn_role=None,
       overlays=None,
       advertised_subnets=None,
       loopback_address_block=None,
       loopback_interface=None,
       loopback_advertised_subnet=None,
       psksecret=None,
       bgp_as=None,
       # ... more parameters
   )

Update this specific resource.

