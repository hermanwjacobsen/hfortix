Start
=====

Configuration endpoint for wifi/vlan_probe.

Python Attribute
----------------

.. code-block:: python

   fgt.api.monitor.wifi.vlan_probe

Available Methods
-----------------

- ``post()`` - POST operation

Examples
--------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')

   # Create new item
   result = fgt.api.monitor.wifi.vlan_probe.post(
       ap_interface='value',  # optional
       wtp='value',  # optional
       start_vlan_id='value',  # optional
   )


Method Reference
----------------

``post()``
^^^^^^^^

.. code-block:: python

   post(
       ap_interface=None,
       wtp=None,
       start_vlan_id=None,
       end_vlan_id=None,
       retries=None,
       timeout=None,
       payload_dict=None,
       raw_json=False,
       **kwargs
   )

Start a VLAN probe.

