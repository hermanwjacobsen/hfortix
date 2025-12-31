Download
========

Configuration endpoint for system/certificate.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.certificate

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.certificate.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       type,
       scope=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download certificate.

