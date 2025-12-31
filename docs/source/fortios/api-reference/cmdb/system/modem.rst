Modem
=====

Configuration endpoint for system/modem.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.modem

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
   items = fgt.api.cmdb.system.modem.get()


   # Update existing item
   result = fgt.api.cmdb.system.modem.put(
       status='updated-value',
       pin_init='updated-value',
       network_init='updated-value',
       lockdown_lac='updated-value',
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
       pin_init=None,
       network_init=None,
       lockdown_lac=None,
       mode=None,
       auto_dial=None,
       dial_on_demand=None,
       idle_timer=None,
       redial=None,
       reset=None,
       holddown_timer=None,
       connect_timeout=None,
       # ... more parameters
   )

Update this specific resource.

