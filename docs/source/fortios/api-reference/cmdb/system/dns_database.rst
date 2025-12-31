DnsDatabase
===========

Configuration endpoint for system/dns_database.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.dns_database

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
   items = fgt.api.cmdb.system.dns_database.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.dns_database.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.dns_database.post(
       nkey='value',  # optional
       name='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.dns_database.put(
       name='updated-value',
       status='updated-value',
       domain='updated-value',
       allow_transfer='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.dns_database.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
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
       name=None,
       status=None,
       domain=None,
       allow_transfer=None,
       type=None,
       view=None,
       ip_primary=None,
       primary_name=None,
       contact=None,
       ttl=None,
       authoritative=None,
       forwarder=None,
       forwarder6=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       domain=None,
       allow_transfer=None,
       type=None,
       view=None,
       ip_primary=None,
       primary_name=None,
       contact=None,
       ttl=None,
       authoritative=None,
       forwarder=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

