UuidTypeLookup
==============

Configuration endpoint for firewall/uuid_type_lookup.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.uuid_type_lookup

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.uuid_type_lookup.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       uuids,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a mapping of UUIDs to their firewall object type for given

