Delete
======

Configuration endpoint for system/config_revision.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.config_revision

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.config_revision.post(
       config_ids='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       config_ids=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Deletes one or more system configuration revisions.

