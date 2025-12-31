System
======

Configuration endpoint for switch_controller/system.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.system

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
   items = fgt.api.cmdb.switch_controller.system.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.system.put(
       parallel_process_override='updated-value',
       parallel_process='updated-value',
       data_sync_interval='updated-value',
       iot_weight_threshold='updated-value',
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
       parallel_process_override=None,
       parallel_process=None,
       data_sync_interval=None,
       iot_weight_threshold=None,
       iot_scan_interval=None,
       iot_holdoff=None,
       iot_mac_idle=None,
       nac_periodic_interval=None,
       dynamic_periodic_interval=None,
       tunnel_mode=None,
       caputp_echo_interval=None,
       caputp_max_retransmit=None,
       # ... more parameters
   )

Update this specific resource.

