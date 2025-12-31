LdbMonitor
==========

Configuration endpoint for firewall/ldb_monitor.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ldb_monitor

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
   items = fgt.api.cmdb.firewall.ldb_monitor.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.ldb_monitor.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.ldb_monitor.post(
       nkey='value',  # optional
       name='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.ldb_monitor.put(
       name='updated-value',
       type='updated-value',
       interval='updated-value',
       timeout='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.ldb_monitor.delete(name='item-name')


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
       type=None,
       interval=None,
       timeout=None,
       retry=None,
       port=None,
       src_ip=None,
       http_get=None,
       http_match=None,
       http_max_redirects=None,
       dns_protocol=None,
       dns_request_domain=None,
       dns_match_ip=None,
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
       type=None,
       interval=None,
       timeout=None,
       retry=None,
       port=None,
       src_ip=None,
       http_get=None,
       http_match=None,
       http_max_redirects=None,
       dns_protocol=None,
       dns_request_domain=None,
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

