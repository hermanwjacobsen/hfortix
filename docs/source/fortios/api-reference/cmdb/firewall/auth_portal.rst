AuthPortal
==========

Configuration endpoint for firewall/auth_portal.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.auth_portal

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
   items = fgt.api.cmdb.firewall.auth_portal.get()


   # Update existing item
   result = fgt.api.cmdb.firewall.auth_portal.put(
       groups='updated-value',
       portal_addr='updated-value',
       portal_addr6='updated-value',
       identity_based_route='updated-value',
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
       groups=None,
       portal_addr=None,
       portal_addr6=None,
       identity_based_route=None,
       proxy_auth=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

