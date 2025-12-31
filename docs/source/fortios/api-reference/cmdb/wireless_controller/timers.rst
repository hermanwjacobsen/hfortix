Timers
======

Configuration endpoint for wireless_controller/timers.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.timers

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
   items = fgt.api.cmdb.wireless_controller.timers.get()


   # Update existing item
   result = fgt.api.cmdb.wireless_controller.timers.put(
       echo_interval='updated-value',
       nat_session_keep_alive='updated-value',
       discovery_interval='updated-value',
       client_idle_timeout='updated-value',
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
       echo_interval=None,
       nat_session_keep_alive=None,
       discovery_interval=None,
       client_idle_timeout=None,
       client_idle_rehome_timeout=None,
       auth_timeout=None,
       rogue_ap_log=None,
       fake_ap_log=None,
       sta_offline_cleanup=None,
       sta_offline_ip2mac_cleanup=None,
       sta_cap_cleanup=None,
       rogue_ap_cleanup=None,
       # ... more parameters
   )

Update this specific resource.

