ObjectTagging
=============

Configuration endpoint for system/object_tagging.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.object_tagging

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
   items = fgt.api.cmdb.system.object_tagging.get()


   # Create new item
   result = fgt.api.cmdb.system.object_tagging.post(
       nkey='value',  # optional
       category='value',  # optional
       address='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.object_tagging.put(
       category='updated-value',
       address='updated-value',
       device='updated-value',
       interface='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.object_tagging.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       category=None,
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
       category=None,
       address=None,
       device=None,
       interface=None,
       multiple=None,
       color=None,
       tags=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       category=None,
       payload_dict=None,
       before=None,
       after=None,
       address=None,
       device=None,
       interface=None,
       multiple=None,
       color=None,
       tags=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       category=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

