StandaloneCluster
=================

Configuration endpoint for system/standalone_cluster.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.standalone_cluster

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
   items = fgt.api.cmdb.system.standalone_cluster.get()


   # Update existing item
   result = fgt.api.cmdb.system.standalone_cluster.put(
       standalone_group_id='updated-value',
       group_member_id='updated-value',
       layer2_connection='updated-value',
       session_sync_dev='updated-value',
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
       standalone_group_id=None,
       group_member_id=None,
       layer2_connection=None,
       session_sync_dev=None,
       encryption=None,
       psksecret=None,
       asymmetric_traffic_control=None,
       cluster_peer=None,
       monitor_interface=None,
       pingsvr_monitor_interface=None,
       monitor_prefix=None,
       helper_traffic_bounce=None,
       # ... more parameters
   )

Update this specific resource.

