Download
========

Configuration endpoint for endpoint_control/installer.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.endpoint_control.installer

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.endpoint_control.installer.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download a FortiClient installer via FortiGuard.

