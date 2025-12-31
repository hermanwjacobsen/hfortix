Log
===

Configuration endpoint for wireless_controller/log.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.wireless_controller.log

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
   items = fgt.api.cmdb.wireless_controller.log.get()


   # Update existing item
   result = fgt.api.cmdb.wireless_controller.log.put(
       status='updated-value',
       addrgrp_log='updated-value',
       ble_log='updated-value',
       clb_log='updated-value',
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
       status=None,
       addrgrp_log=None,
       ble_log=None,
       clb_log=None,
       dhcp_starv_log=None,
       led_sched_log=None,
       radio_event_log=None,
       rogue_event_log=None,
       sta_event_log=None,
       sta_locate_log=None,
       wids_log=None,
       wtp_event_log=None,
       # ... more parameters
   )

Update this specific resource.

