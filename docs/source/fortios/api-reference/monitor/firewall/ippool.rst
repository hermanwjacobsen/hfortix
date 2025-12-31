Mapping
=======

Configuration endpoint for firewall/ippool.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.ippool

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.ippool.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get the list of IPv4 mappings for the specified IP pool.

