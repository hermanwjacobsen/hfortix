VdomResource
============

Configuration endpoint for system/vdom_resource.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.vdom_resource

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.vdom_resource.get()



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

Retrieve VDOM resource information, including CPU and memory usage.

