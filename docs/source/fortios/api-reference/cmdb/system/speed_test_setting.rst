SpeedTestSetting
================

Configuration endpoint for system/speed_test_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.speed_test_setting

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
   items = fgt.api.cmdb.system.speed_test_setting.get()


   # Update existing item
   result = fgt.api.cmdb.system.speed_test_setting.put(
       latency_threshold='updated-value',
       multiple_tcp_stream='updated-value',
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
       latency_threshold=None,
       multiple_tcp_stream=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

