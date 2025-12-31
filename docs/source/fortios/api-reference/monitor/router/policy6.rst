Policy6
=======

Configuration endpoint for router/policy6.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.router.policy6

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.router.policy6.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       count_only=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of active IPv6 policy routes.

