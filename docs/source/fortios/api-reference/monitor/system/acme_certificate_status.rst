AcmeCertificateStatus
=====================

Configuration endpoint for system/acme_certificate_status.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.acme_certificate_status

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.acme_certificate_status.get()



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

Get ACME certificate status.

