Stats
=====

Configuration endpoint for wifi/nac_device.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.nac_device

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.wifi.nac_device.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Return the current WiFi NAC device counts.

