State
=====

Configuration endpoint for log/device.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.device

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.log.device.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve information on state of log devices.

