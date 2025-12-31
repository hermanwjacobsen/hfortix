RedirectPortal
==============

Configuration endpoint for fortiguard/redirect_portal.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.fortiguard.redirect_portal

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.fortiguard.redirect_portal.get()



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

Retrieve the FortiGuard redirect portal IP.

