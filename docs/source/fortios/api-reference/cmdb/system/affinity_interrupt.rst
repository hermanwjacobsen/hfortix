AffinityInterrupt
=================

Configuration endpoint for system/affinity_interrupt.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.affinity_interrupt

Available Methods
-----------------

- ``get()`` - GET operation
- ``post()`` - POST operation
- ``put()`` - PUT operation
- ``delete()`` - DELETE operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.affinity_interrupt.get()


   # Create new item
   result = fgt.api.cmdb.system.affinity_interrupt.post(
       nkey='value',  # optional
       id='value',  # optional
       interrupt='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.affinity_interrupt.put(
       id='updated-value',
       interrupt='updated-value',
       affinity_cpumask='updated-value',
       default_affinity_cpumask='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.affinity_interrupt.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       id=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.


``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       nkey=None,
       id=None,
       interrupt=None,
       affinity_cpumask=None,
       default_affinity_cpumask=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       id=None,
       payload_dict=None,
       before=None,
       after=None,
       interrupt=None,
       affinity_cpumask=None,
       default_affinity_cpumask=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       id=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

