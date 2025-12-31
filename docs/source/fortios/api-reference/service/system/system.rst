FabricAdminLockoutExistsOnFirmwareUpdate
========================================

Configuration endpoint for system/system.

Python Attribute
----------------

.. code-block:: python

   fgt.api.service.system.system

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.service.system.system.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       vdom=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check if there exists a FortiGate in the Fabric that has an

