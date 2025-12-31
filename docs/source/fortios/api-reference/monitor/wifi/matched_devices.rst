MatchedDevices
==============

Configuration endpoint for wifi/matched_devices.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.matched_devices

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.wifi.matched_devices.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mac=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Return a list of devices that match NAC WiFi settings.

