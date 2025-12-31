Eject
=====

Configuration endpoint for system/usb_device.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.usb_device

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.usb_device.post(
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Eject USB drives for safe removal.

