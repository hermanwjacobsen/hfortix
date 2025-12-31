Saml
====

Configuration endpoint for system/saml.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.saml

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
   items = fgt.api.cmdb.system.saml.get()


   # Update existing item
   result = fgt.api.cmdb.system.saml.put(
       status='updated-value',
       role='updated-value',
       default_login_page='updated-value',
       default_profile='updated-value',
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
       role=None,
       default_login_page=None,
       default_profile=None,
       cert=None,
       binding_protocol=None,
       portal_url=None,
       entity_id=None,
       single_sign_on_url=None,
       single_logout_url=None,
       idp_entity_id=None,
       idp_single_sign_on_url=None,
       # ... more parameters
   )

Update this specific resource.

