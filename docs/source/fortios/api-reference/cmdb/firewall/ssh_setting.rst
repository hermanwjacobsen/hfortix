SshSetting
==========

Configuration endpoint for firewall/ssh_setting.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.firewall.ssh_setting

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
   items = fgt.api.cmdb.firewall.ssh_setting.get()


   # Update existing item
   result = fgt.api.cmdb.firewall.ssh_setting.put(
       caname='updated-value',
       untrusted_caname='updated-value',
       hostkey_rsa2048='updated-value',
       hostkey_dsa1024='updated-value',
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
       caname=None,
       untrusted_caname=None,
       hostkey_rsa2048=None,
       hostkey_dsa1024=None,
       hostkey_ecdsa256=None,
       hostkey_ecdsa384=None,
       hostkey_ecdsa521=None,
       hostkey_ed25519=None,
       host_trusted_checking=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

