Disconnect
==========

Configuration endpoint for system/ha_peer.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.ha_peer

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.ha_peer.post(
       serial_no='value',  # optional
       interface='value',  # optional
       ip='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       serial_no=None,
       interface=None,
       ip=None,
       mask=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Update configuration of peer in HA cluster.

