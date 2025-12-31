HaPeer
======

Configuration endpoint for router/lookup.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.router.lookup

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.router.lookup.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       serial,
       destination,
       ipv6=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Performs a route lookup by querying the routing table of an HA peer.

