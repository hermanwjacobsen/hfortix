Download
========

Configuration endpoint for switch_controller/fsw_firmware.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.switch_controller.fsw_firmware

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.switch_controller.fsw_firmware.post(
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

Download FortiSwitch firmware from FortiGuard to the FortiGate

