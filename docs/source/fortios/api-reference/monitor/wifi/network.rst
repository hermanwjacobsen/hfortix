Connect
=======

Configuration endpoint for wifi/network.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.network

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.network.post(
       ssid='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       ssid=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

When FortiWiFi is in client mode, connect to the specified network, if

