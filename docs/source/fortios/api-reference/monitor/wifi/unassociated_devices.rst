UnassociatedDevices
===================

Configuration endpoint for wifi/unassociated_devices.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.unassociated_devices

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.wifi.unassociated_devices.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       with_triangulation=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of unassociated and BLE devices

