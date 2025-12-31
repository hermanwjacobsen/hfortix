ExtensionDevice
===============

Configuration endpoint for firmware/extension_device.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firmware.extension_device

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firmware.extension_device.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       type,
       timeout=None,
       version=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of recommended firmwares for the specified extension

