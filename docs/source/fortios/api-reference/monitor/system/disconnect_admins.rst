Select
======

Configuration endpoint for system/disconnect_admins.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.disconnect_admins

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.disconnect_admins.post(
       id='value',  # optional
       method='value',  # optional
       admins='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       id=None,
       method=None,
       admins=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Disconnects logged in administrators.

