EnableAppBandwidthTracking
==========================

Configuration endpoint for system/traffic_history.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.traffic_history

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.traffic_history.post(
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

Enable FortiView application bandwidth tracking.

