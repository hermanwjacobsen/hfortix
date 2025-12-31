Saml
====

Configuration endpoint for user/saml.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.saml

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
   items = fgt.api.cmdb.user.saml.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.saml.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.saml.post(
       nkey='value',  # optional
       name='value',  # optional
       cert='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.saml.put(
       name='updated-value',
       cert='updated-value',
       entity_id='updated-value',
       single_sign_on_url='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.saml.delete(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
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
       name=None,
       cert=None,
       entity_id=None,
       single_sign_on_url=None,
       single_logout_url=None,
       idp_entity_id=None,
       idp_single_sign_on_url=None,
       idp_single_logout_url=None,
       idp_cert=None,
       scim_client=None,
       scim_user_attr_type=None,
       scim_group_attr_type=None,
       user_name=None,
       # ... more parameters
   )

Create object(s) in this table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       name=None,
       payload_dict=None,
       before=None,
       after=None,
       cert=None,
       entity_id=None,
       single_sign_on_url=None,
       single_logout_url=None,
       idp_entity_id=None,
       idp_single_sign_on_url=None,
       idp_single_logout_url=None,
       idp_cert=None,
       scim_client=None,
       scim_user_attr_type=None,
       scim_group_attr_type=None,
       # ... more parameters
   )

Update this specific resource.


``delete()``
^^^^^^^^^^

.. code-block:: python

   delete(
       name=None,
       payload_dict=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Delete this specific resource.

