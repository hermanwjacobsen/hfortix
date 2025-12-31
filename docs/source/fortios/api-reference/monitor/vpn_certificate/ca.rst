ImportCa
========

Configuration endpoint for vpn_certificate/ca.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.vpn_certificate.ca

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.vpn_certificate.ca.post(
       import_method='value',  # optional
       scep_url='value',  # optional
       scep_ca_id='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       import_method=None,
       scep_url=None,
       scep_ca_id=None,
       scope=None,
       file_content=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Import CA certificate.

