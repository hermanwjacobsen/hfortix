ClearCounters
=============

Configuration endpoint for firewall/dnat.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.dnat

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.dnat.post(
       id='value',  # optional
       is_ipv6='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       id=None,
       is_ipv6=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Reset hit count statistics for one or more firewall virtual IP/server

