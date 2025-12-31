Sladb
=====

Configuration endpoint for virtual_wan/sladb.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.virtual_wan.sladb

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.virtual_wan.sladb.get()



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

Retrieve the Service Level Agreement Database downloaded from

