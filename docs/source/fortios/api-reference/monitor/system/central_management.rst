Status
======

Configuration endpoint for system/central_management.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.central_management

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.central_management.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       skip_detect=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get Central Management status.

