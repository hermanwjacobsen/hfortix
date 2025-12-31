PolicyLookup
============

Configuration endpoint for firewall/policy_lookup.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.policy_lookup

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.policy_lookup.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       srcintf,
       sourceip,
       protocol,
       dest,
       ipv6=None,
       sourceport=None,
       destport=None,
       icmptype=None,
       icmpcode=None,
       policy_type=None,
       auth_type=None,
       user_group=None,
       server_name=None,
       user_db=None,
       group_attr_type=None,
       # ... more parameters
   )

Performs a policy lookup by creating a dummy packet and asking the

