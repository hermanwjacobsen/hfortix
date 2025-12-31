Setting
=======

Configuration endpoint for wireless_controller/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.setting

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
   items = fgt.api.cmdb.wireless_controller.setting.get()


   # Update existing item
   result = fgt.api.cmdb.wireless_controller.setting.put(
       account_id='updated-value',
       country='updated-value',
       duplicate_ssid='updated-value',
       fapc_compatibility='updated-value',
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
       account_id=None,
       country=None,
       duplicate_ssid=None,
       fapc_compatibility=None,
       wfa_compatibility=None,
       phishing_ssid_detect=None,
       fake_ssid_action=None,
       offending_ssid=None,
       device_weight=None,
       device_holdoff=None,
       device_idle=None,
       firmware_provision_on_authorization=None,
       # ... more parameters
   )

Update this specific resource.

