Groups
======

Configuration endpoint for user/scim.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.user.scim

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.user.scim.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       client_name,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Get SCIM client group-names.

