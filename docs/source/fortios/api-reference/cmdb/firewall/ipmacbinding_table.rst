IpmacbindingTable
=================

Configuration endpoint for firewall/ipmacbinding_table.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ipmacbinding_table

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
   items = fgt.api.cmdb.firewall.ipmacbinding_table.get()


   # Create new item
   result = fgt.api.cmdb.firewall.ipmacbinding_table.post(
       nkey='value',  # optional
       seq_num='value',  # optional
       ip='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.ipmacbinding_table.put(
       seq_num='updated-value',
       ip='updated-value',
       mac='updated-value',
       name='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.ipmacbinding_table.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       seq_num=None,
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
       seq_num=None,
       ip=None,
       mac=None,
       name=None,
       status=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       seq_num=None,
       payload_dict=None,
       before=None,
       after=None,
       ip=None,
       mac=None,
       name=None,
       status=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       seq_num=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

