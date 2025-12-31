IotQuery
========

Configuration endpoint for user/device.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.device

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.user.device.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mac,
       ip,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve IoT/OT information for a given device from user device store.

