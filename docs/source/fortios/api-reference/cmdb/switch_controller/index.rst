Switch Controller
=================

Overview
--------

The ``cmdb.switch_controller`` namespace provides configuration management for:

- :doc:`802 1x Settings <_802_1X_settings>` - 802 1x Settings configuration endpoint.
- :doc:`Acl Group <acl_group>` - Acl Group configuration endpoint.
- :doc:`Acl Ingress <acl_ingress>` - Acl Ingress configuration endpoint.
- :doc:`Auto Config Custom <auto_config_custom>` - Auto Config Custom configuration endpoint.
- :doc:`Auto Config Default <auto_config_default>` - Auto Config Default configuration endpoint.
- :doc:`Auto Config Policy <auto_config_policy>` - Auto Config Policy configuration endpoint.
- :doc:`Custom Command <custom_command>` - Custom Command configuration endpoint.
- :doc:`Dynamic Port Policy <dynamic_port_policy>` - Dynamic Port Policy configuration endpoint.
- :doc:`Flow Tracking <flow_tracking>` - Flow Tracking configuration endpoint.
- :doc:`Fortilink Settings <fortilink_settings>` - Fortilink Settings configuration endpoint.
- :doc:`Global <global_>` - Global configuration endpoint.
- :doc:`Igmp Snooping <igmp_snooping>` - Igmp Snooping configuration endpoint.
- :doc:`Initial Config Template <initial_config_template>` - Initial Config Template configuration endpoint.
- :doc:`Initial Config Vlans <initial_config_vlans>` - Initial Config Vlans configuration endpoint.
- :doc:`IP Source Guard Log <ip_source_guard_log>` - IP Source Guard Log configuration endpoint.
- :doc:`Lldp Profile <lldp_profile>` - Lldp Profile configuration endpoint.
- :doc:`Lldp Settings <lldp_settings>` - Lldp Settings configuration endpoint.
- :doc:`Location <location>` - Location configuration endpoint.
- :doc:`Mac Policy <mac_policy>` - Mac Policy configuration endpoint.
- :doc:`Managed Switch <managed_switch>` - Managed Switch configuration endpoint.
- :doc:`Network Monitor Settings <network_monitor_settings>` - Network Monitor Settings configuration endpoint.
- :doc:`Ptp Interface Policy <ptp_interface_policy>` - Ptp Interface Policy configuration endpoint.
- :doc:`Ptp Profile <ptp_profile>` - Ptp Profile configuration endpoint.
- :doc:`Qos Dot1p Map <qos_dot1p_map>` - Qos Dot1p Map configuration endpoint.
- :doc:`Qos IP Dscp Map <qos_ip_dscp_map>` - Qos IP Dscp Map configuration endpoint.
- :doc:`Qos Qos Policy <qos_qos_policy>` - Qos Qos Policy configuration endpoint.
- :doc:`Qos Queue Policy <qos_queue_policy>` - Qos Queue Policy configuration endpoint.
- :doc:`Remote Log <remote_log>` - Remote Log configuration endpoint.
- :doc:`Security Policy 802 1x <security_policy__802_1X>` - Security Policy 802 1x configuration endpoint.
- :doc:`Security Policy Local Access <security_policy_local_access>` - Security Policy Local Access configuration endpoint.
- :doc:`Sflow <sflow>` - Sflow configuration endpoint.
- :doc:`SNMP Community <snmp_community>` - SNMP Community configuration endpoint.
- :doc:`SNMP Sysinfo <snmp_sysinfo>` - SNMP Sysinfo configuration endpoint.
- :doc:`SNMP Trap Threshold <snmp_trap_threshold>` - SNMP Trap Threshold configuration endpoint.
- :doc:`SNMP User <snmp_user>` - SNMP User configuration endpoint.
- :doc:`Storm Control <storm_control>` - Storm Control configuration endpoint.
- :doc:`Storm Control Policy <storm_control_policy>` - Storm Control Policy configuration endpoint.
- :doc:`Stp Instance <stp_instance>` - Stp Instance configuration endpoint.
- :doc:`Stp Settings <stp_settings>` - Stp Settings configuration endpoint.
- :doc:`Switch Group <switch_group>` - Switch Group configuration endpoint.
- :doc:`Switch Interface Tag <switch_interface_tag>` - Switch Interface Tag configuration endpoint.
- :doc:`Switch Log <switch_log>` - Switch Log configuration endpoint.
- :doc:`Switch Profile <switch_profile>` - Switch Profile configuration endpoint.
- :doc:`System <system>` - System configuration endpoint.
- :doc:`Traffic Policy <traffic_policy>` - Traffic Policy configuration endpoint.
- :doc:`Traffic Sniffer <traffic_sniffer>` - Traffic Sniffer configuration endpoint.
- :doc:`Virtual Port Pool <virtual_port_pool>` - Virtual Port Pool configuration endpoint.
- :doc:`Vlan Policy <vlan_policy>` - Vlan Policy configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.switch_controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   _802_1X_settings
   acl_group
   acl_ingress
   auto_config_custom
   auto_config_default
   auto_config_policy
   custom_command
   dynamic_port_policy
   flow_tracking
   fortilink_settings
   global_
   igmp_snooping
   initial_config_template
   initial_config_vlans
   ip_source_guard_log
   lldp_profile
   lldp_settings
   location
   mac_policy
   managed_switch
   network_monitor_settings
   ptp_interface_policy
   ptp_profile
   qos_dot1p_map
   qos_ip_dscp_map
   qos_qos_policy
   qos_queue_policy
   remote_log
   security_policy__802_1X
   security_policy_local_access
   sflow
   snmp_community
   snmp_sysinfo
   snmp_trap_threshold
   snmp_user
   storm_control
   storm_control_policy
   stp_instance
   stp_settings
   switch_group
   switch_interface_tag
   switch_log
   switch_profile
   system
   traffic_policy
   traffic_sniffer
   virtual_port_pool
   vlan_policy

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
