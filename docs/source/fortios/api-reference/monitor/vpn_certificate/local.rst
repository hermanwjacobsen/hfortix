Create
======

Configuration endpoint for vpn_certificate/local.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.vpn_certificate.local

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.vpn_certificate.local.post(
       certname='value',  # optional
       common_name='value',  # optional
       scope='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       certname=None,
       common_name=None,
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Generate a new certificate signed by Fortinet_CA_SSL.

