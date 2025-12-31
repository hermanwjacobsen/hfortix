VdomLink
========

Configuration endpoint for system/vdom_link.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.vdom_link

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.vdom_link.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Gets a list of all NPU VDOM Links and VDOM Links.

