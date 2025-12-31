ClearCounters
=============

Configuration endpoint for firewall/policy.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.firewall.policy

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.firewall.policy.post(
       policy='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       policy=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Reset traffic statistics for one or more firewall policies by policy

