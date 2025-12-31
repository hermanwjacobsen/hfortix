Download
========

Configuration endpoint for wifi/firmware.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.firmware

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.firmware.post(
       image_id='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       image_id=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download FortiAP firmware from FortiGuard to the FortiGate according to

