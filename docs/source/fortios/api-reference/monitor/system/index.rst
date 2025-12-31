System
======

Overview
--------

The ``monitor.system`` namespace provides configuration management for:

- :doc:`3g Modem <3g_modem>` - 3g Modem configuration endpoint.
- :doc:`5g Modem <5g_modem>` - 5g Modem configuration endpoint.
- :doc:`Acme Certificate Status <acme_certificate_status>` - Acme Certificate Status configuration endpoint.
- :doc:`Acquired DNS <acquired_dns>` - Acquired DNS configuration endpoint.
- :doc:`Admin <admin>` - Admin configuration endpoint.
- :doc:`API User <api_user>` - API User configuration endpoint.
- :doc:`Automation Action <automation_action>` - Automation Action configuration endpoint.
- :doc:`Automation Stitch <automation_stitch>` - Automation Stitch configuration endpoint.
- :doc:`Available Certificates <available_certificates>` - Available Certificates configuration endpoint.
- :doc:`Available Interfaces <available_interfaces>` - Available Interfaces configuration endpoint.
- :doc:`Botnet <botnet>` - Botnet configuration endpoint.
- :doc:`Botnet Domains <botnet_domains>` - Botnet Domains configuration endpoint.
- :doc:`Central Management <central_management>` - Central Management configuration endpoint.
- :doc:`Certificate <certificate>` - Certificate configuration endpoint.
- :doc:`Change Password <change_password>` - Change Password configuration endpoint.
- :doc:`Check Port Availability <check_port_availability>` - Check Port Availability configuration endpoint.
- :doc:`Cluster <cluster>` - Cluster configuration endpoint.
- :doc:`Com Log <com_log>` - Com Log configuration endpoint.
- :doc:`Config <config>` - Config configuration endpoint.
- :doc:`Config Error Log <config_error_log>` - Config Error Log configuration endpoint.
- :doc:`Config Revision <config_revision>` - Config Revision configuration endpoint.
- :doc:`Config Script <config_script>` - Config Script configuration endpoint.
- :doc:`Config Sync <config_sync>` - Config Sync configuration endpoint.
- :doc:`Crash Log <crash_log>` - Crash Log configuration endpoint.
- :doc:`Csf <csf>` - Csf configuration endpoint.
- :doc:`Current Admins <current_admins>` - Current Admins configuration endpoint.
- :doc:`Debug <debug>` - Debug configuration endpoint.
- :doc:`DHCP <dhcp>` - DHCP configuration endpoint.
- :doc:`Dhcp6 <dhcp6>` - Dhcp6 configuration endpoint.
- :doc:`Disconnect Admins <disconnect_admins>` - Disconnect Admins configuration endpoint.
- :doc:`External Resource <external_resource>` - External Resource configuration endpoint.
- :doc:`Firmware <firmware>` - Firmware configuration endpoint.
- :doc:`Fortiguard <fortiguard>` - Fortiguard configuration endpoint.
- :doc:`Fortimanager <fortimanager>` - Fortimanager configuration endpoint.
- :doc:`Fsck <fsck>` - Fsck configuration endpoint.
- :doc:`Global Resources <global_resources>` - Global Resources configuration endpoint.
- :doc:`Global Search <global_search>` - Global Search configuration endpoint.
- :doc:`HA Backup Hb Used <ha_backup_hb_used>` - HA Backup Hb Used configuration endpoint.
- :doc:`HA Checksums <ha_checksums>` - HA Checksums configuration endpoint.
- :doc:`HA History <ha_history>` - HA History configuration endpoint.
- :doc:`HA Hw Interface <ha_hw_interface>` - HA Hw Interface configuration endpoint.
- :doc:`HA Nonsync Checksums <ha_nonsync_checksums>` - HA Nonsync Checksums configuration endpoint.
- :doc:`HA Peer <ha_peer>` - HA Peer configuration endpoint.
- :doc:`HA Statistics <ha_statistics>` - HA Statistics configuration endpoint.
- :doc:`HA Table Checksums <ha_table_checksums>` - HA Table Checksums configuration endpoint.
- :doc:`Hscalefw License <hscalefw_license>` - Hscalefw License configuration endpoint.
- :doc:`Interface <interface>` - Interface configuration endpoint.
- :doc:`Interface Connected Admins Info <interface_connected_admins_info>` - Interface Connected Admins Info configuration endpoint.
- :doc:`Ipam <ipam>` - Ipam configuration endpoint.
- :doc:`Ipconf <ipconf>` - Ipconf configuration endpoint.
- :doc:`Link Monitor <link_monitor>` - Link Monitor configuration endpoint.
- :doc:`Logdisk <logdisk>` - Logdisk configuration endpoint.
- :doc:`Lte Modem <lte_modem>` - Lte Modem configuration endpoint.
- :doc:`Modem <modem>` - Modem configuration endpoint.
- :doc:`Modem 3g <modem_3g>` - Modem 3g configuration endpoint.
- :doc:`Modem 5g <modem_5g>` - Modem 5g configuration endpoint.
- :doc:`Monitor Sensor <monitor_sensor>` - Monitor Sensor configuration endpoint.
- :doc:`NTP <ntp>` - NTP configuration endpoint.
- :doc:`Object <object>` - Object configuration endpoint.
- :doc:`Os <os>` - Os configuration endpoint.
- :doc:`Password Policy Conform <password_policy_conform>` - Password Policy Conform configuration endpoint.
- :doc:`Performance <performance>` - Performance configuration endpoint.
- :doc:`Private Data Encryption <private_data_encryption>` - Private Data Encryption configuration endpoint.
- :doc:`Process <process>` - Process configuration endpoint.
- :doc:`Resolve Fqdn <resolve_fqdn>` - Resolve Fqdn configuration endpoint.
- :doc:`Resource <resource>` - Resource configuration endpoint.
- :doc:`Running Processes <running_processes>` - Running Processes configuration endpoint.
- :doc:`Sandbox <sandbox>` - Sandbox configuration endpoint.
- :doc:`SDN Connector <sdn_connector>` - SDN Connector configuration endpoint.
- :doc:`Sensor Info <sensor_info>` - Sensor Info configuration endpoint.
- :doc:`Status <status>` - Status configuration endpoint.
- :doc:`Storage <storage>` - Storage configuration endpoint.
- :doc:`Time <time>` - Time configuration endpoint.
- :doc:`Timezone <timezone>` - Timezone configuration endpoint.
- :doc:`Traffic History <traffic_history>` - Traffic History configuration endpoint.
- :doc:`Trusted Cert Authorities <trusted_cert_authorities>` - Trusted Cert Authorities configuration endpoint.
- :doc:`Upgrade Report <upgrade_report>` - Upgrade Report configuration endpoint.
- :doc:`Usb Device <usb_device>` - Usb Device configuration endpoint.
- :doc:`Usb Log <usb_log>` - Usb Log configuration endpoint.
- :doc:`Vdom Link <vdom_link>` - Vdom Link configuration endpoint.
- :doc:`Vdom Resource <vdom_resource>` - Vdom Resource configuration endpoint.
- :doc:`Vm Information <vm_information>` - Vm Information configuration endpoint.
- :doc:`Vmlicense <vmlicense>` - Vmlicense configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.system.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   3g_modem
   5g_modem
   acme_certificate_status
   acquired_dns
   admin
   api_user
   automation_action
   automation_stitch
   available_certificates
   available_interfaces
   botnet
   botnet_domains
   central_management
   certificate
   change_password
   check_port_availability
   cluster
   com_log
   config
   config_error_log
   config_revision
   config_script
   config_sync
   crash_log
   csf
   current_admins
   debug
   dhcp
   dhcp6
   disconnect_admins
   external_resource
   firmware
   fortiguard
   fortimanager
   fsck
   global_resources
   global_search
   ha_backup_hb_used
   ha_checksums
   ha_history
   ha_hw_interface
   ha_nonsync_checksums
   ha_peer
   ha_statistics
   ha_table_checksums
   hscalefw_license
   interface
   interface_connected_admins_info
   ipam
   ipconf
   link_monitor
   logdisk
   lte_modem
   modem
   modem_3g
   modem_5g
   monitor_sensor
   ntp
   object
   os
   password_policy_conform
   performance
   private_data_encryption
   process
   resolve_fqdn
   resource
   running_processes
   sandbox
   sdn_connector
   sensor_info
   status
   storage
   time
   timezone
   traffic_history
   trusted_cert_authorities
   upgrade_report
   usb_device
   usb_log
   vdom_link
   vdom_resource
   vm_information
   vmlicense

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
