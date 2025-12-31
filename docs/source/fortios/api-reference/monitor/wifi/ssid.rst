GenerateKeys
============

Configuration endpoint for wifi/ssid.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.ssid

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.ssid.post(
       mpsk_profile='value',  # optional
       group='value',  # optional
       prefix='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mpsk_profile=None,
       group=None,
       prefix=None,
       count=None,
       key_length=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Generate pre-shared keys for specific multi pre-shared key profile.

