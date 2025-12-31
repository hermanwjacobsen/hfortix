Setting
=======

Configuration endpoint for automation/setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.automation.setting

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
   items = fgt.api.cmdb.automation.setting.get()


   # Update existing item
   result = fgt.api.cmdb.automation.setting.put(
       max_concurrent_stitches='updated-value',
       fabric_sync='updated-value',
       secure_mode='updated-value',
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
       max_concurrent_stitches=None,
       fabric_sync=None,
       secure_mode=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

