Switch Controller
=================

Configure ACL groups to be applied on managed FortiSwitch ports configuration and management.

Overview
--------

The ``cmdb.switch-controller`` category provides configuration management for:

- :doc:`802 1X Settings <802-1X-settings>` - Configure global 802.1X settings.
- :doc:`Custom Command <custom-command>` - Configure the FortiGate switch controller to send custom commands to managed FortiSwitch devices.
- :doc:`Dynamic Port Policy <dynamic-port-policy>` - Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
- :doc:`Flow Tracking <flow-tracking>` - Configure FortiSwitch flow tracking and export via ipfix/netflow.
- :doc:`Fortilink Settings <fortilink-settings>` - Configure integrated FortiLink settings for FortiSwitch.
- :doc:`Global <global>` - Configure FortiSwitch global settings.
- :doc:`Igmp Snooping <igmp-snooping>` - Configure FortiSwitch IGMP snooping global settings.
- :doc:`Ip Source Guard Log <ip-source-guard-log>` - Configure FortiSwitch ip source guard log.
- :doc:`Lldp Profile <lldp-profile>` - Configure FortiSwitch LLDP profiles.
- :doc:`Lldp Settings <lldp-settings>` - Configure FortiSwitch LLDP settings.
- :doc:`Location <location>` - Configure FortiSwitch location services.
- :doc:`Mac Policy <mac-policy>` - Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
- :doc:`Managed Switch <managed-switch>` - Configure FortiSwitch devices that are managed by this FortiGate.
- :doc:`Network Monitor Settings <network-monitor-settings>` - Configure network monitor settings.
- :doc:`Remote Log <remote-log>` - Configure logging by FortiSwitch device to a remote syslog server.
- :doc:`Sflow <sflow>` - Configure FortiSwitch sFlow.
- :doc:`Snmp Community <snmp-community>` - Configure FortiSwitch SNMP v1/v2c communities globally.
- :doc:`Snmp Sysinfo <snmp-sysinfo>` - Configure FortiSwitch SNMP system information globally.
- :doc:`Snmp Trap Threshold <snmp-trap-threshold>` - Configure FortiSwitch SNMP trap threshold values globally.
- :doc:`Snmp User <snmp-user>` - Configure FortiSwitch SNMP v3 users globally.
- :doc:`Storm Control <storm-control>` - Configure FortiSwitch storm control.
- :doc:`Storm Control Policy <storm-control-policy>` - Configure FortiSwitch storm control policy to be applied on managed-switch ports.
- :doc:`Stp Instance <stp-instance>` - Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.
- :doc:`Stp Settings <stp-settings>` - Configure FortiSwitch spanning tree protocol (STP).
- :doc:`Switch Group <switch-group>` - Configure FortiSwitch switch groups.
- :doc:`Switch Interface Tag <switch-interface-tag>` - Configure switch object tags.
- :doc:`Switch Log <switch-log>` - Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).
- :doc:`Switch Profile <switch-profile>` - Configure FortiSwitch switch profile.
- :doc:`System <system>` - Configure system-wide switch controller settings.
- :doc:`Traffic Policy <traffic-policy>` - Configure FortiSwitch traffic policy.
- :doc:`Traffic Sniffer <traffic-sniffer>` - Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
- :doc:`Virtual Port Pool <virtual-port-pool>` - Configure virtual pool.
- :doc:`Vlan Policy <vlan-policy>` - Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.switch-controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   802-1X-settings
   custom-command
   dynamic-port-policy
   flow-tracking
   fortilink-settings
   global
   igmp-snooping
   ip-source-guard-log
   lldp-profile
   lldp-settings
   location
   mac-policy
   managed-switch
   network-monitor-settings
   remote-log
   sflow
   snmp-community
   snmp-sysinfo
   snmp-trap-threshold
   snmp-user
   storm-control
   storm-control-policy
   stp-instance
   stp-settings
   switch-group
   switch-interface-tag
   switch-log
   switch-profile
   system
   traffic-policy
   traffic-sniffer
   virtual-port-pool
   vlan-policy

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
