HourlyDiskUsage
===============

Configuration endpoint for log/hourly_disk_usage.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.log.hourly_disk_usage

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.log.hourly_disk_usage.get()



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

Return historic hourly disk usage in bytes.

