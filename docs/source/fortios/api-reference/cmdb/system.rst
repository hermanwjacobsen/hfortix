System
======

3G MODEM custom configuration and management.

Overview
--------

The ``cmdb.system`` category provides configuration management for:

- :ref:`Accprofile <system-accprofile>` - Configure access profiles for system administrators.
- :ref:`Acme <system-acme>` - Configure ACME client.
- :ref:`Admin <system-admin>` - Configure admin users.
- :ref:`Affinity Interrupt <system-affinity-interrupt>` - Configure interrupt affinity.
- :ref:`Affinity Packet Redistribution <system-affinity-packet-redistribution>` - Configure packet redistribution.
- :ref:`Alarm <system-alarm>` - Configure alarm.
- :ref:`Alias <system-alias>` - Configure alias command.
- :ref:`Api User <system-api-user>` - Configure API users.
- :ref:`Arp Table <system-arp-table>` - Configure ARP table.
- :ref:`Auto Install <system-auto-install>` - Configure USB auto installation.
- :ref:`Auto Script <system-auto-script>` - Configure auto script.
- :ref:`Automation Action <system-automation-action>` - Action for automation stitches.
- :ref:`Automation Condition <system-automation-condition>` - Condition for automation stitches.
- :ref:`Automation Destination <system-automation-destination>` - Automation destinations.
- :ref:`Automation Stitch <system-automation-stitch>` - Automation stitches.
- :ref:`Automation Trigger <system-automation-trigger>` - Trigger for automation stitches.
- :ref:`Central Management <system-central-management>` - Configure central management.
- :ref:`Cloud Service <system-cloud-service>` - Configure system cloud service.
- :ref:`Console <system-console>` - Configure console.
- :ref:`Csf <system-csf>` - Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
- :ref:`Custom Language <system-custom-language>` - Configure custom languages.
- :ref:`Ddns <system-ddns>` - Configure DDNS.
- :ref:`Dedicated Mgmt <system-dedicated-mgmt>` - Configure dedicated management.
- :ref:`Device Upgrade <system-device-upgrade>` - Independent upgrades for managed devices.
- :ref:`Device Upgrade Exemptions <system-device-upgrade-exemptions>` - Configure device upgrade exemptions. Device will stop receiving upgrade notifications on the GUI.
- :ref:`Dns <system-dns>` - Configure DNS.
- :ref:`Dns Database <system-dns-database>` - Configure DNS databases.
- :ref:`Dns Server <system-dns-server>` - Configure DNS servers.
- :ref:`Dns64 <system-dns64>` - Configure DNS64.
- :ref:`Dscp Based Priority <system-dscp-based-priority>` - Configure DSCP based priority table.
- :ref:`Email Server <system-email-server>` - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
- :ref:`Evpn <system-evpn>` - Configure EVPN instance.
- :ref:`External Resource <system-external-resource>` - Configure external resource.
- :ref:`Fabric Vpn <system-fabric-vpn>` - Setup for self orchestrated fabric auto discovery VPN.
- :ref:`Federated Upgrade <system-federated-upgrade>` - Coordinate federated upgrades within the Security Fabric.
- :ref:`Fips Cc <system-fips-cc>` - Configure FIPS-CC mode.
- :ref:`Fortiguard <system-fortiguard>` - Configure FortiGuard services.
- :ref:`Fortisandbox <system-fortisandbox>` - Configure FortiSandbox.
- :ref:`Fsso Polling <system-fsso-polling>` - Configure Fortinet Single Sign On (FSSO) server.
- :ref:`Ftm Push <system-ftm-push>` - Configure FortiToken Mobile push services.
- :ref:`Geneve <system-geneve>` - Configure GENEVE devices.
- :ref:`Geoip Country <system-geoip-country>` - Define geoip country name-ID table.
- :ref:`Geoip Override <system-geoip-override>` - Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.
- :ref:`Global <system-global>` - Configure global attributes.
- :ref:`Gre Tunnel <system-gre-tunnel>` - Configure GRE tunnel.
- :ref:`Ha <system-ha>` - Configure HA.
- :ref:`Ha Monitor <system-ha-monitor>` - Configure HA monitor.
- :ref:`Health Check Fortiguard <system-health-check-fortiguard>` - SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
- :ref:`Ike <system-ike>` - Configure IKE global attributes.
- :ref:`Interface <system-interface>` - Configure interfaces.
- :ref:`Ipam <system-ipam>` - Configure IP address management services.
- :ref:`Ipip Tunnel <system-ipip-tunnel>` - Configure IP in IP Tunneling.
- :ref:`Ips <system-ips>` - Configure IPS system settings.
- :ref:`Ips Urlfilter Dns <system-ips-urlfilter-dns>` - Configure IPS URL filter DNS servers.
- :ref:`Ips Urlfilter Dns6 <system-ips-urlfilter-dns6>` - Configure IPS URL filter IPv6 DNS servers.
- :ref:`Ipsec Aggregate <system-ipsec-aggregate>` - Configure an aggregate of IPsec tunnels.
- :ref:`Ipv6 Neighbor Cache <system-ipv6-neighbor-cache>` - Configure IPv6 neighbor cache table.
- :ref:`Ipv6 Tunnel <system-ipv6-tunnel>` - Configure IPv6/IPv4 in IPv6 tunnel.
- :ref:`Link Monitor <system-link-monitor>` - Configure Link Health Monitor.
- :ref:`Lte Modem <system-lte-modem>` - Configure USB LTE/WIMAX devices.
- :ref:`Mac Address Table <system-mac-address-table>` - Configure MAC address tables.
- :ref:`Mobile Tunnel <system-mobile-tunnel>` - Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
- :ref:`Modem <system-modem>` - Configure MODEM.
- :ref:`Nd Proxy <system-nd-proxy>` - Configure IPv6 neighbor discovery proxy (RFC4389).
- :ref:`Netflow <system-netflow>` - Configure NetFlow.
- :ref:`Network Visibility <system-network-visibility>` - Configure network visibility settings.
- :ref:`Ngfw Settings <system-ngfw-settings>` - Configure IPS NGFW policy-mode VDOM settings.
- :ref:`Np6Xlite <system-np6xlite>` - Configure NP6XLITE attributes.
- :ref:`Npu <system-npu>` - Configure NPU attributes.
- :ref:`Ntp <system-ntp>` - Configure system NTP information.
- :ref:`Object Tagging <system-object-tagging>` - Configure object tagging.
- :ref:`Password Policy <system-password-policy>` - Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
- :ref:`Password Policy Guest Admin <system-password-policy-guest-admin>` - Configure the password policy for guest administrators.
- :ref:`Pcp Server <system-pcp-server>` - Configure PCP server information.
- :ref:`Physical Switch <system-physical-switch>` - Configure physical switches.
- :ref:`Pppoe Interface <system-pppoe-interface>` - Configure the PPPoE interfaces.
- :ref:`Probe Response <system-probe-response>` - Configure system probe response.
- :ref:`Proxy Arp <system-proxy-arp>` - Configure proxy-ARP.
- :ref:`Ptp <system-ptp>` - Configure system PTP information.
- :ref:`Replacemsg Group <system-replacemsg-group>` - Configure replacement message groups.
- :ref:`Replacemsg Image <system-replacemsg-image>` - Configure replacement message images.
- :ref:`Resource Limits <system-resource-limits>` - Configure resource limits.
- :ref:`Saml <system-saml>` - Global settings for SAML authentication.
- :ref:`Sdn Connector <system-sdn-connector>` - Configure connection to SDN Connector.
- :ref:`Sdn Proxy <system-sdn-proxy>` - Configure SDN proxy.
- :ref:`Sdn Vpn <system-sdn-vpn>` - Configure public cloud VPN service.
- :ref:`Sdwan <system-sdwan>` - Configure redundant Internet connections with multiple outbound links and health-check profiles.
- :ref:`Session Helper <system-session-helper>` - Configure session helper.
- :ref:`Session Ttl <system-session-ttl>` - Configure global session TTL timers for this FortiGate.
- :ref:`Settings <system-settings>` - Configure VDOM settings.
- :ref:`Sflow <system-sflow>` - Configure sFlow.
- :ref:`Sit Tunnel <system-sit-tunnel>` - Configure IPv6 tunnel over IPv4.
- :ref:`Sms Server <system-sms-server>` - Configure SMS server for sending SMS messages to support user authentication.
- :ref:`Sov Sase <system-sov-sase>` - Configure Sovereign SASE.
- :ref:`Speed Test Schedule <system-speed-test-schedule>` - Speed test schedule for each interface.
- :ref:`Speed Test Server <system-speed-test-server>` - Configure speed test server list.
- :ref:`Speed Test Setting <system-speed-test-setting>` - Configure speed test setting.
- :ref:`Ssh Config <system-ssh-config>` - Configure SSH config.
- :ref:`Sso Admin <system-sso-admin>` - Configure SSO admin users.
- :ref:`Sso Forticloud Admin <system-sso-forticloud-admin>` - Configure FortiCloud SSO admin users.
- :ref:`Sso Fortigate Cloud Admin <system-sso-fortigate-cloud-admin>` - Configure FortiCloud SSO admin users.
- :ref:`Standalone Cluster <system-standalone-cluster>` - Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
- :ref:`Storage <system-storage>` - Configure logical storage.
- :ref:`Stp <system-stp>` - Configure Spanning Tree Protocol (STP).
- :ref:`Switch Interface <system-switch-interface>` - Configure software switch interfaces by grouping physical and WiFi interfaces.
- :ref:`Timezone <system-timezone>` - Show timezone.
- :ref:`Tos Based Priority <system-tos-based-priority>` - Configure Type of Service (ToS) based priority table to set network traffic priorities.
- :ref:`Vdom <system-vdom>` - Configure virtual domain.
- :ref:`Vdom Dns <system-vdom-dns>` - Configure DNS servers for a non-management VDOM.
- :ref:`Vdom Exception <system-vdom-exception>` - Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
- :ref:`Vdom Link <system-vdom-link>` - Configure VDOM links.
- :ref:`Vdom Netflow <system-vdom-netflow>` - Configure NetFlow per VDOM.
- :ref:`Vdom Property <system-vdom-property>` - Configure VDOM property.
- :ref:`Vdom Radius Server <system-vdom-radius-server>` - Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.
- :ref:`Vdom Sflow <system-vdom-sflow>` - Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.
- :ref:`Virtual Switch <system-virtual-switch>` - Configure virtual hardware switch interfaces.
- :ref:`Virtual Wire Pair <system-virtual-wire-pair>` - Configure virtual wire pairs.
- :ref:`Vne Interface <system-vne-interface>` - Configure virtual network enabler tunnels.
- :ref:`Vxlan <system-vxlan>` - Configure VXLAN devices.
- :ref:`Wccp <system-wccp>` - Configure WCCP.
- :ref:`Zone <system-zone>` - Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead of individual interfaces in the zone.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.system

Available Endpoints
-------------------

.. _system-accprofile:

accprofile
~~~~~~~~~~

Configure access profiles for system administrators.

**Python attribute:** ``accprofile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.accprofile.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.accprofile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.accprofile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.accprofile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.accprofile.delete(mkey='item-name')

.. _system-acme:

acme
~~~~

Configure ACME client.

**Python attribute:** ``acme``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.acme.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.acme.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.acme.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.acme.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.acme.delete(mkey='item-name')

.. _system-admin:

admin
~~~~~

Configure admin users.

**Python attribute:** ``admin``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.admin.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.admin.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.admin.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.admin.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.admin.delete(mkey='item-name')

.. _system-affinity-interrupt:

affinity-interrupt
~~~~~~~~~~~~~~~~~~

Configure interrupt affinity.

**Python attribute:** ``affinity_interrupt``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.affinity_interrupt.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.affinity_interrupt.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.affinity_interrupt.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.affinity_interrupt.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.affinity_interrupt.delete(mkey='item-name')

.. _system-affinity-packet-redistribution:

affinity-packet-redistribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure packet redistribution.

**Python attribute:** ``affinity_packet_redistribution``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.affinity_packet_redistribution.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.affinity_packet_redistribution.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.affinity_packet_redistribution.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.affinity_packet_redistribution.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.affinity_packet_redistribution.delete(mkey='item-name')

.. _system-alarm:

alarm
~~~~~

Configure alarm.

**Python attribute:** ``alarm``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.alarm.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.alarm.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.alarm.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.alarm.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.alarm.delete(mkey='item-name')

.. _system-alias:

alias
~~~~~

Configure alias command.

**Python attribute:** ``alias``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.alias.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.alias.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.alias.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.alias.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.alias.delete(mkey='item-name')

.. _system-api-user:

api-user
~~~~~~~~

Configure API users.

**Python attribute:** ``api_user``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.api_user.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.api_user.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.api_user.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.api_user.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.api_user.delete(mkey='item-name')

.. _system-arp-table:

arp-table
~~~~~~~~~

Configure ARP table.

**Python attribute:** ``arp_table``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.arp_table.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.arp_table.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.arp_table.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.arp_table.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.arp_table.delete(mkey='item-name')

.. _system-auto-install:

auto-install
~~~~~~~~~~~~

Configure USB auto installation.

**Python attribute:** ``auto_install``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.auto_install.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.auto_install.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.auto_install.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.auto_install.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.auto_install.delete(mkey='item-name')

.. _system-auto-script:

auto-script
~~~~~~~~~~~

Configure auto script.

**Python attribute:** ``auto_script``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.auto_script.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.auto_script.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.auto_script.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.auto_script.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.auto_script.delete(mkey='item-name')

.. _system-automation-action:

automation-action
~~~~~~~~~~~~~~~~~

Action for automation stitches.

**Python attribute:** ``automation_action``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.automation_action.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.automation_action.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.automation_action.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.automation_action.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.automation_action.delete(mkey='item-name')

.. _system-automation-condition:

automation-condition
~~~~~~~~~~~~~~~~~~~~

Condition for automation stitches.

**Python attribute:** ``automation_condition``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.automation_condition.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.automation_condition.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.automation_condition.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.automation_condition.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.automation_condition.delete(mkey='item-name')

.. _system-automation-destination:

automation-destination
~~~~~~~~~~~~~~~~~~~~~~

Automation destinations.

**Python attribute:** ``automation_destination``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.automation_destination.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.automation_destination.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.automation_destination.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.automation_destination.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.automation_destination.delete(mkey='item-name')

.. _system-automation-stitch:

automation-stitch
~~~~~~~~~~~~~~~~~

Automation stitches.

**Python attribute:** ``automation_stitch``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.automation_stitch.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.automation_stitch.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.automation_stitch.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.automation_stitch.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.automation_stitch.delete(mkey='item-name')

.. _system-automation-trigger:

automation-trigger
~~~~~~~~~~~~~~~~~~

Trigger for automation stitches.

**Python attribute:** ``automation_trigger``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.automation_trigger.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.automation_trigger.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.automation_trigger.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.automation_trigger.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.automation_trigger.delete(mkey='item-name')

.. _system-central-management:

central-management
~~~~~~~~~~~~~~~~~~

Configure central management.

**Python attribute:** ``central_management``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.central_management.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.central_management.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.central_management.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.central_management.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.central_management.delete(mkey='item-name')

.. _system-cloud-service:

cloud-service
~~~~~~~~~~~~~

Configure system cloud service.

**Python attribute:** ``cloud_service``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.cloud_service.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.cloud_service.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.cloud_service.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.cloud_service.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.cloud_service.delete(mkey='item-name')

.. _system-console:

console
~~~~~~~

Configure console.

**Python attribute:** ``console``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.console.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.console.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.console.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.console.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.console.delete(mkey='item-name')

.. _system-csf:

csf
~~~

Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.

**Python attribute:** ``csf``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.csf.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.csf.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.csf.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.csf.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.csf.delete(mkey='item-name')

.. _system-custom-language:

custom-language
~~~~~~~~~~~~~~~

Configure custom languages.

**Python attribute:** ``custom_language``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.custom_language.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.custom_language.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.custom_language.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.custom_language.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.custom_language.delete(mkey='item-name')

.. _system-ddns:

ddns
~~~~

Configure DDNS.

**Python attribute:** ``ddns``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ddns.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ddns.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ddns.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ddns.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ddns.delete(mkey='item-name')

.. _system-dedicated-mgmt:

dedicated-mgmt
~~~~~~~~~~~~~~

Configure dedicated management.

**Python attribute:** ``dedicated_mgmt``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.dedicated_mgmt.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.dedicated_mgmt.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.dedicated_mgmt.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.dedicated_mgmt.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.dedicated_mgmt.delete(mkey='item-name')

.. _system-device-upgrade:

device-upgrade
~~~~~~~~~~~~~~

Independent upgrades for managed devices.

**Python attribute:** ``device_upgrade``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.device_upgrade.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.device_upgrade.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.device_upgrade.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.device_upgrade.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.device_upgrade.delete(mkey='item-name')

.. _system-device-upgrade-exemptions:

device-upgrade-exemptions
~~~~~~~~~~~~~~~~~~~~~~~~~

Configure device upgrade exemptions. Device will stop receiving upgrade notifications on the GUI.

**Python attribute:** ``device_upgrade_exemptions``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.device_upgrade_exemptions.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.device_upgrade_exemptions.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.device_upgrade_exemptions.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.device_upgrade_exemptions.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.device_upgrade_exemptions.delete(mkey='item-name')

.. _system-dns:

dns
~~~

Configure DNS.

**Python attribute:** ``dns``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.dns.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.dns.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.dns.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.dns.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.dns.delete(mkey='item-name')

.. _system-dns-database:

dns-database
~~~~~~~~~~~~

Configure DNS databases.

**Python attribute:** ``dns_database``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.dns_database.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.dns_database.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.dns_database.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.dns_database.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.dns_database.delete(mkey='item-name')

.. _system-dns-server:

dns-server
~~~~~~~~~~

Configure DNS servers.

**Python attribute:** ``dns_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.dns_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.dns_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.dns_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.dns_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.dns_server.delete(mkey='item-name')

.. _system-dns64:

dns64
~~~~~

Configure DNS64.

**Python attribute:** ``dns64``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.dns64.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.dns64.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.dns64.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.dns64.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.dns64.delete(mkey='item-name')

.. _system-dscp-based-priority:

dscp-based-priority
~~~~~~~~~~~~~~~~~~~

Configure DSCP based priority table.

**Python attribute:** ``dscp_based_priority``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.dscp_based_priority.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.dscp_based_priority.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.dscp_based_priority.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.dscp_based_priority.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.dscp_based_priority.delete(mkey='item-name')

.. _system-email-server:

email-server
~~~~~~~~~~~~

Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.

**Python attribute:** ``email_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.email_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.email_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.email_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.email_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.email_server.delete(mkey='item-name')

.. _system-evpn:

evpn
~~~~

Configure EVPN instance.

**Python attribute:** ``evpn``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.evpn.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.evpn.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.evpn.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.evpn.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.evpn.delete(mkey='item-name')

.. _system-external-resource:

external-resource
~~~~~~~~~~~~~~~~~

Configure external resource.

**Python attribute:** ``external_resource``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.external_resource.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.external_resource.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.external_resource.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.external_resource.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.external_resource.delete(mkey='item-name')

.. _system-fabric-vpn:

fabric-vpn
~~~~~~~~~~

Setup for self orchestrated fabric auto discovery VPN.

**Python attribute:** ``fabric_vpn``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.fabric_vpn.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.fabric_vpn.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.fabric_vpn.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.fabric_vpn.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.fabric_vpn.delete(mkey='item-name')

.. _system-federated-upgrade:

federated-upgrade
~~~~~~~~~~~~~~~~~

Coordinate federated upgrades within the Security Fabric.

**Python attribute:** ``federated_upgrade``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.federated_upgrade.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.federated_upgrade.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.federated_upgrade.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.federated_upgrade.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.federated_upgrade.delete(mkey='item-name')

.. _system-fips-cc:

fips-cc
~~~~~~~

Configure FIPS-CC mode.

**Python attribute:** ``fips_cc``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.fips_cc.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.fips_cc.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.fips_cc.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.fips_cc.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.fips_cc.delete(mkey='item-name')

.. _system-fortiguard:

fortiguard
~~~~~~~~~~

Configure FortiGuard services.

**Python attribute:** ``fortiguard``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.fortiguard.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.fortiguard.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.fortiguard.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.fortiguard.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.fortiguard.delete(mkey='item-name')

.. _system-fortisandbox:

fortisandbox
~~~~~~~~~~~~

Configure FortiSandbox.

**Python attribute:** ``fortisandbox``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.fortisandbox.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.fortisandbox.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.fortisandbox.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.fortisandbox.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.fortisandbox.delete(mkey='item-name')

.. _system-fsso-polling:

fsso-polling
~~~~~~~~~~~~

Configure Fortinet Single Sign On (FSSO) server.

**Python attribute:** ``fsso_polling``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.fsso_polling.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.fsso_polling.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.fsso_polling.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.fsso_polling.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.fsso_polling.delete(mkey='item-name')

.. _system-ftm-push:

ftm-push
~~~~~~~~

Configure FortiToken Mobile push services.

**Python attribute:** ``ftm_push``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ftm_push.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ftm_push.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ftm_push.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ftm_push.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ftm_push.delete(mkey='item-name')

.. _system-geneve:

geneve
~~~~~~

Configure GENEVE devices.

**Python attribute:** ``geneve``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.geneve.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.geneve.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.geneve.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.geneve.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.geneve.delete(mkey='item-name')

.. _system-geoip-country:

geoip-country
~~~~~~~~~~~~~

Define geoip country name-ID table.

**Python attribute:** ``geoip_country``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.geoip_country.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.geoip_country.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.geoip_country.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.geoip_country.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.geoip_country.delete(mkey='item-name')

.. _system-geoip-override:

geoip-override
~~~~~~~~~~~~~~

Configure geographical location mapping for IP address(es) to override mappings from FortiGuard.

**Python attribute:** ``geoip_override``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.geoip_override.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.geoip_override.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.geoip_override.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.geoip_override.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.geoip_override.delete(mkey='item-name')

.. _system-global:

global
~~~~~~

Configure global attributes.

**Python attribute:** ``global``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.global.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.global.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.global.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.global.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.global.delete(mkey='item-name')

.. _system-gre-tunnel:

gre-tunnel
~~~~~~~~~~

Configure GRE tunnel.

**Python attribute:** ``gre_tunnel``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.gre_tunnel.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.gre_tunnel.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.gre_tunnel.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.gre_tunnel.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.gre_tunnel.delete(mkey='item-name')

.. _system-ha:

ha
~~

Configure HA.

**Python attribute:** ``ha``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ha.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ha.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ha.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ha.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ha.delete(mkey='item-name')

.. _system-ha-monitor:

ha-monitor
~~~~~~~~~~

Configure HA monitor.

**Python attribute:** ``ha_monitor``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ha_monitor.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ha_monitor.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ha_monitor.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ha_monitor.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ha_monitor.delete(mkey='item-name')

.. _system-health-check-fortiguard:

health-check-fortiguard
~~~~~~~~~~~~~~~~~~~~~~~

SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.

**Python attribute:** ``health_check_fortiguard``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.health_check_fortiguard.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.health_check_fortiguard.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.health_check_fortiguard.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.health_check_fortiguard.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.health_check_fortiguard.delete(mkey='item-name')

.. _system-ike:

ike
~~~

Configure IKE global attributes.

**Python attribute:** ``ike``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ike.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ike.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ike.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ike.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ike.delete(mkey='item-name')

.. _system-interface:

interface
~~~~~~~~~

Configure interfaces.

**Python attribute:** ``interface``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.interface.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.interface.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.interface.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.interface.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.interface.delete(mkey='item-name')

.. _system-ipam:

ipam
~~~~

Configure IP address management services.

**Python attribute:** ``ipam``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ipam.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ipam.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ipam.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ipam.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ipam.delete(mkey='item-name')

.. _system-ipip-tunnel:

ipip-tunnel
~~~~~~~~~~~

Configure IP in IP Tunneling.

**Python attribute:** ``ipip_tunnel``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ipip_tunnel.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ipip_tunnel.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ipip_tunnel.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ipip_tunnel.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ipip_tunnel.delete(mkey='item-name')

.. _system-ips:

ips
~~~

Configure IPS system settings.

**Python attribute:** ``ips``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ips.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ips.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ips.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ips.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ips.delete(mkey='item-name')

.. _system-ips-urlfilter-dns:

ips-urlfilter-dns
~~~~~~~~~~~~~~~~~

Configure IPS URL filter DNS servers.

**Python attribute:** ``ips_urlfilter_dns``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ips_urlfilter_dns.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ips_urlfilter_dns.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ips_urlfilter_dns.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ips_urlfilter_dns.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ips_urlfilter_dns.delete(mkey='item-name')

.. _system-ips-urlfilter-dns6:

ips-urlfilter-dns6
~~~~~~~~~~~~~~~~~~

Configure IPS URL filter IPv6 DNS servers.

**Python attribute:** ``ips_urlfilter_dns6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ips_urlfilter_dns6.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ips_urlfilter_dns6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ips_urlfilter_dns6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ips_urlfilter_dns6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ips_urlfilter_dns6.delete(mkey='item-name')

.. _system-ipsec-aggregate:

ipsec-aggregate
~~~~~~~~~~~~~~~

Configure an aggregate of IPsec tunnels.

**Python attribute:** ``ipsec_aggregate``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ipsec_aggregate.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ipsec_aggregate.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ipsec_aggregate.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ipsec_aggregate.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ipsec_aggregate.delete(mkey='item-name')

.. _system-ipv6-neighbor-cache:

ipv6-neighbor-cache
~~~~~~~~~~~~~~~~~~~

Configure IPv6 neighbor cache table.

**Python attribute:** ``ipv6_neighbor_cache``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ipv6_neighbor_cache.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ipv6_neighbor_cache.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ipv6_neighbor_cache.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ipv6_neighbor_cache.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ipv6_neighbor_cache.delete(mkey='item-name')

.. _system-ipv6-tunnel:

ipv6-tunnel
~~~~~~~~~~~

Configure IPv6/IPv4 in IPv6 tunnel.

**Python attribute:** ``ipv6_tunnel``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ipv6_tunnel.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ipv6_tunnel.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ipv6_tunnel.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ipv6_tunnel.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ipv6_tunnel.delete(mkey='item-name')

.. _system-link-monitor:

link-monitor
~~~~~~~~~~~~

Configure Link Health Monitor.

**Python attribute:** ``link_monitor``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.link_monitor.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.link_monitor.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.link_monitor.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.link_monitor.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.link_monitor.delete(mkey='item-name')

.. _system-lte-modem:

lte-modem
~~~~~~~~~

Configure USB LTE/WIMAX devices.

**Python attribute:** ``lte_modem``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.lte_modem.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.lte_modem.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.lte_modem.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.lte_modem.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.lte_modem.delete(mkey='item-name')

.. _system-mac-address-table:

mac-address-table
~~~~~~~~~~~~~~~~~

Configure MAC address tables.

**Python attribute:** ``mac_address_table``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.mac_address_table.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.mac_address_table.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.mac_address_table.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.mac_address_table.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.mac_address_table.delete(mkey='item-name')

.. _system-mobile-tunnel:

mobile-tunnel
~~~~~~~~~~~~~

Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.

**Python attribute:** ``mobile_tunnel``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.mobile_tunnel.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.mobile_tunnel.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.mobile_tunnel.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.mobile_tunnel.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.mobile_tunnel.delete(mkey='item-name')

.. _system-modem:

modem
~~~~~

Configure MODEM.

**Python attribute:** ``modem``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.modem.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.modem.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.modem.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.modem.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.modem.delete(mkey='item-name')

.. _system-nd-proxy:

nd-proxy
~~~~~~~~

Configure IPv6 neighbor discovery proxy (RFC4389).

**Python attribute:** ``nd_proxy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.nd_proxy.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.nd_proxy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.nd_proxy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.nd_proxy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.nd_proxy.delete(mkey='item-name')

.. _system-netflow:

netflow
~~~~~~~

Configure NetFlow.

**Python attribute:** ``netflow``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.netflow.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.netflow.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.netflow.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.netflow.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.netflow.delete(mkey='item-name')

.. _system-network-visibility:

network-visibility
~~~~~~~~~~~~~~~~~~

Configure network visibility settings.

**Python attribute:** ``network_visibility``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.network_visibility.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.network_visibility.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.network_visibility.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.network_visibility.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.network_visibility.delete(mkey='item-name')

.. _system-ngfw-settings:

ngfw-settings
~~~~~~~~~~~~~

Configure IPS NGFW policy-mode VDOM settings.

**Python attribute:** ``ngfw_settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ngfw_settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ngfw_settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ngfw_settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ngfw_settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ngfw_settings.delete(mkey='item-name')

.. _system-np6xlite:

np6xlite
~~~~~~~~

Configure NP6XLITE attributes.

**Python attribute:** ``np6xlite``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.np6xlite.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.np6xlite.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.np6xlite.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.np6xlite.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.np6xlite.delete(mkey='item-name')

.. _system-npu:

npu
~~~

Configure NPU attributes.

**Python attribute:** ``npu``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.npu.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.npu.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.npu.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.npu.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.npu.delete(mkey='item-name')

.. _system-ntp:

ntp
~~~

Configure system NTP information.

**Python attribute:** ``ntp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ntp.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ntp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ntp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ntp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ntp.delete(mkey='item-name')

.. _system-object-tagging:

object-tagging
~~~~~~~~~~~~~~

Configure object tagging.

**Python attribute:** ``object_tagging``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.object_tagging.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.object_tagging.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.object_tagging.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.object_tagging.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.object_tagging.delete(mkey='item-name')

.. _system-password-policy:

password-policy
~~~~~~~~~~~~~~~

Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.

**Python attribute:** ``password_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.password_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.password_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.password_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.password_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.password_policy.delete(mkey='item-name')

.. _system-password-policy-guest-admin:

password-policy-guest-admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the password policy for guest administrators.

**Python attribute:** ``password_policy_guest_admin``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.password_policy_guest_admin.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.password_policy_guest_admin.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.password_policy_guest_admin.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.password_policy_guest_admin.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.password_policy_guest_admin.delete(mkey='item-name')

.. _system-pcp-server:

pcp-server
~~~~~~~~~~

Configure PCP server information.

**Python attribute:** ``pcp_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.pcp_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.pcp_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.pcp_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.pcp_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.pcp_server.delete(mkey='item-name')

.. _system-physical-switch:

physical-switch
~~~~~~~~~~~~~~~

Configure physical switches.

**Python attribute:** ``physical_switch``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.physical_switch.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.physical_switch.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.physical_switch.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.physical_switch.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.physical_switch.delete(mkey='item-name')

.. _system-pppoe-interface:

pppoe-interface
~~~~~~~~~~~~~~~

Configure the PPPoE interfaces.

**Python attribute:** ``pppoe_interface``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.pppoe_interface.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.pppoe_interface.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.pppoe_interface.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.pppoe_interface.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.pppoe_interface.delete(mkey='item-name')

.. _system-probe-response:

probe-response
~~~~~~~~~~~~~~

Configure system probe response.

**Python attribute:** ``probe_response``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.probe_response.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.probe_response.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.probe_response.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.probe_response.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.probe_response.delete(mkey='item-name')

.. _system-proxy-arp:

proxy-arp
~~~~~~~~~

Configure proxy-ARP.

**Python attribute:** ``proxy_arp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.proxy_arp.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.proxy_arp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.proxy_arp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.proxy_arp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.proxy_arp.delete(mkey='item-name')

.. _system-ptp:

ptp
~~~

Configure system PTP information.

**Python attribute:** ``ptp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ptp.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ptp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ptp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ptp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ptp.delete(mkey='item-name')

.. _system-replacemsg-group:

replacemsg-group
~~~~~~~~~~~~~~~~

Configure replacement message groups.

**Python attribute:** ``replacemsg_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.replacemsg_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.replacemsg_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.replacemsg_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.replacemsg_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.replacemsg_group.delete(mkey='item-name')

.. _system-replacemsg-image:

replacemsg-image
~~~~~~~~~~~~~~~~

Configure replacement message images.

**Python attribute:** ``replacemsg_image``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.replacemsg_image.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.replacemsg_image.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.replacemsg_image.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.replacemsg_image.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.replacemsg_image.delete(mkey='item-name')

.. _system-resource-limits:

resource-limits
~~~~~~~~~~~~~~~

Configure resource limits.

**Python attribute:** ``resource_limits``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.resource_limits.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.resource_limits.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.resource_limits.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.resource_limits.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.resource_limits.delete(mkey='item-name')

.. _system-saml:

saml
~~~~

Global settings for SAML authentication.

**Python attribute:** ``saml``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.saml.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.saml.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.saml.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.saml.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.saml.delete(mkey='item-name')

.. _system-sdn-connector:

sdn-connector
~~~~~~~~~~~~~

Configure connection to SDN Connector.

**Python attribute:** ``sdn_connector``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sdn_connector.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sdn_connector.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sdn_connector.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sdn_connector.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sdn_connector.delete(mkey='item-name')

.. _system-sdn-proxy:

sdn-proxy
~~~~~~~~~

Configure SDN proxy.

**Python attribute:** ``sdn_proxy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sdn_proxy.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sdn_proxy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sdn_proxy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sdn_proxy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sdn_proxy.delete(mkey='item-name')

.. _system-sdn-vpn:

sdn-vpn
~~~~~~~

Configure public cloud VPN service.

**Python attribute:** ``sdn_vpn``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sdn_vpn.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sdn_vpn.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sdn_vpn.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sdn_vpn.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sdn_vpn.delete(mkey='item-name')

.. _system-sdwan:

sdwan
~~~~~

Configure redundant Internet connections with multiple outbound links and health-check profiles.

**Python attribute:** ``sdwan``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sdwan.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sdwan.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sdwan.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sdwan.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sdwan.delete(mkey='item-name')

.. _system-session-helper:

session-helper
~~~~~~~~~~~~~~

Configure session helper.

**Python attribute:** ``session_helper``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.session_helper.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.session_helper.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.session_helper.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.session_helper.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.session_helper.delete(mkey='item-name')

.. _system-session-ttl:

session-ttl
~~~~~~~~~~~

Configure global session TTL timers for this FortiGate.

**Python attribute:** ``session_ttl``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.session_ttl.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.session_ttl.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.session_ttl.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.session_ttl.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.session_ttl.delete(mkey='item-name')

.. _system-settings:

settings
~~~~~~~~

Configure VDOM settings.

**Python attribute:** ``settings``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.settings.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.settings.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.settings.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.settings.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.settings.delete(mkey='item-name')

.. _system-sflow:

sflow
~~~~~

Configure sFlow.

**Python attribute:** ``sflow``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sflow.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sflow.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sflow.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sflow.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sflow.delete(mkey='item-name')

.. _system-sit-tunnel:

sit-tunnel
~~~~~~~~~~

Configure IPv6 tunnel over IPv4.

**Python attribute:** ``sit_tunnel``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sit_tunnel.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sit_tunnel.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sit_tunnel.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sit_tunnel.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sit_tunnel.delete(mkey='item-name')

.. _system-sms-server:

sms-server
~~~~~~~~~~

Configure SMS server for sending SMS messages to support user authentication.

**Python attribute:** ``sms_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sms_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sms_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sms_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sms_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sms_server.delete(mkey='item-name')

.. _system-sov-sase:

sov-sase
~~~~~~~~

Configure Sovereign SASE.

**Python attribute:** ``sov_sase``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sov_sase.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sov_sase.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sov_sase.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sov_sase.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sov_sase.delete(mkey='item-name')

.. _system-speed-test-schedule:

speed-test-schedule
~~~~~~~~~~~~~~~~~~~

Speed test schedule for each interface.

**Python attribute:** ``speed_test_schedule``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.speed_test_schedule.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.speed_test_schedule.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.speed_test_schedule.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.speed_test_schedule.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.speed_test_schedule.delete(mkey='item-name')

.. _system-speed-test-server:

speed-test-server
~~~~~~~~~~~~~~~~~

Configure speed test server list.

**Python attribute:** ``speed_test_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.speed_test_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.speed_test_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.speed_test_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.speed_test_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.speed_test_server.delete(mkey='item-name')

.. _system-speed-test-setting:

speed-test-setting
~~~~~~~~~~~~~~~~~~

Configure speed test setting.

**Python attribute:** ``speed_test_setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.speed_test_setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.speed_test_setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.speed_test_setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.speed_test_setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.speed_test_setting.delete(mkey='item-name')

.. _system-ssh-config:

ssh-config
~~~~~~~~~~

Configure SSH config.

**Python attribute:** ``ssh_config``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.ssh_config.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.ssh_config.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.ssh_config.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.ssh_config.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.ssh_config.delete(mkey='item-name')

.. _system-sso-admin:

sso-admin
~~~~~~~~~

Configure SSO admin users.

**Python attribute:** ``sso_admin``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sso_admin.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sso_admin.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sso_admin.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sso_admin.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sso_admin.delete(mkey='item-name')

.. _system-sso-forticloud-admin:

sso-forticloud-admin
~~~~~~~~~~~~~~~~~~~~

Configure FortiCloud SSO admin users.

**Python attribute:** ``sso_forticloud_admin``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sso_forticloud_admin.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sso_forticloud_admin.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sso_forticloud_admin.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sso_forticloud_admin.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sso_forticloud_admin.delete(mkey='item-name')

.. _system-sso-fortigate-cloud-admin:

sso-fortigate-cloud-admin
~~~~~~~~~~~~~~~~~~~~~~~~~

Configure FortiCloud SSO admin users.

**Python attribute:** ``sso_fortigate_cloud_admin``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.sso_fortigate_cloud_admin.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.sso_fortigate_cloud_admin.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.sso_fortigate_cloud_admin.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.sso_fortigate_cloud_admin.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.sso_fortigate_cloud_admin.delete(mkey='item-name')

.. _system-standalone-cluster:

standalone-cluster
~~~~~~~~~~~~~~~~~~

Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.

**Python attribute:** ``standalone_cluster``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.standalone_cluster.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.standalone_cluster.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.standalone_cluster.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.standalone_cluster.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.standalone_cluster.delete(mkey='item-name')

.. _system-storage:

storage
~~~~~~~

Configure logical storage.

**Python attribute:** ``storage``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.storage.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.storage.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.storage.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.storage.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.storage.delete(mkey='item-name')

.. _system-stp:

stp
~~~

Configure Spanning Tree Protocol (STP).

**Python attribute:** ``stp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.stp.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.stp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.stp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.stp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.stp.delete(mkey='item-name')

.. _system-switch-interface:

switch-interface
~~~~~~~~~~~~~~~~

Configure software switch interfaces by grouping physical and WiFi interfaces.

**Python attribute:** ``switch_interface``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.switch_interface.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.switch_interface.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.switch_interface.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.switch_interface.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.switch_interface.delete(mkey='item-name')

.. _system-timezone:

timezone
~~~~~~~~

Show timezone.

**Python attribute:** ``timezone``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.timezone.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.timezone.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.timezone.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.timezone.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.timezone.delete(mkey='item-name')

.. _system-tos-based-priority:

tos-based-priority
~~~~~~~~~~~~~~~~~~

Configure Type of Service (ToS) based priority table to set network traffic priorities.

**Python attribute:** ``tos_based_priority``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.tos_based_priority.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.tos_based_priority.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.tos_based_priority.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.tos_based_priority.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.tos_based_priority.delete(mkey='item-name')

.. _system-vdom:

vdom
~~~~

Configure virtual domain.

**Python attribute:** ``vdom``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom.delete(mkey='item-name')

.. _system-vdom-dns:

vdom-dns
~~~~~~~~

Configure DNS servers for a non-management VDOM.

**Python attribute:** ``vdom_dns``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_dns.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_dns.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_dns.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_dns.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_dns.delete(mkey='item-name')

.. _system-vdom-exception:

vdom-exception
~~~~~~~~~~~~~~

Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.

**Python attribute:** ``vdom_exception``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_exception.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_exception.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_exception.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_exception.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_exception.delete(mkey='item-name')

.. _system-vdom-link:

vdom-link
~~~~~~~~~

Configure VDOM links.

**Python attribute:** ``vdom_link``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_link.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_link.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_link.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_link.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_link.delete(mkey='item-name')

.. _system-vdom-netflow:

vdom-netflow
~~~~~~~~~~~~

Configure NetFlow per VDOM.

**Python attribute:** ``vdom_netflow``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_netflow.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_netflow.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_netflow.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_netflow.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_netflow.delete(mkey='item-name')

.. _system-vdom-property:

vdom-property
~~~~~~~~~~~~~

Configure VDOM property.

**Python attribute:** ``vdom_property``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_property.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_property.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_property.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_property.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_property.delete(mkey='item-name')

.. _system-vdom-radius-server:

vdom-radius-server
~~~~~~~~~~~~~~~~~~

Configure a RADIUS server to use as a RADIUS Single Sign On (RSSO) server for this VDOM.

**Python attribute:** ``vdom_radius_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_radius_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_radius_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_radius_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_radius_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_radius_server.delete(mkey='item-name')

.. _system-vdom-sflow:

vdom-sflow
~~~~~~~~~~

Configure sFlow per VDOM to add or change the IP address and UDP port that FortiGate sFlow agents in this VDOM use to send sFlow datagrams to an sFlow collector.

**Python attribute:** ``vdom_sflow``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vdom_sflow.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vdom_sflow.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vdom_sflow.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vdom_sflow.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vdom_sflow.delete(mkey='item-name')

.. _system-virtual-switch:

virtual-switch
~~~~~~~~~~~~~~

Configure virtual hardware switch interfaces.

**Python attribute:** ``virtual_switch``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.virtual_switch.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.virtual_switch.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.virtual_switch.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.virtual_switch.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.virtual_switch.delete(mkey='item-name')

.. _system-virtual-wire-pair:

virtual-wire-pair
~~~~~~~~~~~~~~~~~

Configure virtual wire pairs.

**Python attribute:** ``virtual_wire_pair``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.virtual_wire_pair.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.virtual_wire_pair.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.virtual_wire_pair.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.virtual_wire_pair.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.virtual_wire_pair.delete(mkey='item-name')

.. _system-vne-interface:

vne-interface
~~~~~~~~~~~~~

Configure virtual network enabler tunnels.

**Python attribute:** ``vne_interface``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vne_interface.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vne_interface.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vne_interface.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vne_interface.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vne_interface.delete(mkey='item-name')

.. _system-vxlan:

vxlan
~~~~~

Configure VXLAN devices.

**Python attribute:** ``vxlan``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.vxlan.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.vxlan.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.vxlan.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.vxlan.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.vxlan.delete(mkey='item-name')

.. _system-wccp:

wccp
~~~~

Configure WCCP.

**Python attribute:** ``wccp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.wccp.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.wccp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.wccp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.wccp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.wccp.delete(mkey='item-name')

.. _system-zone:

zone
~~~~

Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead of individual interfaces in the zone.

**Python attribute:** ``zone``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.system.zone.get()
   
   # Get specific item
   item = fgt.api.cmdb.system.zone.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.system.zone.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.system.zone.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.system.zone.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.system.accprofile.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.system.accprofile.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.system.accprofile.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.system.accprofile.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.system.accprofile.delete(mkey='config-name')

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
