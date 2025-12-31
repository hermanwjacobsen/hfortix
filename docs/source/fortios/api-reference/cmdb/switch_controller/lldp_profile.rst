LldpProfile
===========

Configuration endpoint for switch_controller/lldp_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.lldp_profile

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
   items = fgt.api.cmdb.switch_controller.lldp_profile.get()

   # Get specific item by name
   item = fgt.api.cmdb.switch_controller.lldp_profile.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.switch_controller.lldp_profile.post(
       nkey='value',  # optional
       name='value',  # optional
       med_tlvs='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.lldp_profile.put(
       name='updated-value',
       med_tlvs='updated-value',
       _802_1_tlvs='updated-value',
       _802_3_tlvs='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.lldp_profile.delete(name='item-name')


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
       med_tlvs=None,
       _802_1_tlvs=None,
       _802_3_tlvs=None,
       auto_isl=None,
       auto_isl_hello_timer=None,
       auto_isl_receive_timeout=None,
       auto_isl_port_group=None,
       auto_mclag_icl=None,
       auto_isl_auth=None,
       auto_isl_auth_user=None,
       auto_isl_auth_identity=None,
       auto_isl_auth_reauth=None,
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
       med_tlvs=None,
       _802_1_tlvs=None,
       _802_3_tlvs=None,
       auto_isl=None,
       auto_isl_hello_timer=None,
       auto_isl_receive_timeout=None,
       auto_isl_port_group=None,
       auto_mclag_icl=None,
       auto_isl_auth=None,
       auto_isl_auth_user=None,
       auto_isl_auth_identity=None,
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

