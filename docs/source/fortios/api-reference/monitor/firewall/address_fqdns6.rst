AddressFqdns6
=============

Configuration endpoint for firewall/address_fqdns6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.address_fqdns6

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.address_fqdns6.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List of IPv6 FQDN address objects and the IPs they resolved to.

