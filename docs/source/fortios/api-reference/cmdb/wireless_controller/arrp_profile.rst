ArrpProfile
===========

Configuration endpoint for wireless_controller/arrp_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.arrp_profile

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
   items = fgt.api.cmdb.wireless_controller.arrp_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.wireless_controller.arrp_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.wireless_controller.arrp_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.wireless_controller.arrp_profile.put(
       name='updated-value',
       comment='updated-value',
       selection_period='updated-value',
       monitor_period='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.wireless_controller.arrp_profile.delete(name='item-name')


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
       selection_period=None,
       monitor_period=None,
       weight_managed_ap=None,
       weight_rogue_ap=None,
       weight_noise_floor=None,
       weight_channel_load=None,
       weight_spectral_rssi=None,
       weight_weather_channel=None,
       weight_dfs_channel=None,
       threshold_ap=None,
       threshold_noise_floor=None,
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
       selection_period=None,
       monitor_period=None,
       weight_managed_ap=None,
       weight_rogue_ap=None,
       weight_noise_floor=None,
       weight_channel_load=None,
       weight_spectral_rssi=None,
       weight_weather_channel=None,
       weight_dfs_channel=None,
       threshold_ap=None,
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

