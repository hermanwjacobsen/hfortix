Np6xlite
========

Configuration endpoint for system/np6xlite.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.np6xlite

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
   items = fgt.api.cmdb.system.np6xlite.get()

   # Get specific item by name
   item = fgt.api.cmdb.system.np6xlite.get(name='item-name')

   # Create new item
   result = fgt.api.cmdb.system.np6xlite.post(
       nkey='value',  # optional
       name='value',  # optional
       fastpath='value',  # optional
   )

   # Update existing item
   result = fgt.api.cmdb.system.np6xlite.put(
       name='updated-value',
       fastpath='updated-value',
       per_session_accounting='updated-value',
       session_timeout_interval='updated-value',
   )

   # Delete item
   result = fgt.api.cmdb.system.np6xlite.delete(name='item-name')


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
       fastpath=None,
       per_session_accounting=None,
       session_timeout_interval=None,
       ipsec_inner_fragment=None,
       ipsec_throughput_msg_frequency=None,
       ipsec_sts_timeout=None,
       hpe=None,
       fp_anomaly=None,
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
       fastpath=None,
       per_session_accounting=None,
       session_timeout_interval=None,
       ipsec_inner_fragment=None,
       ipsec_throughput_msg_frequency=None,
       ipsec_sts_timeout=None,
       hpe=None,
       fp_anomaly=None,
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

