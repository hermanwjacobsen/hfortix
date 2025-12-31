ProxyAddress
============

Configuration endpoint for firewall/proxy_address.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.proxy_address

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
   items = fgt.api.cmdb.firewall.proxy_address.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.proxy_address.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.proxy_address.post(
       nkey='value',  # optional
       name='value',  # optional
       uuid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.proxy_address.put(
       name='updated-value',
       uuid='updated-value',
       type='updated-value',
       host='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.proxy_address.delete(name='item-name')


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
       uuid=None,
       type=None,
       host=None,
       host_regex=None,
       path=None,
       query=None,
       referrer=None,
       category=None,
       method=None,
       ua=None,
       ua_min_ver=None,
       ua_max_ver=None,
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
       uuid=None,
       type=None,
       host=None,
       host_regex=None,
       path=None,
       query=None,
       referrer=None,
       category=None,
       method=None,
       ua=None,
       ua_min_ver=None,
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

