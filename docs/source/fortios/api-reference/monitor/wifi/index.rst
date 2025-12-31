Wifi
====

Overview
--------

The ``monitor.wifi`` namespace provides configuration management for:

- :doc:`Ap Channels <ap_channels>` - Ap Channels configuration endpoint.
- :doc:`Ap Names <ap_names>` - Ap Names configuration endpoint.
- :doc:`Ap Profile <ap_profile>` - Ap Profile configuration endpoint.
- :doc:`Ap Status <ap_status>` - Ap Status configuration endpoint.
- :doc:`Client <client>` - Client configuration endpoint.
- :doc:`Euclid <euclid>` - Euclid configuration endpoint.
- :doc:`Firmware <firmware>` - Firmware configuration endpoint.
- :doc:`Interfering Ap <interfering_ap>` - Interfering Ap configuration endpoint.
- :doc:`Managed Ap <managed_ap>` - Managed Ap configuration endpoint.
- :doc:`Matched Devices <matched_devices>` - Matched Devices configuration endpoint.
- :doc:`Meta <meta>` - Meta configuration endpoint.
- :doc:`Nac Device <nac_device>` - Nac Device configuration endpoint.
- :doc:`Network <network>` - Network configuration endpoint.
- :doc:`Region Image <region_image>` - Region Image configuration endpoint.
- :doc:`Rogue Ap <rogue_ap>` - Rogue Ap configuration endpoint.
- :doc:`Spectrum <spectrum>` - Spectrum configuration endpoint.
- :doc:`Ssid <ssid>` - Ssid configuration endpoint.
- :doc:`Station Capability <station_capability>` - Station Capability configuration endpoint.
- :doc:`Statistics <statistics>` - Statistics configuration endpoint.
- :doc:`Unassociated Devices <unassociated_devices>` - Unassociated Devices configuration endpoint.
- :doc:`Vlan Probe <vlan_probe>` - Vlan Probe configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.wifi.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   ap_channels
   ap_names
   ap_profile
   ap_status
   client
   euclid
   firmware
   interfering_ap
   managed_ap
   matched_devices
   meta
   nac_device
   network
   region_image
   rogue_ap
   spectrum
   ssid
   station_capability
   statistics
   unassociated_devices
   vlan_probe

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
