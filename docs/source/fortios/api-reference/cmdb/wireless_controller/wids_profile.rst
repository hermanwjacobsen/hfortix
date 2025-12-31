WidsProfile
===========

Configuration endpoint for wireless_controller/wids_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.wids_profile

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
   items = fgt.api.cmdb.wireless_controller.wids_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.wids_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.wids_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.wids_profile.put(
       name='updated-value',
       comment='updated-value',
       sensor_mode='updated-value',
       ap_scan='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.wids_profile.delete(name='item-name')


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
       sensor_mode=None,
       ap_scan=None,
       ap_scan_channel_list_2G_5G=None,
       ap_scan_channel_list_6G=None,
       ap_bgscan_period=None,
       ap_bgscan_intv=None,
       ap_bgscan_duration=None,
       ap_bgscan_idle=None,
       ap_bgscan_report_intv=None,
       ap_bgscan_disable_schedules=None,
       ap_fgscan_report_intv=None,
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
       sensor_mode=None,
       ap_scan=None,
       ap_scan_channel_list_2G_5G=None,
       ap_scan_channel_list_6G=None,
       ap_bgscan_period=None,
       ap_bgscan_intv=None,
       ap_bgscan_duration=None,
       ap_bgscan_idle=None,
       ap_bgscan_report_intv=None,
       ap_bgscan_disable_schedules=None,
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

