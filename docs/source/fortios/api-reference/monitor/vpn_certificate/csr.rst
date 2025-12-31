Generate
========

Configuration endpoint for vpn_certificate/csr.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.vpn_certificate.csr

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.vpn_certificate.csr.post(
       certname='value',  # optional
       subject='value',  # optional
       keytype='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       certname=None,
       subject=None,
       keytype=None,
       keysize=None,
       curvename=None,
       orgunits=None,
       org=None,
       city=None,
       state=None,
       countrycode=None,
       email=None,
       subject_alt_name=None,
       password=None,
       scep_url=None,
       scep_password=None,
       # ... more parameters
   )

Generate a certificate signing request (CSR) and a private key.

