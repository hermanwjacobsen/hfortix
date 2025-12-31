ApChannels
==========

Configuration endpoint for wifi/ap_channels.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.ap_channels

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.wifi.ap_channels.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       platform_type,
       country=None,
       indoor_outdoor=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve the set of channel lists for all possible band/configurations

