CertStatus
==========

Configuration endpoint for endpoint_control/ems.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.endpoint_control.ems

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.endpoint_control.ems.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       ems_id,
       scope=None,
       with_cert=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve authentication status of the EMS server certificate for a

