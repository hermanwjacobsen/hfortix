MatchedDevices
==============

Configuration endpoint for switch_controller/matched_devices.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.matched_devices

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.switch_controller.matched_devices.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       include_dynamic=None,
       mac=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Return a list of devices that match NAC and/or dynamic port policies.

