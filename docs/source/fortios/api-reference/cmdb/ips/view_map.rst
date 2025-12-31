ViewMap
=======

Configuration endpoint for ips/view_map.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ips.view_map

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
   items = fgt.api.cmdb.ips.view_map.get()


   # Create new item
   result = fgt.api.cmdb.ips.view_map.post(
       nkey='value',  # optional
       id='value',  # optional
       vdom_id='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.ips.view_map.put(
       id='updated-value',
       vdom_id='updated-value',
       policy_id='updated-value',
       id_policy_id='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.ips.view_map.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       id=None,
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
       id=None,
       vdom_id=None,
       policy_id=None,
       id_policy_id=None,
       which=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       id=None,
       payload_dict=None,
       before=None,
       after=None,
       vdom_id=None,
       policy_id=None,
       id_policy_id=None,
       which=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

