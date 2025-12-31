Policy
======

Configuration endpoint for firewall/policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.policy

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
   items = fgt.api.cmdb.firewall.policy.get()


   # Create new item
   result = fgt.api.cmdb.firewall.policy.post(
       nkey='value',  # optional
       policyid='value',  # optional
       status='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.policy.put(
       policyid='updated-value',
       status='updated-value',
       name='updated-value',
       uuid='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.policy.delete()


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
       status=None,
       name=None,
       uuid=None,
       srcintf=None,
       dstintf=None,
       nat64=None,
       nat46=None,
       ztna_status=None,
       ztna_device_ownership=None,
       srcaddr=None,
       dstaddr=None,
       srcaddr6=None,
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
       status=None,
       name=None,
       uuid=None,
       srcintf=None,
       dstintf=None,
       nat64=None,
       nat46=None,
       ztna_status=None,
       ztna_device_ownership=None,
       srcaddr=None,
       dstaddr=None,
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

