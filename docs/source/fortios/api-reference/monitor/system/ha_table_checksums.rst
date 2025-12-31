HaTableChecksums
================

Configuration endpoint for system/ha_table_checksums.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.ha_table_checksums

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.ha_table_checksums.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       serial_no,
       vdom_name=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List of table checksums for members of HA cluster.

