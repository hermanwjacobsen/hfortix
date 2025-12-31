Profile
=======

Configuration endpoint for icap/profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.icap.profile

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
   items = fgt.api.cmdb.icap.profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.icap.profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.icap.profile.post(
       nkey='value',  # optional
       replacemsg_group='value',  # optional
       name='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.icap.profile.put(
       name='updated-value',
       replacemsg_group='updated-value',
       comment='updated-value',
       request='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.icap.profile.delete(name='item-name')


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
       replacemsg_group=None,
       name=None,
       comment=None,
       request=None,
       response=None,
       file_transfer=None,
       streaming_content_bypass=None,
       ocr_only=None,
       _204_size_limit=None,
       _204_response=None,
       preview=None,
       preview_data_length=None,
       request_server=None,
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
       replacemsg_group=None,
       comment=None,
       request=None,
       response=None,
       file_transfer=None,
       streaming_content_bypass=None,
       ocr_only=None,
       _204_size_limit=None,
       _204_response=None,
       preview=None,
       preview_data_length=None,
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

