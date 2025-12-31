Ipv4
====

Configuration endpoint for router/ipv4.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.router.ipv4

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.router.ipv4.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       operator=None,
       ip_mask=None,
       gateway=None,
       type=None,
       origin=None,
       interface=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List all active IPv4 routing table entries.

