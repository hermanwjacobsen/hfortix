Custom
======

Configuration endpoint for application/custom.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.application.custom

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
   items = fgt.api.cmdb.application.custom.get()


   # Create new item
   result = fgt.api.cmdb.application.custom.post(
       nkey='value',  # optional
       tag='value',  # optional
       id='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.application.custom.put(
       tag='updated-value',
       id='updated-value',
       comment='updated-value',
       signature='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.application.custom.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       tag=None,
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
       tag=None,
       id=None,
       comment=None,
       signature=None,
       category=None,
       protocol=None,
       technology=None,
       behavior=None,
       vendor=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       tag=None,
       payload_dict=None,
       before=None,
       after=None,
       id=None,
       comment=None,
       signature=None,
       category=None,
       protocol=None,
       technology=None,
       behavior=None,
       vendor=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       tag=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

