CustomLanguage
==============

Configuration endpoint for system/custom_language.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.custom_language

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
   items = fgt.api.cmdb.system.custom_language.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.custom_language.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.custom_language.post(
       nkey='value',  # optional
       name='value',  # optional
       filename='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.custom_language.put(
       name='updated-value',
       filename='updated-value',
       comments='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.custom_language.delete(name='item-name')


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
       filename=None,
       comments=None,
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
       filename=None,
       comments=None,
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

