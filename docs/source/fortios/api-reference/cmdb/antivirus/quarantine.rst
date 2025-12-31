Quarantine
==========

Configuration endpoint for antivirus/quarantine.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.antivirus.quarantine

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
   items = fgt.api.cmdb.antivirus.quarantine.get()


   # Update existing item
   result = fgt.api.cmdb.antivirus.quarantine.put(
       agelimit='updated-value',
       maxfilesize='updated-value',
       quarantine_quota='updated-value',
       drop_infected='updated-value',
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
       agelimit=None,
       maxfilesize=None,
       quarantine_quota=None,
       drop_infected=None,
       store_infected=None,
       drop_machine_learning=None,
       store_machine_learning=None,
       lowspace=None,
       destination=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

