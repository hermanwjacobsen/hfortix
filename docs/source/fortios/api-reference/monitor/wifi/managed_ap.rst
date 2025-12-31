LedBlink
========

Configuration endpoint for wifi/managed_ap.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.managed_ap

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.managed_ap.post(
       serials='value',  # optional
       blink='value',  # optional
       duration='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       serials=None,
       blink=None,
       duration=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Turn a managed FortiAP's LED blinking on or off.

