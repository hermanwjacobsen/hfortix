IpsecPhase1Interface
====================

Configuration endpoint for vpn/ipsec_phase1_interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.ipsec_phase1_interface

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
   items = fgt.api.cmdb.vpn.ipsec_phase1_interface.get()

   # Get specific item by name
   item = fgt.api.cmdb.vpn.ipsec_phase1_interface.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.vpn.ipsec_phase1_interface.post(
       nkey='value',  # optional
       name='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.vpn.ipsec_phase1_interface.put(
       name='updated-value',
       type='updated-value',
       interface='updated-value',
       ip_version='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.vpn.ipsec_phase1_interface.delete(name='item-name')


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
       type=None,
       interface=None,
       ip_version=None,
       ike_version=None,
       local_gw=None,
       local_gw6=None,
       remote_gw=None,
       remote_gw6=None,
       remotegw_ddns=None,
       keylife=None,
       certificate=None,
       authmethod=None,
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
       type=None,
       interface=None,
       ip_version=None,
       ike_version=None,
       local_gw=None,
       local_gw6=None,
       remote_gw=None,
       remote_gw6=None,
       remotegw_ddns=None,
       keylife=None,
       certificate=None,
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

