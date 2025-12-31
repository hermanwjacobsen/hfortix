AvailableCertificates
=====================

Configuration endpoint for system/available_certificates.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.available_certificates

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.available_certificates.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       scope=None,
       with_remote=None,
       with_ca=None,
       with_crl=None,
       mkey=None,
       find_all_references=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get available certificates.

