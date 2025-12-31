Modem3g
=======

Configuration endpoint for system/modem_3g.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.modem_3g

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.modem_3g.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List all 3G modems available via FortiGuard.

