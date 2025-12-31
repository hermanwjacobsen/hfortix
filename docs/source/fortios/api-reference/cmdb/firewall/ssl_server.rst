SslServer
=========

Configuration endpoint for firewall/ssl_server.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ssl_server

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
   items = fgt.api.cmdb.firewall.ssl_server.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.ssl_server.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.ssl_server.post(
       nkey='value',  # optional
       name='value',  # optional
       ip='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.ssl_server.put(
       name='updated-value',
       ip='updated-value',
       port='updated-value',
       ssl_mode='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.ssl_server.delete(name='item-name')


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
       ip=None,
       port=None,
       ssl_mode=None,
       add_header_x_forwarded_proto=None,
       mapped_port=None,
       ssl_cert=None,
       ssl_dh_bits=None,
       ssl_algorithm=None,
       ssl_client_renegotiation=None,
       ssl_min_version=None,
       ssl_max_version=None,
       ssl_send_empty_frags=None,
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
       ip=None,
       port=None,
       ssl_mode=None,
       add_header_x_forwarded_proto=None,
       mapped_port=None,
       ssl_cert=None,
       ssl_dh_bits=None,
       ssl_algorithm=None,
       ssl_client_renegotiation=None,
       ssl_min_version=None,
       ssl_max_version=None,
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

