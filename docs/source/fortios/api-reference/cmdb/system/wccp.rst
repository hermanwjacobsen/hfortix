Wccp
====

Configuration endpoint for system/wccp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.wccp

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
   items = fgt.api.cmdb.system.wccp.get()


   # Create new item
   result = fgt.api.cmdb.system.wccp.post(
       nkey='value',  # optional
       service_id='value',  # optional
       router_id='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.wccp.put(
       service_id='updated-value',
       router_id='updated-value',
       cache_id='updated-value',
       group_address='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.wccp.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       service_id=None,
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
       service_id=None,
       router_id=None,
       cache_id=None,
       group_address=None,
       server_list=None,
       router_list=None,
       ports_defined=None,
       server_type=None,
       ports=None,
       authentication=None,
       password=None,
       forward_method=None,
       cache_engine_method=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       service_id=None,
       payload_dict=None,
       before=None,
       after=None,
       router_id=None,
       cache_id=None,
       group_address=None,
       server_list=None,
       router_list=None,
       ports_defined=None,
       server_type=None,
       ports=None,
       authentication=None,
       password=None,
       forward_method=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       service_id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

