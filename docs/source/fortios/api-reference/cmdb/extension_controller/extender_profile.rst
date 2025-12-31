ExtenderProfile
===============

Configuration endpoint for extension_controller/extender_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.extension_controller.extender_profile

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
   items = fgt.api.cmdb.extension_controller.extender_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.extension_controller.extender_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.extension_controller.extender_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       id='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.extension_controller.extender_profile.put(
       name='updated-value',
       id='updated-value',
       model='updated-value',
       extension='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.extension_controller.extender_profile.delete(name='item-name')


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
       id=None,
       model=None,
       extension=None,
       allowaccess=None,
       login_password_change=None,
       login_password=None,
       enforce_bandwidth=None,
       bandwidth_limit=None,
       cellular=None,
       wifi=None,
       lan_extension=None,
       vdom=None,
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
       id=None,
       model=None,
       extension=None,
       allowaccess=None,
       login_password_change=None,
       login_password=None,
       enforce_bandwidth=None,
       bandwidth_limit=None,
       cellular=None,
       wifi=None,
       lan_extension=None,
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

