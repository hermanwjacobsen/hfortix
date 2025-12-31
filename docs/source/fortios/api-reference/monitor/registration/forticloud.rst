DeviceStatus
============

Configuration endpoint for registration/forticloud.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.registration.forticloud

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.registration.forticloud.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       serials,
       update_cache=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Fetch device registration status from FortiCloud.

