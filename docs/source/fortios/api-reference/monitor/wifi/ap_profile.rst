CreateDefault
=============

Configuration endpoint for wifi/ap_profile.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.ap_profile

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.ap_profile.post(
       platform='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       platform=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Create a default FortiAP profile for the specified platform.

