GlobalSearch
============

Configuration endpoint for system/global_search.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.global_search

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.global_search.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       search,
       scope=None,
       search_tables=None,
       skip_tables=None,
       exact=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Search for CMDB table objects based on search phrase.

