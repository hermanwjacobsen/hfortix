Start
=====

Configuration endpoint for network/debug_flow.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.network.debug_flow

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.network.debug_flow.post(
       num_packets='value',  # optional
       ipv6='value',  # optional
       negate='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       num_packets=None,
       ipv6=None,
       negate=None,
       addr_from=None,
       addr_to=None,
       daddr_from=None,
       daddr_to=None,
       saddr_from=None,
       saddr_to=None,
       port_from=None,
       port_to=None,
       dport_from=None,
       dport_to=None,
       sport_from=None,
       sport_to=None,
       # ... more parameters
   )

Start debug flow packet capture.

