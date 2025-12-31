System
======

3G MODEM custom configuration and management.

Overview
--------

The ``cmdb.system`` category provides configuration management for:

- :doc:`Accprofile <accprofile>` - Configure access profiles for system administrators.
- :doc:`Acme <acme>` - Configure ACME client.
- :doc:`Admin <admin>` - Configure admin users.
- :doc:`Affinity Interrupt <affinity-interrupt>` - Configure interrupt affinity.
- :doc:`Affinity Packet Redistribution <affinity-packet-redistribution>` - Configure packet redistribution.
- :doc:`Alarm <alarm>` - Configure alarm.
- :doc:`Alias <alias>` - Configure alias command.
- :doc:`Api User <api-user>` - Configure API users.
- :doc:`Arp Table <arp-table>` - Configure ARP table.
- :doc:`Auto Install <auto-install>` - Configure USB auto installation.
- :doc:`Auto Script <auto-script>` - Configure auto script.
- :doc:`Automation Action <automation-action>` - Action for automation stitches.
- :doc:`Automation Condition <automation-condition>` - Condition for automation stitches.
- :doc:`Automation Destination <automation-destination>` - Automation destinations.
- :doc:`Automation Stitch <automation-stitch>` - Automation stitches.
- :doc:`Automation Trigger <automation-trigger>` - Trigger for automation stitches.
- :doc:`Central Management <central-management>` - Configure central management.
- :doc:`Cloud Service <cloud-service>` - Configure system cloud service.
- :doc:`Console <console>` - Configure console.
- :doc:`Csf <csf>` - Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
- :doc:`Custom Language <custom-language>` - Configure custom languages.
- :doc:`Ddns <ddns>` - Configure DDNS.
- :doc:`Dedicated Mgmt <dedicated-mgmt>` - Configure dedicated management.
- :doc:`Device Upgrade <device-upgrade>` - Independent upgrades for managed devices.
- :doc:`Device Upgrade Exemptions <device-upgrade-exemptions>` - Configure device upgrade exemptions. Device will stop receiving upgrade notifications on the GUI.
- :doc:`Dns <dns>` - Configure DNS.
- :doc:`Dns Database <dns-database>` - Configure DNS databases.
- :doc:`Dns Server <dns-server>` - Configure DNS servers.
- :doc:`Dns64 <dns64>` - Configure DNS64.
- :doc:`Dscp Based Priority <dscp-based-priority>` - Configure DSCP based priority table.
- :doc:`Email Server <email-server>` - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
- :doc:`Evpn <evpn>` - Configure EVPN instance.
- :doc:`External Resource <external-resource>` - Configure external resource.
- :doc:`Fabric Vpn <fabric-vpn>` - Setup for self orchestrated fabric auto discovery VPN.
- :doc:`Federated Upgrade <federated-upgrade>` - Coordinate federated upgrades within the Security Fabric.
- :doc:`Fips Cc <fips-cc>` - Configure FIPS-CC mode.
- :doc:`Fortiguard <fortiguard>` - Configure FortiGuard services.
- :doc:`Fortisandbox <fortisandbox>` - Configure FortiSandbox.
- :doc:`Fsso Polling <fsso-polling>` - Configure Fortinet Single Sign On (FSSO) server.
- :doc:`Ftm Push <ftm-push>` - Configure FortiToken Mobile push services.
- :doc:`Geneve <geneve>` - Configure GENEVE devices.
- :doc:`Geoip Country <geoip-country>` - Define geoip country name-ID table.
- :doc:`Geoip Override <geoip-override>` - Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
- :doc:`Global <global>` - Configure global attributes.
- :doc:`Gre Tunnel <gre-tunnel>` - Configure GRE tunnel.
- :doc:`Ha <ha>` - Configure HA.
- :doc:`Ha Monitor <ha-monitor>` - Configure HA monitor.
- :doc:`Health Check Fortiguard <health-check-fortiguard>` - SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
- :doc:`Ike <ike>` - Configure IKE global attributes.
- :doc:`Interface <interface>` - Configure interfaces.
- :doc:`Ipam <ipam>` - Configure IP address management services.
- :doc:`Ipip Tunnel <ipip-tunnel>` - Configure IP in IP Tunneling.
- :doc:`Ips <ips>` - Configure IPS system settings.
- :doc:`Ips Urlfilter Dns <ips-urlfilter-dns>` - Configure IPS URL filter DNS servers.
- :doc:`Ips Urlfilter Dns6 <ips-urlfilter-dns6>` - Configure IPS URL filter IPv6 DNS servers.
- :doc:`Ipsec Aggregate <ipsec-aggregate>` - Configure an aggregate of IPsec tunnels.
- :doc:`Ipv6 Neighbor Cache <ipv6-neighbor-cache>` - Configure IPv6 neighbor cache table.
- :doc:`Ipv6 Tunnel <ipv6-tunnel>` - Configure IPv6/IPv4 in IPv6 tunnel.
- :doc:`Link Monitor <link-monitor>` - Configure Link Health Monitor.
- :doc:`Lte Modem <lte-modem>` - Configure USB LTE/WIMAX devices.
- :doc:`Mac Address Table <mac-address-table>` - Configure MAC address tables.
- :doc:`Mobile Tunnel <mobile-tunnel>` - Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
- :doc:`Modem <modem>` - Configure MODEM.
- :doc:`Nd Proxy <nd-proxy>` - Configure IPv6 neighbor discovery proxy (RFC4389).
- :doc:`Netflow <netflow>` - Configure NetFlow.
- :doc:`Network Visibility <network-visibility>` - Configure network visibility settings.
- :doc:`Ngfw Settings <ngfw-settings>` - Configure IPS NGFW policy-mode VDOM settings.
- :doc:`Np6Xlite <np6xlite>` - Configure NP6XLITE attributes.
- :doc:`Npu <npu>` - Configure NPU attributes.
- :doc:`Ntp <ntp>` - Configure system NTP information.
- :doc:`Object Tagging <object-tagging>` - Configure object tagging.
- :doc:`Password Policy <password-policy>` - Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
- :doc:`Password Policy Guest Admin <password-policy-guest-admin>` - Configure the password policy for guest administrators.
- :doc:`Pcp Server <pcp-server>` - Configure PCP server information.
- :doc:`Physical Switch <physical-switch>` - Configure physical switches.
- :doc:`Pppoe Interface <pppoe-interface>` - Configure the PPPoE interfaces.
- :doc:`Probe Response <probe-response>` - Configure system probe response.
- :doc:`Proxy Arp <proxy-arp>` - Configure proxy-ARP.
- :doc:`Ptp <ptp>` - Configure system PTP information.
- :doc:`Replacemsg Group <replacemsg-group>` - Configure replacement message groups.
- :doc:`Replacemsg Image <replacemsg-image>` - Configure replacement message images.
- :doc:`Resource Limits <resource-limits>` - Configure resource limits.
- :doc:`Saml <saml>` - Global settings for SAML authentication.
- :doc:`Sdn Connector <sdn-connector>` - Configure connection to SDN Connector.
- :doc:`Sdn Proxy <sdn-proxy>` - Configure SDN proxy.
- :doc:`Sdn Vpn <sdn-vpn>` - Configure public cloud VPN service.
- :doc:`Sdwan <sdwan>` - Configure redundant Internet connections with multiple outbound links and health-check profiles.
- :doc:`Session Helper <session-helper>` - Configure session helper.
- :doc:`Session Ttl <session-ttl>` - Configure global session TTL timers for this FortiGate.
- :doc:`Settings <settings>` - Configure VDOM settings.
- :doc:`Sflow <sflow>` - Configure sFlow.
- :doc:`Sit Tunnel <sit-tunnel>` - Configure IPv6 tunnel over IPv4.
- :doc:`Sms Server <sms-server>` - Configure SMS server for sending SMS messages to support user authentication.
- :doc:`Sov Sase <sov-sase>` - Configure Sovereign SASE.
- :doc:`Speed Test Schedule <speed-test-schedule>` - Speed test schedule for each interface.
- :doc:`Speed Test Server <speed-test-server>` - Configure speed test server list.
- :doc:`Speed Test Setting <speed-test-setting>` - Configure speed test setting.
- :doc:`Ssh Config <ssh-config>` - Configure SSH config.
- :doc:`Sso Admin <sso-admin>` - Configure SSO admin users.
- :doc:`Sso Forticloud Admin <sso-forticloud-admin>` - Configure FortiCloud SSO admin users.
- :doc:`Sso Fortigate Cloud Admin <sso-fortigate-cloud-admin>` - Configure FortiCloud SSO admin users.
- :doc:`Standalone Cluster <standalone-cluster>` - Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
- :doc:`Storage <storage>` - Configure logical storage.
- :doc:`Stp <stp>` - Configure Spanning Tree Protocol (STP).
- :doc:`Switch Interface <switch-interface>` - Configure software switch interfaces by grouping physical and WiFi interfaces.
- :doc:`Timezone <timezone>` - Show timezone.
- :doc:`Tos Based Priority <tos-based-priority>` - Configure Type of Service (ToS) based priority table to set network traffic priorities.
- :doc:`Vdom <vdom>` - Configure virtual domain.
- :doc:`Vdom Dns <vdom-dns>` - Configure DNS servers for a non-management VDOM.
- :doc:`Vdom Exception <vdom-exception>` - Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
- :doc:`Vdom Link <vdom-link>` - Configure VDOM links.
- :doc:`Vdom Netflow <vdom-netflow>` - Configure NetFlow per VDOM.
- :doc:`Vdom Property <vdom-property>` - Configure VDOM property.
- :doc:`Vdom Radius Server <vdom-radius-server>` - Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.
- :doc:`Vdom Sflow <vdom-sflow>` - Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.
- :doc:`Virtual Switch <virtual-switch>` - Configure virtual hardware switch interfaces.
- :doc:`Virtual Wire Pair <virtual-wire-pair>` - Configure virtual wire pairs.
- :doc:`Vne Interface <vne-interface>` - Configure virtual network enabler tunnels.
- :doc:`Vxlan <vxlan>` - Configure VXLAN devices.
- :doc:`Wccp <wccp>` - Configure WCCP.
- :doc:`Zone <zone>` - Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead of individual interfaces in the zone.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.system.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   accprofile
   acme
   admin
   affinity-interrupt
   affinity-packet-redistribution
   alarm
   alias
   api-user
   arp-table
   auto-install
   auto-script
   automation-action
   automation-condition
   automation-destination
   automation-stitch
   automation-trigger
   central-management
   cloud-service
   console
   csf
   custom-language
   ddns
   dedicated-mgmt
   device-upgrade
   device-upgrade-exemptions
   dns
   dns-database
   dns-server
   dns64
   dscp-based-priority
   email-server
   evpn
   external-resource
   fabric-vpn
   federated-upgrade
   fips-cc
   fortiguard
   fortisandbox
   fsso-polling
   ftm-push
   geneve
   geoip-country
   geoip-override
   global
   gre-tunnel
   ha
   ha-monitor
   health-check-fortiguard
   ike
   interface
   ipam
   ipip-tunnel
   ips
   ips-urlfilter-dns
   ips-urlfilter-dns6
   ipsec-aggregate
   ipv6-neighbor-cache
   ipv6-tunnel
   link-monitor
   lte-modem
   mac-address-table
   mobile-tunnel
   modem
   nd-proxy
   netflow
   network-visibility
   ngfw-settings
   np6xlite
   npu
   ntp
   object-tagging
   password-policy
   password-policy-guest-admin
   pcp-server
   physical-switch
   pppoe-interface
   probe-response
   proxy-arp
   ptp
   replacemsg-group
   replacemsg-image
   resource-limits
   saml
   sdn-connector
   sdn-proxy
   sdn-vpn
   sdwan
   session-helper
   session-ttl
   settings
   sflow
   sit-tunnel
   sms-server
   sov-sase
   speed-test-schedule
   speed-test-server
   speed-test-setting
   ssh-config
   sso-admin
   sso-forticloud-admin
   sso-fortigate-cloud-admin
   standalone-cluster
   storage
   stp
   switch-interface
   timezone
   tos-based-priority
   vdom
   vdom-dns
   vdom-exception
   vdom-link
   vdom-netflow
   vdom-property
   vdom-radius-server
   vdom-sflow
   virtual-switch
   virtual-wire-pair
   vne-interface
   vxlan
   wccp
   zone

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
