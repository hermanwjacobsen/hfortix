Switch Controller
=================

Configure ACL groups to be applied on managed FortiSwitch ports configuration and management.

Overview
--------

The ``cmdb.switch-controller`` category provides configuration management for:

- :ref:`802 1X Settings <switch-controller-802-1X-settings>` - Configure global 802.1X settings.
- :ref:`Custom Command <switch-controller-custom-command>` - Configure the FortiGate switch controller to send custom commands to managed FortiSwitch devices.
- :ref:`Dynamic Port Policy <switch-controller-dynamic-port-policy>` - Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
- :ref:`Flow Tracking <switch-controller-flow-tracking>` - Configure FortiSwitch flow tracking and export via ipfix/netflow.
- :ref:`Fortilink Settings <switch-controller-fortilink-settings>` - Configure integrated FortiLink settings for FortiSwitch.
- :ref:`Global <switch-controller-global>` - Configure FortiSwitch global settings.
- :ref:`Igmp Snooping <switch-controller-igmp-snooping>` - Configure FortiSwitch IGMP snooping global settings.
- :ref:`Ip Source Guard Log <switch-controller-ip-source-guard-log>` - Configure FortiSwitch ip source guard log.
- :ref:`Lldp Profile <switch-controller-lldp-profile>` - Configure FortiSwitch LLDP profiles.
- :ref:`Lldp Settings <switch-controller-lldp-settings>` - Configure FortiSwitch LLDP settings.
- :ref:`Location <switch-controller-location>` - Configure FortiSwitch location services.
- :ref:`Mac Policy <switch-controller-mac-policy>` - Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
- :ref:`Managed Switch <switch-controller-managed-switch>` - Configure FortiSwitch devices that are managed by this FortiGate.
- :ref:`Network Monitor Settings <switch-controller-network-monitor-settings>` - Configure network monitor settings.
- :ref:`Remote Log <switch-controller-remote-log>` - Configure logging by FortiSwitch device to a remote syslog server.
- :ref:`Sflow <switch-controller-sflow>` - Configure FortiSwitch sFlow.
- :ref:`Snmp Community <switch-controller-snmp-community>` - Configure FortiSwitch SNMP v1/v2c communities globally.
- :ref:`Snmp Sysinfo <switch-controller-snmp-sysinfo>` - Configure FortiSwitch SNMP system information globally.
- :ref:`Snmp Trap Threshold <switch-controller-snmp-trap-threshold>` - Configure FortiSwitch SNMP trap threshold values globally.
- :ref:`Snmp User <switch-controller-snmp-user>` - Configure FortiSwitch SNMP v3 users globally.
- :ref:`Storm Control <switch-controller-storm-control>` - Configure FortiSwitch storm control.
- :ref:`Storm Control Policy <switch-controller-storm-control-policy>` - Configure FortiSwitch storm control policy to be applied on managed-switch ports.
- :ref:`Stp Instance <switch-controller-stp-instance>` - Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.
- :ref:`Stp Settings <switch-controller-stp-settings>` - Configure FortiSwitch spanning tree protocol (STP).
- :ref:`Switch Group <switch-controller-switch-group>` - Configure FortiSwitch switch groups.
- :ref:`Switch Interface Tag <switch-controller-switch-interface-tag>` - Configure switch object tags.
- :ref:`Switch Log <switch-controller-switch-log>` - Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).
- :ref:`Switch Profile <switch-controller-switch-profile>` - Configure FortiSwitch switch profile.
- :ref:`System <switch-controller-system>` - Configure system-wide switch controller settings.
- :ref:`Traffic Policy <switch-controller-traffic-policy>` - Configure FortiSwitch traffic policy.
- :ref:`Traffic Sniffer <switch-controller-traffic-sniffer>` - Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
- :ref:`Virtual Port Pool <switch-controller-virtual-port-pool>` - Configure virtual pool.
- :ref:`Vlan Policy <switch-controller-vlan-policy>` - Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.switch-controller

Available Endpoints
-------------------

.. _switch-controller-802-1X-settings:

802-1X-settings
~~~~~~~~~~~~~~~

Configure global 802.1X settings.

**Python attribute:** ``802_1X_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.802_1X_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.802_1X_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.802_1X_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.802_1X_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.802_1X_settings.delete(mkey='item-name')

.. _switch-controller-custom-command:

custom-command
~~~~~~~~~~~~~~

Configure the FortiGate switch controller to send custom commands to managed FortiSwitch devices.

**Python attribute:** ``custom_command``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.custom_command.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.custom_command.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.custom_command.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.custom_command.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.custom_command.delete(mkey='item-name')

.. _switch-controller-dynamic-port-policy:

dynamic-port-policy
~~~~~~~~~~~~~~~~~~~

Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.

**Python attribute:** ``dynamic_port_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.dynamic_port_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.dynamic_port_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.dynamic_port_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.dynamic_port_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.dynamic_port_policy.delete(mkey='item-name')

.. _switch-controller-flow-tracking:

flow-tracking
~~~~~~~~~~~~~

Configure FortiSwitch flow tracking and export via ipfix/netflow.

**Python attribute:** ``flow_tracking``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.flow_tracking.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.flow_tracking.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.flow_tracking.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.flow_tracking.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.flow_tracking.delete(mkey='item-name')

.. _switch-controller-fortilink-settings:

fortilink-settings
~~~~~~~~~~~~~~~~~~

Configure integrated FortiLink settings for FortiSwitch.

**Python attribute:** ``fortilink_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.fortilink_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.fortilink_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.fortilink_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.fortilink_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.fortilink_settings.delete(mkey='item-name')

.. _switch-controller-global:

global
~~~~~~

Configure FortiSwitch global settings.

**Python attribute:** ``global``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.global.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.global.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.global.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.global.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.global.delete(mkey='item-name')

.. _switch-controller-igmp-snooping:

igmp-snooping
~~~~~~~~~~~~~

Configure FortiSwitch IGMP snooping global settings.

**Python attribute:** ``igmp_snooping``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.igmp_snooping.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.igmp_snooping.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.igmp_snooping.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.igmp_snooping.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.igmp_snooping.delete(mkey='item-name')

.. _switch-controller-ip-source-guard-log:

ip-source-guard-log
~~~~~~~~~~~~~~~~~~~

Configure FortiSwitch ip source guard log.

**Python attribute:** ``ip_source_guard_log``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.ip_source_guard_log.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.ip_source_guard_log.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.ip_source_guard_log.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.ip_source_guard_log.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.ip_source_guard_log.delete(mkey='item-name')

.. _switch-controller-lldp-profile:

lldp-profile
~~~~~~~~~~~~

Configure FortiSwitch LLDP profiles.

**Python attribute:** ``lldp_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.lldp_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.lldp_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.lldp_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.lldp_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.lldp_profile.delete(mkey='item-name')

.. _switch-controller-lldp-settings:

lldp-settings
~~~~~~~~~~~~~

Configure FortiSwitch LLDP settings.

**Python attribute:** ``lldp_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.lldp_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.lldp_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.lldp_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.lldp_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.lldp_settings.delete(mkey='item-name')

.. _switch-controller-location:

location
~~~~~~~~

Configure FortiSwitch location services.

**Python attribute:** ``location``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.location.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.location.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.location.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.location.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.location.delete(mkey='item-name')

.. _switch-controller-mac-policy:

mac-policy
~~~~~~~~~~

Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.

**Python attribute:** ``mac_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.mac_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.mac_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.mac_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.mac_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.mac_policy.delete(mkey='item-name')

.. _switch-controller-managed-switch:

managed-switch
~~~~~~~~~~~~~~

Configure FortiSwitch devices that are managed by this FortiGate.

**Python attribute:** ``managed_switch``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.managed_switch.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.managed_switch.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.managed_switch.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.managed_switch.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.managed_switch.delete(mkey='item-name')

.. _switch-controller-network-monitor-settings:

network-monitor-settings
~~~~~~~~~~~~~~~~~~~~~~~~

Configure network monitor settings.

**Python attribute:** ``network_monitor_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.network_monitor_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.network_monitor_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.network_monitor_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.network_monitor_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.network_monitor_settings.delete(mkey='item-name')

.. _switch-controller-remote-log:

remote-log
~~~~~~~~~~

Configure logging by FortiSwitch device to a remote syslog server.

**Python attribute:** ``remote_log``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.remote_log.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.remote_log.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.remote_log.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.remote_log.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.remote_log.delete(mkey='item-name')

.. _switch-controller-sflow:

sflow
~~~~~

Configure FortiSwitch sFlow.

**Python attribute:** ``sflow``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.sflow.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.sflow.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.sflow.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.sflow.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.sflow.delete(mkey='item-name')

.. _switch-controller-snmp-community:

snmp-community
~~~~~~~~~~~~~~

Configure FortiSwitch SNMP v1/v2c communities globally.

**Python attribute:** ``snmp_community``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.snmp_community.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.snmp_community.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.snmp_community.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.snmp_community.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.snmp_community.delete(mkey='item-name')

.. _switch-controller-snmp-sysinfo:

snmp-sysinfo
~~~~~~~~~~~~

Configure FortiSwitch SNMP system information globally.

**Python attribute:** ``snmp_sysinfo``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.snmp_sysinfo.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.snmp_sysinfo.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.snmp_sysinfo.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.snmp_sysinfo.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.snmp_sysinfo.delete(mkey='item-name')

.. _switch-controller-snmp-trap-threshold:

snmp-trap-threshold
~~~~~~~~~~~~~~~~~~~

Configure FortiSwitch SNMP trap threshold values globally.

**Python attribute:** ``snmp_trap_threshold``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.snmp_trap_threshold.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.snmp_trap_threshold.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.snmp_trap_threshold.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.snmp_trap_threshold.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.snmp_trap_threshold.delete(mkey='item-name')

.. _switch-controller-snmp-user:

snmp-user
~~~~~~~~~

Configure FortiSwitch SNMP v3 users globally.

**Python attribute:** ``snmp_user``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.snmp_user.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.snmp_user.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.snmp_user.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.snmp_user.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.snmp_user.delete(mkey='item-name')

.. _switch-controller-storm-control:

storm-control
~~~~~~~~~~~~~

Configure FortiSwitch storm control.

**Python attribute:** ``storm_control``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.storm_control.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.storm_control.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.storm_control.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.storm_control.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.storm_control.delete(mkey='item-name')

.. _switch-controller-storm-control-policy:

storm-control-policy
~~~~~~~~~~~~~~~~~~~~

Configure FortiSwitch storm control policy to be applied on managed-switch ports.

**Python attribute:** ``storm_control_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.storm_control_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.storm_control_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.storm_control_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.storm_control_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.storm_control_policy.delete(mkey='item-name')

.. _switch-controller-stp-instance:

stp-instance
~~~~~~~~~~~~

Configure FortiSwitch multiple spanning tree protocol (MSTP) instances.

**Python attribute:** ``stp_instance``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.stp_instance.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.stp_instance.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.stp_instance.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.stp_instance.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.stp_instance.delete(mkey='item-name')

.. _switch-controller-stp-settings:

stp-settings
~~~~~~~~~~~~

Configure FortiSwitch spanning tree protocol (STP).

**Python attribute:** ``stp_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.stp_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.stp_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.stp_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.stp_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.stp_settings.delete(mkey='item-name')

.. _switch-controller-switch-group:

switch-group
~~~~~~~~~~~~

Configure FortiSwitch switch groups.

**Python attribute:** ``switch_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.switch_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.switch_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.switch_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.switch_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.switch_group.delete(mkey='item-name')

.. _switch-controller-switch-interface-tag:

switch-interface-tag
~~~~~~~~~~~~~~~~~~~~

Configure switch object tags.

**Python attribute:** ``switch_interface_tag``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.switch_interface_tag.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.switch_interface_tag.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.switch_interface_tag.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.switch_interface_tag.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.switch_interface_tag.delete(mkey='item-name')

.. _switch-controller-switch-log:

switch-log
~~~~~~~~~~

Configure FortiSwitch logging (logs are transferred to and inserted into FortiGate event log).

**Python attribute:** ``switch_log``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.switch_log.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.switch_log.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.switch_log.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.switch_log.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.switch_log.delete(mkey='item-name')

.. _switch-controller-switch-profile:

switch-profile
~~~~~~~~~~~~~~

Configure FortiSwitch switch profile.

**Python attribute:** ``switch_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.switch_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.switch_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.switch_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.switch_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.switch_profile.delete(mkey='item-name')

.. _switch-controller-system:

system
~~~~~~

Configure system-wide switch controller settings.

**Python attribute:** ``system``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.system.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.system.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.system.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.system.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.system.delete(mkey='item-name')

.. _switch-controller-traffic-policy:

traffic-policy
~~~~~~~~~~~~~~

Configure FortiSwitch traffic policy.

**Python attribute:** ``traffic_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.traffic_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.traffic_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.traffic_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.traffic_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.traffic_policy.delete(mkey='item-name')

.. _switch-controller-traffic-sniffer:

traffic-sniffer
~~~~~~~~~~~~~~~

Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.

**Python attribute:** ``traffic_sniffer``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.traffic_sniffer.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.traffic_sniffer.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.traffic_sniffer.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.traffic_sniffer.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.traffic_sniffer.delete(mkey='item-name')

.. _switch-controller-virtual-port-pool:

virtual-port-pool
~~~~~~~~~~~~~~~~~

Configure virtual pool.

**Python attribute:** ``virtual_port_pool``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.virtual_port_pool.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.virtual_port_pool.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.virtual_port_pool.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.virtual_port_pool.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.virtual_port_pool.delete(mkey='item-name')

.. _switch-controller-vlan-policy:

vlan-policy
~~~~~~~~~~~

Configure VLAN policy to be applied on the managed FortiSwitch ports through dynamic-port-policy.

**Python attribute:** ``vlan_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.switch-controller.vlan_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.switch-controller.vlan_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.switch-controller.vlan_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.switch-controller.vlan_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.switch-controller.vlan_policy.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.switch-controller.802_1X_settings.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.switch-controller.802_1X_settings.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.switch-controller.802_1X_settings.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.switch-controller.802_1X_settings.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.switch-controller.802_1X_settings.delete(mkey='config-name')

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
