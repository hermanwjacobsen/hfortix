UuidList
========

Configuration endpoint for firewall/uuid_list.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.uuid_list

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.uuid_list.get()



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

Retrieve a list of all UUIDs with their object type and VDOM.

