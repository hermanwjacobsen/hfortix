ExtenderVap
===========

Configuration endpoint for extension_controller/extender_vap.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.extension_controller.extender_vap

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
   items = fgt.api.cmdb.extension_controller.extender_vap.get()

   # Get specific item by name
   item = fgt.api.cmdb.extension_controller.extender_vap.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.extension_controller.extender_vap.post(
       nkey='value',  # optional
       name='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.extension_controller.extender_vap.put(
       name='updated-value',
       type='updated-value',
       ssid='updated-value',
       max_clients='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.extension_controller.extender_vap.delete(name='item-name')


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
       ssid=None,
       max_clients=None,
       broadcast_ssid=None,
       security=None,
       dtim=None,
       rts_threshold=None,
       pmf=None,
       target_wake_time=None,
       bss_color_partial=None,
       mu_mimo=None,
       passphrase=None,
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
       ssid=None,
       max_clients=None,
       broadcast_ssid=None,
       security=None,
       dtim=None,
       rts_threshold=None,
       pmf=None,
       target_wake_time=None,
       bss_color_partial=None,
       mu_mimo=None,
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

