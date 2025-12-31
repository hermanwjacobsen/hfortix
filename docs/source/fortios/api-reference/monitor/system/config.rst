Backup
======

Configuration endpoint for system/config.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.config

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.config.post(
       destination='value',  # optional
       usb_filename='value',  # optional
       password='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       destination=None,
       usb_filename=None,
       password=None,
       scope=None,
       vdom=None,
       password_mask=None,
       file_format=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Backup system config

