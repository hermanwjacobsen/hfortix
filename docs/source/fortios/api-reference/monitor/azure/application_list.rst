Refresh
=======

Configuration endpoint for azure/application_list.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.azure.application_list

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.azure.application_list.post(
       last_update_time='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       last_update_time=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Update the Azure application list data or get the status of an update.

