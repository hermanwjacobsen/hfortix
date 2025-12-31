AutoInstall
===========

Configuration endpoint for system/auto_install.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.auto_install

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
   items = fgt.api.cmdb.system.auto_install.get()


   # Update existing item
   result = fgt.api.cmdb.system.auto_install.put(
       auto_install_config='updated-value',
       auto_install_image='updated-value',
       default_config_file='updated-value',
       default_image_file='updated-value',
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
       auto_install_config=None,
       auto_install_image=None,
       default_config_file=None,
       default_image_file=None,
       vdom=None,
       raw_json=False,
       **kwargs
   )

Update this specific resource.

