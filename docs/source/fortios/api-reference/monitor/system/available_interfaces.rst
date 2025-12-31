Meta
====

Configuration endpoint for system/available_interfaces.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.available_interfaces

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.available_interfaces.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       include_ha=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get metadata for the system/available-interfaces API endpoint.

