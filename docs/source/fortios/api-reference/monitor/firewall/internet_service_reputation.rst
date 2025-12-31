InternetServiceReputation
=========================

Configuration endpoint for firewall/internet_service_reputation.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.internet_service_reputation

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.internet_service_reputation.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ip,
       is_ipv6=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List internet services with reputation information that exist at a

