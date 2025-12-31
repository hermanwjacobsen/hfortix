Flush
=====

Configuration endpoint for firewall/gtp.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.gtp

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.gtp.post(
       scope='value',  # optional
       gtp_profile='value',  # optional
       version='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       scope=None,
       gtp_profile=None,
       version=None,
       imsi=None,
       msisdn=None,
       ms_addr=None,
       ms_addr6=None,
       cteid=None,
       cteid_addr=None,
       cteid_addr6=None,
       fteid=None,
       fteid_addr=None,
       fteid_addr6=None,
       apn=None,
       payload_dict=None,
       # ... more parameters
   )

Flush GTP tunnels.

