DomainController
================

Configuration endpoint for user/domain_controller.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.user.domain_controller

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
   items = fgt.api.cmdb.user.domain_controller.get()

   # Get specific item by name
   item = fgt.api.cmdb.user.domain_controller.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.user.domain_controller.post(
       nkey='value',  # optional
       name='value',  # optional
       ad_mode='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.user.domain_controller.put(
       name='updated-value',
       ad_mode='updated-value',
       hostname='updated-value',
       username='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.user.domain_controller.delete(name='item-name')


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
       ad_mode=None,
       hostname=None,
       username=None,
       password=None,
       ip_address=None,
       ip6=None,
       port=None,
       source_ip_address=None,
       source_ip6=None,
       source_port=None,
       interface_select_method=None,
       interface=None,
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
       ad_mode=None,
       hostname=None,
       username=None,
       password=None,
       ip_address=None,
       ip6=None,
       port=None,
       source_ip_address=None,
       source_ip6=None,
       source_port=None,
       interface_select_method=None,
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

