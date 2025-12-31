ChangeVdomMode
==============

Configuration endpoint for system/admin.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.admin

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.admin.post(
       vdom_mode='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       vdom_mode=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Switch between VDOM modes.

