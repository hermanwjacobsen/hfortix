Delete
======

Configuration endpoint for system/config_script.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.system.config_script

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.system.config_script.post(
       id_list='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       id_list=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Delete the history of config scripts.

