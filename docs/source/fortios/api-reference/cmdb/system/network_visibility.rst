NetworkVisibility
=================

Configuration endpoint for system/network_visibility.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.network_visibility

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
   items = fgt.api.cmdb.system.network_visibility.get()


   # Update existing item
   result = fgt.api.cmdb.system.network_visibility.put(
       destination_visibility='updated-value',
       source_location='updated-value',
       destination_hostname_visibility='updated-value',
       destination_location='updated-value',
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
       destination_visibility=None,
       source_location=None,
       destination_hostname_visibility=None,
       destination_location=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

