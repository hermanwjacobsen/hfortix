Profile
=======

Configuration endpoint for voip/profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.voip.profile

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
   items = fgt.api.cmdb.voip.profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.voip.profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.voip.profile.post(
       nkey='value',  # optional
       name='value',  # optional
       feature_set='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.voip.profile.put(
       name='updated-value',
       feature_set='updated-value',
       comment='updated-value',
       sip='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.voip.profile.delete(name='item-name')


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
       feature_set=None,
       comment=None,
       sip=None,
       sccp=None,
       msrp=None,
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
       feature_set=None,
       comment=None,
       sip=None,
       sccp=None,
       msrp=None,
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

