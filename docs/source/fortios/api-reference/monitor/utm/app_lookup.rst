AppLookup
=========

Configuration endpoint for utm/app_lookup.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.utm.app_lookup

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.utm.app_lookup.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       hosts=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Query ISDB to resolve hosts to application control entries.

