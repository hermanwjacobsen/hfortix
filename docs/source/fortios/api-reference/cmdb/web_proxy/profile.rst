Profile
=======

Configuration endpoint for web_proxy/profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.web_proxy.profile

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
   items = fgt.api.cmdb.web_proxy.profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.web_proxy.profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.web_proxy.profile.post(
       nkey='value',  # optional
       name='value',  # optional
       header_client_ip='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.web_proxy.profile.put(
       name='updated-value',
       header_client_ip='updated-value',
       header_via_request='updated-value',
       header_via_response='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.web_proxy.profile.delete(name='item-name')


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
       header_client_ip=None,
       header_via_request=None,
       header_via_response=None,
       header_client_cert=None,
       header_x_forwarded_for=None,
       header_x_forwarded_client_cert=None,
       header_front_end_https=None,
       header_x_authenticated_user=None,
       header_x_authenticated_groups=None,
       strip_encoding=None,
       log_header_change=None,
       headers=None,
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
       header_client_ip=None,
       header_via_request=None,
       header_via_response=None,
       header_client_cert=None,
       header_x_forwarded_for=None,
       header_x_forwarded_client_cert=None,
       header_front_end_https=None,
       header_x_authenticated_user=None,
       header_x_authenticated_groups=None,
       strip_encoding=None,
       log_header_change=None,
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

