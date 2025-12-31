InterfaceLog
============

Configuration endpoint for virtual_wan/interface_log.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.virtual_wan.interface_log

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.virtual_wan.interface_log.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       interface=None,
       since=None,
       seconds=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve log of SD-WAN interface quality information.

