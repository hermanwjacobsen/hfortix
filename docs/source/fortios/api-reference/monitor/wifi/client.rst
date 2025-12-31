Disassociate
============

Configuration endpoint for wifi/client.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.client

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.client.post(
       mac='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mac=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Disassociate a WiFi client from the FortiAP it's currently connected

