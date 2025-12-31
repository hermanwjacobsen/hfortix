StpSettings
===========

Configuration endpoint for switch_controller/stp_settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.stp_settings

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
   items = fgt.api.cmdb.switch_controller.stp_settings.get()


   # Update existing item
   result = fgt.api.cmdb.switch_controller.stp_settings.put(
       name='updated-value',
       revision='updated-value',
       hello_time='updated-value',
       forward_time='updated-value',
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
       name=None,
       revision=None,
       hello_time=None,
       forward_time=None,
       max_age=None,
       max_hops=None,
       pending_timer=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

