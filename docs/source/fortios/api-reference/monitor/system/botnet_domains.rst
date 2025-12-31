Hits
====

Configuration endpoint for system/botnet_domains.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.botnet_domains

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.botnet_domains.get()



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

List hit botnet domains with hit count > 0.

