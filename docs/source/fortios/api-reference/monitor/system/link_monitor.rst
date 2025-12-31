LinkMonitor
===========

Configuration endpoint for system/link_monitor.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.link_monitor

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.link_monitor.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve per-interface statistics for active link monitors.

