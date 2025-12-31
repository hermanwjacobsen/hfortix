Scheme
======

Configuration endpoint for authentication/scheme.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.authentication.scheme

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
   items = fgt.api.cmdb.authentication.scheme.get()

   # Get specific item by name
   item = fgt.api.cmdb.authentication.scheme.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.authentication.scheme.post(
       nkey='value',  # optional
       name='value',  # optional
       method='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.authentication.scheme.put(
       name='updated-value',
       method='updated-value',
       negotiate_ntlm='updated-value',
       kerberos_keytab='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.authentication.scheme.delete(name='item-name')


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
       method=None,
       negotiate_ntlm=None,
       kerberos_keytab=None,
       domain_controller=None,
       saml_server=None,
       saml_timeout=None,
       fsso_agent_for_ntlm=None,
       require_tfa=None,
       fsso_guest=None,
       user_cert=None,
       cert_http_header=None,
       user_database=None,
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
       method=None,
       negotiate_ntlm=None,
       kerberos_keytab=None,
       domain_controller=None,
       saml_server=None,
       saml_timeout=None,
       fsso_agent_for_ntlm=None,
       require_tfa=None,
       fsso_guest=None,
       user_cert=None,
       cert_http_header=None,
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

