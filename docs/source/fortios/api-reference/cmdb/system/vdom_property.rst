VdomProperty
============

Configuration endpoint for system/vdom_property.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.vdom_property

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
   items = fgt.api.cmdb.system.vdom_property.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.vdom_property.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.vdom_property.post(
       nkey='value',  # optional
       name='value',  # optional
       description='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.vdom_property.put(
       name='updated-value',
       description='updated-value',
       snmp_index='updated-value',
       session='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.vdom_property.delete(name='item-name')


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
       description=None,
       snmp_index=None,
       session=None,
       ipsec_phase1=None,
       ipsec_phase2=None,
       ipsec_phase1_interface=None,
       ipsec_phase2_interface=None,
       dialup_tunnel=None,
       firewall_policy=None,
       firewall_address=None,
       firewall_addrgrp=None,
       custom_service=None,
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
       description=None,
       snmp_index=None,
       session=None,
       ipsec_phase1=None,
       ipsec_phase2=None,
       ipsec_phase1_interface=None,
       ipsec_phase2_interface=None,
       dialup_tunnel=None,
       firewall_policy=None,
       firewall_address=None,
       firewall_addrgrp=None,
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

