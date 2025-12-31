Cfm
===

Configuration endpoint for ethernet_oam/cfm.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.ethernet_oam.cfm

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
   items = fgt.api.cmdb.ethernet_oam.cfm.get()


   # Create new item
   result = fgt.api.cmdb.ethernet_oam.cfm.post(
       nkey='value',  # optional
       domain_id='value',  # optional
       domain_name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.ethernet_oam.cfm.put(
       domain_id='updated-value',
       domain_name='updated-value',
       domain_level='updated-value',
       service='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.ethernet_oam.cfm.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       domain_id=None,
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
       domain_id=None,
       domain_name=None,
       domain_level=None,
       service=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       domain_id=None,
       payload_dict=None,
       before=None,
       after=None,
       domain_name=None,
       domain_level=None,
       service=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       domain_id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

