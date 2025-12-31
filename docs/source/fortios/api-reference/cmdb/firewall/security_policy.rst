SecurityPolicy
==============

Configuration endpoint for firewall/security_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.security_policy

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
   items = fgt.api.cmdb.firewall.security_policy.get()


   # Create new item
   result = fgt.api.cmdb.firewall.security_policy.post(
       nkey='value',  # optional
       uuid='value',  # optional
       policyid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.security_policy.put(
       policyid='updated-value',
       uuid='updated-value',
       name='updated-value',
       comments='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.security_policy.delete()


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
       uuid=None,
       policyid=None,
       name=None,
       comments=None,
       srcintf=None,
       dstintf=None,
       srcaddr=None,
       srcaddr_negate=None,
       dstaddr=None,
       dstaddr_negate=None,
       srcaddr6=None,
       srcaddr6_negate=None,
       dstaddr6=None,
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
       name=None,
       comments=None,
       srcintf=None,
       dstintf=None,
       srcaddr=None,
       srcaddr_negate=None,
       dstaddr=None,
       dstaddr_negate=None,
       srcaddr6=None,
       srcaddr6_negate=None,
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

