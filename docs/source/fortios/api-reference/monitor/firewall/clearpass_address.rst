Add
===

Configuration endpoint for firewall/clearpass_address.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.clearpass_address

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.clearpass_address.post(
       endpoint_ip='value',  # optional
       spt='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       endpoint_ip=None,
       spt=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Add ClearPass address with SPT (System Posture Token) value.

