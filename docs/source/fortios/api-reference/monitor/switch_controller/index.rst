Switch Controller
=================

Overview
--------

The ``monitor.switch_controller`` namespace provides configuration management for:

- :doc:`Detected Device <detected_device>` - Detected Device configuration endpoint.
- :doc:`Fsw Firmware <fsw_firmware>` - Fsw Firmware configuration endpoint.
- :doc:`Isl Lockdown <isl_lockdown>` - Isl Lockdown configuration endpoint.
- :doc:`Known Nac Device Criteria List <known_nac_device_criteria_list>` - Known Nac Device Criteria List configuration endpoint.
- :doc:`Managed Switch <managed_switch>` - Managed Switch configuration endpoint.
- :doc:`Matched Devices <matched_devices>` - Matched Devices configuration endpoint.
- :doc:`Mclag Icl <mclag_icl>` - Mclag Icl configuration endpoint.
- :doc:`Nac Device <nac_device>` - Nac Device configuration endpoint.
- :doc:`Recommendation <recommendation>` - Recommendation configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.switch_controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   detected_device
   fsw_firmware
   isl_lockdown
   known_nac_device_criteria_list
   managed_switch
   matched_devices
   mclag_icl
   nac_device
   recommendation

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
