# API Coverage

This document tracks the implementation status of FortiOS API endpoints in the Fortinet Python SDK.

**Last Updated:** 2025-12-17  
**SDK Version:** 0.3.13  
**FortiOS Version:** 7.6.5

## 🎯 Key Features

### raw_json Parameter ✨
**All API methods support raw_json parameter for full response access:**
- **Default Behavior**: `get('name')` → returns just the results
- **Full Response**: `get('name', raw_json=True)` → returns complete API response with status codes
- **Coverage**: 100% of all implemented methods (45+ endpoints)

### Dual-Pattern Interface ✨
**All create/update methods support flexible syntax:**
- **Dictionary Pattern**: `create(data_dict={'name': 'x', 'subnet': '10.0.0.0/24'})`
- **Keyword Pattern**: `create(name='x', subnet='10.0.0.0/24')`
- **Mixed Pattern**: `create(data_dict=base, name='override')`

**Coverage**: 43 methods (38 CMDB + 5 Service) - 100% of implemented operations

---

## 📊 Overall Progress

**⚠️ BETA STATUS**: All current implementations are in beta. APIs are functional but may have incomplete parameter coverage or undiscovered edge cases.

**FortiOS Version:** 7.6.5

| API Category | Status | Implemented | Total Available | Coverage |
|--------------|--------|-------------|-----------------|----------|
| **Configuration (CMDB)** | 🔷 Beta | 24 categories | 40 categories | 60.0% |
| **Monitoring** | 🔷 Beta | 6 categories | 33 categories | 18% |
| **Logging** | 🔷 Beta | 5 categories | 5 categories | 100% |
| **Service** | 🔷 Beta | 3 categories | 3 categories | 100% |
| **Overall** | 🔷 Beta | **38 categories** | **77 categories** | **49%** |

**CMDB Detailed Progress:**
- **Total Categories Available:** 40 (FortiOS 7.6.5 Configuration API)
- **Categories Implemented:** 24 (60.0% coverage)
- **Total Endpoints Implemented:** 200+ endpoints (including 26 router endpoints)
- **Coverage:** 60.0% of all CMDB categories

**Note:** All implementations are in beta status and will remain so until version 1.0.0 with comprehensive unit test coverage.

**Legend:**
- 🔷 **Beta** - Implemented and functional (all endpoints remain in beta until v1.0.0)
- 🚧 **In Progress** - Partially implemented
- ⏸️ **Not Started** - Not yet implemented
- 🚫 **Not Applicable** - Read-only or special endpoint
- 🔧 **Hardware Required** - Requires physical hardware or specific licenses

---

## 🔧 CMDB (Configuration Management Database)

### Implemented Categories (23 categories, 200+ endpoints)

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

#### 9. DLP (dlp/) - 🔷 Beta (8 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/dlp/data-type` | 🔷 Beta | GET, POST, PUT, DELETE | Predefined data type patterns |
| `/cmdb/dlp/dictionary` | 🔷 Beta | GET, POST, PUT, DELETE | Custom DLP dictionaries |
| `/cmdb/dlp/exact-data-match` | 🔷 Beta | GET, POST, PUT, DELETE | Fingerprinting for exact data matching |
| `/cmdb/dlp/filepattern` | 🔷 Beta | GET, POST, PUT, DELETE | File type and pattern matching |
| `/cmdb/dlp/label` | 🔷 Beta | GET, POST, PUT, DELETE | Classification labels |
| `/cmdb/dlp/profile` | 🔷 Beta | GET, POST, PUT, DELETE | DLP policy profiles |
| `/cmdb/dlp/sensor` | 🔷 Beta | GET, POST, PUT, DELETE | DLP sensor configuration |
| `/cmdb/dlp/settings` | 🔷 Beta | GET, PUT | Global DLP settings |

#### 10. DNS Filter (dnsfilter/) - 🔷 Beta (2 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/dnsfilter/domain-filter` | 🔷 Beta | GET, POST, PUT, DELETE | Custom domain filtering lists |
| `/cmdb/dnsfilter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | DNS filtering profiles |

#### 11. Email Filter (emailfilter/) - 🔷 Beta (8 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/emailfilter/block-allow-list` | 🔷 Beta | GET, POST, PUT, DELETE | Email sender block/allow lists |
| `/cmdb/emailfilter/bword` | 🔷 Beta | GET, POST, PUT, DELETE | Banned word filtering |
| `/cmdb/emailfilter/dnsbl` | 🔷 Beta | GET, POST, PUT, DELETE | DNS-based blacklist checking |
| `/cmdb/emailfilter/fortishield` | 🔷 Beta | GET, POST, PUT, DELETE | FortiShield spam filtering |
| `/cmdb/emailfilter/iptrust` | 🔷 Beta | GET, POST, PUT, DELETE | Trusted IP addresses |
| `/cmdb/emailfilter/mheader` | 🔷 Beta | GET, POST, PUT, DELETE | Email header filtering rules |
| `/cmdb/emailfilter/options` | 🔷 Beta | GET, PUT | Global email filter options |
| `/cmdb/emailfilter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | Email filtering profiles |

#### 12. Endpoint Control (endpoint-control/) - 🔷 Beta (3 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/endpoint-control/fctems` | 🔷 Beta | GET, PUT | FortiClient EMS integration (pre-allocated slots) |
| `/cmdb/endpoint-control/fctems-override` | 🔷 Beta | GET, PUT | EMS override configurations |
| `/cmdb/endpoint-control/settings` | 🔷 Beta | GET, PUT | Endpoint control settings |

#### 13. Ethernet OAM (ethernet-oam/) - 🔧 Hardware Required (1 endpoint)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/ethernet-oam/cfm` | 🔧 Hardware | GET, POST, PUT, DELETE | Connectivity Fault Management (requires physical FortiGate) |

#### 14. Extension Controller (extension-controller/) - 🔷 Beta (6 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/extension-controller/dataplan` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender data plan configuration |
| `/cmdb/extension-controller/extender` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender controller settings |
| `/cmdb/extension-controller/extender-profile` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender profiles |
| `/cmdb/extension-controller/extender-vap` | 🔷 Beta | GET, POST, PUT, DELETE | FortiExtender WiFi VAP |
| `/cmdb/extension-controller/fortigate` | 🔷 Beta | GET, POST, PUT, DELETE | FortiGate controller configuration |
| `/cmdb/extension-controller/fortigate-profile` | 🔷 Beta | GET, POST, PUT, DELETE | FortiGate connector profiles |

#### 15. File Filter (file-filter/) - 🔷 Beta (1 endpoint)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/file-filter/profile` | 🔷 Beta | GET, POST, PUT, DELETE | File content filtering profiles |

#### 16. Firewall (firewall/) - 🔷 Beta (29 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| **DoS-policy** | 🔷 Beta | GET, POST, PUT, DELETE | IPv4 DoS protection policies |
| **DoS-policy6** | 🔷 Beta | GET, POST, PUT, DELETE | IPv6 DoS protection policies |
| **access-proxy** | 🔷 Beta | GET, POST, PUT, DELETE | IPv4 reverse proxy/WAF |
| **access-proxy6** | 🔷 Beta | GET, POST, PUT, DELETE | IPv6 reverse proxy/WAF |
| **access-proxy-ssh-client-cert** | 🔷 Beta | GET, POST, PUT, DELETE | SSH client certificates |
| **access-proxy-virtual-host** | 🔷 Beta | GET, POST, PUT, DELETE | Virtual host configuration |
| **ipmacbinding/setting** | 🔷 Beta | GET, PUT | IP/MAC binding settings |
| **ipmacbinding/table** | 🔷 Beta | GET, POST, PUT, DELETE | IP/MAC binding table |
| **schedule/group** | 🔷 Beta | GET, POST, PUT, DELETE | Schedule groups |
| **schedule/onetime** | 🔷 Beta | GET, POST, PUT, DELETE | One-time schedules |
| **schedule/recurring** | 🔷 Beta | GET, POST, PUT, DELETE | Recurring schedules |
| **service/category** | 🔷 Beta | GET, POST, PUT, DELETE | Service categories |
| **service/custom** | 🔷 Beta | GET, POST, PUT, DELETE | Custom services |
| **service/group** | 🔷 Beta | GET, POST, PUT, DELETE | Service groups |
| **shaper/per-ip-shaper** | 🔷 Beta | GET, POST, PUT, DELETE | Per-IP traffic shaper |
| **shaper/traffic-shaper** | 🔷 Beta | GET, POST, PUT, DELETE | Shared traffic shaper |
| **ssh/host-key** | 🔷 Beta | GET, POST, PUT, DELETE | SSH proxy host keys |
| **ssh/local-ca** | 🔷 Beta | GET, POST, PUT, DELETE | SSH proxy local CA |
| **ssh/local-key** | 🔷 Beta | GET, POST, PUT, DELETE | SSH proxy local keys |
| **ssh/setting** | 🔷 Beta | GET, PUT | SSH proxy settings |
| **ssl/setting** | 🔷 Beta | GET, PUT | SSL proxy settings |
| **wildcard-fqdn/custom** | 🔷 Beta | GET, POST, PUT, DELETE | Wildcard FQDN addresses |
| **wildcard-fqdn/group** | 🔷 Beta | GET, POST, PUT, DELETE | Wildcard FQDN groups |

**Sub-categories Implemented:** 7 (ipmacbinding, schedule, service, shaper, ssh, ssl, wildcard-fqdn)  
**Flat Endpoints Implemented:** 6 (DoS-policy, DoS-policy6, access-proxy, access-proxy6, access-proxy-ssh-client-cert, access-proxy-virtual-host)  
**Test Coverage:** 186 tests (100% pass rate)  
**Pattern:** 
- Nested: `fgt.api.cmdb.firewall.[subcategory].[endpoint]`
- Flat: `fgt.api.cmdb.firewall.[endpoint]`

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

#### 17. FTP Proxy (ftp-proxy/) - 🔷 Beta (1 endpoint)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/ftp-proxy/explicit` | 🔷 Beta | GET, PUT | Explicit FTP proxy configuration |

**Features:**
- Enable/disable explicit FTP proxy
- Configure incoming/outgoing IP and port
- Security default action (accept/deny)
- Server data mode (client/passive)
- FTPS support with SSL configuration
- SSL certificate selection and DH bits
- Singleton endpoint (no POST/DELETE)

#### 18. ICAP (icap/) - 🔷 Beta (3 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/icap/profile` | 🔷 Beta | GET, POST, PUT, DELETE | ICAP profiles with 30+ parameters |
| `/cmdb/icap/server` | 🔷 Beta | GET, POST, PUT, DELETE | ICAP server configuration |
| `/cmdb/icap/server-group` | 🔷 Beta | GET, POST, PUT, DELETE | ICAP server groups |

**Features:**
- Complete parameter coverage from FortiOS 7.6.5 API
- Request/response modification support
- SSL/TLS ICAP connections
- Preview, streaming, and bypass options

#### 19. IPS (ips/) - 🔷 Beta (8 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/ips/custom` | 🔷 Beta | GET, POST, PUT, DELETE | Custom IPS signatures |
| `/cmdb/ips/decoder` | 🔷 Beta | GET, POST, PUT, DELETE | Protocol decoders |
| `/cmdb/ips/global` | 🔷 Beta | GET, PUT | Global IPS settings (singleton) |
| `/cmdb/ips/rule` | 🔷 Beta | GET, POST, PUT, DELETE | IPS rules |
| `/cmdb/ips/rule-settings` | 🔷 Beta | GET, POST, PUT, DELETE | IPS rule settings |
| `/cmdb/ips/sensor` | 🔷 Beta | GET, POST, PUT, DELETE | IPS sensors (main profiles) |
| `/cmdb/ips/settings` | 🔷 Beta | GET, PUT | VDOM IPS settings (singleton) |
| `/cmdb/ips/view-map` | 🔷 Beta | GET, POST, PUT, DELETE | IPS view-map configuration |

**Features:**
- Custom signature creation
- Protocol decoder configuration
- Sensor-based IPS profiles
- Rate-based and anomaly-based detection

#### 20. Log (log/) - 🔷 Beta (56 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| **disk/filter** | 🔷 Beta | GET, PUT | Disk log filtering (12 params) |
| **disk/setting** | 🔷 Beta | GET, PUT | Disk log settings (28 params) |
| **memory/filter** | 🔷 Beta | GET, PUT | Memory log filtering (12 params) |
| **memory/global-setting** | 🔷 Beta | GET, PUT | Memory log global settings (4 params) |
| **memory/setting** | 🔷 Beta | GET, PUT | Memory log settings (1 param) |
| **fortianalyzer-cloud/filter** | 🔷 Beta | GET, PUT | FortiAnalyzer Cloud log filter |
| **fortianalyzer-cloud/override-filter** | 🔷 Beta | GET, PUT | FAC override filter |
| **fortianalyzer-cloud/override-setting** | 🔷 Beta | GET, PUT | FAC override settings |
| **fortianalyzer-cloud/setting** | 🔷 Beta | GET, PUT | FAC log settings |
| **fortianalyzer/filter** | 🔷 Beta | GET, PUT | FortiAnalyzer log filter |
| **fortianalyzer/override-filter** | 🔷 Beta | GET, PUT | FA override filter |
| **fortianalyzer/override-setting** | 🔷 Beta | GET, PUT | FA override settings |
| **fortianalyzer/setting** | 🔷 Beta | GET, PUT | FA log settings |
| **fortianalyzer2/** | 🔷 Beta | GET, PUT | FortiAnalyzer 2 (4 endpoints) |
| **fortianalyzer3/** | 🔷 Beta | GET, PUT | FortiAnalyzer 3 (4 endpoints) |
| **fortiguard/filter** | 🔷 Beta | GET, PUT | FortiGuard log filter |
| **fortiguard/override-filter** | 🔷 Beta | GET, PUT | FG override filter |
| **fortiguard/override-setting** | 🔷 Beta | GET, PUT | FG override settings |
| **fortiguard/setting** | 🔷 Beta | GET, PUT | FG log settings |
| **null-device/filter** | 🔷 Beta | GET, PUT | Null device log filter (12 params) |
| **null-device/setting** | 🔷 Beta | GET, PUT | Null device settings (1 param) |
| **syslogd/filter** | 🔷 Beta | GET, PUT | Syslog filter (12 params) |
| **syslogd/override-filter** | 🔷 Beta | GET, PUT | Syslog override filter (12 params) |
| **syslogd/override-setting** | 🔷 Beta | GET, PUT | Syslog override settings (18 params) |
| **syslogd/setting** | 🔷 Beta | GET, PUT | Syslog settings (17 params) |
| **syslogd2/** | 🔷 Beta | GET, PUT | Syslog server 2 (4 endpoints) |
| **syslogd3/** | 🔷 Beta | GET, PUT | Syslog server 3 (4 endpoints) |
| **syslogd4/** | 🔷 Beta | GET, PUT | Syslog server 4 (4 endpoints) |
| **tacacs+accounting/filter** | 🔷 Beta | GET, PUT | TACACS+ accounting filter (3 params) |
| **tacacs+accounting/setting** | 🔷 Beta | GET, PUT | TACACS+ accounting settings (7 params) |
| **tacacs+accounting2/** | 🔷 Beta | GET, PUT | TACACS+ server 2 (2 endpoints) |
| **tacacs+accounting3/** | 🔷 Beta | GET, PUT | TACACS+ server 3 (2 endpoints) |
| **webtrends/filter** | 🔷 Beta | GET, PUT | WebTrends log filter (12 params) |
| **webtrends/setting** | 🔷 Beta | GET, PUT | WebTrends settings (2 params) |
| **custom-field** | 🔷 Beta | GET, POST, PUT, DELETE | Custom log fields (CRUD) |
| **eventfilter** | 🔷 Beta | GET, PUT | Event filter configuration (17 params) |
| **gui-display** | 🔷 Beta | GET, PUT | GUI display settings (3 params) |
| **setting** | 🔷 Beta | GET, PUT | General log settings (29 params) |
| **threat-weight** | 🔷 Beta | GET, PUT | Threat weight settings (11 params) |

**Architecture:**
- **Nested object pattern** for sub-categories: `fgt.api.cmdb.log.disk.filter.get()`
- **51 nested endpoints** across 9 intermediate classes
- **5 singleton endpoints** at root level
- Test Coverage: 12 test files, 47 test cases (100% pass rate)

**Key Features:**
- Multiple FortiAnalyzer server support (1/2/3)
- Multiple syslog server support (1/2/3/4)
- Multiple TACACS+ accounting server support (1/2/3)
- Custom field management for log enrichment
- Comprehensive filtering and override capabilities

#### 21. Monitoring (monitoring/) - 🔷 Beta (1 endpoint)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/monitoring/npu-hpe` | 🔷 Beta | GET, PUT | NPU-HPE monitoring configuration (3 params) |

**Features:**
- NPU-HPE performance monitoring settings
- Interval, multipliers, and status configuration
- Requires hardware NPU support

#### 22. Report (report/) - 🔷 Beta (2 endpoints)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/cmdb/report/layout` | 🔷 Beta | GET, POST, PUT, DELETE | Report layouts with CRUD (17 params) |
| `/cmdb/report/setting` | 🔷 Beta | GET, PUT | Report settings (5 params) |

**Features:**
- Custom report layout creation
- Email scheduling support
- PDF report generation
- FortiView and web browsing report settings

---

### Not Yet Implemented (16 Categories Remaining)

**FortiOS 7.6.5 CMDB Categories Not Yet Implemented:**

<details>
<summary><strong>Click to expand full list of remaining CMDB categories</strong></summary>

1. **rule** - Traffic shaping and QoS rules
2. **sctp-filter** - Stream Control Transmission Protocol filtering
3. **ssh-filter** - SSH protocol filtering
4. **switch-controller** - FortiSwitch management and configuration
5. **system** - 🔥 **HIGH PRIORITY** - System-wide settings (admin, interface, zone, HA, etc.)
6. **telemetry-controller** - Telemetry and monitoring integration
7. **user** - 🔥 **HIGH PRIORITY** - User authentication and LDAP/RADIUS servers
8. **videofilter** - Video streaming filtering
9. **virtual-patch** - Virtual patching for vulnerabilities
10. **voip** - VoIP inspection and SIP configuration
11. **vpn** - 🔥 **HIGH PRIORITY** - VPN configuration (IPsec, SSL-VPN, tunnels)
12. **waf** - Web Application Firewall profiles
13. **wanopt** - WAN optimization configuration
14. **web-proxy** - Explicit web proxy configuration
15. **webfilter** - 🔥 **HIGH PRIORITY** - Web filtering and URL categories
16. **wireless-controller** - FortiAP wireless management
17. **ztna** - Zero Trust Network Access configuration

**Note:** All 24 implemented CMDB categories are in beta status.

---

## 📝 Configuration API (CMDB) - Complete List

**FortiOS 7.6.5 Configuration API - All 40 Categories:**

| # | Category | Status | Notes |
|---|----------|--------|-------|
| 1 | alertemail | 🔷 Beta | Email alerts |
| 2 | antivirus | 🔷 Beta | Antivirus profiles |
| 3 | application | 🔷 Beta | Application control |
| 4 | authentication | 🔷 Beta | Authentication schemes |
| 5 | automation | 🔷 Beta | Automation stitch |
| 6 | casb | 🔷 Beta | CASB profiles |
| 7 | certificate | 🔷 Beta | Certificate management |
| 8 | diameter-filter | 🔷 Beta | Diameter filtering |
| 9 | dlp | 🔷 Beta | Data loss prevention |
| 10 | dnsfilter | 🔷 Beta | DNS filtering |
| 11 | emailfilter | 🔷 Beta | Email filtering |
| 12 | endpoint-control | 🔷 Beta | Endpoint control |
| 13 | ethernet-oam | 🔷 Beta | Ethernet OAM |
| 14 | extension-controller | 🔷 Beta | FortiExtender |
| 15 | file-filter | 🔷 Beta | File filtering |
| 16 | firewall | 🔷 Beta | Firewall objects & policies |
| 17 | ftp-proxy | 🔷 Beta | FTP proxy |
| 18 | icap | 🔷 Beta | ICAP integration |
| 19 | ips | 🔷 Beta | IPS sensors |
| 20 | log | 🔷 Beta | Log configuration |
| 21 | monitoring | 🔷 Beta | Monitoring config |
| 22 | report | 🔷 Beta | Report configuration |
| 23 | router | 🔷 Beta | Routing protocols (⚠️ singleton pattern) |
| 24 | rule | ⏸️ Not Started | Traffic rules |
| 25 | sctp-filter | ⏸️ Not Started | SCTP filtering |
| 26 | ssh-filter | ⏸️ Not Started | SSH filtering |
| 27 | switch-controller | ⏸️ Not Started | FortiSwitch |
| 28 | system | ⏸️ Not Started | System settings |
| 29 | telemetry-controller | ⏸️ Not Started | Telemetry |
| 30 | user | ⏸️ Not Started | User management |
| 31 | videofilter | ⏸️ Not Started | Video filtering |
| 32 | virtual-patch | ⏸️ Not Started | Virtual patching |
| 33 | voip | ⏸️ Not Started | VoIP profiles |
| 34 | vpn | ⏸️ Not Started | VPN configuration |
| 35 | waf | ⏸️ Not Started | WAF profiles |
| 36 | wanopt | ⏸️ Not Started | WAN optimization |
| 37 | web-proxy | ⏸️ Not Started | Web proxy |
| 38 | webfilter | ⏸️ Not Started | Web filtering |
| 39 | wireless-controller | ⏸️ Not Started | FortiAP |
| 40 | ztna | ⏸️ Not Started | ZTNA |

**Implementation Status:**
- 🔷 **Beta (Implemented):** 24 categories (60.0%)
- ⏸️ **Not Started:** 16 categories (40.0%)

**Note:** All implemented categories remain in beta status until v1.0.0 with comprehensive unit test coverage.

---

## 📊 Log API - FortiOS 7.6.5

**Status:** 🔷 Beta - 5 of 5 categories implemented (100%)

| # | Category | Status | Notes |
|---|----------|--------|-------|
| 1 | disk | 🔷 Beta | Read logs from disk |
| 2 | fortianalyzer | 🔷 Beta | Read logs from FortiAnalyzer |
| 3 | memory | 🔷 Beta | Read logs from memory |
| 4 | forticloud | 🔷 Beta | Read logs from FortiCloud |
| 5 | search | 🔷 Beta | Log search sessions |

**Note:** The `/log/*` API endpoints are for **reading logs**, not configuring logging. For logging configuration, use `/cmdb/log/*` endpoints (already implemented - see category #19 above). All endpoints remain in beta until v1.0.0.

---

## 🔍 Monitor API - FortiOS 7.6.5

**Status:** 🔷 Beta - 6 of 33 categories implemented (18%)

### Implemented Categories (6 categories, 39+ endpoints)

#### 1. Azure (azure/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/azure/application-list` | 🔷 Beta | GET | List Azure applications |

#### 2. CASB (casb/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/casb/saas-application` | 🔷 Beta | GET | SaaS application statistics |

#### 3. Endpoint Control (endpoint-control/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/endpoint-control/ems-status` | 🔷 Beta | GET | EMS connection status |
| `/monitor/endpoint-control/ems-status-summary` | 🔷 Beta | GET | EMS status summary |
| `/monitor/endpoint-control/installer` | 🔷 Beta | GET, POST | FortiClient installer management |
| `/monitor/endpoint-control/profile-xml` | 🔷 Beta | GET | FortiClient XML profiles |
| `/monitor/endpoint-control/record-list` | 🔷 Beta | GET | Endpoint control records |
| `/monitor/endpoint-control/registration-password` | 🔷 Beta | POST | Generate registration passwords |
| `/monitor/endpoint-control/summary` | 🔷 Beta | GET | Endpoint control summary |

#### 4. Extender Controller (extender-controller/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/extender-controller/extender` | 🔷 Beta | GET | FortiExtender status |

#### 5. Extension Controller (extension-controller/)
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/extension-controller/extender` | 🔷 Beta | GET | Extension controller status |
| `/monitor/extension-controller/fortigate` | 🔷 Beta | GET | FortiGate connector status |

#### 6. Firewall (firewall/) - 39 endpoints
| Endpoint | Status | Methods | Notes |
|----------|--------|---------|-------|
| `/monitor/firewall/acl` | 🔷 Beta | GET, POST | IPv4 ACL counters |
| `/monitor/firewall/acl6` | 🔷 Beta | GET, POST | IPv6 ACL counters |
| `/monitor/firewall/address` | 🔷 Beta | GET | Address objects statistics |
| `/monitor/firewall/address-dynamic` | 🔷 Beta | GET | Dynamic address statistics |
| `/monitor/firewall/address-fqdn` | 🔷 Beta | GET | FQDN address resolution |
| `/monitor/firewall/address-fqdn6` | 🔷 Beta | GET | IPv6 FQDN resolution |
| `/monitor/firewall/address6` | 🔷 Beta | GET | IPv6 address statistics |
| `/monitor/firewall/carrier-endpoint-bwl` | 🔷 Beta | GET | Carrier endpoint bandwidth limits |
| `/monitor/firewall/check-addrgrp-exclude-mac-member` | 🔷 Beta | GET | Check address group MAC exclusions |
| `/monitor/firewall/clearpass-address` | 🔷 Beta | POST | ClearPass address management |
| `/monitor/firewall/consolidate-policy` | 🔷 Beta | GET | Policy consolidation analysis |
| `/monitor/firewall/gtp-runtime-statistics` | 🔷 Beta | GET | GTP protocol statistics |
| `/monitor/firewall/gtp-statistics` | 🔷 Beta | GET | GTP statistics summary |
| `/monitor/firewall/health` | 🔷 Beta | GET | Firewall health status |
| `/monitor/firewall/internet-service-match` | 🔷 Beta | GET | Internet service matching |
| `/monitor/firewall/internet-service-reputation` | 🔷 Beta | GET | Internet service reputation |
| `/monitor/firewall/iprope` | 🔷 Beta | GET | IP reputation |
| `/monitor/firewall/load-balance` | 🔷 Beta | GET | Load balancing statistics |
| `/monitor/firewall/local-in` | 🔷 Beta | GET | Local-in policy statistics |
| `/monitor/firewall/local-in6` | 🔷 Beta | GET | IPv6 local-in statistics |
| `/monitor/firewall/multicast-policy` | 🔷 Beta | GET | Multicast policy statistics |
| `/monitor/firewall/multicast-policy6` | 🔷 Beta | GET | IPv6 multicast statistics |
| `/monitor/firewall/network-service-dynamic` | 🔷 Beta | GET | Dynamic network services |
| `/monitor/firewall/per-ip-shaper` | 🔷 Beta | GET, POST | Per-IP shaper statistics |
| `/monitor/firewall/policy` | 🔷 Beta | GET | Policy statistics |
| `/monitor/firewall/policy-lookup` | 🔷 Beta | GET (Callable) | Policy lookup by packet |
| `/monitor/firewall/policy6` | 🔷 Beta | GET | IPv6 policy statistics |
| `/monitor/firewall/proute` | 🔷 Beta | GET | Policy-based routing |
| `/monitor/firewall/proute6` | 🔷 Beta | GET | IPv6 policy routing |
| `/monitor/firewall/proxy-policy` | 🔷 Beta | GET | Proxy policy statistics |
| `/monitor/firewall/saas-application` | 🔷 Beta | GET | SaaS application statistics |
| `/monitor/firewall/sdn-connector-filters` | 🔷 Beta | GET | SDN connector filters |
| `/monitor/firewall/security-policy` | 🔷 Beta | GET | Security policy statistics |
| `/monitor/firewall/sessions` | 🔷 Beta | GET | Active firewall sessions |
| `/monitor/firewall/shaper` | 🔷 Beta | GET, POST | Traffic shaper statistics |
| `/monitor/firewall/shaper-multi-class-shaper` | 🔷 Beta | GET | Multi-class shaper stats |
| `/monitor/firewall/uuid` | 🔷 Beta | GET | UUID-based objects |
| `/monitor/firewall/vip-overlap` | 🔷 Beta | GET | VIP overlap detection |
| `/monitor/firewall/ztna-firewall-policy` | 🔷 Beta | POST | ZTNA policy counters |

**Test Coverage:** 39 test files with 100% pass rate

### Not Yet Implemented (27 categories)

| # | Category | Status | Notes |
|---|----------|--------|-------|
| 7 | firmware | ⏸️ Not Started | Firmware status |
| 8 | fortiguard | ⏸️ Not Started | FortiGuard services |
| 9 | fortiview | ⏸️ Not Started | FortiView data |
| 10 | geoip | ⏸️ Not Started | GeoIP database |
| 11 | ips | ⏸️ Not Started | IPS statistics |
| 12 | license | ⏸️ Not Started | License information |
| 13 | log | ⏸️ Not Started | Log statistics |
| 14 | network | ⏸️ Not Started | Network statistics |
| 15 | registration | ⏸️ Not Started | Device registration |
| 16 | router | ⏸️ Not Started | Routing tables |
| 17 | sdwan | ⏸️ Not Started | SD-WAN metrics |
| 18 | service | ⏸️ Not Started | Service status |
| 19 | switch-controller | ⏸️ Not Started | FortiSwitch monitoring |
| 20 | system | 🔷 Beta | System resources (partial via CMDB) |
| 21 | user | ⏸️ Not Started | Active users |
| 22 | utm | ⏸️ Not Started | UTM statistics |
| 23 | videofilter | ⏸️ Not Started | Video filter stats |
| 24 | virtual-wan | ⏸️ Not Started | Virtual WAN |
| 25 | vpn | ⏸️ Not Started | VPN status |
| 26 | vpn-certificate | ⏸️ Not Started | VPN certificates |
| 27 | wanopt | ⏸️ Not Started | WAN optimization |
| 28 | web-ui | ⏸️ Not Started | Web UI sessions |
| 29 | webcache | ⏸️ Not Started | Web cache stats |
| 30 | webfilter | ⏸️ Not Started | Web filter stats |
| 31 | webproxy | ⏸️ Not Started | Web proxy stats |
| 32 | wifi | ⏸️ Not Started | WiFi statistics |

**Note:** Monitor API category #20 (system) partially implemented via monitoring/npu-hpe configuration endpoint.

---

## ⚙️ Service API - FortiOS 7.6.5

**Status:** 🔷 Beta - 3 of 3 categories implemented (100%)

| # | Category | Status | Methods | Notes |
|---|----------|--------|---------|-------|
| 1 | sniffer | 🔷 Beta | GET, POST, DELETE | Packet capture |
| 2 | security-rating | 🔷 Beta | GET | Security Fabric rating |
| 3 | system | 🔷 Beta | Various | System operations (reboot, backup) |

**Note:** All service endpoints remain in beta until v1.0.0 with comprehensive unit test coverage.

---

## 📊 API Scope Summary

**FortiOS 7.6.5 Coverage Overview:**

| API Type | Implemented | Total Available | Coverage |
|----------|-------------|-----------------|----------|
| **Configuration (CMDB)** | 18 categories | 40 categories | 45% |
| **Monitoring** | 1 category (partial) | 33 categories | 3% |
| **Logging** | 5 categories | 5 categories | 100% |
| **Services** | 3 categories | 3 categories | 100% |
| **Overall** | **27 categories** | **77 categories** | **35%** |

**Endpoint Level Detail:**
- **CMDB Endpoints:** 150+ endpoints implemented across 18 categories
- **Log Endpoints:** 42 methods (configuration only)
- **Service Endpoints:** 21 methods  
- **Total Methods:** 200+ API methods available

**Recent Additions (v0.3.10-beta):**
- ✅ **Log category:** 56 endpoints with nested object pattern (disk, memory, fortianalyzer, syslogd, tacacs+, webtrends)
- ✅ **Monitoring category:** NPU-HPE configuration
- ✅ **Report category:** Layout management and settings
- ✅ **ICAP category:** Complete with 30+ parameters per endpoint
- ✅ **IPS category:** All 8 endpoints (custom signatures, sensors, decoders, rules)
- ✅ **Firewall category:** 29 endpoints with nested object pattern
- ✅ raw_json parameter added to all 200+ API methods
- ✅ Code quality: 100% PEP 8 compliance (black + isort + flake8)
- ✅ Comprehensive error handling with 387 error codes
- ✅ Full type hints and docstrings

---

## 🤝 Contributing

Want to help implement more endpoints? Contributions are welcome!

### How to Add Coverage

1. Check FortiOS API documentation for endpoint details
2. Implement endpoint following existing patterns
3. Test your implementation thoroughly
4. Update this file with implementation status
5. Update CHANGELOG.md
6. Submit a pull request
6. Submit pull request

---

## 📚 Resources

- [FortiOS REST API Guide](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [Fortinet Developer Network](https://fndn.fortinet.net)
- [API Reference](https://fndn.fortinet.net/index.php?/fortiapi/1-fortios/)

---

**Note:** This coverage map is for FortiOS 7.6.x. Some endpoints may vary in different FortiOS versions.
