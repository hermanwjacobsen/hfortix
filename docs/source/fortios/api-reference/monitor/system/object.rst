Usage
=====

Configuration endpoint for system/object.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.object

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.object.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       q_path=None,
       q_name=None,
       qtypes=None,
       scope=None,
       mkey=None,
       child_path=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve all objects that are currently using as well as objects that

