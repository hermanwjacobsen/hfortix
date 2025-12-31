ImportCrl
=========

Configuration endpoint for vpn_certificate/crl.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.vpn_certificate.crl

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.vpn_certificate.crl.post(
       scope='value',  # optional
       file_content='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       scope=None,
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Import certificate revocation lists (CRL) from file content.

