InterferingAp
=============

Configuration endpoint for wifi/interfering_ap.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.interfering_ap

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.wifi.interfering_ap.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       wtp=None,
       radio=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of interfering APs for one FortiAP radio.

