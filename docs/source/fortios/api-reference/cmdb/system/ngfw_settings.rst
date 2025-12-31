NgfwSettings
============

Configuration endpoint for system/ngfw_settings.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ngfw_settings

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
   items = fgt.api.cmdb.system.ngfw_settings.get()


   # Update existing item
   result = fgt.api.cmdb.system.ngfw_settings.put(
       match_timeout='updated-value',
       tcp_match_timeout='updated-value',
       tcp_halfopen_match_timeout='updated-value',
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
       match_timeout=None,
       tcp_match_timeout=None,
       tcp_halfopen_match_timeout=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

