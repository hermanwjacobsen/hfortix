Ipconf
======

Configuration endpoint for system/ipconf.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.ipconf

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.ipconf.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       devs,
       ipaddr,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Determine if there is an IP conflict for a specific IP using ARP.

