Ippool
======

Configuration endpoint for firewall/ippool.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ippool

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
   items = fgt.api.cmdb.firewall.ippool.get()

   # Get specific item by name
   item = fgt.api.cmdb.firewall.ippool.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.firewall.ippool.post(
       nkey='value',  # optional
       name='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.ippool.put(
       name='updated-value',
       type='updated-value',
       startip='updated-value',
       endip='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.ippool.delete(name='item-name')


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
       startip=None,
       endip=None,
       startport=None,
       endport=None,
       source_startip=None,
       source_endip=None,
       block_size=None,
       port_per_user=None,
       num_blocks_per_user=None,
       pba_timeout=None,
       pba_interim_log=None,
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
       startip=None,
       endip=None,
       startport=None,
       endport=None,
       source_startip=None,
       source_endip=None,
       block_size=None,
       port_per_user=None,
       num_blocks_per_user=None,
       pba_timeout=None,
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

