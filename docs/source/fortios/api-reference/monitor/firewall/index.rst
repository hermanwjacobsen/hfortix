Firewall
========

Overview
--------

The ``monitor.firewall`` namespace provides configuration management for:

- :doc:`Acl <acl>` - Acl configuration endpoint.
- :doc:`Acl6 <acl6>` - Acl6 configuration endpoint.
- :doc:`Address6 Dynamic <address6_dynamic>` - Address6 Dynamic configuration endpoint.
- :doc:`Address Dynamic <address_dynamic>` - Address Dynamic configuration endpoint.
- :doc:`Address Fqdns <address_fqdns>` - Address Fqdns configuration endpoint.
- :doc:`Address Fqdns6 <address_fqdns6>` - Address Fqdns6 configuration endpoint.
- :doc:`Central Snat Map <central_snat_map>` - Central Snat Map configuration endpoint.
- :doc:`Check Addrgrp Exclude Mac Member <check_addrgrp_exclude_mac_member>` - Check Addrgrp Exclude Mac Member configuration endpoint.
- :doc:`Clearpass Address <clearpass_address>` - Clearpass Address configuration endpoint.
- :doc:`Dnat <dnat>` - Dnat configuration endpoint.
- :doc:`Gtp <gtp>` - Gtp configuration endpoint.
- :doc:`Gtp Runtime Statistics <gtp_runtime_statistics>` - Gtp Runtime Statistics configuration endpoint.
- :doc:`Gtp Statistics <gtp_statistics>` - Gtp Statistics configuration endpoint.
- :doc:`Health <health>` - Health configuration endpoint.
- :doc:`Internet Service Basic <internet_service_basic>` - Internet Service Basic configuration endpoint.
- :doc:`Internet Service Details <internet_service_details>` - Internet Service Details configuration endpoint.
- :doc:`Internet Service Fqdn <internet_service_fqdn>` - Internet Service Fqdn configuration endpoint.
- :doc:`Internet Service Fqdn Icon Ids <internet_service_fqdn_icon_ids>` - Internet Service Fqdn Icon Ids configuration endpoint.
- :doc:`Internet Service Match <internet_service_match>` - Internet Service Match configuration endpoint.
- :doc:`Internet Service Reputation <internet_service_reputation>` - Internet Service Reputation configuration endpoint.
- :doc:`IP Pool <ippool>` - IP Pool configuration endpoint.
- :doc:`Load Balance <load_balance>` - Load Balance configuration endpoint.
- :doc:`Local In <local_in>` - Local In configuration endpoint.
- :doc:`Local In6 <local_in6>` - Local In6 configuration endpoint.
- :doc:`Multicast Policy <multicast_policy>` - Multicast Policy configuration endpoint.
- :doc:`Multicast Policy6 <multicast_policy6>` - Multicast Policy6 configuration endpoint.
- :doc:`Network Service Dynamic <network_service_dynamic>` - Network Service Dynamic configuration endpoint.
- :doc:`Per IP Shaper <per_ip_shaper>` - Per IP Shaper configuration endpoint.
- :doc:`Policy <policy>` - Policy configuration endpoint.
- :doc:`Policy Lookup <policy_lookup>` - Policy Lookup configuration endpoint.
- :doc:`Proxy <proxy>` - Proxy configuration endpoint.
- :doc:`Proxy Policy <proxy_policy>` - Proxy Policy configuration endpoint.
- :doc:`Saas Application <saas_application>` - Saas Application configuration endpoint.
- :doc:`SDN Connector Filters <sdn_connector_filters>` - SDN Connector Filters configuration endpoint.
- :doc:`Security Policy <security_policy>` - Security Policy configuration endpoint.
- :doc:`Session <session>` - Session configuration endpoint.
- :doc:`Session6 <session6>` - Session6 configuration endpoint.
- :doc:`Sessions <sessions>` - Sessions configuration endpoint.
- :doc:`Shaper <shaper>` - Shaper configuration endpoint.
- :doc:`Uuid <uuid>` - Uuid configuration endpoint.
- :doc:`Uuid List <uuid_list>` - Uuid List configuration endpoint.
- :doc:`Uuid Type Lookup <uuid_type_lookup>` - Uuid Type Lookup configuration endpoint.
- :doc:`VIP Overlap <vip_overlap>` - VIP Overlap configuration endpoint.
- :doc:`ZTNA Firewall Policy <ztna_firewall_policy>` - ZTNA Firewall Policy configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.firewall.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   acl
   acl6
   address6_dynamic
   address_dynamic
   address_fqdns
   address_fqdns6
   central_snat_map
   check_addrgrp_exclude_mac_member
   clearpass_address
   dnat
   gtp
   gtp_runtime_statistics
   gtp_statistics
   health
   internet_service_basic
   internet_service_details
   internet_service_fqdn
   internet_service_fqdn_icon_ids
   internet_service_match
   internet_service_reputation
   ippool
   load_balance
   local_in
   local_in6
   multicast_policy
   multicast_policy6
   network_service_dynamic
   per_ip_shaper
   policy
   policy_lookup
   proxy
   proxy_policy
   saas_application
   sdn_connector_filters
   security_policy
   session
   session6
   sessions
   shaper
   uuid
   uuid_list
   uuid_type_lookup
   vip_overlap
   ztna_firewall_policy

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
