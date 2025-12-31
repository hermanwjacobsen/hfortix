System
======

3G MODEM custom configuration and management.

Overview
--------

The ``cmdb.system`` category provides configuration management for:

- **Accprofile** - Configure access profiles for system administrators.
- **Acme** - Configure ACME client.
- **Admin** - Configure admin users.
- **Affinity Interrupt** - Configure interrupt affinity.
- **Affinity Packet Redistribution** - Configure packet redistribution.
- **Alarm** - Configure alarm.
- **Alias** - Configure alias command.
- **Api User** - Configure API users.
- **Arp Table** - Configure ARP table.
- **Auto Install** - Configure USB auto installation.
- **Auto Script** - Configure auto script.
- **Automation Action** - Action for automation stitches.
- **Automation Condition** - Condition for automation stitches.
- **Automation Destination** - Automation destinations.
- **Automation Stitch** - Automation stitches.
- **Automation Trigger** - Trigger for automation stitches.
- **Central Management** - Configure central management.
- **Cloud Service** - Configure system cloud service.
- **Console** - Configure console.
- **Csf** - Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
- **Custom Language** - Configure custom languages.
- **Ddns** - Configure DDNS.
- **Dedicated Mgmt** - Configure dedicated management.
- **Device Upgrade** - Independent upgrades for managed devices.
- **Device Upgrade Exemptions** - Configure device upgrade exemptions. Device will stop receiving upgrade notifications on the GUI.
- **Dns** - Configure DNS.
- **Dns Database** - Configure DNS databases.
- **Dns Server** - Configure DNS servers.
- **Dns64** - Configure DNS64.
- **Dscp Based Priority** - Configure DSCP based priority table.
- **Email Server** - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
- **Evpn** - Configure EVPN instance.
- **External Resource** - Configure external resource.
- **Fabric Vpn** - Setup for self orchestrated fabric auto discovery VPN.
- **Federated Upgrade** - Coordinate federated upgrades within the Security Fabric.
- **Fips Cc** - Configure FIPS-CC mode.
- **Fortiguard** - Configure FortiGuard services.
- **Fortisandbox** - Configure FortiSandbox.
- **Fsso Polling** - Configure Fortinet Single Sign On (FSSO) server.
- **Ftm Push** - Configure FortiToken Mobile push services.
- **Geneve** - Configure GENEVE devices.
- **Geoip Country** - Define geoip country name-ID table.
- **Geoip Override** - Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
- **Global** - Configure global attributes.
- **Gre Tunnel** - Configure GRE tunnel.
- **Ha** - Configure HA.
- **Ha Monitor** - Configure HA monitor.
- **Health Check Fortiguard** - SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
- **Ike** - Configure IKE global attributes.
- **Interface** - Configure interfaces.
- **Ipam** - Configure IP address management services.
- **Ipip Tunnel** - Configure IP in IP Tunneling.
- **Ips** - Configure IPS system settings.
- **Ips Urlfilter Dns** - Configure IPS URL filter DNS servers.
- **Ips Urlfilter Dns6** - Configure IPS URL filter IPv6 DNS servers.
- **Ipsec Aggregate** - Configure an aggregate of IPsec tunnels.
- **Ipv6 Neighbor Cache** - Configure IPv6 neighbor cache table.
- **Ipv6 Tunnel** - Configure IPv6/IPv4 in IPv6 tunnel.
- **Link Monitor** - Configure Link Health Monitor.
- **Lte Modem** - Configure USB LTE/WIMAX devices.
- **Mac Address Table** - Configure MAC address tables.
- **Mobile Tunnel** - Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
- **Modem** - Configure MODEM.
- **Nd Proxy** - Configure IPv6 neighbor discovery proxy (RFC4389).
- **Netflow** - Configure NetFlow.
- **Network Visibility** - Configure network visibility settings.
- **Ngfw Settings** - Configure IPS NGFW policy-mode VDOM settings.
- **Np6Xlite** - Configure NP6XLITE attributes.
- **Npu** - Configure NPU attributes.
- **Ntp** - Configure system NTP information.
- **Object Tagging** - Configure object tagging.
- **Password Policy** - Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
- **Password Policy Guest Admin** - Configure the password policy for guest administrators.
- **Pcp Server** - Configure PCP server information.
- **Physical Switch** - Configure physical switches.
- **Pppoe Interface** - Configure the PPPoE interfaces.
- **Probe Response** - Configure system probe response.
- **Proxy Arp** - Configure proxy-ARP.
- **Ptp** - Configure system PTP information.
- **Replacemsg Group** - Configure replacement message groups.
- **Replacemsg Image** - Configure replacement message images.
- **Resource Limits** - Configure resource limits.
- **Saml** - Global settings for SAML authentication.
- **Sdn Connector** - Configure connection to SDN Connector.
- **Sdn Proxy** - Configure SDN proxy.
- **Sdn Vpn** - Configure public cloud VPN service.
- **Sdwan** - Configure redundant Internet connections with multiple outbound links and health-check profiles.
- **Session Helper** - Configure session helper.
- **Session Ttl** - Configure global session TTL timers for this FortiGate.
- **Settings** - Configure VDOM settings.
- **Sflow** - Configure sFlow.
- **Sit Tunnel** - Configure IPv6 tunnel over IPv4.
- **Sms Server** - Configure SMS server for sending SMS messages to support user authentication.
- **Sov Sase** - Configure Sovereign SASE.
- **Speed Test Schedule** - Speed test schedule for each interface.
- **Speed Test Server** - Configure speed test server list.
- **Speed Test Setting** - Configure speed test setting.
- **Ssh Config** - Configure SSH config.
- **Sso Admin** - Configure SSO admin users.
- **Sso Forticloud Admin** - Configure FortiCloud SSO admin users.
- **Sso Fortigate Cloud Admin** - Configure FortiCloud SSO admin users.
- **Standalone Cluster** - Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
- **Storage** - Configure logical storage.
- **Stp** - Configure Spanning Tree Protocol (STP).
- **Switch Interface** - Configure software switch interfaces by grouping physical and WiFi interfaces.
- **Timezone** - Show timezone.
- **Tos Based Priority** - Configure Type of Service (ToS) based priority table to set network traffic priorities.
- **Vdom** - Configure virtual domain.
- **Vdom Dns** - Configure DNS servers for a non-management VDOM.
- **Vdom Exception** - Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
- **Vdom Link** - Configure VDOM links.
- **Vdom Netflow** - Configure NetFlow per VDOM.
- **Vdom Property** - Configure VDOM property.
- **Vdom Radius Server** - Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.
- **Vdom Sflow** - Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.
- **Virtual Switch** - Configure virtual hardware switch interfaces.
- **Virtual Wire Pair** - Configure virtual wire pairs.
- **Vne Interface** - Configure virtual network enabler tunnels.
- **Vxlan** - Configure VXLAN devices.
- **Wccp** - Configure WCCP.
- **Zone** - Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead of individual interfaces in the zone.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.system

Available Endpoints
-------------------

**accprofile**
   Configure access profiles for system administrators.
   
   .. code-block:: python
   
      # List all accprofile
      items = fgt.api.cmdb.system.accprofile.get()
      
      # Get specific accprofile
      item = fgt.api.cmdb.system.accprofile.get(mkey='name')

**acme**
   Configure ACME client.
   
   .. code-block:: python
   
      # List all acme
      items = fgt.api.cmdb.system.acme.get()
      
      # Get specific acme
      item = fgt.api.cmdb.system.acme.get(mkey='name')

**admin**
   Configure admin users.
   
   .. code-block:: python
   
      # List all admin
      items = fgt.api.cmdb.system.admin.get()
      
      # Get specific admin
      item = fgt.api.cmdb.system.admin.get(mkey='name')

**affinity-interrupt**
   Configure interrupt affinity.
   
   .. code-block:: python
   
      # List all affinity-interrupt
      items = fgt.api.cmdb.system.affinity_interrupt.get()
      
      # Get specific affinity-interrupt
      item = fgt.api.cmdb.system.affinity_interrupt.get(mkey='name')

**affinity-packet-redistribution**
   Configure packet redistribution.
   
   .. code-block:: python
   
      # List all affinity-packet-redistribution
      items = fgt.api.cmdb.system.affinity_packet_redistribution.get()
      
      # Get specific affinity-packet-redistribution
      item = fgt.api.cmdb.system.affinity_packet_redistribution.get(mkey='name')

**alarm**
   Configure alarm.
   
   .. code-block:: python
   
      # List all alarm
      items = fgt.api.cmdb.system.alarm.get()
      
      # Get specific alarm
      item = fgt.api.cmdb.system.alarm.get(mkey='name')

**alias**
   Configure alias command.
   
   .. code-block:: python
   
      # List all alias
      items = fgt.api.cmdb.system.alias.get()
      
      # Get specific alias
      item = fgt.api.cmdb.system.alias.get(mkey='name')

**api-user**
   Configure API users.
   
   .. code-block:: python
   
      # List all api-user
      items = fgt.api.cmdb.system.api_user.get()
      
      # Get specific api-user
      item = fgt.api.cmdb.system.api_user.get(mkey='name')

**arp-table**
   Configure ARP table.
   
   .. code-block:: python
   
      # List all arp-table
      items = fgt.api.cmdb.system.arp_table.get()
      
      # Get specific arp-table
      item = fgt.api.cmdb.system.arp_table.get(mkey='name')

**auto-install**
   Configure USB auto installation.
   
   .. code-block:: python
   
      # List all auto-install
      items = fgt.api.cmdb.system.auto_install.get()
      
      # Get specific auto-install
      item = fgt.api.cmdb.system.auto_install.get(mkey='name')

**auto-script**
   Configure auto script.
   
   .. code-block:: python
   
      # List all auto-script
      items = fgt.api.cmdb.system.auto_script.get()
      
      # Get specific auto-script
      item = fgt.api.cmdb.system.auto_script.get(mkey='name')

**automation-action**
   Action for automation stitches.
   
   .. code-block:: python
   
      # List all automation-action
      items = fgt.api.cmdb.system.automation_action.get()
      
      # Get specific automation-action
      item = fgt.api.cmdb.system.automation_action.get(mkey='name')

**automation-condition**
   Condition for automation stitches.
   
   .. code-block:: python
   
      # List all automation-condition
      items = fgt.api.cmdb.system.automation_condition.get()
      
      # Get specific automation-condition
      item = fgt.api.cmdb.system.automation_condition.get(mkey='name')

**automation-destination**
   Automation destinations.
   
   .. code-block:: python
   
      # List all automation-destination
      items = fgt.api.cmdb.system.automation_destination.get()
      
      # Get specific automation-destination
      item = fgt.api.cmdb.system.automation_destination.get(mkey='name')

**automation-stitch**
   Automation stitches.
   
   .. code-block:: python
   
      # List all automation-stitch
      items = fgt.api.cmdb.system.automation_stitch.get()
      
      # Get specific automation-stitch
      item = fgt.api.cmdb.system.automation_stitch.get(mkey='name')

**automation-trigger**
   Trigger for automation stitches.
   
   .. code-block:: python
   
      # List all automation-trigger
      items = fgt.api.cmdb.system.automation_trigger.get()
      
      # Get specific automation-trigger
      item = fgt.api.cmdb.system.automation_trigger.get(mkey='name')

**central-management**
   Configure central management.
   
   .. code-block:: python
   
      # List all central-management
      items = fgt.api.cmdb.system.central_management.get()
      
      # Get specific central-management
      item = fgt.api.cmdb.system.central_management.get(mkey='name')

**cloud-service**
   Configure system cloud service.
   
   .. code-block:: python
   
      # List all cloud-service
      items = fgt.api.cmdb.system.cloud_service.get()
      
      # Get specific cloud-service
      item = fgt.api.cmdb.system.cloud_service.get(mkey='name')

**console**
   Configure console.
   
   .. code-block:: python
   
      # List all console
      items = fgt.api.cmdb.system.console.get()
      
      # Get specific console
      item = fgt.api.cmdb.system.console.get(mkey='name')

**csf**
   Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
   
   .. code-block:: python
   
      # List all csf
      items = fgt.api.cmdb.system.csf.get()
      
      # Get specific csf
      item = fgt.api.cmdb.system.csf.get(mkey='name')

**custom-language**
   Configure custom languages.
   
   .. code-block:: python
   
      # List all custom-language
      items = fgt.api.cmdb.system.custom_language.get()
      
      # Get specific custom-language
      item = fgt.api.cmdb.system.custom_language.get(mkey='name')

**ddns**
   Configure DDNS.
   
   .. code-block:: python
   
      # List all ddns
      items = fgt.api.cmdb.system.ddns.get()
      
      # Get specific ddns
      item = fgt.api.cmdb.system.ddns.get(mkey='name')

**dedicated-mgmt**
   Configure dedicated management.
   
   .. code-block:: python
   
      # List all dedicated-mgmt
      items = fgt.api.cmdb.system.dedicated_mgmt.get()
      
      # Get specific dedicated-mgmt
      item = fgt.api.cmdb.system.dedicated_mgmt.get(mkey='name')

**device-upgrade**
   Independent upgrades for managed devices.
   
   .. code-block:: python
   
      # List all device-upgrade
      items = fgt.api.cmdb.system.device_upgrade.get()
      
      # Get specific device-upgrade
      item = fgt.api.cmdb.system.device_upgrade.get(mkey='name')

**device-upgrade-exemptions**
   Configure device upgrade exemptions. Device will stop receiving upgrade notifications on the GUI.
   
   .. code-block:: python
   
      # List all device-upgrade-exemptions
      items = fgt.api.cmdb.system.device_upgrade_exemptions.get()
      
      # Get specific device-upgrade-exemptions
      item = fgt.api.cmdb.system.device_upgrade_exemptions.get(mkey='name')

**dns**
   Configure DNS.
   
   .. code-block:: python
   
      # List all dns
      items = fgt.api.cmdb.system.dns.get()
      
      # Get specific dns
      item = fgt.api.cmdb.system.dns.get(mkey='name')

**dns-database**
   Configure DNS databases.
   
   .. code-block:: python
   
      # List all dns-database
      items = fgt.api.cmdb.system.dns_database.get()
      
      # Get specific dns-database
      item = fgt.api.cmdb.system.dns_database.get(mkey='name')

**dns-server**
   Configure DNS servers.
   
   .. code-block:: python
   
      # List all dns-server
      items = fgt.api.cmdb.system.dns_server.get()
      
      # Get specific dns-server
      item = fgt.api.cmdb.system.dns_server.get(mkey='name')

**dns64**
   Configure DNS64.
   
   .. code-block:: python
   
      # List all dns64
      items = fgt.api.cmdb.system.dns64.get()
      
      # Get specific dns64
      item = fgt.api.cmdb.system.dns64.get(mkey='name')

**dscp-based-priority**
   Configure DSCP based priority table.
   
   .. code-block:: python
   
      # List all dscp-based-priority
      items = fgt.api.cmdb.system.dscp_based_priority.get()
      
      # Get specific dscp-based-priority
      item = fgt.api.cmdb.system.dscp_based_priority.get(mkey='name')

**email-server**
   Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
   
   .. code-block:: python
   
      # List all email-server
      items = fgt.api.cmdb.system.email_server.get()
      
      # Get specific email-server
      item = fgt.api.cmdb.system.email_server.get(mkey='name')

**evpn**
   Configure EVPN instance.
   
   .. code-block:: python
   
      # List all evpn
      items = fgt.api.cmdb.system.evpn.get()
      
      # Get specific evpn
      item = fgt.api.cmdb.system.evpn.get(mkey='name')

**external-resource**
   Configure external resource.
   
   .. code-block:: python
   
      # List all external-resource
      items = fgt.api.cmdb.system.external_resource.get()
      
      # Get specific external-resource
      item = fgt.api.cmdb.system.external_resource.get(mkey='name')

**fabric-vpn**
   Setup for self orchestrated fabric auto discovery VPN.
   
   .. code-block:: python
   
      # List all fabric-vpn
      items = fgt.api.cmdb.system.fabric_vpn.get()
      
      # Get specific fabric-vpn
      item = fgt.api.cmdb.system.fabric_vpn.get(mkey='name')

**federated-upgrade**
   Coordinate federated upgrades within the Security Fabric.
   
   .. code-block:: python
   
      # List all federated-upgrade
      items = fgt.api.cmdb.system.federated_upgrade.get()
      
      # Get specific federated-upgrade
      item = fgt.api.cmdb.system.federated_upgrade.get(mkey='name')

**fips-cc**
   Configure FIPS-CC mode.
   
   .. code-block:: python
   
      # List all fips-cc
      items = fgt.api.cmdb.system.fips_cc.get()
      
      # Get specific fips-cc
      item = fgt.api.cmdb.system.fips_cc.get(mkey='name')

**fortiguard**
   Configure FortiGuard services.
   
   .. code-block:: python
   
      # List all fortiguard
      items = fgt.api.cmdb.system.fortiguard.get()
      
      # Get specific fortiguard
      item = fgt.api.cmdb.system.fortiguard.get(mkey='name')

**fortisandbox**
   Configure FortiSandbox.
   
   .. code-block:: python
   
      # List all fortisandbox
      items = fgt.api.cmdb.system.fortisandbox.get()
      
      # Get specific fortisandbox
      item = fgt.api.cmdb.system.fortisandbox.get(mkey='name')

**fsso-polling**
   Configure Fortinet Single Sign On (FSSO) server.
   
   .. code-block:: python
   
      # List all fsso-polling
      items = fgt.api.cmdb.system.fsso_polling.get()
      
      # Get specific fsso-polling
      item = fgt.api.cmdb.system.fsso_polling.get(mkey='name')

**ftm-push**
   Configure FortiToken Mobile push services.
   
   .. code-block:: python
   
      # List all ftm-push
      items = fgt.api.cmdb.system.ftm_push.get()
      
      # Get specific ftm-push
      item = fgt.api.cmdb.system.ftm_push.get(mkey='name')

**geneve**
   Configure GENEVE devices.
   
   .. code-block:: python
   
      # List all geneve
      items = fgt.api.cmdb.system.geneve.get()
      
      # Get specific geneve
      item = fgt.api.cmdb.system.geneve.get(mkey='name')

**geoip-country**
   Define geoip country name-ID table.
   
   .. code-block:: python
   
      # List all geoip-country
      items = fgt.api.cmdb.system.geoip_country.get()
      
      # Get specific geoip-country
      item = fgt.api.cmdb.system.geoip_country.get(mkey='name')

**geoip-override**
   Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
   
   .. code-block:: python
   
      # List all geoip-override
      items = fgt.api.cmdb.system.geoip_override.get()
      
      # Get specific geoip-override
      item = fgt.api.cmdb.system.geoip_override.get(mkey='name')

**global**
   Configure global attributes.
   
   .. code-block:: python
   
      # List all global
      items = fgt.api.cmdb.system.global.get()
      
      # Get specific global
      item = fgt.api.cmdb.system.global.get(mkey='name')

**gre-tunnel**
   Configure GRE tunnel.
   
   .. code-block:: python
   
      # List all gre-tunnel
      items = fgt.api.cmdb.system.gre_tunnel.get()
      
      # Get specific gre-tunnel
      item = fgt.api.cmdb.system.gre_tunnel.get(mkey='name')

**ha**
   Configure HA.
   
   .. code-block:: python
   
      # List all ha
      items = fgt.api.cmdb.system.ha.get()
      
      # Get specific ha
      item = fgt.api.cmdb.system.ha.get(mkey='name')

**ha-monitor**
   Configure HA monitor.
   
   .. code-block:: python
   
      # List all ha-monitor
      items = fgt.api.cmdb.system.ha_monitor.get()
      
      # Get specific ha-monitor
      item = fgt.api.cmdb.system.ha_monitor.get(mkey='name')

**health-check-fortiguard**
   SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
   
   .. code-block:: python
   
      # List all health-check-fortiguard
      items = fgt.api.cmdb.system.health_check_fortiguard.get()
      
      # Get specific health-check-fortiguard
      item = fgt.api.cmdb.system.health_check_fortiguard.get(mkey='name')

**ike**
   Configure IKE global attributes.
   
   .. code-block:: python
   
      # List all ike
      items = fgt.api.cmdb.system.ike.get()
      
      # Get specific ike
      item = fgt.api.cmdb.system.ike.get(mkey='name')

**interface**
   Configure interfaces.
   
   .. code-block:: python
   
      # List all interface
      items = fgt.api.cmdb.system.interface.get()
      
      # Get specific interface
      item = fgt.api.cmdb.system.interface.get(mkey='name')

**ipam**
   Configure IP address management services.
   
   .. code-block:: python
   
      # List all ipam
      items = fgt.api.cmdb.system.ipam.get()
      
      # Get specific ipam
      item = fgt.api.cmdb.system.ipam.get(mkey='name')

**ipip-tunnel**
   Configure IP in IP Tunneling.
   
   .. code-block:: python
   
      # List all ipip-tunnel
      items = fgt.api.cmdb.system.ipip_tunnel.get()
      
      # Get specific ipip-tunnel
      item = fgt.api.cmdb.system.ipip_tunnel.get(mkey='name')

**ips**
   Configure IPS system settings.
   
   .. code-block:: python
   
      # List all ips
      items = fgt.api.cmdb.system.ips.get()
      
      # Get specific ips
      item = fgt.api.cmdb.system.ips.get(mkey='name')

**ips-urlfilter-dns**
   Configure IPS URL filter DNS servers.
   
   .. code-block:: python
   
      # List all ips-urlfilter-dns
      items = fgt.api.cmdb.system.ips_urlfilter_dns.get()
      
      # Get specific ips-urlfilter-dns
      item = fgt.api.cmdb.system.ips_urlfilter_dns.get(mkey='name')

**ips-urlfilter-dns6**
   Configure IPS URL filter IPv6 DNS servers.
   
   .. code-block:: python
   
      # List all ips-urlfilter-dns6
      items = fgt.api.cmdb.system.ips_urlfilter_dns6.get()
      
      # Get specific ips-urlfilter-dns6
      item = fgt.api.cmdb.system.ips_urlfilter_dns6.get(mkey='name')

**ipsec-aggregate**
   Configure an aggregate of IPsec tunnels.
   
   .. code-block:: python
   
      # List all ipsec-aggregate
      items = fgt.api.cmdb.system.ipsec_aggregate.get()
      
      # Get specific ipsec-aggregate
      item = fgt.api.cmdb.system.ipsec_aggregate.get(mkey='name')

**ipv6-neighbor-cache**
   Configure IPv6 neighbor cache table.
   
   .. code-block:: python
   
      # List all ipv6-neighbor-cache
      items = fgt.api.cmdb.system.ipv6_neighbor_cache.get()
      
      # Get specific ipv6-neighbor-cache
      item = fgt.api.cmdb.system.ipv6_neighbor_cache.get(mkey='name')

**ipv6-tunnel**
   Configure IPv6/IPv4 in IPv6 tunnel.
   
   .. code-block:: python
   
      # List all ipv6-tunnel
      items = fgt.api.cmdb.system.ipv6_tunnel.get()
      
      # Get specific ipv6-tunnel
      item = fgt.api.cmdb.system.ipv6_tunnel.get(mkey='name')

**link-monitor**
   Configure Link Health Monitor.
   
   .. code-block:: python
   
      # List all link-monitor
      items = fgt.api.cmdb.system.link_monitor.get()
      
      # Get specific link-monitor
      item = fgt.api.cmdb.system.link_monitor.get(mkey='name')

**lte-modem**
   Configure USB LTE/WIMAX devices.
   
   .. code-block:: python
   
      # List all lte-modem
      items = fgt.api.cmdb.system.lte_modem.get()
      
      # Get specific lte-modem
      item = fgt.api.cmdb.system.lte_modem.get(mkey='name')

**mac-address-table**
   Configure MAC address tables.
   
   .. code-block:: python
   
      # List all mac-address-table
      items = fgt.api.cmdb.system.mac_address_table.get()
      
      # Get specific mac-address-table
      item = fgt.api.cmdb.system.mac_address_table.get(mkey='name')

**mobile-tunnel**
   Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
   
   .. code-block:: python
   
      # List all mobile-tunnel
      items = fgt.api.cmdb.system.mobile_tunnel.get()
      
      # Get specific mobile-tunnel
      item = fgt.api.cmdb.system.mobile_tunnel.get(mkey='name')

**modem**
   Configure MODEM.
   
   .. code-block:: python
   
      # List all modem
      items = fgt.api.cmdb.system.modem.get()
      
      # Get specific modem
      item = fgt.api.cmdb.system.modem.get(mkey='name')

**nd-proxy**
   Configure IPv6 neighbor discovery proxy (RFC4389).
   
   .. code-block:: python
   
      # List all nd-proxy
      items = fgt.api.cmdb.system.nd_proxy.get()
      
      # Get specific nd-proxy
      item = fgt.api.cmdb.system.nd_proxy.get(mkey='name')

**netflow**
   Configure NetFlow.
   
   .. code-block:: python
   
      # List all netflow
      items = fgt.api.cmdb.system.netflow.get()
      
      # Get specific netflow
      item = fgt.api.cmdb.system.netflow.get(mkey='name')

**network-visibility**
   Configure network visibility settings.
   
   .. code-block:: python
   
      # List all network-visibility
      items = fgt.api.cmdb.system.network_visibility.get()
      
      # Get specific network-visibility
      item = fgt.api.cmdb.system.network_visibility.get(mkey='name')

**ngfw-settings**
   Configure IPS NGFW policy-mode VDOM settings.
   
   .. code-block:: python
   
      # List all ngfw-settings
      items = fgt.api.cmdb.system.ngfw_settings.get()
      
      # Get specific ngfw-settings
      item = fgt.api.cmdb.system.ngfw_settings.get(mkey='name')

**np6xlite**
   Configure NP6XLITE attributes.
   
   .. code-block:: python
   
      # List all np6xlite
      items = fgt.api.cmdb.system.np6xlite.get()
      
      # Get specific np6xlite
      item = fgt.api.cmdb.system.np6xlite.get(mkey='name')

**npu**
   Configure NPU attributes.
   
   .. code-block:: python
   
      # List all npu
      items = fgt.api.cmdb.system.npu.get()
      
      # Get specific npu
      item = fgt.api.cmdb.system.npu.get(mkey='name')

**ntp**
   Configure system NTP information.
   
   .. code-block:: python
   
      # List all ntp
      items = fgt.api.cmdb.system.ntp.get()
      
      # Get specific ntp
      item = fgt.api.cmdb.system.ntp.get(mkey='name')

**object-tagging**
   Configure object tagging.
   
   .. code-block:: python
   
      # List all object-tagging
      items = fgt.api.cmdb.system.object_tagging.get()
      
      # Get specific object-tagging
      item = fgt.api.cmdb.system.object_tagging.get(mkey='name')

**password-policy**
   Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
   
   .. code-block:: python
   
      # List all password-policy
      items = fgt.api.cmdb.system.password_policy.get()
      
      # Get specific password-policy
      item = fgt.api.cmdb.system.password_policy.get(mkey='name')

**password-policy-guest-admin**
   Configure the password policy for guest administrators.
   
   .. code-block:: python
   
      # List all password-policy-guest-admin
      items = fgt.api.cmdb.system.password_policy_guest_admin.get()
      
      # Get specific password-policy-guest-admin
      item = fgt.api.cmdb.system.password_policy_guest_admin.get(mkey='name')

**pcp-server**
   Configure PCP server information.
   
   .. code-block:: python
   
      # List all pcp-server
      items = fgt.api.cmdb.system.pcp_server.get()
      
      # Get specific pcp-server
      item = fgt.api.cmdb.system.pcp_server.get(mkey='name')

**physical-switch**
   Configure physical switches.
   
   .. code-block:: python
   
      # List all physical-switch
      items = fgt.api.cmdb.system.physical_switch.get()
      
      # Get specific physical-switch
      item = fgt.api.cmdb.system.physical_switch.get(mkey='name')

**pppoe-interface**
   Configure the PPPoE interfaces.
   
   .. code-block:: python
   
      # List all pppoe-interface
      items = fgt.api.cmdb.system.pppoe_interface.get()
      
      # Get specific pppoe-interface
      item = fgt.api.cmdb.system.pppoe_interface.get(mkey='name')

**probe-response**
   Configure system probe response.
   
   .. code-block:: python
   
      # List all probe-response
      items = fgt.api.cmdb.system.probe_response.get()
      
      # Get specific probe-response
      item = fgt.api.cmdb.system.probe_response.get(mkey='name')

**proxy-arp**
   Configure proxy-ARP.
   
   .. code-block:: python
   
      # List all proxy-arp
      items = fgt.api.cmdb.system.proxy_arp.get()
      
      # Get specific proxy-arp
      item = fgt.api.cmdb.system.proxy_arp.get(mkey='name')

**ptp**
   Configure system PTP information.
   
   .. code-block:: python
   
      # List all ptp
      items = fgt.api.cmdb.system.ptp.get()
      
      # Get specific ptp
      item = fgt.api.cmdb.system.ptp.get(mkey='name')

**replacemsg-group**
   Configure replacement message groups.
   
   .. code-block:: python
   
      # List all replacemsg-group
      items = fgt.api.cmdb.system.replacemsg_group.get()
      
      # Get specific replacemsg-group
      item = fgt.api.cmdb.system.replacemsg_group.get(mkey='name')

**replacemsg-image**
   Configure replacement message images.
   
   .. code-block:: python
   
      # List all replacemsg-image
      items = fgt.api.cmdb.system.replacemsg_image.get()
      
      # Get specific replacemsg-image
      item = fgt.api.cmdb.system.replacemsg_image.get(mkey='name')

**resource-limits**
   Configure resource limits.
   
   .. code-block:: python
   
      # List all resource-limits
      items = fgt.api.cmdb.system.resource_limits.get()
      
      # Get specific resource-limits
      item = fgt.api.cmdb.system.resource_limits.get(mkey='name')

**saml**
   Global settings for SAML authentication.
   
   .. code-block:: python
   
      # List all saml
      items = fgt.api.cmdb.system.saml.get()
      
      # Get specific saml
      item = fgt.api.cmdb.system.saml.get(mkey='name')

**sdn-connector**
   Configure connection to SDN Connector.
   
   .. code-block:: python
   
      # List all sdn-connector
      items = fgt.api.cmdb.system.sdn_connector.get()
      
      # Get specific sdn-connector
      item = fgt.api.cmdb.system.sdn_connector.get(mkey='name')

**sdn-proxy**
   Configure SDN proxy.
   
   .. code-block:: python
   
      # List all sdn-proxy
      items = fgt.api.cmdb.system.sdn_proxy.get()
      
      # Get specific sdn-proxy
      item = fgt.api.cmdb.system.sdn_proxy.get(mkey='name')

**sdn-vpn**
   Configure public cloud VPN service.
   
   .. code-block:: python
   
      # List all sdn-vpn
      items = fgt.api.cmdb.system.sdn_vpn.get()
      
      # Get specific sdn-vpn
      item = fgt.api.cmdb.system.sdn_vpn.get(mkey='name')

**sdwan**
   Configure redundant Internet connections with multiple outbound links and health-check profiles.
   
   .. code-block:: python
   
      # List all sdwan
      items = fgt.api.cmdb.system.sdwan.get()
      
      # Get specific sdwan
      item = fgt.api.cmdb.system.sdwan.get(mkey='name')

**session-helper**
   Configure session helper.
   
   .. code-block:: python
   
      # List all session-helper
      items = fgt.api.cmdb.system.session_helper.get()
      
      # Get specific session-helper
      item = fgt.api.cmdb.system.session_helper.get(mkey='name')

**session-ttl**
   Configure global session TTL timers for this FortiGate.
   
   .. code-block:: python
   
      # List all session-ttl
      items = fgt.api.cmdb.system.session_ttl.get()
      
      # Get specific session-ttl
      item = fgt.api.cmdb.system.session_ttl.get(mkey='name')

**settings**
   Configure VDOM settings.
   
   .. code-block:: python
   
      # List all settings
      items = fgt.api.cmdb.system.settings.get()
      
      # Get specific settings
      item = fgt.api.cmdb.system.settings.get(mkey='name')

**sflow**
   Configure sFlow.
   
   .. code-block:: python
   
      # List all sflow
      items = fgt.api.cmdb.system.sflow.get()
      
      # Get specific sflow
      item = fgt.api.cmdb.system.sflow.get(mkey='name')

**sit-tunnel**
   Configure IPv6 tunnel over IPv4.
   
   .. code-block:: python
   
      # List all sit-tunnel
      items = fgt.api.cmdb.system.sit_tunnel.get()
      
      # Get specific sit-tunnel
      item = fgt.api.cmdb.system.sit_tunnel.get(mkey='name')

**sms-server**
   Configure SMS server for sending SMS messages to support user authentication.
   
   .. code-block:: python
   
      # List all sms-server
      items = fgt.api.cmdb.system.sms_server.get()
      
      # Get specific sms-server
      item = fgt.api.cmdb.system.sms_server.get(mkey='name')

**sov-sase**
   Configure Sovereign SASE.
   
   .. code-block:: python
   
      # List all sov-sase
      items = fgt.api.cmdb.system.sov_sase.get()
      
      # Get specific sov-sase
      item = fgt.api.cmdb.system.sov_sase.get(mkey='name')

**speed-test-schedule**
   Speed test schedule for each interface.
   
   .. code-block:: python
   
      # List all speed-test-schedule
      items = fgt.api.cmdb.system.speed_test_schedule.get()
      
      # Get specific speed-test-schedule
      item = fgt.api.cmdb.system.speed_test_schedule.get(mkey='name')

**speed-test-server**
   Configure speed test server list.
   
   .. code-block:: python
   
      # List all speed-test-server
      items = fgt.api.cmdb.system.speed_test_server.get()
      
      # Get specific speed-test-server
      item = fgt.api.cmdb.system.speed_test_server.get(mkey='name')

**speed-test-setting**
   Configure speed test setting.
   
   .. code-block:: python
   
      # List all speed-test-setting
      items = fgt.api.cmdb.system.speed_test_setting.get()
      
      # Get specific speed-test-setting
      item = fgt.api.cmdb.system.speed_test_setting.get(mkey='name')

**ssh-config**
   Configure SSH config.
   
   .. code-block:: python
   
      # List all ssh-config
      items = fgt.api.cmdb.system.ssh_config.get()
      
      # Get specific ssh-config
      item = fgt.api.cmdb.system.ssh_config.get(mkey='name')

**sso-admin**
   Configure SSO admin users.
   
   .. code-block:: python
   
      # List all sso-admin
      items = fgt.api.cmdb.system.sso_admin.get()
      
      # Get specific sso-admin
      item = fgt.api.cmdb.system.sso_admin.get(mkey='name')

**sso-forticloud-admin**
   Configure FortiCloud SSO admin users.
   
   .. code-block:: python
   
      # List all sso-forticloud-admin
      items = fgt.api.cmdb.system.sso_forticloud_admin.get()
      
      # Get specific sso-forticloud-admin
      item = fgt.api.cmdb.system.sso_forticloud_admin.get(mkey='name')

**sso-fortigate-cloud-admin**
   Configure FortiCloud SSO admin users.
   
   .. code-block:: python
   
      # List all sso-fortigate-cloud-admin
      items = fgt.api.cmdb.system.sso_fortigate_cloud_admin.get()
      
      # Get specific sso-fortigate-cloud-admin
      item = fgt.api.cmdb.system.sso_fortigate_cloud_admin.get(mkey='name')

**standalone-cluster**
   Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
   
   .. code-block:: python
   
      # List all standalone-cluster
      items = fgt.api.cmdb.system.standalone_cluster.get()
      
      # Get specific standalone-cluster
      item = fgt.api.cmdb.system.standalone_cluster.get(mkey='name')

**storage**
   Configure logical storage.
   
   .. code-block:: python
   
      # List all storage
      items = fgt.api.cmdb.system.storage.get()
      
      # Get specific storage
      item = fgt.api.cmdb.system.storage.get(mkey='name')

**stp**
   Configure Spanning Tree Protocol (STP).
   
   .. code-block:: python
   
      # List all stp
      items = fgt.api.cmdb.system.stp.get()
      
      # Get specific stp
      item = fgt.api.cmdb.system.stp.get(mkey='name')

**switch-interface**
   Configure software switch interfaces by grouping physical and WiFi interfaces.
   
   .. code-block:: python
   
      # List all switch-interface
      items = fgt.api.cmdb.system.switch_interface.get()
      
      # Get specific switch-interface
      item = fgt.api.cmdb.system.switch_interface.get(mkey='name')

**timezone**
   Show timezone.
   
   .. code-block:: python
   
      # List all timezone
      items = fgt.api.cmdb.system.timezone.get()
      
      # Get specific timezone
      item = fgt.api.cmdb.system.timezone.get(mkey='name')

**tos-based-priority**
   Configure Type of Service (ToS) based priority table to set network traffic priorities.
   
   .. code-block:: python
   
      # List all tos-based-priority
      items = fgt.api.cmdb.system.tos_based_priority.get()
      
      # Get specific tos-based-priority
      item = fgt.api.cmdb.system.tos_based_priority.get(mkey='name')

**vdom**
   Configure virtual domain.
   
   .. code-block:: python
   
      # List all vdom
      items = fgt.api.cmdb.system.vdom.get()
      
      # Get specific vdom
      item = fgt.api.cmdb.system.vdom.get(mkey='name')

**vdom-dns**
   Configure DNS servers for a non-management VDOM.
   
   .. code-block:: python
   
      # List all vdom-dns
      items = fgt.api.cmdb.system.vdom_dns.get()
      
      # Get specific vdom-dns
      item = fgt.api.cmdb.system.vdom_dns.get(mkey='name')

**vdom-exception**
   Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
   
   .. code-block:: python
   
      # List all vdom-exception
      items = fgt.api.cmdb.system.vdom_exception.get()
      
      # Get specific vdom-exception
      item = fgt.api.cmdb.system.vdom_exception.get(mkey='name')

**vdom-link**
   Configure VDOM links.
   
   .. code-block:: python
   
      # List all vdom-link
      items = fgt.api.cmdb.system.vdom_link.get()
      
      # Get specific vdom-link
      item = fgt.api.cmdb.system.vdom_link.get(mkey='name')

**vdom-netflow**
   Configure NetFlow per VDOM.
   
   .. code-block:: python
   
      # List all vdom-netflow
      items = fgt.api.cmdb.system.vdom_netflow.get()
      
      # Get specific vdom-netflow
      item = fgt.api.cmdb.system.vdom_netflow.get(mkey='name')

**vdom-property**
   Configure VDOM property.
   
   .. code-block:: python
   
      # List all vdom-property
      items = fgt.api.cmdb.system.vdom_property.get()
      
      # Get specific vdom-property
      item = fgt.api.cmdb.system.vdom_property.get(mkey='name')

**vdom-radius-server**
   Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.
   
   .. code-block:: python
   
      # List all vdom-radius-server
      items = fgt.api.cmdb.system.vdom_radius_server.get()
      
      # Get specific vdom-radius-server
      item = fgt.api.cmdb.system.vdom_radius_server.get(mkey='name')

**vdom-sflow**
   Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.
   
   .. code-block:: python
   
      # List all vdom-sflow
      items = fgt.api.cmdb.system.vdom_sflow.get()
      
      # Get specific vdom-sflow
      item = fgt.api.cmdb.system.vdom_sflow.get(mkey='name')

**virtual-switch**
   Configure virtual hardware switch interfaces.
   
   .. code-block:: python
   
      # List all virtual-switch
      items = fgt.api.cmdb.system.virtual_switch.get()
      
      # Get specific virtual-switch
      item = fgt.api.cmdb.system.virtual_switch.get(mkey='name')

**virtual-wire-pair**
   Configure virtual wire pairs.
   
   .. code-block:: python
   
      # List all virtual-wire-pair
      items = fgt.api.cmdb.system.virtual_wire_pair.get()
      
      # Get specific virtual-wire-pair
      item = fgt.api.cmdb.system.virtual_wire_pair.get(mkey='name')

**vne-interface**
   Configure virtual network enabler tunnels.
   
   .. code-block:: python
   
      # List all vne-interface
      items = fgt.api.cmdb.system.vne_interface.get()
      
      # Get specific vne-interface
      item = fgt.api.cmdb.system.vne_interface.get(mkey='name')

**vxlan**
   Configure VXLAN devices.
   
   .. code-block:: python
   
      # List all vxlan
      items = fgt.api.cmdb.system.vxlan.get()
      
      # Get specific vxlan
      item = fgt.api.cmdb.system.vxlan.get(mkey='name')

**wccp**
   Configure WCCP.
   
   .. code-block:: python
   
      # List all wccp
      items = fgt.api.cmdb.system.wccp.get()
      
      # Get specific wccp
      item = fgt.api.cmdb.system.wccp.get(mkey='name')

**zone**
   Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead of individual interfaces in the zone.
   
   .. code-block:: python
   
      # List all zone
      items = fgt.api.cmdb.system.zone.get()
      
      # Get specific zone
      item = fgt.api.cmdb.system.zone.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.system.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.system.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.system.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.system.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.system.{endpoint}.delete(mkey='config-name')

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
