# Firewall Policy Convenience Wrapper

The `FirewallPolicy` wrapper provides an intuitive, GUI-like interface for managing firewall policies, with explicit parameters matching FortiOS terminology.

## Usage

Instead of using the low-level REST API:
```python
# Old way - REST API
fgt.api.cmdb.firewall.policy.post(data={
    'name': 'Allow-Web',
    'srcintf': [{'name': 'port1'}],
    'dstintf': [{'name': 'port2'}],
    'srcaddr': [{'name': 'internal-net'}],
    'dstaddr': [{'name': 'all'}],
    'action': 'accept',
    'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
    'schedule': 'always',
    'nat': 'enable'
})
```

Use the convenience wrapper with explicit parameters:
```python
# New way - Convenience wrapper
fgt.firewall.policy.create(
    name='Allow-Web',
    srcintf=['port1'],
    dstintf=['port2'],
    srcaddr=['internal-net'],
    dstaddr=['all'],
    action='accept',
    service=['HTTP', 'HTTPS'],
    nat='enable'
)
```

## Create Policy

Create a policy with security profiles:

```python
result = fgt.firewall.policy.create(
    name='Secure-Web-Access',
    srcintf=['internal'],
    dstintf=['wan1'],
    srcaddr=['LAN-Subnet'],
    dstaddr=['all'],
    service=['HTTP', 'HTTPS'],
    action='accept',
    schedule='always',
    # Inspection
    inspection_mode='proxy',
    ssl_ssh_profile='deep-inspection',
    # Security profiles
    av_profile='default',
    webfilter_profile='default',
    ips_sensor='default',
    application_list='default',
    dlp_profile='default',
    # Logging
    logtraffic='all',
    logtraffic_start='enable',
    # Advanced features
    webcache='enable',
    http_policy_redirect='enable',
    comments='Created via API wrapper'
)
```

## Update Policy

Update only the fields you need to change:

```python
# Enable deep inspection on existing policy
result = fgt.firewall.policy.update(
    policy_id=2,
    inspection_mode='proxy',
    ssl_ssh_profile='deep-inspection',
    passive_wan_health_measurement='enable',
    webcache='enable',
    wccp='enable',
    disclaimer='enable',
    captive_portal_exempt='enable'
)
```

## Get Policy

```python
# Get all policies
policies = fgt.firewall.policy.get()

# Get specific policy by ID
policy = fgt.firewall.policy.get(policy_id=1)

# Get policy by name
policy = fgt.firewall.policy.get_by_name('Allow-Web')

# Get with filter
policies = fgt.firewall.policy.get(filter='srcintf==port1')
```

## Delete Policy

```python
result = fgt.firewall.policy.delete(policy_id=5)
```

## Check Existence

```python
if fgt.firewall.policy.exists(policy_id=1):
    print("Policy exists")
```

## Enable/Disable Policy

```python
# Disable policy temporarily
fgt.firewall.policy.disable(policy_id=10)

# Re-enable policy
fgt.firewall.policy.enable(policy_id=10)
```

## Move Policy

Reorder policies in the policy list:

```python
# Move policy 5 before policy 3
fgt.firewall.policy.move(policy_id=5, position='before', reference_id=3)

# Move policy 10 after policy 8
fgt.firewall.policy.move(policy_id=10, position='after', reference_id=8)
```

## Clone Policy

Duplicate an existing policy with modifications:

```python
# Clone policy 1 with a new name
result = fgt.firewall.policy.clone(
    policy_id=1,
    new_name='Cloned-Policy',
    additional_changes={'comments': 'Cloned from policy 1'}
)
```

## Available Parameters

**Total: 150+ parameters covering all FortiOS 7.6.5 firewall policy features**

### Required (for create)
- `name` - Policy name
- `srcintf` - Source interface names (list)
- `dstintf` - Destination interface names (list)
- `srcaddr` - Source address names (list)
- `dstaddr` - Destination address names (list)

### Common Optional
- `action` - 'accept', 'deny', 'ipsec' (default: 'accept')
- `schedule` - Schedule name (default: 'always')
- `service` - Service names (default: ['ALL'])
- `status` - 'enable' or 'disable' (default: 'enable')

### IPv6 Support
- `srcaddr6` - Source IPv6 addresses (list)
- `dstaddr6` - Destination IPv6 addresses (list)
- `srcaddr6_negate` - Negate IPv6 source
- `dstaddr6_negate` - Negate IPv6 destination

### Internet Services (IPv4 & IPv6)
- **Destination IPv4:** `internet_service`, `internet_service_name`, `internet_service_group`, `internet_service_custom`, `internet_service_custom_group`, `internet_service_negate`
- **Source IPv4:** `internet_service_src`, `internet_service_src_name`, `internet_service_src_group`, etc.
- **Destination IPv6:** `internet_service6`, `internet_service6_name`, `internet_service6_group`, etc.
- **Source IPv6:** `internet_service6_src`, `internet_service6_src_name`, etc.

### Inspection & NAT
- `inspection_mode` - 'proxy' or 'flow'
- `nat` - 'enable' or 'disable'
- `nat64`, `nat46` - IPv6/IPv4 NAT
- `ippool`, `poolname`, `poolname6` - IP pools
- `natip` - NAT IP address
- `fixedport`, `port_preserve` - Port handling

### VPN
- `vpntunnel` - VPN tunnel name
- `inbound`, `outbound` - VPN directions
- `natinbound`, `natoutbound` - VPN NAT

### Security Profiles (20+)
- `av_profile` - Antivirus profile
- `webfilter_profile` - Web filter profile
- `dnsfilter_profile` - DNS filter profile
- `emailfilter_profile` - Email filter profile
- `dlp_profile` - DLP profile
- `file_filter_profile` - File filter profile
- `ips_sensor` - IPS sensor
- `application_list` - Application control
- `voip_profile` - VoIP profile
- `icap_profile` - ICAP profile
- `waf_profile` - Web application firewall
- `ssh_filter_profile` - SSH filter
- `ssl_ssh_profile` - SSL/SSH inspection
- `casb_profile` - CASB profile
- `videofilter_profile` - Video filter
- `sctp_filter_profile` - SCTP filter
- `diameter_filter_profile` - Diameter filter
- `virtual_patch_profile` - Virtual patching
- `profile_protocol_options` - Protocol options
- `profile_type`, `profile_group` - Profile grouping

### Users & Authentication
- `users`, `groups` - User/group names (lists)
- `fsso_groups` - FSSO groups
- `ntlm`, `ntlm_guest` - NTLM authentication
- `auth_path`, `auth_cert` - Authentication settings
- `email_collect` - Email collection

### ZTNA & Security Posture
- `ztna_status` - 'enable' or 'disable'
- `ztna_device_ownership` - Device ownership
- `ztna_ems_tag` - EMS tags (list)
- `ztna_ems_tag_secondary` - Secondary EMS tags (list)
- `ztna_tags_match_logic` - Tag matching logic
- `ztna_geo_tag` - Geographic tags
- `ztna_policy_redirect` - Policy redirect

### Reputation & Geo-IP
- `reputation_minimum`, `reputation_direction` - IPv4 reputation
- `reputation_minimum6`, `reputation_direction6` - IPv6 reputation
- `geoip_anycast`, `geoip_match` - Geographic matching

### Security Groups
- `sgt`, `sgt_check` - Security Group Tags
- `identity_based_route` - Identity routing

### Traffic Shaping & QoS
- `traffic_shaper`, `traffic_shaper_reverse` - Traffic shaping
- `per_ip_shaper` - Per-IP shaping
- `vlan_cos_fwd`, `vlan_cos_rev` - VLAN CoS
- `diffserv_forward`, `diffserv_reverse` - DiffServ
- `tos`, `tos_mask`, `tos_negate` - Type of Service

### Session Control
- `send_deny_packet` - Send deny packet
- `firewall_session_dirty` - Session handling
- `schedule_timeout` - Schedule timeout
- `policy_expiry`, `policy_expiry_date` - Policy expiration
- `session_ttl`, `timeout_send_rst` - Session timeouts

### TCP/IP Settings
- `tcp_mss_sender`, `tcp_mss_receiver` - TCP MSS
- `tcp_session_without_syn` - TCP SYN handling
- `anti_replay` - Anti-replay

### Advanced Features
- `http_policy_redirect`, `ssh_policy_redirect` - Policy redirects
- `webproxy_profile`, `webproxy_forward_server` - Web proxy
- `webcache`, `wccp` - Caching
- `disclaimer`, `captive_portal_exempt` - User interaction
- `decrypted_traffic_mirror` - Traffic mirroring
- `passive_wan_health_measurement` - WAN monitoring
- `app_monitor`, `dynamic_shaping`, `fec` - Performance features

### RTP & PCP
- `rtp_nat`, `rtp_addr` - RTP settings
- `pcp_outbound`, `pcp_inbound`, `pcp_poolname` - Port Control Protocol

### Negation Options
- `srcaddr_negate`, `dstaddr_negate` - Address negation
- `srcaddr6_negate`, `dstaddr6_negate` - IPv6 negation
- `service_negate` - Service negation
- `internet_service_negate`, `internet_service6_negate` - ISDB negation

### Logging
- `logtraffic` - 'all', 'utm', 'disable'
- `logtraffic_start` - 'enable' or 'disable'
- `log_http_transaction` - HTTP logging
- `capture_packet` - Packet capture
- `custom_log_fields` - Custom log fields
- `comments` - Policy comments

### Performance
- `auto_asic_offload`, `np_acceleration` - Hardware acceleration
- `delay_tcp_npu_session` - NPU session delay

### VIP & Matching
- `match_vip`, `match_vip_only` - VIP matching

### Other
- `uuid` - Policy UUID
- `src_vendor_mac` - Source vendor MAC
- `radius_mac_auth_bypass`, `radius_ip_auth_bypass` - RADIUS bypass

### API Options
- `vdom` - Virtual domain name
- `datasource` - Include datasource in response
- `with_meta` - Include metadata in response
- `data` - Additional fields as dictionary (merged with explicit parameters)

**Note:** Most list-based parameters accept both single values and lists. See docstrings for full type information.

## Combining Explicit and Data Parameters

You can mix explicit parameters with the `data` parameter for additional fields:

```python
result = fgt.firewall.policy.create(
    name='MyPolicy',
    srcintf=['port1'],
    dstintf=['port2'],
    srcaddr=['all'],
    dstaddr=['all'],
    ssl_ssh_profile='deep-inspection',
    # Additional fields via data parameter
    data={
        'utm-status': 'enable',
        'profile-group': 'custom-group',
        'custom-field': 'custom-value'
    }
)
```

The `data` parameter is merged with explicit parameters, allowing you to use both approaches simultaneously.
