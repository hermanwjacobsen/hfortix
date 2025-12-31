Reboot
======

Configuration endpoint for system/os.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.os

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.os.post(
       event_log_message='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       event_log_message=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Immediately reboot this device.

