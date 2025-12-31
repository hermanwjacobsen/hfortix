GlobalResources
===============

Configuration endpoint for system/global_resources.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.global_resources

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.global_resources.get()



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

Retrieve current usage of global resources as well as both the default

