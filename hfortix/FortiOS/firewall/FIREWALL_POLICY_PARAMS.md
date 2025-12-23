# Firewall Policy Parameters Reference

This document lists all available parameters for the FirewallPolicy wrapper based on FortiOS 7.6.5 API.

## Parameter Categories

### Core Required Parameters
- `name`: Policy name (required for create)
- `srcintf`: Source interface(s) - single or list
- `dstintf`: Destination interface(s) - single or list
- `srcaddr`: Source address(es) - single or list
- `dstaddr`: Destination address(es) - single or list
- `action`: 'accept', 'deny', 'ipsec'
- `schedule`: Schedule name (default: 'always')
- `service`: Service(s) - single or list

### IPv6 Addresses
- `srcaddr6`: Source IPv6 address(es) - single or list
- `dstaddr6`: Destination IPv6 address(es) - single or list
- `srcaddr6_negate`: Negate IPv6 source match
- `dstaddr6_negate`: Negate IPv6 destination match

### Internet Services (IPv4)
- `internet_service`: Enable/disable Internet Services
- `internet_service_name`: Internet Service name(s) - single or list
- `internet_service_group`: Internet Service group(s) - single or list
- `internet_service_custom`: Custom Internet Service(s) - single or list
- `internet_service_custom_group`: Custom IS group(s) - single or list
- `internet_service_negate`: Negate Internet Service match
- `network_service_dynamic`: Dynamic Network Service(s) - single or list
- `internet_service_fortiguard`: FortiGuard Internet Service(s) - single or list

### Internet Services Source (IPv4)
- `internet_service_src`: Enable/disable source Internet Services
- `internet_service_src_name`: Source IS name(s) - single or list
- `internet_service_src_group`: Source IS group(s) - single or list
- `internet_service_src_custom`: Source custom IS - single or list
- `internet_service_src_custom_group`: Source custom IS group(s) - single or list
- `internet_service_src_negate`: Negate source IS match
- `network_service_src_dynamic`: Source dynamic network service(s) - single or list
- `internet_service_src_fortiguard`: Source FortiGuard IS - single or list

### Internet Services (IPv6)
- `internet_service6`: Enable/disable IPv6 Internet Services
- `internet_service6_name`: IPv6 IS name(s) - single or list
- `internet_service6_group`: IPv6 IS group(s) - single or list
- `internet_service6_custom`: IPv6 custom IS - single or list
- `internet_service6_custom_group`: IPv6 custom IS group(s) - single or list
- `internet_service6_negate`: Negate IPv6 IS match
- `internet_service6_fortiguard`: FortiGuard IPv6 IS - single or list

### Internet Services Source (IPv6)
- `internet_service6_src`: Enable/disable IPv6 source IS
- `internet_service6_src_name`: IPv6 source IS name(s) - single or list
- `internet_service6_src_group`: IPv6 source IS group(s) - single or list
- `internet_service6_src_custom`: IPv6 source custom IS - single or list
- `internet_service6_src_custom_group`: IPv6 source custom IS group(s) - single or list
- `internet_service6_src_negate`: Negate IPv6 source IS match
- `internet_service6_src_fortiguard`: IPv6 source FortiGuard IS - single or list

### ZTNA
- `ztna_status`: Enable/disable ZTNA
- `ztna_device_ownership`: Enable/disable device ownership check
- `ztna_ems_tag`: ZTNA EMS tag(s) - single or list
- `ztna_ems_tag_secondary`: Secondary EMS tag(s) - single or list
- `ztna_tags_match_logic`: 'or' or 'and'
- `ztna_ems_tag_negate`: Negate EMS tag match
- `ztna_geo_tag`: ZTNA geo tag(s) - single or list
- `ztna_policy_redirect`: Enable/disable ZTNA policy redirect

### Security Profiles
- `utm_status`: Enable UTM profiles
- `profile_type`: 'single' or 'group'
- `profile_group`: Profile group name
- `profile_protocol_options`: Protocol options profile
- `ssl_ssh_profile`: SSL/SSH inspection profile
- `av_profile`: Antivirus profile
- `webfilter_profile`: Web filter profile
- `dnsfilter_profile`: DNS filter profile
- `emailfilter_profile`: Email filter profile
- `dlp_profile`: DLP profile
- `file_filter_profile`: File filter profile
- `ips_sensor`: IPS sensor
- `application_list`: Application control
- `voip_profile`: VoIP profile
- `ips_voip_filter`: VoIP IPS filter
- `sctp_filter_profile`: SCTP filter
- `diameter_filter_profile`: Diameter filter
- `virtual_patch_profile`: Virtual patch profile
- `icap_profile`: ICAP profile
- `videofilter_profile`: Video filter
- `waf_profile`: WAF profile
- `ssh_filter_profile`: SSH filter
- `casb_profile`: CASB profile

### NAT Settings
- `nat`: Enable/disable source NAT
- `nat64`: Enable/disable NAT64
- `nat46`: Enable/disable NAT46
- `ippool`: Enable IP pools
- `poolname`: IP pool name(s) - single or list
- `poolname6`: IPv6 pool name(s) - single or list
- `natip`: Source NAT IP
- `fixedport`: Prevent source port change
- `permit_any_host`: Fullcone NAT
- `permit_stun_host`: Accept STUN packets
- `port_preserve`: Preserve original source port
- `port_random`: Random source port
- `pcp_outbound`: PCP outbound SNAT
- `pcp_inbound`: PCP inbound DNAT
- `pcp_poolname`: PCP pool name(s) - single or list

### VPN Settings
- `vpntunnel`: IPsec VPN Phase 1 name
- `inbound`: Policy-based VPN inbound
- `outbound`: Policy-based VPN outbound
- `natinbound`: Policy-based VPN NAT inbound
- `natoutbound`: Policy-based VPN NAT outbound

### Inspection & Proxies
- `inspection_mode`: 'proxy' or 'flow'
- `http_policy_redirect`: HTTP(S) policy redirect
- `ssh_policy_redirect`: SSH policy redirect
- `webproxy_profile`: Webproxy profile name
- `webproxy_forward_server`: Webproxy forward server

### Users & Authentication
- `users`: User name(s) - single or list
- `groups`: User group name(s) - single or list
- `fsso_groups`: FSSO group name(s) - single or list
- `fsso_agent_for_ntlm`: FSSO agent for NTLM
- `ntlm`: Enable/disable NTLM
- `ntlm_guest`: Enable/disable NTLM guest
- `ntlm_enabled_browsers`: Browser user agents - single or list
- `auth_path`: Enable authentication-based routing
- `auth_cert`: HTTPS server certificate
- `auth_redirect_addr`: HTTP-to-HTTPS redirect address
- `disclaimer`: Enable user authentication disclaimer
- `email_collect`: Enable email collection

### Traffic Shaping
- `traffic_shaper`: Traffic shaper name
- `traffic_shaper_reverse`: Reverse traffic shaper
- `per_ip_shaper`: Per-IP traffic shaper

### Advanced Features
- `wccp`: Enable/disable WCCP
- `passive_wan_health_measurement`: Enable passive WAN health
- `app_monitor`: Enable TCP metrics logging
- `captive_portal_exempt`: Captive portal exemption
- `decrypted_traffic_mirror`: Decrypted traffic mirror name
- `dynamic_shaping`: Dynamic RADIUS shaping
- `fec`: Forward Error Correction
- `rtp_nat`: RTP NAT
- `rtp_addr`: RTP address(es) - single or list

### Logging
- `logtraffic`: 'all', 'utm', 'disable'
- `logtraffic_start`: Log session start
- `log_http_transaction`: Log HTTP transactions
- `capture_packet`: Enable packet capture
- `custom_log_fields`: Custom log fields - single or list

### Status & Control
- `status`: 'enable' or 'disable'
- `auto_asic_offload`: ASIC offloading
- `np_acceleration`: NP acceleration
- `firewall_session_dirty`: Session handling on config change
- `send_deny_packet`: Send RST on deny
- `timeout_send_rst`: Send RST on timeout
- `block_notification`: Block notification
- `dsri`: Enable DSRI
- `delay_tcp_npu_session`: TCP NPU session delay

### Policy Scheduling & Expiry
- `schedule`: Schedule name
- `schedule_timeout`: Force session end on timeout
- `policy_expiry`: Enable policy expiry
- `policy_expiry_date`: Expiry date (YYYY-MM-DD HH:MM:SS)
- `policy_expiry_date_utc`: Expiry in epoch format
- `session_ttl`: Session TTL in seconds

### QoS & VLAN
- `vlan_cos_fwd`: Forward VLAN priority (0-7)
- `vlan_cos_rev`: Reverse VLAN priority (0-7)
- `vlan_filter`: VLAN ranges
- `diffserv_copy`: Copy DiffServ values
- `diffserv_forward`: Set forward DiffServ
- `diffserv_reverse`: Set reverse DiffServ
- `diffservcode_forward`: Forward DiffServ code
- `diffservcode_rev`: Reverse DiffServ code
- `tos`: ToS value
- `tos_mask`: ToS mask
- `tos_negate`: Negate ToS match

### TCP/IP Settings
- `tcp_mss_sender`: Sender TCP MSS
- `tcp_mss_receiver`: Receiver TCP MSS
- `tcp_session_without_syn`: TCP session without SYN
- `anti_replay`: Anti-replay check

### Reputation & Geo-IP
- `reputation_minimum`: Minimum reputation score
- `reputation_direction`: 'source' or 'destination'
- `reputation_minimum6`: IPv6 minimum reputation
- `reputation_direction6`: IPv6 reputation direction
- `geoip_anycast`: Recognize anycast IPs
- `geoip_match`: 'physical-location' or 'registered-location'

### Security Groups & MAC
- `sgt_check`: Enable SGT check
- `sgt`: Security group tag(s) - single or list
- `src_vendor_mac`: Vendor MAC source ID(s) - single or list

### VIP Matching
- `match_vip`: Match DNATed packets
- `match_vip_only`: Match only DNATed packets

### RADIUS Bypass
- `radius_mac_auth_bypass`: MAC authentication bypass
- `radius_ip_auth_bypass`: IP authentication bypass

### Identity-Based Routing
- `identity_based_route`: Identity-based routing rule name

### Redirect & Replacement Messages
- `redirect_url`: Post-authentication redirect URL
- `replacemsg_override_group`: Override replacement message group

### Negation Options
- `srcaddr_negate`: Negate source address
- `dstaddr_negate`: Negate destination address
- `srcaddr6_negate`: Negate IPv6 source
- `dstaddr6_negate`: Negate IPv6 destination
- `service_negate`: Negate service
- `internet_service_negate`: Negate Internet Service
- `internet_service_src_negate`: Negate source IS
- `internet_service6_negate`: Negate IPv6 IS
- `internet_service6_src_negate`: Negate IPv6 source IS
- `ztna_ems_tag_negate`: Negate ZTNA EMS tags

### Miscellaneous
- `comments`: Policy comments
- `uuid`: Policy UUID
- `policyid`: Policy ID (read-only, auto-assigned)

### API Parameters
- `vdom`: Virtual domain
- `datasource`: Include datasource in response
- `with_meta`: Include metadata in response
- `data`: Additional fields as dictionary

## Notes

- All list-based parameters support both single values and lists:
  - `srcintf='port1'` OR `srcintf=['port1', 'port2']`
  - `users='admin'` OR `users=['admin', 'user1']`

- Internet Services are alternatives to traditional addresses
  - Use either `srcaddr` OR `internet_service_src_*`
  - Use either `dstaddr` OR `internet_service_*`

- The `_normalize_to_name_list()` helper automatically converts:
  - `'port1'` → `[{'name': 'port1'}]`
  - `['port1', 'port2']` → `[{'name': 'port1'}, {'name': 'port2'}]`
  - Filters out empty objects `{}`
