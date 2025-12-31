Download
========

Configuration endpoint for system/config_error_log.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.config_error_log

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.config_error_log.get()



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

Download the error log of the configuration management database.

