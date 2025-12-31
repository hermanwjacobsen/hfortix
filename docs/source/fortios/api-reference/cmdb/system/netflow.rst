Netflow
=======

Configuration endpoint for system/netflow.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.netflow

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
   items = fgt.api.cmdb.system.netflow.get()


   # Update existing item
   result = fgt.api.cmdb.system.netflow.put(
       active_flow_timeout='updated-value',
       inactive_flow_timeout='updated-value',
       template_tx_timeout='updated-value',
       template_tx_counter='updated-value',
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
       active_flow_timeout=None,
       inactive_flow_timeout=None,
       template_tx_timeout=None,
       template_tx_counter=None,
       session_cache_size=None,
       exclusion_filters=None,
       collectors=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

