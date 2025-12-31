ProxyPolicy
===========

Configuration endpoint for firewall/proxy_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.proxy_policy

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
   items = fgt.api.cmdb.firewall.proxy_policy.get()


   # Create new item
   result = fgt.api.cmdb.firewall.proxy_policy.post(
       nkey='value',  # optional
       uuid='value',  # optional
       policyid='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.firewall.proxy_policy.put(
       policyid='updated-value',
       uuid='updated-value',
       name='updated-value',
       proxy='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.firewall.proxy_policy.delete()


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
       proxy=None,
       access_proxy=None,
       access_proxy6=None,
       ztna_proxy=None,
       srcintf=None,
       dstintf=None,
       srcaddr=None,
       poolname=None,
       poolname6=None,
       dstaddr=None,
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
       proxy=None,
       access_proxy=None,
       access_proxy6=None,
       ztna_proxy=None,
       srcintf=None,
       dstintf=None,
       srcaddr=None,
       poolname=None,
       poolname6=None,
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

