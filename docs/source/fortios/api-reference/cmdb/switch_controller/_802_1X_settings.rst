Eight02OneXSettings
===================

Configuration endpoint for switch_controller/_802_1X_settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller._802_1X_settings

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
   items = fgt.api.cmdb.switch_controller._802_1X_settings.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller._802_1X_settings.put(
       link_down_auth='updated-value',
       reauth_period='updated-value',
       max_reauth_attempt='updated-value',
       tx_period='updated-value',
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
       link_down_auth=None,
       reauth_period=None,
       max_reauth_attempt=None,
       tx_period=None,
       mab_reauth=None,
       mac_username_delimiter=None,
       mac_password_delimiter=None,
       mac_calling_station_delimiter=None,
       mac_called_station_delimiter=None,
       mac_case=None,
       vdom=None,
       raw_json=False,
       # ... more parameters
   )

Update this specific resource.

