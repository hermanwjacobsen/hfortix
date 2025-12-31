KeepAlive
=========

Configuration endpoint for wifi/spectrum.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.spectrum

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.spectrum.post(
       wtp_id='value',  # optional
       radio_id='value',  # optional
       duration='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       wtp_id=None,
       radio_id=None,
       duration=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Extend duration of an existing spectrum analysis for a specific

