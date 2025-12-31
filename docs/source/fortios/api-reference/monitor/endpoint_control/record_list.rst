RecordList
==========

Configuration endpoint for endpoint_control/record_list.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.endpoint_control.record_list

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.endpoint_control.record_list.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       intf_name=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

List endpoint records.

