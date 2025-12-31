Abort
=====

Configuration endpoint for search/search.

Python Attribute
----------------

.. code-block:: python

   fgt.api.log.search.search

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.log.search.search.post(
       session_id='value',
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       session_id,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Abort a running log search session.

