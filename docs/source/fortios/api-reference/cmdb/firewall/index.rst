Firewall
========

Overview
--------

The ``cmdb.firewall`` namespace provides configuration management for:

- :doc:`DoS Policy <DoS_policy>` - DoS Policy configuration endpoint.
- :doc:`DoS Policy6 <DoS_policy6>` - DoS Policy6 configuration endpoint.
- :doc:`Access Proxy <access_proxy>` - Access Proxy configuration endpoint.
- :doc:`Access Proxy6 <access_proxy6>` - Access Proxy6 configuration endpoint.
- :doc:`Access Proxy Ssh Client Cert <access_proxy_ssh_client_cert>` - Access Proxy Ssh Client Cert configuration endpoint.
- :doc:`Access Proxy Virtual Host <access_proxy_virtual_host>` - Access Proxy Virtual Host configuration endpoint.
- :doc:`Address <address>` - Address configuration endpoint.
- :doc:`Address6 <address6>` - Address6 configuration endpoint.
- :doc:`Address6 Template <address6_template>` - Address6 Template configuration endpoint.
- :doc:`Addrgrp <addrgrp>` - Addrgrp configuration endpoint.
- :doc:`Addrgrp6 <addrgrp6>` - Addrgrp6 configuration endpoint.
- :doc:`Auth Portal <auth_portal>` - Auth Portal configuration endpoint.
- :doc:`Central Snat Map <central_snat_map>` - Central Snat Map configuration endpoint.
- :doc:`City <city>` - City configuration endpoint.
- :doc:`Country <country>` - Country configuration endpoint.
- :doc:`Decrypted Traffic Mirror <decrypted_traffic_mirror>` - Decrypted Traffic Mirror configuration endpoint.
- :doc:`Dnstranslation <dnstranslation>` - Dnstranslation configuration endpoint.
- :doc:`Global <global_>` - Global configuration endpoint.
- :doc:`Identity Based Route <identity_based_route>` - Identity Based Route configuration endpoint.
- :doc:`Interface Policy <interface_policy>` - Interface Policy configuration endpoint.
- :doc:`Interface Policy6 <interface_policy6>` - Interface Policy6 configuration endpoint.
- :doc:`Internet Service <internet_service>` - Internet Service configuration endpoint.
- :doc:`Internet Service Addition <internet_service_addition>` - Internet Service Addition configuration endpoint.
- :doc:`Internet Service Append <internet_service_append>` - Internet Service Append configuration endpoint.
- :doc:`Internet Service Botnet <internet_service_botnet>` - Internet Service Botnet configuration endpoint.
- :doc:`Internet Service Custom <internet_service_custom>` - Internet Service Custom configuration endpoint.
- :doc:`Internet Service Custom Group <internet_service_custom_group>` - Internet Service Custom Group configuration endpoint.
- :doc:`Internet Service Definition <internet_service_definition>` - Internet Service Definition configuration endpoint.
- :doc:`Internet Service Extension <internet_service_extension>` - Internet Service Extension configuration endpoint.
- :doc:`Internet Service Fortiguard <internet_service_fortiguard>` - Internet Service Fortiguard configuration endpoint.
- :doc:`Internet Service Group <internet_service_group>` - Internet Service Group configuration endpoint.
- :doc:`Internet Service Ipbl Reason <internet_service_ipbl_reason>` - Internet Service Ipbl Reason configuration endpoint.
- :doc:`Internet Service Ipbl Vendor <internet_service_ipbl_vendor>` - Internet Service Ipbl Vendor configuration endpoint.
- :doc:`Internet Service List <internet_service_list>` - Internet Service List configuration endpoint.
- :doc:`Internet Service Name <internet_service_name>` - Internet Service Name configuration endpoint.
- :doc:`Internet Service Owner <internet_service_owner>` - Internet Service Owner configuration endpoint.
- :doc:`Internet Service Reputation <internet_service_reputation>` - Internet Service Reputation configuration endpoint.
- :doc:`Internet Service Sld <internet_service_sld>` - Internet Service Sld configuration endpoint.
- :doc:`Internet Service Subapp <internet_service_subapp>` - Internet Service Subapp configuration endpoint.
- :doc:`IP Translation <ip_translation>` - IP Translation configuration endpoint.
- :doc:`Ipmacbinding Setting <ipmacbinding_setting>` - Ipmacbinding Setting configuration endpoint.
- :doc:`Ipmacbinding Table <ipmacbinding_table>` - Ipmacbinding Table configuration endpoint.
- :doc:`IP Pool <ippool>` - IP Pool configuration endpoint.
- :doc:`IPv6 IP Pool <ippool6>` - IPv6 IP Pool configuration endpoint.
- :doc:`Ldb Monitor <ldb_monitor>` - Ldb Monitor configuration endpoint.
- :doc:`Local In Policy <local_in_policy>` - Local In Policy configuration endpoint.
- :doc:`Local In Policy6 <local_in_policy6>` - Local In Policy6 configuration endpoint.
- :doc:`Multicast Address <multicast_address>` - Multicast Address configuration endpoint.
- :doc:`Multicast Address6 <multicast_address6>` - Multicast Address6 configuration endpoint.
- :doc:`Multicast Policy <multicast_policy>` - Multicast Policy configuration endpoint.
- :doc:`Multicast Policy6 <multicast_policy6>` - Multicast Policy6 configuration endpoint.
- :doc:`Network Service Dynamic <network_service_dynamic>` - Network Service Dynamic configuration endpoint.
- :doc:`On Demand Sniffer <on_demand_sniffer>` - On Demand Sniffer configuration endpoint.
- :doc:`Policy <policy>` - Policy configuration endpoint.
- :doc:`Profile Group <profile_group>` - Profile Group configuration endpoint.
- :doc:`Profile Protocol Options <profile_protocol_options>` - Profile Protocol Options configuration endpoint.
- :doc:`Proxy Address <proxy_address>` - Proxy Address configuration endpoint.
- :doc:`Proxy Addrgrp <proxy_addrgrp>` - Proxy Addrgrp configuration endpoint.
- :doc:`Proxy Policy <proxy_policy>` - Proxy Policy configuration endpoint.
- :doc:`Region <region>` - Region configuration endpoint.
- :doc:`Schedule Group <schedule_group>` - Schedule Group configuration endpoint.
- :doc:`Schedule Onetime <schedule_onetime>` - Schedule Onetime configuration endpoint.
- :doc:`Schedule Recurring <schedule_recurring>` - Schedule Recurring configuration endpoint.
- :doc:`Security Policy <security_policy>` - Security Policy configuration endpoint.
- :doc:`Service Category <service_category>` - Service Category configuration endpoint.
- :doc:`Service Custom <service_custom>` - Service Custom configuration endpoint.
- :doc:`Service Group <service_group>` - Service Group configuration endpoint.
- :doc:`Shaper Per IP Shaper <shaper_per_ip_shaper>` - Shaper Per IP Shaper configuration endpoint.
- :doc:`Shaper Traffic Shaper <shaper_traffic_shaper>` - Shaper Traffic Shaper configuration endpoint.
- :doc:`Shaping Policy <shaping_policy>` - Shaping Policy configuration endpoint.
- :doc:`Shaping Profile <shaping_profile>` - Shaping Profile configuration endpoint.
- :doc:`Sniffer <sniffer>` - Sniffer configuration endpoint.
- :doc:`SSH Host Key <ssh_host_key>` - SSH Host Key configuration endpoint.
- :doc:`Ssh Local Ca <ssh_local_ca>` - Ssh Local Ca configuration endpoint.
- :doc:`Ssh Local Key <ssh_local_key>` - Ssh Local Key configuration endpoint.
- :doc:`Ssh Setting <ssh_setting>` - Ssh Setting configuration endpoint.
- :doc:`SSL Server <ssl_server>` - SSL Server configuration endpoint.
- :doc:`Ssl Setting <ssl_setting>` - Ssl Setting configuration endpoint.
- :doc:`SSL/SSH Profile <ssl_ssh_profile>` - SSL/SSH Profile configuration endpoint.
- :doc:`Traffic Class <traffic_class>` - Traffic Class configuration endpoint.
- :doc:`Ttl Policy <ttl_policy>` - Ttl Policy configuration endpoint.
- :doc:`Vendor Mac <vendor_mac>` - Vendor Mac configuration endpoint.
- :doc:`Vendor Mac Summary <vendor_mac_summary>` - Vendor Mac Summary configuration endpoint.
- :doc:`VIP <vip>` - VIP configuration endpoint.
- :doc:`VIP6 <vip6>` - VIP6 configuration endpoint.
- :doc:`VIP Group <vipgrp>` - VIP Group configuration endpoint.
- :doc:`VIP6 Group <vipgrp6>` - VIP6 Group configuration endpoint.
- :doc:`Wildcard Fqdn Custom <wildcard_fqdn_custom>` - Wildcard Fqdn Custom configuration endpoint.
- :doc:`Wildcard Fqdn Group <wildcard_fqdn_group>` - Wildcard Fqdn Group configuration endpoint.


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
   
   DoS_policy
   DoS_policy6
   access_proxy
   access_proxy6
   access_proxy_ssh_client_cert
   access_proxy_virtual_host
   address
   address6
   address6_template
   addrgrp
   addrgrp6
   auth_portal
   central_snat_map
   city
   country
   decrypted_traffic_mirror
   dnstranslation
   global_
   identity_based_route
   interface_policy
   interface_policy6
   internet_service
   internet_service_addition
   internet_service_append
   internet_service_botnet
   internet_service_custom
   internet_service_custom_group
   internet_service_definition
   internet_service_extension
   internet_service_fortiguard
   internet_service_group
   internet_service_ipbl_reason
   internet_service_ipbl_vendor
   internet_service_list
   internet_service_name
   internet_service_owner
   internet_service_reputation
   internet_service_sld
   internet_service_subapp
   ip_translation
   ipmacbinding_setting
   ipmacbinding_table
   ippool
   ippool6
   ldb_monitor
   local_in_policy
   local_in_policy6
   multicast_address
   multicast_address6
   multicast_policy
   multicast_policy6
   network_service_dynamic
   on_demand_sniffer
   policy
   profile_group
   profile_protocol_options
   proxy_address
   proxy_addrgrp
   proxy_policy
   region
   schedule_group
   schedule_onetime
   schedule_recurring
   security_policy
   service_category
   service_custom
   service_group
   shaper_per_ip_shaper
   shaper_traffic_shaper
   shaping_policy
   shaping_profile
   sniffer
   ssh_host_key
   ssh_local_ca
   ssh_local_key
   ssh_setting
   ssl_server
   ssl_setting
   ssl_ssh_profile
   traffic_class
   ttl_policy
   vendor_mac
   vendor_mac_summary
   vip
   vip6
   vipgrp
   vipgrp6
   wildcard_fqdn_custom
   wildcard_fqdn_group

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
