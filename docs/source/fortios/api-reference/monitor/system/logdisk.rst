Format
======

Configuration endpoint for system/logdisk.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.logdisk

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.logdisk.post(
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

Format log disk.

