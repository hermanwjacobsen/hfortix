List
====

Configuration endpoint for application/list.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.application.list

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
   items = fgt.api.cmdb.application.list.get()

   # Get specific item by name
   item = fgt.api.cmdb.application.list.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.application.list.post(
       nkey='value',  # optional
       name='value',  # optional
       comment='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.application.list.put(
       name='updated-value',
       comment='updated-value',
       replacemsg_group='updated-value',
       extended_log='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.application.list.delete(name='item-name')


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
       comment=None,
       replacemsg_group=None,
       extended_log=None,
       other_application_action=None,
       app_replacemsg=None,
       other_application_log=None,
       enforce_default_app_port=None,
       force_inclusion_ssl_di_sigs=None,
       unknown_application_action=None,
       unknown_application_log=None,
       p2p_block_list=None,
       deep_app_inspection=None,
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
       comment=None,
       replacemsg_group=None,
       extended_log=None,
       other_application_action=None,
       app_replacemsg=None,
       other_application_log=None,
       enforce_default_app_port=None,
       force_inclusion_ssl_di_sigs=None,
       unknown_application_action=None,
       unknown_application_log=None,
       p2p_block_list=None,
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

