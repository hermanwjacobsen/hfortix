TrustedCertAuthorities
======================

Configuration endpoint for system/trusted_cert_authorities.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.trusted_cert_authorities

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.trusted_cert_authorities.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get trusted certifiate authorities.

