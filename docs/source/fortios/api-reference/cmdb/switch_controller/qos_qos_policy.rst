QosQosPolicy
============

Configuration endpoint for switch_controller/qos_qos_policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.switch_controller.qos_qos_policy

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
   items = fgt.api.cmdb.switch_controller.qos_qos_policy.get()

   # Get specific item by name
   item = fgt.api.cmdb.switch_controller.qos_qos_policy.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.switch_controller.qos_qos_policy.post(
       nkey='value',  # optional
       name='value',  # optional
       default_cos='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.switch_controller.qos_qos_policy.put(
       name='updated-value',
       default_cos='updated-value',
       trust_dot1p_map='updated-value',
       trust_ip_dscp_map='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.switch_controller.qos_qos_policy.delete(name='item-name')


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
       default_cos=None,
       trust_dot1p_map=None,
       trust_ip_dscp_map=None,
       queue_policy=None,
       vdom=None,
       raw_json=False,
       **kwargs
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
       default_cos=None,
       trust_dot1p_map=None,
       trust_ip_dscp_map=None,
       queue_policy=None,
       vdom=None,
       raw_json=False,
       **kwargs
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

