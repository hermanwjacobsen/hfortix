Query
=====

Configuration endpoint for service/ldap.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.service.ldap

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.service.ldap.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       mkey=None,
       server_info_only=None,
       skip_schema=None,
       ldap_filter=None,
       ldap=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve LDAP server information and LDAP entries.

