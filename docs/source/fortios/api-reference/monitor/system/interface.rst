DhcpRenew
=========

Configuration endpoint for system/interface.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.interface

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.interface.post(
       mkey='value',  # optional
       ipv6='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       mkey=None,
       ipv6=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Renew DHCP lease of an interface.

