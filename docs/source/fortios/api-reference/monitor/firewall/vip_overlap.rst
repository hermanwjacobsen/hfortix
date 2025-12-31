VipOverlap
==========

Configuration endpoint for firewall/vip_overlap.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.vip_overlap

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.firewall.vip_overlap.get()



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

List any Virtual IPs that overlap with another Virtual IP.

