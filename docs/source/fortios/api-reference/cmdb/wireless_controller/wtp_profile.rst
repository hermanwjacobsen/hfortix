WtpProfile
==========

Configuration endpoint for wireless_controller/wtp_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.wtp_profile

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
   items = fgt.api.cmdb.wireless_controller.wtp_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.wtp_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.wtp_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.wtp_profile.put(
       name='updated-value',
       comment='updated-value',
       platform='updated-value',
       control_message_offload='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.wtp_profile.delete(name='item-name')


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
       comment=None,
       platform=None,
       control_message_offload=None,
       bonjour_profile=None,
       apcfg_profile=None,
       apcfg_mesh=None,
       apcfg_mesh_ap_type=None,
       apcfg_mesh_ssid=None,
       apcfg_mesh_eth_bridge=None,
       ble_profile=None,
       lw_profile=None,
       syslog_profile=None,
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
       comment=None,
       platform=None,
       control_message_offload=None,
       bonjour_profile=None,
       apcfg_profile=None,
       apcfg_mesh=None,
       apcfg_mesh_ap_type=None,
       apcfg_mesh_ssid=None,
       apcfg_mesh_eth_bridge=None,
       ble_profile=None,
       lw_profile=None,
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

