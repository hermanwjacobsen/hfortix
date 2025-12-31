Acme
====

Configuration endpoint for system/acme.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.acme

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
   items = fgt.api.cmdb.system.acme.get()


   # Update existing item
   result = fgt.api.cmdb.system.acme.put(
       interface='updated-value',
       use_ha_direct='updated-value',
       source_ip='updated-value',
       source_ip6='updated-value',
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
       interface=None,
       use_ha_direct=None,
       source_ip=None,
       source_ip6=None,
       accounts=None,
       acc_details=None,
       status=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

