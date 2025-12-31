SdnProxy
========

Configuration endpoint for system/sdn_proxy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.sdn_proxy

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
   items = fgt.api.cmdb.system.sdn_proxy.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.sdn_proxy.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.sdn_proxy.post(
       nkey='value',  # optional
       name='value',  # optional
       type='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.sdn_proxy.put(
       name='updated-value',
       type='updated-value',
       server='updated-value',
       server_port='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.sdn_proxy.delete(name='item-name')


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
       server=None,
       server_port=None,
       username=None,
       password=None,
       vdom=None,
       raw_json=False,
       **kwargs
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
       server=None,
       server_port=None,
       username=None,
       password=None,
       vdom=None,
       raw_json=False,
       **kwargs
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

