Reset
=====

Configuration endpoint for firewall/per_ip_shaper.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.per_ip_shaper

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.per_ip_shaper.post(
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

Reset statistics for all configured firewall per-IP traffic shapers.

