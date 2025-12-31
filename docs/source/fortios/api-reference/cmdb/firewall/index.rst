Firewall
========

Configure IP to MAC binding settings configuration and management.

Overview
--------

The ``cmdb.firewall`` category provides configuration management for:

- :doc:`Dos Policy <DoS-policy>` - Configure IPv4 DoS policies.
- :doc:`Dos Policy6 <DoS-policy6>` - Configure IPv6 DoS policies.
- :doc:`Access Proxy <access-proxy>` - Configure IPv4 access proxy.
- :doc:`Access Proxy Ssh Client Cert <access-proxy-ssh-client-cert>` - Configure Access Proxy SSH client certificate.
- :doc:`Access Proxy Virtual Host <access-proxy-virtual-host>` - Configure Access Proxy virtual hosts.
- :doc:`Access Proxy6 <access-proxy6>` - Configure IPv6 access proxy.
- :doc:`Address <address>` - Configure IPv4 addresses.
- :doc:`Address6 <address6>` - Configure IPv6 firewall addresses.
- :doc:`Address6 Template <address6-template>` - Configure IPv6 address templates.
- :doc:`Addrgrp <addrgrp>` - Configure IPv4 address groups.
- :doc:`Addrgrp6 <addrgrp6>` - Configure IPv6 address groups.
- :doc:`Auth Portal <auth-portal>` - Configure firewall authentication portals.
- :doc:`Central Snat Map <central-snat-map>` - Configure IPv4 and IPv6 central SNAT policies.
- :doc:`City <city>` - Define city table.
- :doc:`Country <country>` - Define country table.
- :doc:`Decrypted Traffic Mirror <decrypted-traffic-mirror>` - Configure decrypted traffic mirror.
- :doc:`Dnstranslation <dnstranslation>` - Configure DNS translation.
- :doc:`Global <global>` - Global firewall settings.
- :doc:`Identity Based Route <identity-based-route>` - Configure identity based routing.
- :doc:`Interface Policy <interface-policy>` - Configure IPv4 interface policies.
- :doc:`Interface Policy6 <interface-policy6>` - Configure IPv6 interface policies.
- :doc:`Internet Service <internet-service>` - Show Internet Service application.
- :doc:`Internet Service Addition <internet-service-addition>` - Configure Internet Services Addition.
- :doc:`Internet Service Append <internet-service-append>` - Configure additional port mappings for Internet Services.
- :doc:`Internet Service Botnet <internet-service-botnet>` - Show Internet Service botnet.
- :doc:`Internet Service Custom <internet-service-custom>` - Configure custom Internet Services.
- :doc:`Internet Service Custom Group <internet-service-custom-group>` - Configure custom Internet Service group.
- :doc:`Internet Service Definition <internet-service-definition>` - Configure Internet Service definition.
- :doc:`Internet Service Extension <internet-service-extension>` - Configure Internet Services Extension.
- :doc:`Internet Service Fortiguard <internet-service-fortiguard>` - Configure FortiGuard Internet Services.
- :doc:`Internet Service Group <internet-service-group>` - Configure group of Internet Service.
- :doc:`Internet Service Ipbl Reason <internet-service-ipbl-reason>` - IP block list reason.
- :doc:`Internet Service Ipbl Vendor <internet-service-ipbl-vendor>` - IP block list vendor.
- :doc:`Internet Service List <internet-service-list>` - Internet Service list.
- :doc:`Internet Service Name <internet-service-name>` - Define internet service names.
- :doc:`Internet Service Owner <internet-service-owner>` - Internet Service owner.
- :doc:`Internet Service Reputation <internet-service-reputation>` - Show Internet Service reputation.
- :doc:`Internet Service Sld <internet-service-sld>` - Internet Service Second Level Domain.
- :doc:`Internet Service Subapp <internet-service-subapp>` - Show Internet Service sub app ID.
- :doc:`Ip Translation <ip-translation>` - Configure firewall IP-translation.
- :doc:`Ippool <ippool>` - Configure IPv4 IP pools.
- :doc:`Ippool6 <ippool6>` - Configure IPv6 IP pools.
- :doc:`Ldb Monitor <ldb-monitor>` - Configure server load balancing health monitors.
- :doc:`Local In Policy <local-in-policy>` - Configure user defined IPv4 local-in policies.
- :doc:`Local In Policy6 <local-in-policy6>` - Configure user defined IPv6 local-in policies.
- :doc:`Multicast Address <multicast-address>` - Configure multicast addresses.
- :doc:`Multicast Address6 <multicast-address6>` - Configure IPv6 multicast address.
- :doc:`Multicast Policy <multicast-policy>` - Configure multicast NAT policies.
- :doc:`Multicast Policy6 <multicast-policy6>` - Configure IPv6 multicast NAT policies.
- :doc:`Network Service Dynamic <network-service-dynamic>` - Configure Dynamic Network Services.
- :doc:`On Demand Sniffer <on-demand-sniffer>` - Configure on-demand packet sniffer.
- :doc:`Policy <policy>` - Configure IPv4/IPv6 policies.
- :doc:`Profile Group <profile-group>` - Configure profile groups.
- :doc:`Profile Protocol Options <profile-protocol-options>` - Configure protocol options.
- :doc:`Proxy Address <proxy-address>` - Configure web proxy address.
- :doc:`Proxy Addrgrp <proxy-addrgrp>` - Configure web proxy address group.
- :doc:`Proxy Policy <proxy-policy>` - Configure proxy policies.
- :doc:`Region <region>` - Define region table.
- :doc:`Security Policy <security-policy>` - Configure NGFW IPv4/IPv6 application policies.
- :doc:`Shaping Policy <shaping-policy>` - Configure shaping policies.
- :doc:`Shaping Profile <shaping-profile>` - Configure shaping profiles.
- :doc:`Sniffer <sniffer>` - Configure sniffer.
- :doc:`Ssl Server <ssl-server>` - Configure SSL servers.
- :doc:`Ssl Ssh Profile <ssl-ssh-profile>` - Configure SSL/SSH protocol options.
- :doc:`Traffic Class <traffic-class>` - Configure names for shaping classes.
- :doc:`Ttl Policy <ttl-policy>` - Configure TTL policies.
- :doc:`Vendor Mac <vendor-mac>` - Show vendor and the MAC address they have.
- :doc:`Vendor Mac Summary <vendor-mac-summary>` - Vendor MAC database summary.
- :doc:`Vip <vip>` - Configure virtual IP for IPv4.
- :doc:`Vip6 <vip6>` - Configure virtual IP for IPv6.
- :doc:`Vipgrp <vipgrp>` - Configure IPv4 virtual IP groups.
- :doc:`Vipgrp6 <vipgrp6>` - Configure IPv6 virtual IP groups.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.firewall.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   DoS-policy
   DoS-policy6
   access-proxy
   access-proxy-ssh-client-cert
   access-proxy-virtual-host
   access-proxy6
   address
   address6
   address6-template
   addrgrp
   addrgrp6
   auth-portal
   central-snat-map
   city
   country
   decrypted-traffic-mirror
   dnstranslation
   global
   identity-based-route
   interface-policy
   interface-policy6
   internet-service
   internet-service-addition
   internet-service-append
   internet-service-botnet
   internet-service-custom
   internet-service-custom-group
   internet-service-definition
   internet-service-extension
   internet-service-fortiguard
   internet-service-group
   internet-service-ipbl-reason
   internet-service-ipbl-vendor
   internet-service-list
   internet-service-name
   internet-service-owner
   internet-service-reputation
   internet-service-sld
   internet-service-subapp
   ip-translation
   ippool
   ippool6
   ldb-monitor
   local-in-policy
   local-in-policy6
   multicast-address
   multicast-address6
   multicast-policy
   multicast-policy6
   network-service-dynamic
   on-demand-sniffer
   policy
   profile-group
   profile-protocol-options
   proxy-address
   proxy-addrgrp
   proxy-policy
   region
   security-policy
   shaping-policy
   shaping-profile
   sniffer
   ssl-server
   ssl-ssh-profile
   traffic-class
   ttl-policy
   vendor-mac
   vendor-mac-summary
   vip
   vip6
   vipgrp
   vipgrp6

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
