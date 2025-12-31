FssoPolling
===========

Configuration endpoint for system/fsso_polling.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.fsso_polling

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.fsso_polling.get()


   # Update existing item
   result = fgt.api.cmdb.system.fsso_polling.put(
       status='updated-value',
       listening_port='updated-value',
       authentication='updated-value',
       auth_password='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       status=None,
       listening_port=None,
       authentication=None,
       auth_password=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

