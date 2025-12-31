Query
=====

Configuration endpoint for user/info.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.info

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.user.info.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       timestamp_from=None,
       timestamp_to=None,
       filters=None,
       query_type=None,
       query_id=None,
       cache_query=None,
       key_only=None,
       filter_logic=None,
       total_only=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Query user info.

