Abort
=====

Configuration endpoint for user/query.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.query

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.user.query.post(
       query_id='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       query_id=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Abort a running user device unified query.

