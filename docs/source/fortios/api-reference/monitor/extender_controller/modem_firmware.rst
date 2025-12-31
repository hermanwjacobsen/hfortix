ModemFirmware
=============

Configuration endpoint for extender_controller/modem_firmware.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.extender_controller.modem_firmware

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.extender_controller.modem_firmware.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       serial,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get available modem firmware for a FortiExtender.

