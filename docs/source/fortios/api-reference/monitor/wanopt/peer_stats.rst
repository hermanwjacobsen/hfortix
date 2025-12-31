Reset
=====

Configuration endpoint for wanopt/peer_stats.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wanopt.peer_stats

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wanopt.peer_stats.post(
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Reset WAN opt peer statistics.

