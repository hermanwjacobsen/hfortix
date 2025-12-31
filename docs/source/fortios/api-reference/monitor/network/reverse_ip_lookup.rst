ReverseIpLookup
===============

Configuration endpoint for network/reverse_ip_lookup.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.network.reverse_ip_lookup

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.network.reverse_ip_lookup.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ip,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve the resolved DNS domain name for a given IP address.

