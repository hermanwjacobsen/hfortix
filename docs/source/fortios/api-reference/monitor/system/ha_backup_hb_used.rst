HaBackupHbUsed
==============

Configuration endpoint for system/ha_backup_hb_used.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.ha_backup_hb_used

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.ha_backup_hb_used.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get HA backup heartbeat interface usage.

