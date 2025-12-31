Remote
======

Configuration endpoint for certificate/remote.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.certificate.remote

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.certificate.remote.get()

   # Get specific item by name
   item = fgt.api.cmdb.certificate.remote.get(name='item-name')


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       name=None,
       payload_dict=None,
       attr=None,
       skip_to_datasource=None,
       acs=None,
       search=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select a specific entry from a CLI table.

