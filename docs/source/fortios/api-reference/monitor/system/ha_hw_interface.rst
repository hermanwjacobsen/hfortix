HaHwInterface
=============

Configuration endpoint for system/ha_hw_interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.ha_hw_interface

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.ha_hw_interface.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get HA NPU hardware interface status.

