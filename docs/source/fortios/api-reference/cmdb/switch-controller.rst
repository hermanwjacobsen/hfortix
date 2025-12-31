Switch Controller
=================

Configure ACL groups to be applied on managed FortiSwitch ports configuration and management.

Overview
--------

The ``cmdb.switch-controller`` category provides configuration management for:

- **802 1X Settings** - Configure global 802.1X settings.
- **Custom Command** - Configure the FortiGate switch controller to send custom commands to managed FortiSwitch devices.
- **Dynamic Port Policy** - Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
- **Flow Tracking** - Configure FortiSwitch flow tracking and export via ipfix/netflow.
- **Fortilink Settings** - Configure integrated FortiLink settings for FortiSwitch.
- **Global** - Configure FortiSwitch global settings.
- **Igmp Snooping** - Configure FortiSwitch IGMP snooping global settings.
- **Ip Source Guard Log** - Configure FortiSwitch ip source guard log.
- **Lldp Profile** - Configure FortiSwitch LLDP profiles.
- **Lldp Settings** - Configure FortiSwitch LLDP settings.
- **Location** - Configure FortiSwitch location services.
- **Mac Policy** - Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
- **Managed Switch** - Configure FortiSwitch devices that are managed by this FortiGate.
- **Network Monitor Settings** - Configure network monitor settings.
- **Remote Log** - Configure logging by FortiSwitch device to a remote syslog server.
- **Sflow** - Configure FortiSwitch sFlow.
- **Snmp Community** - Configure FortiSwitch SNMP v1/v2c communities globally.
- **Snmp Sysinfo** - Configure FortiSwitch SNMP system information globally.
- **Snmp Trap Threshold** - Configure FortiSwitch SNMP trap threshold values globally.
- **Snmp User** - Configure FortiSwitch SNMP v3 users globally.
- **Storm Control** - Configure FortiSwitch storm control.
- **Storm Control Policy** - Configure FortiSwitch storm control policy to be applied on managed-switch ports.
- **Stp Instance** - Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.
- **Stp Settings** - Configure FortiSwitch spanning tree protocol (STP).
- **Switch Group** - Configure FortiSwitch switch groups.
- **Switch Interface Tag** - Configure switch object tags.
- **Switch Log** - Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).
- **Switch Profile** - Configure FortiSwitch switch profile.
- **System** - Configure system-wide switch controller settings.
- **Traffic Policy** - Configure FortiSwitch traffic policy.
- **Traffic Sniffer** - Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
- **Virtual Port Pool** - Configure virtual pool.
- **Vlan Policy** - Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.switch-controller

Available Endpoints
-------------------

**802-1X-settings**
   Configure global 802.1X settings.
   
   .. code-block:: python
   
      # List all 802-1X-settings
      items = fgt.api.cmdb.switch-controller.802_1X_settings.get()
      
      # Get specific 802-1X-settings
      item = fgt.api.cmdb.switch-controller.802_1X_settings.get(mkey='name')

**custom-command**
   Configure the FortiGate switch controller to send custom commands to managed FortiSwitch devices.
   
   .. code-block:: python
   
      # List all custom-command
      items = fgt.api.cmdb.switch-controller.custom_command.get()
      
      # Get specific custom-command
      item = fgt.api.cmdb.switch-controller.custom_command.get(mkey='name')

**dynamic-port-policy**
   Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
   
   .. code-block:: python
   
      # List all dynamic-port-policy
      items = fgt.api.cmdb.switch-controller.dynamic_port_policy.get()
      
      # Get specific dynamic-port-policy
      item = fgt.api.cmdb.switch-controller.dynamic_port_policy.get(mkey='name')

**flow-tracking**
   Configure FortiSwitch flow tracking and export via ipfix/netflow.
   
   .. code-block:: python
   
      # List all flow-tracking
      items = fgt.api.cmdb.switch-controller.flow_tracking.get()
      
      # Get specific flow-tracking
      item = fgt.api.cmdb.switch-controller.flow_tracking.get(mkey='name')

**fortilink-settings**
   Configure integrated FortiLink settings for FortiSwitch.
   
   .. code-block:: python
   
      # List all fortilink-settings
      items = fgt.api.cmdb.switch-controller.fortilink_settings.get()
      
      # Get specific fortilink-settings
      item = fgt.api.cmdb.switch-controller.fortilink_settings.get(mkey='name')

**global**
   Configure FortiSwitch global settings.
   
   .. code-block:: python
   
      # List all global
      items = fgt.api.cmdb.switch-controller.global.get()
      
      # Get specific global
      item = fgt.api.cmdb.switch-controller.global.get(mkey='name')

**igmp-snooping**
   Configure FortiSwitch IGMP snooping global settings.
   
   .. code-block:: python
   
      # List all igmp-snooping
      items = fgt.api.cmdb.switch-controller.igmp_snooping.get()
      
      # Get specific igmp-snooping
      item = fgt.api.cmdb.switch-controller.igmp_snooping.get(mkey='name')

**ip-source-guard-log**
   Configure FortiSwitch ip source guard log.
   
   .. code-block:: python
   
      # List all ip-source-guard-log
      items = fgt.api.cmdb.switch-controller.ip_source_guard_log.get()
      
      # Get specific ip-source-guard-log
      item = fgt.api.cmdb.switch-controller.ip_source_guard_log.get(mkey='name')

**lldp-profile**
   Configure FortiSwitch LLDP profiles.
   
   .. code-block:: python
   
      # List all lldp-profile
      items = fgt.api.cmdb.switch-controller.lldp_profile.get()
      
      # Get specific lldp-profile
      item = fgt.api.cmdb.switch-controller.lldp_profile.get(mkey='name')

**lldp-settings**
   Configure FortiSwitch LLDP settings.
   
   .. code-block:: python
   
      # List all lldp-settings
      items = fgt.api.cmdb.switch-controller.lldp_settings.get()
      
      # Get specific lldp-settings
      item = fgt.api.cmdb.switch-controller.lldp_settings.get(mkey='name')

**location**
   Configure FortiSwitch location services.
   
   .. code-block:: python
   
      # List all location
      items = fgt.api.cmdb.switch-controller.location.get()
      
      # Get specific location
      item = fgt.api.cmdb.switch-controller.location.get(mkey='name')

**mac-policy**
   Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
   
   .. code-block:: python
   
      # List all mac-policy
      items = fgt.api.cmdb.switch-controller.mac_policy.get()
      
      # Get specific mac-policy
      item = fgt.api.cmdb.switch-controller.mac_policy.get(mkey='name')

**managed-switch**
   Configure FortiSwitch devices that are managed by this FortiGate.
   
   .. code-block:: python
   
      # List all managed-switch
      items = fgt.api.cmdb.switch-controller.managed_switch.get()
      
      # Get specific managed-switch
      item = fgt.api.cmdb.switch-controller.managed_switch.get(mkey='name')

**network-monitor-settings**
   Configure network monitor settings.
   
   .. code-block:: python
   
      # List all network-monitor-settings
      items = fgt.api.cmdb.switch-controller.network_monitor_settings.get()
      
      # Get specific network-monitor-settings
      item = fgt.api.cmdb.switch-controller.network_monitor_settings.get(mkey='name')

**remote-log**
   Configure logging by FortiSwitch device to a remote syslog server.
   
   .. code-block:: python
   
      # List all remote-log
      items = fgt.api.cmdb.switch-controller.remote_log.get()
      
      # Get specific remote-log
      item = fgt.api.cmdb.switch-controller.remote_log.get(mkey='name')

**sflow**
   Configure FortiSwitch sFlow.
   
   .. code-block:: python
   
      # List all sflow
      items = fgt.api.cmdb.switch-controller.sflow.get()
      
      # Get specific sflow
      item = fgt.api.cmdb.switch-controller.sflow.get(mkey='name')

**snmp-community**
   Configure FortiSwitch SNMP v1/v2c communities globally.
   
   .. code-block:: python
   
      # List all snmp-community
      items = fgt.api.cmdb.switch-controller.snmp_community.get()
      
      # Get specific snmp-community
      item = fgt.api.cmdb.switch-controller.snmp_community.get(mkey='name')

**snmp-sysinfo**
   Configure FortiSwitch SNMP system information globally.
   
   .. code-block:: python
   
      # List all snmp-sysinfo
      items = fgt.api.cmdb.switch-controller.snmp_sysinfo.get()
      
      # Get specific snmp-sysinfo
      item = fgt.api.cmdb.switch-controller.snmp_sysinfo.get(mkey='name')

**snmp-trap-threshold**
   Configure FortiSwitch SNMP trap threshold values globally.
   
   .. code-block:: python
   
      # List all snmp-trap-threshold
      items = fgt.api.cmdb.switch-controller.snmp_trap_threshold.get()
      
      # Get specific snmp-trap-threshold
      item = fgt.api.cmdb.switch-controller.snmp_trap_threshold.get(mkey='name')

**snmp-user**
   Configure FortiSwitch SNMP v3 users globally.
   
   .. code-block:: python
   
      # List all snmp-user
      items = fgt.api.cmdb.switch-controller.snmp_user.get()
      
      # Get specific snmp-user
      item = fgt.api.cmdb.switch-controller.snmp_user.get(mkey='name')

**storm-control**
   Configure FortiSwitch storm control.
   
   .. code-block:: python
   
      # List all storm-control
      items = fgt.api.cmdb.switch-controller.storm_control.get()
      
      # Get specific storm-control
      item = fgt.api.cmdb.switch-controller.storm_control.get(mkey='name')

**storm-control-policy**
   Configure FortiSwitch storm control policy to be applied on managed-switch ports.
   
   .. code-block:: python
   
      # List all storm-control-policy
      items = fgt.api.cmdb.switch-controller.storm_control_policy.get()
      
      # Get specific storm-control-policy
      item = fgt.api.cmdb.switch-controller.storm_control_policy.get(mkey='name')

**stp-instance**
   Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.
   
   .. code-block:: python
   
      # List all stp-instance
      items = fgt.api.cmdb.switch-controller.stp_instance.get()
      
      # Get specific stp-instance
      item = fgt.api.cmdb.switch-controller.stp_instance.get(mkey='name')

**stp-settings**
   Configure FortiSwitch spanning tree protocol (STP).
   
   .. code-block:: python
   
      # List all stp-settings
      items = fgt.api.cmdb.switch-controller.stp_settings.get()
      
      # Get specific stp-settings
      item = fgt.api.cmdb.switch-controller.stp_settings.get(mkey='name')

**switch-group**
   Configure FortiSwitch switch groups.
   
   .. code-block:: python
   
      # List all switch-group
      items = fgt.api.cmdb.switch-controller.switch_group.get()
      
      # Get specific switch-group
      item = fgt.api.cmdb.switch-controller.switch_group.get(mkey='name')

**switch-interface-tag**
   Configure switch object tags.
   
   .. code-block:: python
   
      # List all switch-interface-tag
      items = fgt.api.cmdb.switch-controller.switch_interface_tag.get()
      
      # Get specific switch-interface-tag
      item = fgt.api.cmdb.switch-controller.switch_interface_tag.get(mkey='name')

**switch-log**
   Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).
   
   .. code-block:: python
   
      # List all switch-log
      items = fgt.api.cmdb.switch-controller.switch_log.get()
      
      # Get specific switch-log
      item = fgt.api.cmdb.switch-controller.switch_log.get(mkey='name')

**switch-profile**
   Configure FortiSwitch switch profile.
   
   .. code-block:: python
   
      # List all switch-profile
      items = fgt.api.cmdb.switch-controller.switch_profile.get()
      
      # Get specific switch-profile
      item = fgt.api.cmdb.switch-controller.switch_profile.get(mkey='name')

**system**
   Configure system-wide switch controller settings.
   
   .. code-block:: python
   
      # List all system
      items = fgt.api.cmdb.switch-controller.system.get()
      
      # Get specific system
      item = fgt.api.cmdb.switch-controller.system.get(mkey='name')

**traffic-policy**
   Configure FortiSwitch traffic policy.
   
   .. code-block:: python
   
      # List all traffic-policy
      items = fgt.api.cmdb.switch-controller.traffic_policy.get()
      
      # Get specific traffic-policy
      item = fgt.api.cmdb.switch-controller.traffic_policy.get(mkey='name')

**traffic-sniffer**
   Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
   
   .. code-block:: python
   
      # List all traffic-sniffer
      items = fgt.api.cmdb.switch-controller.traffic_sniffer.get()
      
      # Get specific traffic-sniffer
      item = fgt.api.cmdb.switch-controller.traffic_sniffer.get(mkey='name')

**virtual-port-pool**
   Configure virtual pool.
   
   .. code-block:: python
   
      # List all virtual-port-pool
      items = fgt.api.cmdb.switch-controller.virtual_port_pool.get()
      
      # Get specific virtual-port-pool
      item = fgt.api.cmdb.switch-controller.virtual_port_pool.get(mkey='name')

**vlan-policy**
   Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.
   
   .. code-block:: python
   
      # List all vlan-policy
      items = fgt.api.cmdb.switch-controller.vlan_policy.get()
      
      # Get specific vlan-policy
      item = fgt.api.cmdb.switch-controller.vlan_policy.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.switch-controller.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.switch-controller.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.switch-controller.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.switch-controller.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.switch-controller.{endpoint}.delete(mkey='config-name')

HTTP Methods
------------

All CMDB endpoints support standard HTTP methods:

**.get()**
   HTTP GET - Retrieve configuration(s)

**.post()**
   HTTP POST - Create new configuration

**.put()**
   HTTP PUT - Update existing configuration

**.delete()**
   HTTP DELETE - Remove configuration

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
