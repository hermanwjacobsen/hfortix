ReplacemsgFortiguardWf
======================

Configuration endpoint for system/replacemsg_fortiguard_wf.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.replacemsg_fortiguard_wf

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
   items = fgt.api.cmdb.system.replacemsg_fortiguard_wf.get()


   # Create new item
   result = fgt.api.cmdb.system.replacemsg_fortiguard_wf.post(
       nkey='value',  # optional
       msg_type='value',  # optional
       buffer='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.replacemsg_fortiguard_wf.put(
       msg_type='updated-value',
       buffer='updated-value',
       header='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.replacemsg_fortiguard_wf.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       msg_type=None,
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
       msg_type=None,
       buffer=None,
       header=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       msg_type=None,
       payload_dict=None,
       before=None,
       after=None,
       buffer=None,
       header=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       msg_type=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

