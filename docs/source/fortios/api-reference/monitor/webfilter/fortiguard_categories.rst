FortiguardCategories
====================

Configuration endpoint for webfilter/fortiguard_categories.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.webfilter.fortiguard_categories

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.webfilter.fortiguard_categories.get()



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

Return FortiGuard web filter categories.

