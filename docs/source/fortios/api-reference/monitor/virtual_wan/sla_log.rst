SlaLog
======

Configuration endpoint for virtual_wan/sla_log.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.virtual_wan.sla_log

Available Methods
-----------------

- ``get()`` - GET operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # List all items
   items = fgt.api.monitor.virtual_wan.sla_log.get()



Method Reference
----------------

``get()``
^^^^^^^

.. code-block:: python

   get(
       sla=None,
       interface=None,
       since=None,
       seconds=None,
       latest=None,
       min_sample_interval=None,
       sampling_interval=None,
       skip_vpn_child=None,
       include_sla_targets_met=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Retrieve logs of SLA probe results for the specified SD-WAN SLA or

