IpsecPhase2Interface
====================

Configuration endpoint for vpn/ipsec_phase2_interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.vpn.ipsec_phase2_interface

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
   items = fgt.api.cmdb.vpn.ipsec_phase2_interface.get()

   # Get specific item by name
   item = fgt.api.cmdb.vpn.ipsec_phase2_interface.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.vpn.ipsec_phase2_interface.post(
       nkey='value',  # optional
       name='value',  # optional
       phase1name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.vpn.ipsec_phase2_interface.put(
       name='updated-value',
       phase1name='updated-value',
       dhcp_ipsec='updated-value',
       proposal='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.vpn.ipsec_phase2_interface.delete(name='item-name')


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
       phase1name=None,
       dhcp_ipsec=None,
       proposal=None,
       pfs=None,
       dhgrp=None,
       addke1=None,
       addke2=None,
       addke3=None,
       addke4=None,
       addke5=None,
       addke6=None,
       addke7=None,
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
       phase1name=None,
       dhcp_ipsec=None,
       proposal=None,
       pfs=None,
       dhgrp=None,
       addke1=None,
       addke2=None,
       addke3=None,
       addke4=None,
       addke5=None,
       addke6=None,
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

