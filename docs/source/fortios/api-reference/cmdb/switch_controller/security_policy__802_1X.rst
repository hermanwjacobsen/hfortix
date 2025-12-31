SecurityPolicyEight02OneX
=========================

Configuration endpoint for switch_controller/security_policy__802_1X.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.security_policy__802_1X

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
   items = fgt.api.cmdb.switch_controller.security_policy__802_1X.get()

   # Get specific item by name
   item = fgt.api.cmdb.switch_controller.security_policy__802_1X.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.switch_controller.security_policy__802_1X.post(
       nkey='value',  # optional
       name='value',  # optional
       security_mode='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.security_policy__802_1X.put(
       name='updated-value',
       security_mode='updated-value',
       user_group='updated-value',
       mac_auth_bypass='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.security_policy__802_1X.delete(name='item-name')


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
       security_mode=None,
       user_group=None,
       mac_auth_bypass=None,
       auth_order=None,
       auth_priority=None,
       open_auth=None,
       eap_passthru=None,
       eap_auto_untagged_vlans=None,
       guest_vlan=None,
       guest_vlan_id=None,
       guest_auth_delay=None,
       auth_fail_vlan=None,
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
       security_mode=None,
       user_group=None,
       mac_auth_bypass=None,
       auth_order=None,
       auth_priority=None,
       open_auth=None,
       eap_passthru=None,
       eap_auto_untagged_vlans=None,
       guest_vlan=None,
       guest_vlan_id=None,
       guest_auth_delay=None,
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

