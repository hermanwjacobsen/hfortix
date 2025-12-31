Server
======

Configuration endpoint for icap/server.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.icap.server

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
   items = fgt.api.cmdb.icap.server.get()

   # Get specific item by name
   item = fgt.api.cmdb.icap.server.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.icap.server.post(
       nkey='value',  # optional
       name='value',  # optional
       addr_type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.icap.server.put(
       name='updated-value',
       addr_type='updated-value',
       ip_address='updated-value',
       ip6_address='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.icap.server.delete(name='item-name')


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
       addr_type=None,
       ip_address=None,
       ip6_address=None,
       fqdn=None,
       port=None,
       max_connections=None,
       secure=None,
       ssl_cert=None,
       healthcheck=None,
       healthcheck_service=None,
       vdom=None,
       raw_json=False,
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
       addr_type=None,
       ip_address=None,
       ip6_address=None,
       fqdn=None,
       port=None,
       max_connections=None,
       secure=None,
       ssl_cert=None,
       healthcheck=None,
       healthcheck_service=None,
       vdom=None,
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

