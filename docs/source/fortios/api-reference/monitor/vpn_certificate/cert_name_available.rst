CertNameAvailable
=================

Configuration endpoint for vpn_certificate/cert_name_available.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.vpn_certificate.cert_name_available

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.vpn_certificate.cert_name_available.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Check if the local certificate name is available to use.

