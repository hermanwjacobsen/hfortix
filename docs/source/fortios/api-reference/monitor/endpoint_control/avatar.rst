Download
========

Configuration endpoint for endpoint_control/avatar.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.endpoint_control.avatar

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.endpoint_control.avatar.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       uid=None,
       user=None,
       fingerprint=None,
       default=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Download an endpoint avatar image.

