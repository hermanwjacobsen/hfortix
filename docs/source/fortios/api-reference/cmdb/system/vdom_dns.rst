VdomDns
=======

Configuration endpoint for system/vdom_dns.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.vdom_dns

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
   items = fgt.api.cmdb.system.vdom_dns.get()


   # Update existing item
   result = fgt.api.cmdb.system.vdom_dns.put(
       vdom_dns='updated-value',
       primary='updated-value',
       secondary='updated-value',
       protocol='updated-value',
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
       vdom_dns=None,
       primary=None,
       secondary=None,
       protocol=None,
       ssl_certificate=None,
       server_hostname=None,
       ip6_primary=None,
       ip6_secondary=None,
       source_ip=None,
       source_ip_interface=None,
       interface_select_method=None,
       interface=None,
       # ... more parameters
   )

Update this specific resource.

