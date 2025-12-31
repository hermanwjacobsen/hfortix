ManagedSwitch
=============

Configuration endpoint for switch_controller/managed_switch.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.managed_switch

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
   items = fgt.api.cmdb.switch_controller.managed_switch.get()


   # Create new item
   result = fgt.api.cmdb.switch_controller.managed_switch.post(
       nkey='value',  # optional
       switch_id='value',  # optional
       sn='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.managed_switch.put(
       switch_id='updated-value',
       sn='updated-value',
       description='updated-value',
       switch_profile='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.managed_switch.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       switch_id=None,
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
       switch_id=None,
       sn=None,
       description=None,
       switch_profile=None,
       access_profile=None,
       purdue_level=None,
       fsw_wan1_peer=None,
       fsw_wan1_admin=None,
       poe_pre_standard_detection=None,
       dhcp_server_access_list=None,
       poe_detection_type=None,
       max_poe_budget=None,
       directly_connected=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       switch_id=None,
       payload_dict=None,
       before=None,
       after=None,
       sn=None,
       description=None,
       switch_profile=None,
       access_profile=None,
       purdue_level=None,
       fsw_wan1_peer=None,
       fsw_wan1_admin=None,
       poe_pre_standard_detection=None,
       dhcp_server_access_list=None,
       poe_detection_type=None,
       max_poe_budget=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       switch_id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

