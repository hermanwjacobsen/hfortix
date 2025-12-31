Upgrade
=======

Configuration endpoint for system/firmware.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.firmware

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.firmware.post(
       source='value',  # optional
       url='value',  # optional
       passphrase='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       source=None,
       url=None,
       passphrase=None,
       force=None,
       filename=None,
       format_partition=None,
       ignore_invalid_signature=None,
       file_id=None,
       ignore_admin_lockout_upon_downgrade=None,
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Upgrade firmware image on this device.

