Exchange
========

Configuration endpoint for user/exchange.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.exchange

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
   items = fgt.api.cmdb.user.exchange.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.exchange.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.exchange.post(
       nkey='value',  # optional
       name='value',  # optional
       server_name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.exchange.put(
       name='updated-value',
       server_name='updated-value',
       domain_name='updated-value',
       username='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.exchange.delete(name='item-name')


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
       server_name=None,
       domain_name=None,
       username=None,
       password=None,
       ip=None,
       connect_protocol=None,
       validate_server_certificate=None,
       auth_type=None,
       auth_level=None,
       http_auth_type=None,
       ssl_min_proto_version=None,
       auto_discover_kdc=None,
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
       server_name=None,
       domain_name=None,
       username=None,
       password=None,
       ip=None,
       connect_protocol=None,
       validate_server_certificate=None,
       auth_type=None,
       auth_level=None,
       http_auth_type=None,
       ssl_min_proto_version=None,
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

