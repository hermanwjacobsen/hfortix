Usage
=====

Configuration endpoint for system/resource.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.resource

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.resource.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       resource=None,
       interval=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retreive current and historical usage data for a provided resource.

