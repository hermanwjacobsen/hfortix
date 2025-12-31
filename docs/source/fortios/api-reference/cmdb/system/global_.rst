Global
======

Configuration endpoint for system/global_.

Python Attribute
----------------

.. code-block:: python

   fgt.api.cmdb.system.global_

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
   items = fgt.api.cmdb.system.global_.get()


   # Update existing item
   result = fgt.api.cmdb.system.global_.put(
       language='updated-value',
       gui_allow_incompatible_fabric_fgt='updated-value',
       gui_ipv6='updated-value',
       gui_replacement_message_groups='updated-value',
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
       language=None,
       gui_allow_incompatible_fabric_fgt=None,
       gui_ipv6=None,
       gui_replacement_message_groups=None,
       gui_local_out=None,
       gui_certificates=None,
       gui_custom_language=None,
       gui_wireless_opensecurity=None,
       gui_app_detection_sdwan=None,
       gui_display_hostname=None,
       gui_fortigate_cloud_sandbox=None,
       gui_firmware_upgrade_warning=None,
       # ... more parameters
   )

Update this specific resource.

