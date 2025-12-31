LanExtensionVdom
================

Configuration endpoint for extension_controller/lan_extension_vdom.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.extension_controller.lan_extension_vdom

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.extension_controller.lan_extension_vdom.get()



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

Get FortiGate LAN Extension VDOM status.

