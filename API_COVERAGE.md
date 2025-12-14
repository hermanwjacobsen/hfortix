# API Coverage

This document tracks the implementation status of FortiOS API endpoints in the Fortinet Python SDK.

**Last Updated:** 2025-12-14  
**SDK Version:** 0.3.0  
**FortiOS Version:** 7.6.x

## 📊 Overall Progress

| Category | Status | Endpoints | Coverage |
|----------|--------|-----------|----------|
| **CMDB** | 🔷 Beta | 15 of 38 categories | ~39% |
| **Monitor** | ⏸️ Not Started | 0 of 29 categories | 0% |
| **Log** | ✅ Complete | 5 of 5 categories | 100% |
| **Service** | ✅ Complete | 3 of 3 categories | 100% |

**CMDB Detailed Progress:**
- **Total Endpoints Implemented:** 74 endpoints across 15 categories
- **Total Endpoints Available:** 150+ endpoints across 38 categories
- **Coverage:** ~49% of all CMDB endpoints
- **New:** Firewall category with 23 endpoints across 7 sub-categories

**Legend:**
- ✅ **Complete** - Full CRUD support, tested, documented
- 🔷 **Beta** - Implemented, functional, may need additional testing
- 🚧 **In Progress** - Partially implemented
- ⏸️ **Not Started** - Not yet implemented
- 🚫 **Not Applicable** - Read-only or special endpoint
- 🔧 **Hardware Required** - Requires physical hardware or specific licenses

---

## 🔧 CMDB (Configuration Management Database)

### Implemented Categories (15 categories, 68 endpoints)

#### 1. Alert Email (alertemail/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/alertemail/setting` | 🔷 Beta | GET, PUT | Email alert configuration |

#### 2. Antivirus (antivirus/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/antivirus/profile` | 🔷 Beta | GET, POST, PUT, DELETE | Antivirus profiles |
| `/cmdb/antivirus/settings` | 🔷 Beta | GET, PUT | Global AV settings |
| `/cmdb/antivirus/quarantine` | 🔷 Beta | GET, POST, PUT, DELETE | Quarantine configuration |
| `/cmdb/antivirus/exempt-list` | 🔷 Beta | GET, POST, PUT, DELETE | AV exemption list |

#### 3. Application (application/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/application/name` | 🔷 Beta | GET | Read-only application database |
| `/cmdb/application/list` | 🔷 Beta | GET, POST, PUT, DELETE | Application filter lists |
| `/cmdb/application/group` | 🔷 Beta | GET, POST, PUT, DELETE | Application groups |
| `/cmdb/application/custom` | 🔷 Beta | GET, POST, PUT, DELETE | Custom applications |

#### 4. Authentication (authentication/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/authentication/scheme` | 🔷 Beta | GET, POST, PUT, DELETE | Auth schemes |
| `/cmdb/authentication/rule` | 🔷 Beta | GET, POST, PUT, DELETE | Auth rules |
| `/cmdb/authentication/setting` | 🔷 Beta | GET, PUT | Global auth settings |

#### 5. Automation (automation/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/automation/setting` | 🔷 Beta | GET, PUT | Automation configuration |

#### 6. CASB (casb/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/casb/saas-application` | 🔷 Beta | GET, POST, PUT, DELETE | SaaS app definitions |
| `/cmdb/casb/user-activity` | 🔷 Beta | GET, POST, PUT, DELETE | User activity controls |
| `/cmdb/casb/profile` | 🔷 Beta | GET, POST, PUT, DELETE | CASB profiles |
| `/cmdb/casb/attribute-match` | 🔷 Beta | GET | Attribute matching |

#### 7. Certificate (certificate/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/certificate/ca` | 🔷 Beta | GET | CA certificates (read-only, imported via GUI/CLI) |
| `/cmdb/certificate/local` | 🔷 Beta | GET | Local certificates (read-only, imported via GUI/CLI) |
| `/cmdb/certificate/remote` | 🔷 Beta | GET | Remote certificates (read-only, imported via GUI/CLI) |
| `/cmdb/certificate/crl` | 🔷 Beta | GET | Certificate revocation lists (read-only) |
| `/cmdb/certificate/hsm-local` | 🔷 Beta | GET, POST, PUT, DELETE | HSM-stored certificates (full CRUD) |

#### 8. Diameter Filter (diameter_filter/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/diameter-filter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | Diameter filter profiles |

#### 9. DLP (dlp/) - ✅ Complete (8 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/dlp/data-type` | ✅ Complete | GET, POST, PUT, DELETE | Predefined data type patterns |
| `/cmdb/dlp/dictionary` | ✅ Complete | GET, POST, PUT, DELETE | Custom DLP dictionaries |
| `/cmdb/dlp/exact-data-match` | ✅ Complete | GET, POST, PUT, DELETE | Fingerprinting for exact data matching |
| `/cmdb/dlp/filepattern` | ✅ Complete | GET, POST, PUT, DELETE | File type and pattern matching |
| `/cmdb/dlp/label` | ✅ Complete | GET, POST, PUT, DELETE | Classification labels |
| `/cmdb/dlp/profile` | ✅ Complete | GET, POST, PUT, DELETE | DLP policy profiles |
| `/cmdb/dlp/sensor` | ✅ Complete | GET, POST, PUT, DELETE | DLP sensor configuration |
| `/cmdb/dlp/settings` | ✅ Complete | GET, PUT | Global DLP settings |

#### 10. DNS Filter (dnsfilter/) - ✅ Complete (2 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/dnsfilter/domain-filter` | ✅ Complete | GET, POST, PUT, DELETE | Custom domain filtering lists |
| `/cmdb/dnsfilter/profile` | ✅ Complete | GET, POST, PUT, DELETE | DNS filtering profiles |

#### 11. Email Filter (emailfilter/) - ✅ Complete (8 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/emailfilter/block-allow-list` | ✅ Complete | GET, POST, PUT, DELETE | Email sender block/allow lists |
| `/cmdb/emailfilter/bword` | ✅ Complete | GET, POST, PUT, DELETE | Banned word filtering |
| `/cmdb/emailfilter/dnsbl` | ✅ Complete | GET, POST, PUT, DELETE | DNS-based blacklist checking |
| `/cmdb/emailfilter/fortishield` | ✅ Complete | GET, POST, PUT, DELETE | FortiShield spam filtering |
| `/cmdb/emailfilter/iptrust` | ✅ Complete | GET, POST, PUT, DELETE | Trusted IP addresses |
| `/cmdb/emailfilter/mheader` | ✅ Complete | GET, POST, PUT, DELETE | Email header filtering rules |
| `/cmdb/emailfilter/options` | ✅ Complete | GET, PUT | Global email filter options |
| `/cmdb/emailfilter/profile` | ✅ Complete | GET, POST, PUT, DELETE | Email filtering profiles |

#### 12. Endpoint Control (endpoint-control/) - ✅ Complete (3 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/endpoint-control/fctems` | ✅ Complete | GET, PUT | FortiClient EMS integration (pre-allocated slots) |
| `/cmdb/endpoint-control/fctems-override` | ✅ Complete | GET, PUT | EMS override configurations |
| `/cmdb/endpoint-control/settings` | ✅ Complete | GET, PUT | Endpoint control settings |

#### 13. Ethernet OAM (ethernet-oam/) - 🔧 Hardware Required (1 endpoint)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/ethernet-oam/cfm` | 🔧 Hardware | GET, POST, PUT, DELETE | Connectivity Fault Management (requires physical FortiGate) |

#### 14. Extension Controller (extension-controller/) - ✅ Complete (6 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/extension-controller/dataplan` | ✅ Complete | GET, POST, PUT, DELETE | FortiExtender data plan configuration |
| `/cmdb/extension-controller/extender` | ✅ Complete | GET, POST, PUT, DELETE | FortiExtender controller settings |
| `/cmdb/extension-controller/extender-profile` | ✅ Complete | GET, POST, PUT, DELETE | FortiExtender profiles |
| `/cmdb/extension-controller/extender-vap` | ✅ Complete | GET, POST, PUT, DELETE | FortiExtender WiFi VAP |
| `/cmdb/extension-controller/fortigate` | ✅ Complete | GET, POST, PUT, DELETE | FortiGate controller configuration |
| `/cmdb/extension-controller/fortigate-profile` | ✅ Complete | GET, POST, PUT, DELETE | FortiGate connector profiles |

#### 15. File Filter (file-filter/) - ✅ Complete (1 endpoint)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/file-filter/profile` | ✅ Complete | GET, POST, PUT, DELETE | File content filtering profiles |

---

### Not Yet Implemented (24 Categories Remaining)

<details>
<summary><strong>Click to expand full list of remaining CMDB categories</strong></summary>

#### 1. DDoS (ddos/) - ⏸️ Not Started

#### 2. DNS Filter (dnsfilter/) - ⏸️ Not Started
DNS filtering profiles and domain filters

#### 3. Email Filter (emailfilter/) - ⏸️ Not Started
Email filtering and anti-spam configuration

#### 4. Endpoint Control (endpoint-control/) - ⏸️ Not Started
Endpoint security and compliance

#### 5. Ethernet OAM (ethernet-oam/) - ⏸️ Not Started
Ethernet Operations, Administration, and Maintenance

#### 6. Extension Controller (extension-controller/) - ⏸️ Not Started
FortiExtender management

#### 7. File Filter (file-filter/) - ⏸️ Not Started
File filtering profiles

#### 8. Firewall (firewall/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| **DoS-policy** | ✅ Complete | GET, POST, PUT, DELETE | IPv4 DoS protection policies |
| **DoS-policy6** | ✅ Complete | GET, POST, PUT, DELETE | IPv6 DoS protection policies |
| **access-proxy** | ✅ Complete | GET, POST, PUT, DELETE | IPv4 reverse proxy/WAF |
| **access-proxy6** | ✅ Complete | GET, POST, PUT, DELETE | IPv6 reverse proxy/WAF |
| **access-proxy-ssh-client-cert** | ✅ Complete | GET, POST, PUT, DELETE | SSH client certificates |
| **access-proxy-virtual-host** | ✅ Complete | GET, POST, PUT, DELETE | Virtual host configuration |
| **ipmacbinding/setting** | ✅ Complete | GET, PUT | IP/MAC binding settings |
| **ipmacbinding/table** | ✅ Complete | GET, POST, PUT, DELETE | IP/MAC binding table |
| **schedule/group** | ✅ Complete | GET, POST, PUT, DELETE | Schedule groups |
| **schedule/onetime** | ✅ Complete | GET, POST, PUT, DELETE | One-time schedules |
| **schedule/recurring** | ✅ Complete | GET, POST, PUT, DELETE | Recurring schedules |
| **service/category** | ✅ Complete | GET, POST, PUT, DELETE | Service categories |
| **service/custom** | ✅ Complete | GET, POST, PUT, DELETE | Custom services |
| **service/group** | ✅ Complete | GET, POST, PUT, DELETE | Service groups |
| **shaper/per-ip-shaper** | ✅ Complete | GET, POST, PUT, DELETE | Per-IP traffic shaper |
| **shaper/traffic-shaper** | ✅ Complete | GET, POST, PUT, DELETE | Shared traffic shaper |
| **ssh/host-key** | ✅ Complete | GET, POST, PUT, DELETE | SSH proxy host keys |
| **ssh/local-ca** | ✅ Complete | GET, POST, PUT, DELETE | SSH proxy local CA |
| **ssh/local-key** | ✅ Complete | GET, POST, PUT, DELETE | SSH proxy local keys |
| **ssh/setting** | ✅ Complete | GET, PUT | SSH proxy settings |
| **ssl/setting** | ✅ Complete | GET, PUT | SSL proxy settings |
| **wildcard-fqdn/custom** | ✅ Complete | GET, POST, PUT, DELETE | Wildcard FQDN addresses |
| **wildcard-fqdn/group** | ✅ Complete | GET, POST, PUT, DELETE | Wildcard FQDN groups |

**Sub-categories Implemented:** 7 (ipmacbinding, schedule, service, shaper, ssh, ssl, wildcard-fqdn)  
**Flat Endpoints Implemented:** 6 (DoS-policy, DoS-policy6, access-proxy, access-proxy6, access-proxy-ssh-client-cert, access-proxy-virtual-host)  
**Test Coverage:** 186 tests (100% pass rate)  
**Pattern:** 
- Nested: `fgt.cmdb.firewall.[subcategory].[endpoint]`
- Flat: `fgt.cmdb.firewall.[endpoint]`

**Key Features:**
- Simplified API with automatic type conversion
- DoS policies include comprehensive anomaly detection (18 types)
- Access-proxy supports reverse proxy/WAF with VIP integration
- All endpoints lazy-loaded via @property pattern

**Remaining Firewall Endpoints (83):**
- address, address6, addrgrp, addrgrp6 - Address management
- policy, security-policy - Policy configuration
- vip, vip6, vipgrp, vipgrp6 - Virtual IP configuration
- ippool, ippool6 - IP pool configuration
- proxy-address, proxy-addrgrp, proxy-policy - Proxy configuration
- interface-policy, interface-policy6 - Interface policies
- local-in-policy, local-in-policy6 - Local-in policies
- multicast-address, multicast-policy - Multicast configuration
- ssl-server, ssl-ssh-profile - SSL/SSH profiles
- And 60+ more endpoints...

#### 9. FTP Proxy (ftp-proxy/) - ⏸️ Not Started
FTP proxy configuration

#### 10. ICAP (icap/) - ⏸️ Not Started
Internet Content Adaptation Protocol

#### 11. IPS (ips/) - ⏸️ Not Started
Intrusion Prevention System sensors and custom signatures

#### 12. Log (log/) - ⏸️ Not Started
Logging configuration (disk, syslog, FortiAnalyzer settings)

#### 13. Monitoring (monitoring/) - ⏸️ Not Started
SNMP and monitoring configuration

#### 14. Report (report/) - ⏸️ Not Started
Report settings and configuration

#### 15. Router (router/) - ⏸️ Not Started
**HIGH PRIORITY** - Routing configuration (static, BGP, OSPF, policy routing)

#### 16. Rule (rule/) - ⏸️ Not Started
Traffic shaping and QoS rules

#### 17. SCTP Filter (sctp-filter/) - ⏸️ Not Started
Stream Control Transmission Protocol filtering

#### 18. SSH Filter (ssh-filter/) - ⏸️ Not Started
SSH protocol filtering

#### 19. Switch Controller (switch-controller/) - ⏸️ Not Started
Managed FortiSwitch configuration

#### 20. System (system/) - ⏸️ Not Started
**HIGH PRIORITY** - System settings (global, interface, admin, DNS, NTP, etc.)

#### 21. Telemetry Controller (telemetry-controller/) - ⏸️ Not Started
Telemetry and analytics configuration

#### 22. User (user/) - ⏸️ Not Started
User and group management, LDAP, RADIUS, local users

#### 23. Video Filter (videofilter/) - ⏸️ Not Started
Video streaming filtering

#### 24. Virtual Patch (virtual-patch/) - ⏸️ Not Started
Virtual patching for vulnerability protection

#### 25. VoIP (voip/) - ⏸️ Not Started
Voice over IP profiles and configuration

#### 26. VPN (vpn/) - ⏸️ Not Started
**HIGH PRIORITY** - IPsec and SSL VPN configuration

#### 27. WAF (waf/) - ⏸️ Not Started
Web Application Firewall profiles

#### 28. WAN Optimization (wanopt/) - ⏸️ Not Started
WAN optimization and caching

#### 29. Web Proxy (web-proxy/) - ⏸️ Not Started
Explicit web proxy configuration

#### 30. Web Filter (webfilter/) - ⏸️ Not Started
Web filtering profiles and URL filters

#### 31. Wireless Controller (wireless-controller/) - ⏸️ Not Started
FortiAP management and wireless configuration

#### 32. ZTNA (ztna/) - ⏸️ Not Started
Zero Trust Network Access configuration

</details>

---

## 📝 Log Endpoints

| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/log/disk/*` | 🔷 Beta | GET | Traffic, event, virus logs from disk |
| `/log/fortianalyzer/*` | 🔷 Beta | GET | Logs from FortiAnalyzer |
| `/log/forticloud/*` | 🔷 Beta | GET | Logs from FortiCloud |
| `/log/memory/*` | 🔷 Beta | GET | Logs from memory |
| `/log/search` | 🔷 Beta | GET, POST, DELETE | Log search sessions |

**Supported Log Types:**
- Traffic logs (forward, local, sniffer, fortiview)
- Event logs (system, router, VPN, user, etc.)
- Security logs (virus, webfilter, IPS, etc.)
- Raw log format support

---

## 🔍 Monitor Endpoints

⏸️ **Status:** Not yet implemented (0 of 29 categories)

<details>
<summary><strong>Click to expand full list of Monitor API categories</strong></summary>

### All Monitor Categories (29 total)

1. **azure** - Azure SD-WAN monitoring
2. **casb** - CASB monitoring and statistics
3. **endpoint-control** - Endpoint status and compliance monitoring
4. **extender-controller** - FortiExtender status
5. **extension-controller** - Extension controller monitoring
6. **firewall** - Firewall statistics (sessions, policies, addresses)
7. **firmware** - Firmware version and update status
8. **fortiguard** - FortiGuard services status
9. **fortiview** - FortiView statistics and data
10. **geoip** - GeoIP database information
11. **ips** - IPS statistics and events
12. **license** - License information and status
13. **log** - Log statistics and disk usage
14. **network** - Network statistics and ARP tables
15. **registration** - Device registration status
16. **router** - Routing table and BGP/OSPF status
17. **sdwan** - SD-WAN health and performance metrics
18. **service** - Service availability and status
19. **switch-controller** - FortiSwitch monitoring
20. **system** - **HIGH PRIORITY** - System resources (CPU, memory, disk, interfaces)
21. **user** - Active users and authentication sessions
22. **utm** - UTM statistics (AV, web filter, etc.)
23. **videofilter** - Video filtering statistics
24. **virtual-wan** - Virtual WAN monitoring
25. **vpn** - **HIGH PRIORITY** - VPN tunnel status and statistics
26. **vpn-certificate** - VPN certificate status
27. **wanopt** - WAN optimization statistics
28. **web-ui** - Web UI session information
29. **webcache** - Web cache statistics
30. **webfilter** - Web filter statistics
31. **webproxy** - Web proxy statistics
32. **wifi** - WiFi controller statistics

</details>

---

## ⚙️ Service Endpoints

✅ **Status:** All 3 categories implemented (100% coverage)

| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/service/sniffer` | 🔷 Beta | GET, POST, DELETE | Packet capture |
| `/service/security-rating` | 🔷 Beta | GET | Security Fabric rating |
| `/service/system` | 🔷 Beta | Various | System operations (reboot, backup, etc.) |

---
## �� API Scope Summary

| API Type | Implemented | Total | Coverage |

|----------|-------------|-------|----------|
| **Configuration (CMDB)** | 8 | 38 | 21% |
| **Monitoring** | 0 | 29 | 0% |
| **Logging** | 5 | 5 | 100% |
| **Services** | 3 | 3 | 100% |
| **Overall** | **16** | **75** | **21%** |

---

## 🤝 Contributing

Want to help implement more endpoints? See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines!

### How to Add Coverage

1. Check FortiOS API documentation for endpoint details
2. Implement endpoint following existing patterns
3. Test your implementation thoroughly
4. Update this file with implementation status
5. Update CHANGELOG.md
6. Submit pull request

---

## 📚 Resources

- [FortiOS REST API Guide](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [Fortinet Developer Network](https://fndn.fortinet.net)
- [API Reference](https://fndn.fortinet.net/index.php?/fortiapi/1-fortios/)

---

**Note:** This coverage map is for FortiOS 7.6.x. Some endpoints may vary in different FortiOS versions.
