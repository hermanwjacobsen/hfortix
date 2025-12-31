Firewall
========

Configure IP to MAC binding settings configuration and management.

Overview
--------

The ``cmdb.firewall`` category provides configuration management for:

- **Dos Policy** - Configure IPv4 DoS policies.
- **Dos Policy6** - Configure IPv6 DoS policies.
- **Access Proxy** - Configure IPv4 access proxy.
- **Access Proxy Ssh Client Cert** - Configure Access Proxy SSH client certificate.
- **Access Proxy Virtual Host** - Configure Access Proxy virtual hosts.
- **Access Proxy6** - Configure IPv6 access proxy.
- **Address** - Configure IPv4 addresses.
- **Address6** - Configure IPv6 firewall addresses.
- **Address6 Template** - Configure IPv6 address templates.
- **Addrgrp** - Configure IPv4 address groups.
- **Addrgrp6** - Configure IPv6 address groups.
- **Auth Portal** - Configure firewall authentication portals.
- **Central Snat Map** - Configure IPv4 and IPv6 central SNAT policies.
- **City** - Define city table.
- **Country** - Define country table.
- **Decrypted Traffic Mirror** - Configure decrypted traffic mirror.
- **Dnstranslation** - Configure DNS translation.
- **Global** - Global firewall settings.
- **Identity Based Route** - Configure identity based routing.
- **Interface Policy** - Configure IPv4 interface policies.
- **Interface Policy6** - Configure IPv6 interface policies.
- **Internet Service** - Show Internet Service application.
- **Internet Service Addition** - Configure Internet Services Addition.
- **Internet Service Append** - Configure additional port mappings for Internet Services.
- **Internet Service Botnet** - Show Internet Service botnet.
- **Internet Service Custom** - Configure custom Internet Services.
- **Internet Service Custom Group** - Configure custom Internet Service group.
- **Internet Service Definition** - Configure Internet Service definition.
- **Internet Service Extension** - Configure Internet Services Extension.
- **Internet Service Fortiguard** - Configure FortiGuard Internet Services.
- **Internet Service Group** - Configure group of Internet Service.
- **Internet Service Ipbl Reason** - IP block list reason.
- **Internet Service Ipbl Vendor** - IP block list vendor.
- **Internet Service List** - Internet Service list.
- **Internet Service Name** - Define internet service names.
- **Internet Service Owner** - Internet Service owner.
- **Internet Service Reputation** - Show Internet Service reputation.
- **Internet Service Sld** - Internet Service Second Level Domain.
- **Internet Service Subapp** - Show Internet Service sub app ID.
- **Ip Translation** - Configure firewall IP-translation.
- **Ippool** - Configure IPv4 IP pools.
- **Ippool6** - Configure IPv6 IP pools.
- **Ldb Monitor** - Configure server load balancing health monitors.
- **Local In Policy** - Configure user defined IPv4 local-in policies.
- **Local In Policy6** - Configure user defined IPv6 local-in policies.
- **Multicast Address** - Configure multicast addresses.
- **Multicast Address6** - Configure IPv6 multicast address.
- **Multicast Policy** - Configure multicast NAT policies.
- **Multicast Policy6** - Configure IPv6 multicast NAT policies.
- **Network Service Dynamic** - Configure Dynamic Network Services.
- **On Demand Sniffer** - Configure on-demand packet sniffer.
- **Policy** - Configure IPv4/IPv6 policies.
- **Profile Group** - Configure profile groups.
- **Profile Protocol Options** - Configure protocol options.
- **Proxy Address** - Configure web proxy address.
- **Proxy Addrgrp** - Configure web proxy address group.
- **Proxy Policy** - Configure proxy policies.
- **Region** - Define region table.
- **Security Policy** - Configure NGFW IPv4/IPv6 application policies.
- **Shaping Policy** - Configure shaping policies.
- **Shaping Profile** - Configure shaping profiles.
- **Sniffer** - Configure sniffer.
- **Ssl Server** - Configure SSL servers.
- **Ssl Ssh Profile** - Configure SSL/SSH protocol options.
- **Traffic Class** - Configure names for shaping classes.
- **Ttl Policy** - Configure TTL policies.
- **Vendor Mac** - Show vendor and the MAC address they have.
- **Vendor Mac Summary** - Vendor MAC database summary.
- **Vip** - Configure virtual IP for IPv4.
- **Vip6** - Configure virtual IP for IPv6.
- **Vipgrp** - Configure IPv4 virtual IP groups.
- **Vipgrp6** - Configure IPv6 virtual IP groups.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.firewall

Available Endpoints
-------------------

**DoS-policy**
   Configure IPv4 DoS policies.
   
   .. code-block:: python
   
      # List all DoS-policy
      items = fgt.api.cmdb.firewall.DoS_policy.get()
      
      # Get specific DoS-policy
      item = fgt.api.cmdb.firewall.DoS_policy.get(mkey='name')

**DoS-policy6**
   Configure IPv6 DoS policies.
   
   .. code-block:: python
   
      # List all DoS-policy6
      items = fgt.api.cmdb.firewall.DoS_policy6.get()
      
      # Get specific DoS-policy6
      item = fgt.api.cmdb.firewall.DoS_policy6.get(mkey='name')

**access-proxy**
   Configure IPv4 access proxy.
   
   .. code-block:: python
   
      # List all access-proxy
      items = fgt.api.cmdb.firewall.access_proxy.get()
      
      # Get specific access-proxy
      item = fgt.api.cmdb.firewall.access_proxy.get(mkey='name')

**access-proxy-ssh-client-cert**
   Configure Access Proxy SSH client certificate.
   
   .. code-block:: python
   
      # List all access-proxy-ssh-client-cert
      items = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get()
      
      # Get specific access-proxy-ssh-client-cert
      item = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get(mkey='name')

**access-proxy-virtual-host**
   Configure Access Proxy virtual hosts.
   
   .. code-block:: python
   
      # List all access-proxy-virtual-host
      items = fgt.api.cmdb.firewall.access_proxy_virtual_host.get()
      
      # Get specific access-proxy-virtual-host
      item = fgt.api.cmdb.firewall.access_proxy_virtual_host.get(mkey='name')

**access-proxy6**
   Configure IPv6 access proxy.
   
   .. code-block:: python
   
      # List all access-proxy6
      items = fgt.api.cmdb.firewall.access_proxy6.get()
      
      # Get specific access-proxy6
      item = fgt.api.cmdb.firewall.access_proxy6.get(mkey='name')

**address**
   Configure IPv4 addresses.
   
   .. code-block:: python
   
      # List all address
      items = fgt.api.cmdb.firewall.address.get()
      
      # Get specific address
      item = fgt.api.cmdb.firewall.address.get(mkey='name')

**address6**
   Configure IPv6 firewall addresses.
   
   .. code-block:: python
   
      # List all address6
      items = fgt.api.cmdb.firewall.address6.get()
      
      # Get specific address6
      item = fgt.api.cmdb.firewall.address6.get(mkey='name')

**address6-template**
   Configure IPv6 address templates.
   
   .. code-block:: python
   
      # List all address6-template
      items = fgt.api.cmdb.firewall.address6_template.get()
      
      # Get specific address6-template
      item = fgt.api.cmdb.firewall.address6_template.get(mkey='name')

**addrgrp**
   Configure IPv4 address groups.
   
   .. code-block:: python
   
      # List all addrgrp
      items = fgt.api.cmdb.firewall.addrgrp.get()
      
      # Get specific addrgrp
      item = fgt.api.cmdb.firewall.addrgrp.get(mkey='name')

**addrgrp6**
   Configure IPv6 address groups.
   
   .. code-block:: python
   
      # List all addrgrp6
      items = fgt.api.cmdb.firewall.addrgrp6.get()
      
      # Get specific addrgrp6
      item = fgt.api.cmdb.firewall.addrgrp6.get(mkey='name')

**auth-portal**
   Configure firewall authentication portals.
   
   .. code-block:: python
   
      # List all auth-portal
      items = fgt.api.cmdb.firewall.auth_portal.get()
      
      # Get specific auth-portal
      item = fgt.api.cmdb.firewall.auth_portal.get(mkey='name')

**central-snat-map**
   Configure IPv4 and IPv6 central SNAT policies.
   
   .. code-block:: python
   
      # List all central-snat-map
      items = fgt.api.cmdb.firewall.central_snat_map.get()
      
      # Get specific central-snat-map
      item = fgt.api.cmdb.firewall.central_snat_map.get(mkey='name')

**city**
   Define city table.
   
   .. code-block:: python
   
      # List all city
      items = fgt.api.cmdb.firewall.city.get()
      
      # Get specific city
      item = fgt.api.cmdb.firewall.city.get(mkey='name')

**country**
   Define country table.
   
   .. code-block:: python
   
      # List all country
      items = fgt.api.cmdb.firewall.country.get()
      
      # Get specific country
      item = fgt.api.cmdb.firewall.country.get(mkey='name')

**decrypted-traffic-mirror**
   Configure decrypted traffic mirror.
   
   .. code-block:: python
   
      # List all decrypted-traffic-mirror
      items = fgt.api.cmdb.firewall.decrypted_traffic_mirror.get()
      
      # Get specific decrypted-traffic-mirror
      item = fgt.api.cmdb.firewall.decrypted_traffic_mirror.get(mkey='name')

**dnstranslation**
   Configure DNS translation.
   
   .. code-block:: python
   
      # List all dnstranslation
      items = fgt.api.cmdb.firewall.dnstranslation.get()
      
      # Get specific dnstranslation
      item = fgt.api.cmdb.firewall.dnstranslation.get(mkey='name')

**global**
   Global firewall settings.
   
   .. code-block:: python
   
      # List all global
      items = fgt.api.cmdb.firewall.global.get()
      
      # Get specific global
      item = fgt.api.cmdb.firewall.global.get(mkey='name')

**identity-based-route**
   Configure identity based routing.
   
   .. code-block:: python
   
      # List all identity-based-route
      items = fgt.api.cmdb.firewall.identity_based_route.get()
      
      # Get specific identity-based-route
      item = fgt.api.cmdb.firewall.identity_based_route.get(mkey='name')

**interface-policy**
   Configure IPv4 interface policies.
   
   .. code-block:: python
   
      # List all interface-policy
      items = fgt.api.cmdb.firewall.interface_policy.get()
      
      # Get specific interface-policy
      item = fgt.api.cmdb.firewall.interface_policy.get(mkey='name')

**interface-policy6**
   Configure IPv6 interface policies.
   
   .. code-block:: python
   
      # List all interface-policy6
      items = fgt.api.cmdb.firewall.interface_policy6.get()
      
      # Get specific interface-policy6
      item = fgt.api.cmdb.firewall.interface_policy6.get(mkey='name')

**internet-service**
   Show Internet Service application.
   
   .. code-block:: python
   
      # List all internet-service
      items = fgt.api.cmdb.firewall.internet_service.get()
      
      # Get specific internet-service
      item = fgt.api.cmdb.firewall.internet_service.get(mkey='name')

**internet-service-addition**
   Configure Internet Services Addition.
   
   .. code-block:: python
   
      # List all internet-service-addition
      items = fgt.api.cmdb.firewall.internet_service_addition.get()
      
      # Get specific internet-service-addition
      item = fgt.api.cmdb.firewall.internet_service_addition.get(mkey='name')

**internet-service-append**
   Configure additional port mappings for Internet Services.
   
   .. code-block:: python
   
      # List all internet-service-append
      items = fgt.api.cmdb.firewall.internet_service_append.get()
      
      # Get specific internet-service-append
      item = fgt.api.cmdb.firewall.internet_service_append.get(mkey='name')

**internet-service-botnet**
   Show Internet Service botnet.
   
   .. code-block:: python
   
      # List all internet-service-botnet
      items = fgt.api.cmdb.firewall.internet_service_botnet.get()
      
      # Get specific internet-service-botnet
      item = fgt.api.cmdb.firewall.internet_service_botnet.get(mkey='name')

**internet-service-custom**
   Configure custom Internet Services.
   
   .. code-block:: python
   
      # List all internet-service-custom
      items = fgt.api.cmdb.firewall.internet_service_custom.get()
      
      # Get specific internet-service-custom
      item = fgt.api.cmdb.firewall.internet_service_custom.get(mkey='name')

**internet-service-custom-group**
   Configure custom Internet Service group.
   
   .. code-block:: python
   
      # List all internet-service-custom-group
      items = fgt.api.cmdb.firewall.internet_service_custom_group.get()
      
      # Get specific internet-service-custom-group
      item = fgt.api.cmdb.firewall.internet_service_custom_group.get(mkey='name')

**internet-service-definition**
   Configure Internet Service definition.
   
   .. code-block:: python
   
      # List all internet-service-definition
      items = fgt.api.cmdb.firewall.internet_service_definition.get()
      
      # Get specific internet-service-definition
      item = fgt.api.cmdb.firewall.internet_service_definition.get(mkey='name')

**internet-service-extension**
   Configure Internet Services Extension.
   
   .. code-block:: python
   
      # List all internet-service-extension
      items = fgt.api.cmdb.firewall.internet_service_extension.get()
      
      # Get specific internet-service-extension
      item = fgt.api.cmdb.firewall.internet_service_extension.get(mkey='name')

**internet-service-fortiguard**
   Configure FortiGuard Internet Services.
   
   .. code-block:: python
   
      # List all internet-service-fortiguard
      items = fgt.api.cmdb.firewall.internet_service_fortiguard.get()
      
      # Get specific internet-service-fortiguard
      item = fgt.api.cmdb.firewall.internet_service_fortiguard.get(mkey='name')

**internet-service-group**
   Configure group of Internet Service.
   
   .. code-block:: python
   
      # List all internet-service-group
      items = fgt.api.cmdb.firewall.internet_service_group.get()
      
      # Get specific internet-service-group
      item = fgt.api.cmdb.firewall.internet_service_group.get(mkey='name')

**internet-service-ipbl-reason**
   IP block list reason.
   
   .. code-block:: python
   
      # List all internet-service-ipbl-reason
      items = fgt.api.cmdb.firewall.internet_service_ipbl_reason.get()
      
      # Get specific internet-service-ipbl-reason
      item = fgt.api.cmdb.firewall.internet_service_ipbl_reason.get(mkey='name')

**internet-service-ipbl-vendor**
   IP block list vendor.
   
   .. code-block:: python
   
      # List all internet-service-ipbl-vendor
      items = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.get()
      
      # Get specific internet-service-ipbl-vendor
      item = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.get(mkey='name')

**internet-service-list**
   Internet Service list.
   
   .. code-block:: python
   
      # List all internet-service-list
      items = fgt.api.cmdb.firewall.internet_service_list.get()
      
      # Get specific internet-service-list
      item = fgt.api.cmdb.firewall.internet_service_list.get(mkey='name')

**internet-service-name**
   Define internet service names.
   
   .. code-block:: python
   
      # List all internet-service-name
      items = fgt.api.cmdb.firewall.internet_service_name.get()
      
      # Get specific internet-service-name
      item = fgt.api.cmdb.firewall.internet_service_name.get(mkey='name')

**internet-service-owner**
   Internet Service owner.
   
   .. code-block:: python
   
      # List all internet-service-owner
      items = fgt.api.cmdb.firewall.internet_service_owner.get()
      
      # Get specific internet-service-owner
      item = fgt.api.cmdb.firewall.internet_service_owner.get(mkey='name')

**internet-service-reputation**
   Show Internet Service reputation.
   
   .. code-block:: python
   
      # List all internet-service-reputation
      items = fgt.api.cmdb.firewall.internet_service_reputation.get()
      
      # Get specific internet-service-reputation
      item = fgt.api.cmdb.firewall.internet_service_reputation.get(mkey='name')

**internet-service-sld**
   Internet Service Second Level Domain.
   
   .. code-block:: python
   
      # List all internet-service-sld
      items = fgt.api.cmdb.firewall.internet_service_sld.get()
      
      # Get specific internet-service-sld
      item = fgt.api.cmdb.firewall.internet_service_sld.get(mkey='name')

**internet-service-subapp**
   Show Internet Service sub app ID.
   
   .. code-block:: python
   
      # List all internet-service-subapp
      items = fgt.api.cmdb.firewall.internet_service_subapp.get()
      
      # Get specific internet-service-subapp
      item = fgt.api.cmdb.firewall.internet_service_subapp.get(mkey='name')

**ip-translation**
   Configure firewall IP-translation.
   
   .. code-block:: python
   
      # List all ip-translation
      items = fgt.api.cmdb.firewall.ip_translation.get()
      
      # Get specific ip-translation
      item = fgt.api.cmdb.firewall.ip_translation.get(mkey='name')

**ippool**
   Configure IPv4 IP pools.
   
   .. code-block:: python
   
      # List all ippool
      items = fgt.api.cmdb.firewall.ippool.get()
      
      # Get specific ippool
      item = fgt.api.cmdb.firewall.ippool.get(mkey='name')

**ippool6**
   Configure IPv6 IP pools.
   
   .. code-block:: python
   
      # List all ippool6
      items = fgt.api.cmdb.firewall.ippool6.get()
      
      # Get specific ippool6
      item = fgt.api.cmdb.firewall.ippool6.get(mkey='name')

**ldb-monitor**
   Configure server load balancing health monitors.
   
   .. code-block:: python
   
      # List all ldb-monitor
      items = fgt.api.cmdb.firewall.ldb_monitor.get()
      
      # Get specific ldb-monitor
      item = fgt.api.cmdb.firewall.ldb_monitor.get(mkey='name')

**local-in-policy**
   Configure user defined IPv4 local-in policies.
   
   .. code-block:: python
   
      # List all local-in-policy
      items = fgt.api.cmdb.firewall.local_in_policy.get()
      
      # Get specific local-in-policy
      item = fgt.api.cmdb.firewall.local_in_policy.get(mkey='name')

**local-in-policy6**
   Configure user defined IPv6 local-in policies.
   
   .. code-block:: python
   
      # List all local-in-policy6
      items = fgt.api.cmdb.firewall.local_in_policy6.get()
      
      # Get specific local-in-policy6
      item = fgt.api.cmdb.firewall.local_in_policy6.get(mkey='name')

**multicast-address**
   Configure multicast addresses.
   
   .. code-block:: python
   
      # List all multicast-address
      items = fgt.api.cmdb.firewall.multicast_address.get()
      
      # Get specific multicast-address
      item = fgt.api.cmdb.firewall.multicast_address.get(mkey='name')

**multicast-address6**
   Configure IPv6 multicast address.
   
   .. code-block:: python
   
      # List all multicast-address6
      items = fgt.api.cmdb.firewall.multicast_address6.get()
      
      # Get specific multicast-address6
      item = fgt.api.cmdb.firewall.multicast_address6.get(mkey='name')

**multicast-policy**
   Configure multicast NAT policies.
   
   .. code-block:: python
   
      # List all multicast-policy
      items = fgt.api.cmdb.firewall.multicast_policy.get()
      
      # Get specific multicast-policy
      item = fgt.api.cmdb.firewall.multicast_policy.get(mkey='name')

**multicast-policy6**
   Configure IPv6 multicast NAT policies.
   
   .. code-block:: python
   
      # List all multicast-policy6
      items = fgt.api.cmdb.firewall.multicast_policy6.get()
      
      # Get specific multicast-policy6
      item = fgt.api.cmdb.firewall.multicast_policy6.get(mkey='name')

**network-service-dynamic**
   Configure Dynamic Network Services.
   
   .. code-block:: python
   
      # List all network-service-dynamic
      items = fgt.api.cmdb.firewall.network_service_dynamic.get()
      
      # Get specific network-service-dynamic
      item = fgt.api.cmdb.firewall.network_service_dynamic.get(mkey='name')

**on-demand-sniffer**
   Configure on-demand packet sniffer.
   
   .. code-block:: python
   
      # List all on-demand-sniffer
      items = fgt.api.cmdb.firewall.on_demand_sniffer.get()
      
      # Get specific on-demand-sniffer
      item = fgt.api.cmdb.firewall.on_demand_sniffer.get(mkey='name')

**policy**
   Configure IPv4/IPv6 policies.
   
   .. code-block:: python
   
      # List all policy
      items = fgt.api.cmdb.firewall.policy.get()
      
      # Get specific policy
      item = fgt.api.cmdb.firewall.policy.get(mkey='name')

**profile-group**
   Configure profile groups.
   
   .. code-block:: python
   
      # List all profile-group
      items = fgt.api.cmdb.firewall.profile_group.get()
      
      # Get specific profile-group
      item = fgt.api.cmdb.firewall.profile_group.get(mkey='name')

**profile-protocol-options**
   Configure protocol options.
   
   .. code-block:: python
   
      # List all profile-protocol-options
      items = fgt.api.cmdb.firewall.profile_protocol_options.get()
      
      # Get specific profile-protocol-options
      item = fgt.api.cmdb.firewall.profile_protocol_options.get(mkey='name')

**proxy-address**
   Configure web proxy address.
   
   .. code-block:: python
   
      # List all proxy-address
      items = fgt.api.cmdb.firewall.proxy_address.get()
      
      # Get specific proxy-address
      item = fgt.api.cmdb.firewall.proxy_address.get(mkey='name')

**proxy-addrgrp**
   Configure web proxy address group.
   
   .. code-block:: python
   
      # List all proxy-addrgrp
      items = fgt.api.cmdb.firewall.proxy_addrgrp.get()
      
      # Get specific proxy-addrgrp
      item = fgt.api.cmdb.firewall.proxy_addrgrp.get(mkey='name')

**proxy-policy**
   Configure proxy policies.
   
   .. code-block:: python
   
      # List all proxy-policy
      items = fgt.api.cmdb.firewall.proxy_policy.get()
      
      # Get specific proxy-policy
      item = fgt.api.cmdb.firewall.proxy_policy.get(mkey='name')

**region**
   Define region table.
   
   .. code-block:: python
   
      # List all region
      items = fgt.api.cmdb.firewall.region.get()
      
      # Get specific region
      item = fgt.api.cmdb.firewall.region.get(mkey='name')

**security-policy**
   Configure NGFW IPv4/IPv6 application policies.
   
   .. code-block:: python
   
      # List all security-policy
      items = fgt.api.cmdb.firewall.security_policy.get()
      
      # Get specific security-policy
      item = fgt.api.cmdb.firewall.security_policy.get(mkey='name')

**shaping-policy**
   Configure shaping policies.
   
   .. code-block:: python
   
      # List all shaping-policy
      items = fgt.api.cmdb.firewall.shaping_policy.get()
      
      # Get specific shaping-policy
      item = fgt.api.cmdb.firewall.shaping_policy.get(mkey='name')

**shaping-profile**
   Configure shaping profiles.
   
   .. code-block:: python
   
      # List all shaping-profile
      items = fgt.api.cmdb.firewall.shaping_profile.get()
      
      # Get specific shaping-profile
      item = fgt.api.cmdb.firewall.shaping_profile.get(mkey='name')

**sniffer**
   Configure sniffer.
   
   .. code-block:: python
   
      # List all sniffer
      items = fgt.api.cmdb.firewall.sniffer.get()
      
      # Get specific sniffer
      item = fgt.api.cmdb.firewall.sniffer.get(mkey='name')

**ssl-server**
   Configure SSL servers.
   
   .. code-block:: python
   
      # List all ssl-server
      items = fgt.api.cmdb.firewall.ssl_server.get()
      
      # Get specific ssl-server
      item = fgt.api.cmdb.firewall.ssl_server.get(mkey='name')

**ssl-ssh-profile**
   Configure SSL/SSH protocol options.
   
   .. code-block:: python
   
      # List all ssl-ssh-profile
      items = fgt.api.cmdb.firewall.ssl_ssh_profile.get()
      
      # Get specific ssl-ssh-profile
      item = fgt.api.cmdb.firewall.ssl_ssh_profile.get(mkey='name')

**traffic-class**
   Configure names for shaping classes.
   
   .. code-block:: python
   
      # List all traffic-class
      items = fgt.api.cmdb.firewall.traffic_class.get()
      
      # Get specific traffic-class
      item = fgt.api.cmdb.firewall.traffic_class.get(mkey='name')

**ttl-policy**
   Configure TTL policies.
   
   .. code-block:: python
   
      # List all ttl-policy
      items = fgt.api.cmdb.firewall.ttl_policy.get()
      
      # Get specific ttl-policy
      item = fgt.api.cmdb.firewall.ttl_policy.get(mkey='name')

**vendor-mac**
   Show vendor and the MAC address they have.
   
   .. code-block:: python
   
      # List all vendor-mac
      items = fgt.api.cmdb.firewall.vendor_mac.get()
      
      # Get specific vendor-mac
      item = fgt.api.cmdb.firewall.vendor_mac.get(mkey='name')

**vendor-mac-summary**
   Vendor MAC database summary.
   
   .. code-block:: python
   
      # List all vendor-mac-summary
      items = fgt.api.cmdb.firewall.vendor_mac_summary.get()
      
      # Get specific vendor-mac-summary
      item = fgt.api.cmdb.firewall.vendor_mac_summary.get(mkey='name')

**vip**
   Configure virtual IP for IPv4.
   
   .. code-block:: python
   
      # List all vip
      items = fgt.api.cmdb.firewall.vip.get()
      
      # Get specific vip
      item = fgt.api.cmdb.firewall.vip.get(mkey='name')

**vip6**
   Configure virtual IP for IPv6.
   
   .. code-block:: python
   
      # List all vip6
      items = fgt.api.cmdb.firewall.vip6.get()
      
      # Get specific vip6
      item = fgt.api.cmdb.firewall.vip6.get(mkey='name')

**vipgrp**
   Configure IPv4 virtual IP groups.
   
   .. code-block:: python
   
      # List all vipgrp
      items = fgt.api.cmdb.firewall.vipgrp.get()
      
      # Get specific vipgrp
      item = fgt.api.cmdb.firewall.vipgrp.get(mkey='name')

**vipgrp6**
   Configure IPv6 virtual IP groups.
   
   .. code-block:: python
   
      # List all vipgrp6
      items = fgt.api.cmdb.firewall.vipgrp6.get()
      
      # Get specific vipgrp6
      item = fgt.api.cmdb.firewall.vipgrp6.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.firewall.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.firewall.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.firewall.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.firewall.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.firewall.{endpoint}.delete(mkey='config-name')

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
