CentralSnatMap
==============

Configuration endpoint for firewall/central_snat_map.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.central_snat_map

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
   items = fgt.api.cmdb.firewall.central_snat_map.get()


   # Create new item
   result = fgt.api.cmdb.firewall.central_snat_map.post(
       nkey='value',  # optional
       policyid='value',  # optional
       uuid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.central_snat_map.put(
       policyid='updated-value',
       uuid='updated-value',
       status='updated-value',
       type='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.central_snat_map.delete()


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       policyid=None,
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
       policyid=None,
       uuid=None,
       status=None,
       type=None,
       srcintf=None,
       dstintf=None,
       orig_addr=None,
       orig_addr6=None,
       dst_addr=None,
       dst_addr6=None,
       protocol=None,
       orig_port=None,
       nat=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       policyid=None,
       payload_dict=None,
       before=None,
       after=None,
       uuid=None,
       status=None,
       type=None,
       srcintf=None,
       dstintf=None,
       orig_addr=None,
       orig_addr6=None,
       dst_addr=None,
       dst_addr6=None,
       protocol=None,
       orig_port=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       policyid=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

