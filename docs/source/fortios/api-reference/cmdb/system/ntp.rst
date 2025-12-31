Ntp
===

Configuration endpoint for system/ntp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ntp

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
   items = fgt.api.cmdb.system.ntp.get()


   # Update existing item
   result = fgt.api.cmdb.system.ntp.put(
       ntpsync='updated-value',
       type='updated-value',
       syncinterval='updated-value',
       ntpserver='updated-value',
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
       ntpsync=None,
       type=None,
       syncinterval=None,
       ntpserver=None,
       source_ip=None,
       source_ip6=None,
       server_mode=None,
       authentication=None,
       key_type=None,
       key_id=None,
       interface=None,
       vdom=None,
       # ... more parameters
   )

Update this specific resource.

