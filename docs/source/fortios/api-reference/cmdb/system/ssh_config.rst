SshConfig
=========

Configuration endpoint for system/ssh_config.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.ssh_config

Available Methods
-----------------

- ``get()`` - GET operation
- ``put()`` - PUT operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.cmdb.system.ssh_config.get()


   # Update existing item
   result = fgt.api.cmdb.system.ssh_config.put(
       ssh_kex_algo='updated-value',
       ssh_enc_algo='updated-value',
       ssh_mac_algo='updated-value',
       ssh_hsk_algo='updated-value',
   )


Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       payload_dict=None,
       exclude_default_values=None,
       stat_items=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Select all entries in a CLI table.


``put()``
^^^^^^^

.. code-block:: python

   put(
       payload_dict=None,
       before=None,
       after=None,
       ssh_kex_algo=None,
       ssh_enc_algo=None,
       ssh_mac_algo=None,
       ssh_hsk_algo=None,
       ssh_hsk_override=None,
       ssh_hsk_password=None,
       ssh_hsk=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

