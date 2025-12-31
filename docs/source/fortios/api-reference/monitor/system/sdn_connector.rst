NsxSecurityTags
===============

Configuration endpoint for system/sdn_connector.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.sdn_connector

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.system.sdn_connector.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve a list of NSX security tags for connected NSX servers.

