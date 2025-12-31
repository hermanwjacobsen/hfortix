BackupAction
============

Configuration endpoint for system/fortimanager.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.fortimanager

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.fortimanager.post(
       operation='value',  # optional
       objects='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       operation=None,
       objects=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Import or update from FortiManager objects.

