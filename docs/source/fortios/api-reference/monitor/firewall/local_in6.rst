LocalIn6
========

Configuration endpoint for firewall/local_in6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.local_in6

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.local_in6.get()



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

List implicit and explicit IPv6 local-in firewall policies.

