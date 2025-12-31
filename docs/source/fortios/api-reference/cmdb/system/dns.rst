Dns
===

Configuration endpoint for system/dns.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.dns

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.dns.get()


   # Update existing item
   result = fgt.api.cmdb.system.dns.put(
       primary='updated-value',
       secondary='updated-value',
       protocol='updated-value',
       ssl_certificate='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       primary=None,
       secondary=None,
       protocol=None,
       ssl_certificate=None,
       server_hostname=None,
       domain=None,
       ip6_primary=None,
       ip6_secondary=None,
       timeout=None,
       retry=None,
       dns_cache_limit=None,
       dns_cache_ttl=None,
       # ... more parameters
   )

Update this specific resource.

