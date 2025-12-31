InterfaceConnectedAdminsInfo
============================

Configuration endpoint for system/interface_connected_admins_info.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.interface_connected_admins_info

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.interface_connected_admins_info.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       interface,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Return admins info that are connected to current interface.

