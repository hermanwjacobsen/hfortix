ClearCounters
=============

Configuration endpoint for firewall/multicast_policy6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.multicast_policy6

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.multicast_policy6.post(
       policy='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       policy=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Reset traffic statistics for one or more firewall IPv6 multicast

