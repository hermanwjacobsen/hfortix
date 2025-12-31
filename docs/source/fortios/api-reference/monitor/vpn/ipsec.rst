ConnectionCount
===============

Configuration endpoint for vpn/ipsec.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.vpn.ipsec

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.vpn.ipsec.get()



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

Return the connection counts for every ipsec tunnel.

