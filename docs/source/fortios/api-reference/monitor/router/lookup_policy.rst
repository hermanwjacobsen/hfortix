LookupPolicy
============

Configuration endpoint for router/lookup_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.router.lookup_policy

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.router.lookup_policy.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       destination,
       ipv6=None,
       source=None,
       destination_port=None,
       source_port=None,
       interface_name=None,
       protocol_number=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Performs a route lookup by querying the policy routing table.

