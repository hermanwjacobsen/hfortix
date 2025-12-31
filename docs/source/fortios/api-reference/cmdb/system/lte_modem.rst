LteModem
========

Configuration endpoint for system/lte_modem.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.lte_modem

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
   items = fgt.api.cmdb.system.lte_modem.get()


   # Update existing item
   result = fgt.api.cmdb.system.lte_modem.put(
       status='updated-value',
       extra_init='updated-value',
       pdptype='updated-value',
       authtype='updated-value',
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
       extra_init=None,
       pdptype=None,
       authtype=None,
       username=None,
       passwd=None,
       apn=None,
       modem_port=None,
       mode=None,
       holddown_timer=None,
       interface=None,
       vdom=None,
       # ... more parameters
   )

Update this specific resource.

