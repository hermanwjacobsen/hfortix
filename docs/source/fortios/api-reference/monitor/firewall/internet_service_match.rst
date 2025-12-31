InternetServiceMatch
====================

Configuration endpoint for firewall/internet_service_match.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.internet_service_match

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.internet_service_match.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ip,
       is_ipv6=None,
       ipv4_mask=None,
       ipv6_prefix=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List internet services that exist at a given IP or Subnet.

