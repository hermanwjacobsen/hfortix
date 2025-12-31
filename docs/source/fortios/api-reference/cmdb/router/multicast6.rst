Multicast6
==========

Configuration endpoint for router/multicast6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.router.multicast6

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
   items = fgt.api.cmdb.router.multicast6.get()


   # Update existing item
   result = fgt.api.cmdb.router.multicast6.put(
       multicast_routing='updated-value',
       multicast_pmtu='updated-value',
       interface='updated-value',
       pim_sm_global='updated-value',
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
       multicast_routing=None,
       multicast_pmtu=None,
       interface=None,
       pim_sm_global=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

