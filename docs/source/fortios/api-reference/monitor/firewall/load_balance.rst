LoadBalance
===========

Configuration endpoint for firewall/load_balance.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.load_balance

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.load_balance.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       count,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List all firewall load balance servers.

