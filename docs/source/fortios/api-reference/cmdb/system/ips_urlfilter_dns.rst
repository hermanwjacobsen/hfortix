IpsUrlfilterDns
===============

Configuration endpoint for system/ips_urlfilter_dns.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ips_urlfilter_dns

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.ips_urlfilter_dns.get()


   # Create new item
   result = fgt.api.cmdb.system.ips_urlfilter_dns.post(
       nkey='value',  # optional
       address='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.ips_urlfilter_dns.put(
       address='updated-value',
       status='updated-value',
       ipv6_capability='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.ips_urlfilter_dns.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       address=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       address=None,
       status=None,
       ipv6_capability=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       address=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       ipv6_capability=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       address=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

