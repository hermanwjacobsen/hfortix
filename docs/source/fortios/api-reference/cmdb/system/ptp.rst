Ptp
===

Configuration endpoint for system/ptp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ptp

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
   items = fgt.api.cmdb.system.ptp.get()


   # Update existing item
   result = fgt.api.cmdb.system.ptp.put(
       status='updated-value',
       mode='updated-value',
       delay_mechanism='updated-value',
       request_interval='updated-value',
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
       mode=None,
       delay_mechanism=None,
       request_interval=None,
       interface=None,
       server_mode=None,
       server_interface=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

