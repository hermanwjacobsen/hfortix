Ddns
====

Configuration endpoint for system/ddns.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ddns

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
   items = fgt.api.cmdb.system.ddns.get()


   # Create new item
   result = fgt.api.cmdb.system.ddns.post(
       nkey='value',  # optional
       ddnsid='value',  # optional
       ddns_server='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.ddns.put(
       ddnsid='updated-value',
       ddns_server='updated-value',
       addr_type='updated-value',
       server_type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.ddns.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ddnsid=None,
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
       ddnsid=None,
       ddns_server=None,
       addr_type=None,
       server_type=None,
       ddns_server_addr=None,
       ddns_zone=None,
       ddns_ttl=None,
       ddns_auth=None,
       ddns_keyname=None,
       ddns_key=None,
       ddns_domain=None,
       ddns_username=None,
       ddns_sn=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       ddnsid=None,
       payload_dict=None,
       before=None,
       after=None,
       ddns_server=None,
       addr_type=None,
       server_type=None,
       ddns_server_addr=None,
       ddns_zone=None,
       ddns_ttl=None,
       ddns_auth=None,
       ddns_keyname=None,
       ddns_key=None,
       ddns_domain=None,
       ddns_username=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       ddnsid=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

