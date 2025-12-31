# FortiOS API Endpoints - Complete Method Reference

This document lists all available methods for every endpoint in the hfortix library.

## Summary

- **Total Endpoints**: 857
  - **CMDB**: 561 endpoints
  - **LOG**: 19 endpoints
  - **MONITOR**: 274 endpoints
  - **SERVICE**: 3 endpoints
- **Endpoints with `.exists()`**: 288

## Available Methods

- **`.get()`** - Retrieve data/configuration
- **`.post()`** - Create new objects or execute operations
- **`.put()`** - Update existing objects
- **`.delete()`** - Remove objects
- **`.exists()`** - Check if object exists without exceptions (CMDB only)

## Quick Navigation


### CMDB API

- [alertemail](#alertemail-1-endpoints)
- [antivirus](#antivirus-4-endpoints)
- [application](#application-5-endpoints)
- [authentication](#authentication-3-endpoints)
- [automation](#automation-1-endpoints)
- [casb](#casb-4-endpoints)
- [certificate](#certificate-5-endpoints)
- [diameter-filter](#diameter-filter-1-endpoints)
- [dlp](#dlp-8-endpoints)
- [dnsfilter](#dnsfilter-2-endpoints)
- [emailfilter](#emailfilter-8-endpoints)
- [endpoint-control](#endpoint-control-3-endpoints)
- [ethernet-oam](#ethernet-oam-1-endpoints)
- [extension-controller](#extension-controller-6-endpoints)
- [file-filter](#file-filter-1-endpoints)
- [firewall](#firewall-89-endpoints)
- [ftp-proxy](#ftp-proxy-1-endpoints)
- [icap](#icap-3-endpoints)
- [ips](#ips-8-endpoints)
- [log](#log-56-endpoints)
- [monitoring](#monitoring-1-endpoints)
- [report](#report-2-endpoints)
- [router](#router-26-endpoints)
- [rule](#rule-4-endpoints)
- [sctp-filter](#sctp-filter-1-endpoints)
- [switch-controller](#switch-controller-48-endpoints)
- [system](#system-145-endpoints)
- [user](#user-24-endpoints)
- [videofilter](#videofilter-3-endpoints)
- [virtual-patch](#virtual-patch-1-endpoints)
- [voip](#voip-1-endpoints)
- [vpn](#vpn-19-endpoints)
- [waf](#waf-3-endpoints)
- [web-proxy](#web-proxy-10-endpoints)
- [webfilter](#webfilter-14-endpoints)
- [wireless-controller](#wireless-controller-44-endpoints)
- [ztna](#ztna-5-endpoints)

### LOG API

- [anomaly](#anomaly-1-endpoints)
- [app_ctrl](#app-ctrl-1-endpoints)
- [base](#base-1-endpoints)
- [cifs](#cifs-1-endpoints)
- [dlp](#dlp-1-endpoints)
- [dns](#dns-1-endpoints)
- [emailfilter](#emailfilter-1-endpoints)
- [event](#event-1-endpoints)
- [file_filter](#file-filter-1-endpoints)
- [gtp](#gtp-1-endpoints)
- [ips](#ips-1-endpoints)
- [search](#search-1-endpoints)
- [ssh](#ssh-1-endpoints)
- [ssl](#ssl-1-endpoints)
- [traffic](#traffic-1-endpoints)
- [virus](#virus-1-endpoints)
- [voip](#voip-1-endpoints)
- [waf](#waf-1-endpoints)
- [webfilter](#webfilter-1-endpoints)

### MONITOR API

- [azure](#azure-1-endpoints)
- [casb](#casb-1-endpoints)
- [endpoint_control](#endpoint-control-5-endpoints)
- [extender_controller](#extender-controller-2-endpoints)
- [extension_controller](#extension-controller-3-endpoints)
- [firewall](#firewall-44-endpoints)
- [firmware](#firmware-1-endpoints)
- [fortiguard](#fortiguard-3-endpoints)
- [fortiview](#fortiview-4-endpoints)
- [geoip](#geoip-1-endpoints)
- [ips](#ips-5-endpoints)
- [license](#license-5-endpoints)
- [log](#log-15-endpoints)
- [network](#network-7-endpoints)
- [registration](#registration-3-endpoints)
- [router](#router-11-endpoints)
- [sdwan](#sdwan-1-endpoints)
- [service](#service-1-endpoints)
- [switch_controller](#switch-controller-9-endpoints)
- [system](#system-83-endpoints)
- [user](#user-16-endpoints)
- [utm](#utm-5-endpoints)
- [videofilter](#videofilter-1-endpoints)
- [virtual_wan](#virtual-wan-5-endpoints)
- [vpn](#vpn-3-endpoints)
- [vpn_certificate](#vpn-certificate-6-endpoints)
- [wanopt](#wanopt-3-endpoints)
- [web_ui](#web-ui-2-endpoints)
- [webcache](#webcache-1-endpoints)
- [webfilter](#webfilter-5-endpoints)
- [webproxy](#webproxy-1-endpoints)
- [wifi](#wifi-21-endpoints)

### SERVICE API

- [security_rating](#security-rating-1-endpoints)
- [sniffer](#sniffer-1-endpoints)
- [system](#system-1-endpoints)

---

# CMDB API (561 endpoints)


## alertemail (1 endpoints)

- `alertemail.setting`: `.get()`, `.put()`

## antivirus (4 endpoints)

- `antivirus.exempt_list`: `.delete()`, `.get()`, `.post()`, `.put()`
- `antivirus.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `antivirus.quarantine`: `.get()`, `.put()`
- `antivirus.settings`: `.get()`, `.put()`

## application (5 endpoints)

- `application.custom`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `application.group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `application.list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `application.name`: `.delete()`, `.get()`, `.post()`, `.put()`
- `application.rule_settings`: `.delete()`, `.get()`, `.post()`, `.put()`

## authentication (3 endpoints)

- `authentication.rule`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `authentication.scheme`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `authentication.setting`: `.get()`, `.put()`

## automation (1 endpoints)

- `automation.setting`: `.get()`, `.put()`

## casb (4 endpoints)

- `casb.attribute_match`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `casb.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `casb.saas_application`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `casb.user_activity`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## certificate (5 endpoints)

- `certificate.ca`: `.get()`
- `certificate.crl`: `.get()`
- `certificate.hsm_local`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `certificate.local`: `.get()`
- `certificate.remote`: `.get()`

## diameter-filter (1 endpoints)

- `diameter-filter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## dlp (8 endpoints)

- `dlp.data_type`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.dictionary`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.exact_data_match`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.filepattern`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.label`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.sensor`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dlp.settings`: `.get()`, `.put()`

## dnsfilter (2 endpoints)

- `dnsfilter.domain_filter`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `dnsfilter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## emailfilter (8 endpoints)

- `emailfilter.block_allow_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `emailfilter.bword`: `.delete()`, `.get()`, `.post()`, `.put()`
- `emailfilter.dnsbl`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `emailfilter.fortishield`: `.get()`, `.put()`
- `emailfilter.iptrust`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `emailfilter.mheader`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `emailfilter.options`: `.get()`, `.put()`
- `emailfilter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## endpoint-control (3 endpoints)

- `endpoint-control.fctems`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `endpoint-control.fctems_override`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `endpoint-control.settings`: `.get()`, `.put()`

## ethernet-oam (1 endpoints)

- `ethernet-oam.cfm`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## extension-controller (6 endpoints)

- `extension-controller.dataplan`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `extension-controller.extender`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `extension-controller.extender_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `extension-controller.extender_vap`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `extension-controller.fortigate`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `extension-controller.fortigate_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## file-filter (1 endpoints)

- `file-filter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## firewall (89 endpoints)

- `firewall.DoS_policy`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.DoS_policy6`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.access_proxy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.access_proxy6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.access_proxy_ssh_client_cert`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.access_proxy_virtual_host`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.address`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.address6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.address6_template`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.addrgrp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.addrgrp6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.auth_portal`: `.get()`, `.put()`
- `firewall.central_snat_map`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.city`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.country`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.decrypted_traffic_mirror`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.dnstranslation`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.global_`: `.get()`, `.put()`
- `firewall.identity_based_route`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.interface_policy`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.interface_policy6`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_addition`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_append`: `.get()`, `.put()`
- `firewall.internet_service_botnet`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_custom`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_custom_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_definition`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_extension`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_fortiguard`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_ipbl_reason`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_ipbl_vendor`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_name`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_owner`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_reputation`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_sld`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.internet_service_subapp`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.ip_translation`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.ipmacbinding_setting`: `.get()`, `.put()`
- `firewall.ipmacbinding_table`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.ippool`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.ippool6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.ldb_monitor`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.local_in_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.local_in_policy6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.multicast_address`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.multicast_address6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.multicast_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.multicast_policy6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.network_service_dynamic`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.on_demand_sniffer`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.profile_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.profile_protocol_options`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.proxy_address`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.proxy_addrgrp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.proxy_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.region`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.schedule_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.schedule_onetime`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.schedule_recurring`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.security_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.service_category`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.service_custom`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.service_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.shaper_per_ip_shaper`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.shaper_traffic_shaper`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.shaping_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.shaping_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.sniffer`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.ssh_host_key`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.ssh_local_ca`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.ssh_local_key`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.ssh_setting`: `.get()`, `.put()`
- `firewall.ssl_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.ssl_setting`: `.get()`, `.put()`
- `firewall.ssl_ssh_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.traffic_class`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.ttl_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.vendor_mac`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.vendor_mac_summary`: `.get()`, `.put()`
- `firewall.vip`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.vip6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.vipgrp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.vipgrp6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `firewall.wildcard_fqdn_custom`: `.delete()`, `.get()`, `.post()`, `.put()`
- `firewall.wildcard_fqdn_group`: `.delete()`, `.get()`, `.post()`, `.put()`

## ftp-proxy (1 endpoints)

- `ftp-proxy.explicit`: `.get()`, `.put()`

## icap (3 endpoints)

- `icap.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `icap.server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `icap.server_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## ips (8 endpoints)

- `ips.custom`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ips.decoder`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ips.global_`: `.get()`, `.put()`
- `ips.rule`: `.delete()`, `.get()`, `.post()`, `.put()`
- `ips.rule_settings`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ips.sensor`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ips.settings`: `.get()`, `.put()`
- `ips.view_map`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## log (56 endpoints)

- `log.custom_field`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `log.disk_filter`: `.get()`, `.put()`
- `log.disk_setting`: `.get()`, `.put()`
- `log.eventfilter`: `.get()`, `.put()`
- `log.fortianalyzer2_filter`: `.get()`, `.put()`
- `log.fortianalyzer2_override_filter`: `.get()`, `.put()`
- `log.fortianalyzer2_override_setting`: `.get()`, `.put()`
- `log.fortianalyzer2_setting`: `.get()`, `.put()`
- `log.fortianalyzer3_filter`: `.get()`, `.put()`
- `log.fortianalyzer3_override_filter`: `.get()`, `.put()`
- `log.fortianalyzer3_override_setting`: `.get()`, `.put()`
- `log.fortianalyzer3_setting`: `.get()`, `.put()`
- `log.fortianalyzer_cloud_filter`: `.get()`, `.put()`
- `log.fortianalyzer_cloud_override_filter`: `.get()`, `.put()`
- `log.fortianalyzer_cloud_override_setting`: `.get()`, `.put()`
- `log.fortianalyzer_cloud_setting`: `.get()`, `.put()`
- `log.fortianalyzer_filter`: `.get()`, `.put()`
- `log.fortianalyzer_override_filter`: `.get()`, `.put()`
- `log.fortianalyzer_override_setting`: `.get()`, `.put()`
- `log.fortianalyzer_setting`: `.get()`, `.put()`
- `log.fortiguard_filter`: `.get()`, `.put()`
- `log.fortiguard_override_filter`: `.get()`, `.put()`
- `log.fortiguard_override_setting`: `.get()`, `.put()`
- `log.fortiguard_setting`: `.get()`, `.put()`
- `log.gui_display`: `.get()`, `.put()`
- `log.memory_filter`: `.get()`, `.put()`
- `log.memory_global_setting`: `.get()`, `.put()`
- `log.memory_setting`: `.get()`, `.put()`
- `log.null_device_filter`: `.get()`, `.put()`
- `log.null_device_setting`: `.get()`, `.put()`
- `log.setting`: `.get()`, `.put()`
- `log.syslogd2_filter`: `.get()`, `.put()`
- `log.syslogd2_override_filter`: `.get()`, `.put()`
- `log.syslogd2_override_setting`: `.get()`, `.put()`
- `log.syslogd2_setting`: `.get()`, `.put()`
- `log.syslogd3_filter`: `.get()`, `.put()`
- `log.syslogd3_override_filter`: `.get()`, `.put()`
- `log.syslogd3_override_setting`: `.get()`, `.put()`
- `log.syslogd3_setting`: `.get()`, `.put()`
- `log.syslogd4_filter`: `.get()`, `.put()`
- `log.syslogd4_override_filter`: `.get()`, `.put()`
- `log.syslogd4_override_setting`: `.get()`, `.put()`
- `log.syslogd4_setting`: `.get()`, `.put()`
- `log.syslogd_filter`: `.get()`, `.put()`
- `log.syslogd_override_filter`: `.get()`, `.put()`
- `log.syslogd_override_setting`: `.get()`, `.put()`
- `log.syslogd_setting`: `.get()`, `.put()`
- `log.tacacs_plus_accounting2_filter`: `.get()`, `.put()`
- `log.tacacs_plus_accounting2_setting`: `.get()`, `.put()`
- `log.tacacs_plus_accounting3_filter`: `.get()`, `.put()`
- `log.tacacs_plus_accounting3_setting`: `.get()`, `.put()`
- `log.tacacs_plus_accounting_filter`: `.get()`, `.put()`
- `log.tacacs_plus_accounting_setting`: `.get()`, `.put()`
- `log.threat_weight`: `.get()`, `.put()`
- `log.webtrends_filter`: `.get()`, `.put()`
- `log.webtrends_setting`: `.get()`, `.put()`

## monitoring (1 endpoints)

- `monitoring.npu_hpe`: `.get()`, `.put()`

## report (2 endpoints)

- `report.layout`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `report.setting`: `.get()`, `.put()`

## router (26 endpoints)

- `router.access_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.access_list6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.aspath_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.auth_path`: `.delete()`, `.get()`, `.post()`, `.put()`
- `router.bfd`: `.get()`, `.put()`
- `router.bfd6`: `.get()`, `.put()`
- `router.bgp`: `.get()`, `.put()`
- `router.community_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.extcommunity_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.isis`: `.get()`, `.put()`
- `router.key_chain`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.multicast`: `.get()`, `.put()`
- `router.multicast6`: `.get()`, `.put()`
- `router.multicast_flow`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.ospf`: `.get()`, `.put()`
- `router.ospf6`: `.get()`, `.put()`
- `router.policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.policy6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.prefix_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.prefix_list6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.rip`: `.get()`, `.put()`
- `router.ripng`: `.get()`, `.put()`
- `router.route_map`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.setting`: `.get()`, `.put()`
- `router.static`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `router.static6`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## rule (4 endpoints)

- `rule.fmwp`: `.delete()`, `.get()`, `.post()`, `.put()`
- `rule.iotd`: `.delete()`, `.get()`, `.post()`, `.put()`
- `rule.otdt`: `.delete()`, `.get()`, `.post()`, `.put()`
- `rule.otvp`: `.delete()`, `.get()`, `.post()`, `.put()`

## sctp-filter (1 endpoints)

- `sctp-filter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## switch-controller (48 endpoints)

- `switch-controller._802_1X_settings`: `.get()`, `.put()`
- `switch-controller.acl_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.acl_ingress`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.auto_config_custom`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.auto_config_default`: `.get()`, `.put()`
- `switch-controller.auto_config_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.custom_command`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.dynamic_port_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.flow_tracking`: `.get()`, `.put()`
- `switch-controller.fortilink_settings`: `.delete()`, `.get()`, `.post()`, `.put()`
- `switch-controller.global_`: `.get()`, `.put()`
- `switch-controller.igmp_snooping`: `.get()`, `.put()`
- `switch-controller.initial_config_template`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.initial_config_vlans`: `.get()`, `.put()`
- `switch-controller.ip_source_guard_log`: `.get()`, `.put()`
- `switch-controller.lldp_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.lldp_settings`: `.get()`, `.put()`
- `switch-controller.location`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.mac_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.managed_switch`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.network_monitor_settings`: `.get()`, `.put()`
- `switch-controller.ptp_interface_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.ptp_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.qos_dot1p_map`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.qos_ip_dscp_map`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.qos_qos_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.qos_queue_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.remote_log`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.security_policy__802_1X`: `.delete()`, `.get()`, `.post()`, `.put()`
- `switch-controller.security_policy_local_access`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.sflow`: `.get()`, `.put()`
- `switch-controller.snmp_community`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.snmp_sysinfo`: `.get()`, `.put()`
- `switch-controller.snmp_trap_threshold`: `.get()`, `.put()`
- `switch-controller.snmp_user`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.storm_control`: `.get()`, `.put()`
- `switch-controller.storm_control_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.stp_instance`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.stp_settings`: `.get()`, `.put()`
- `switch-controller.switch_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.switch_interface_tag`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.switch_log`: `.get()`, `.put()`
- `switch-controller.switch_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.system`: `.get()`, `.put()`
- `switch-controller.traffic_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.traffic_sniffer`: `.get()`, `.put()`
- `switch-controller.virtual_port_pool`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `switch-controller.vlan_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## system (145 endpoints)

- `system._3g_modem_custom`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.accprofile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.acme`: `.get()`, `.put()`
- `system.admin`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.affinity_interrupt`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.affinity_packet_redistribution`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.alarm`: `.get()`, `.put()`
- `system.alias`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.api_user`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.arp_table`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.auto_install`: `.get()`, `.put()`
- `system.auto_script`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.automation_action`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.automation_condition`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.automation_destination`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.automation_stitch`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.automation_trigger`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.autoupdate_schedule`: `.get()`, `.put()`
- `system.central_management`: `.get()`, `.put()`
- `system.cloud_service`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.console`: `.get()`, `.put()`
- `system.csf`: `.get()`, `.put()`
- `system.custom_language`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ddns`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.dedicated_mgmt`: `.get()`, `.put()`
- `system.device_upgrade`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.device_upgrade_exemptions`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.dhcp6_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.dhcp_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.dns`: `.get()`, `.put()`
- `system.dns64`: `.get()`, `.put()`
- `system.dns_database`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.dns_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.dscp_based_priority`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.email_server`: `.get()`, `.put()`
- `system.evpn`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.external_resource`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.fabric_vpn`: `.get()`, `.put()`
- `system.federated_upgrade`: `.get()`, `.put()`
- `system.fips_cc`: `.get()`, `.put()`
- `system.fortiguard`: `.get()`, `.put()`
- `system.fortisandbox`: `.get()`, `.put()`
- `system.fsso_polling`: `.get()`, `.put()`
- `system.ftm_push`: `.get()`, `.put()`
- `system.geneve`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.geoip_country`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.geoip_override`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.global_`: `.get()`, `.put()`
- `system.gre_tunnel`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ha`: `.get()`, `.put()`
- `system.ha_monitor`: `.get()`, `.put()`
- `system.health_check_fortiguard`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.ike`: `.get()`, `.put()`
- `system.interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ipam`: `.get()`, `.put()`
- `system.ipip_tunnel`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ips`: `.get()`, `.put()`
- `system.ips_urlfilter_dns`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.ips_urlfilter_dns6`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.ipsec_aggregate`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ipv6_neighbor_cache`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ipv6_tunnel`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.link_monitor`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.lldp_network_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.lte_modem`: `.get()`, `.put()`
- `system.mac_address_table`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.mobile_tunnel`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.modem`: `.get()`, `.put()`
- `system.nd_proxy`: `.get()`, `.put()`
- `system.netflow`: `.get()`, `.put()`
- `system.network_visibility`: `.get()`, `.put()`
- `system.ngfw_settings`: `.get()`, `.put()`
- `system.np6xlite`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.npu`: `.get()`, `.put()`
- `system.ntp`: `.get()`, `.put()`
- `system.object_tagging`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.password_policy`: `.get()`, `.put()`
- `system.password_policy_guest_admin`: `.get()`, `.put()`
- `system.pcp_server`: `.get()`, `.put()`
- `system.physical_switch`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.pppoe_interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.probe_response`: `.get()`, `.put()`
- `system.proxy_arp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.ptp`: `.get()`, `.put()`
- `system.replacemsg_admin`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_alertmail`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_auth`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_automation`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_fortiguard_wf`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_group`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_http`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_image`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_mail`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_nac_quar`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_spam`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_sslvpn`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_traffic_quota`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.replacemsg_utm`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.resource_limits`: `.get()`, `.put()`
- `system.saml`: `.get()`, `.put()`
- `system.sdn_connector`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sdn_proxy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sdn_vpn`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sdwan`: `.get()`, `.put()`
- `system.security_rating_controls`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.security_rating_settings`: `.get()`, `.put()`
- `system.session_helper`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.session_ttl`: `.get()`, `.put()`
- `system.settings`: `.get()`, `.put()`
- `system.sflow`: `.get()`, `.put()`
- `system.sit_tunnel`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sms_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.snmp_community`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.snmp_mib_view`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.snmp_rmon_stat`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.snmp_sysinfo`: `.get()`, `.put()`
- `system.snmp_user`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sov_sase`: `.get()`, `.put()`
- `system.speed_test_schedule`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.speed_test_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.speed_test_setting`: `.get()`, `.put()`
- `system.ssh_config`: `.get()`, `.put()`
- `system.sso_admin`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sso_forticloud_admin`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.sso_fortigate_cloud_admin`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.standalone_cluster`: `.get()`, `.put()`
- `system.storage`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.stp`: `.get()`, `.put()`
- `system.switch_interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.timezone`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.tos_based_priority`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vdom`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vdom_dns`: `.get()`, `.put()`
- `system.vdom_exception`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vdom_link`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vdom_netflow`: `.get()`, `.put()`
- `system.vdom_property`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vdom_radius_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vdom_sflow`: `.get()`, `.put()`
- `system.virtual_switch`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.virtual_wire_pair`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vne_interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.vxlan`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `system.wccp`: `.delete()`, `.get()`, `.post()`, `.put()`
- `system.zone`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## user (24 endpoints)

- `user.adgrp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.certificate`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.domain_controller`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.exchange`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.external_identity_provider`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.fortitoken`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.fsso`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.fsso_polling`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.krb_keytab`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.ldap`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.local`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.nac_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.password_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.peer`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.peergrp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.pop3`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.quarantine`: `.get()`, `.put()`
- `user.radius`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.saml`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.scim`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.security_exempt_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `user.setting`: `.get()`, `.put()`
- `user.tacacs_plus_`: `.delete()`, `.get()`, `.post()`, `.put()`

## videofilter (3 endpoints)

- `videofilter.keyword`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `videofilter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `videofilter.youtube_key`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## virtual-patch (1 endpoints)

- `virtual-patch.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## voip (1 endpoints)

- `voip.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## vpn (19 endpoints)

- `vpn.certificate_ca`: `.get()`, `.post()`
- `vpn.certificate_crl`: `.get()`, `.post()`
- `vpn.certificate_hsm_local`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.certificate_local`: `.get()`, `.post()`
- `vpn.certificate_ocsp_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.certificate_remote`: `.get()`, `.post()`
- `vpn.certificate_setting`: `.get()`, `.put()`
- `vpn.ipsec_concentrator`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_fec`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_manualkey`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_manualkey_interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_phase1`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_phase1_interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_phase2`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.ipsec_phase2_interface`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.kmip_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `vpn.l2tp`: `.get()`, `.put()`
- `vpn.pptp`: `.get()`, `.put()`
- `vpn.qkd`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## waf (3 endpoints)

- `waf.main_class`: `.delete()`, `.get()`, `.post()`, `.put()`
- `waf.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `waf.signature`: `.delete()`, `.get()`, `.post()`, `.put()`

## web-proxy (10 endpoints)

- `web-proxy.debug_url`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `web-proxy.explicit`: `.get()`, `.put()`
- `web-proxy.fast_fallback`: `.delete()`, `.get()`, `.post()`, `.put()`
- `web-proxy.forward_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `web-proxy.forward_server_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `web-proxy.global_`: `.get()`, `.put()`
- `web-proxy.isolator_server`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `web-proxy.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `web-proxy.url_match`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `web-proxy.wisp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## webfilter (14 endpoints)

- `webfilter.content`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.content_header`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.fortiguard`: `.get()`, `.put()`
- `webfilter.ftgd_local_cat`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.ftgd_local_rating`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.ftgd_local_risk`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.ftgd_risk_level`: `.delete()`, `.get()`, `.post()`, `.put()`
- `webfilter.ips_urlfilter_cache_setting`: `.get()`, `.put()`
- `webfilter.ips_urlfilter_setting`: `.get()`, `.put()`
- `webfilter.ips_urlfilter_setting6`: `.get()`, `.put()`
- `webfilter.override`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.search_engine`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `webfilter.urlfilter`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## wireless-controller (44 endpoints)

- `wireless-controller.access_control_list`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.ap_status`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.apcfg_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.arrp_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.ble_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.bonjour_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.global_`: `.get()`, `.put()`
- `wireless-controller.hotspot20_anqp_3gpp_cellular`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_anqp_ip_address_type`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_anqp_nai_realm`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_anqp_network_auth_type`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_anqp_roaming_consortium`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_anqp_venue_name`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_anqp_venue_url`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_advice_of_charge`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_conn_capability`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_operator_name`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_osu_provider`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_osu_provider_nai`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_terms_and_conditions`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_h2qp_wan_metric`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_hs_profile`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_icon`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.hotspot20_qos_map`: `.delete()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.inter_controller`: `.get()`, `.put()`
- `wireless-controller.log`: `.get()`, `.put()`
- `wireless-controller.lw_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.mpsk_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.nac_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.qos_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.region`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.setting`: `.get()`, `.put()`
- `wireless-controller.snmp`: `.get()`, `.put()`
- `wireless-controller.ssid_policy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.syslog_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.timers`: `.get()`, `.put()`
- `wireless-controller.utm_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.vap`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.vap_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.wag_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.wids_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.wtp`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.wtp_group`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `wireless-controller.wtp_profile`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`

## ztna (5 endpoints)

- `ztna.reverse_connector`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ztna.traffic_forward_proxy`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ztna.web_portal`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ztna.web_portal_bookmark`: `.delete()`, `.exists()`, `.get()`, `.post()`, `.put()`
- `ztna.web_proxy`: `.delete()`, `.get()`, `.post()`, `.put()`

---

# LOG API (19 endpoints)


## anomaly (1 endpoints)

- `anomaly`: `.get()`

## app_ctrl (1 endpoints)

- `app_ctrl`: `.get()`

## base (1 endpoints)

- `base`: `.get()`

## cifs (1 endpoints)

- `cifs`: `.get()`

## dlp (1 endpoints)

- `dlp`: `.get()`

## dns (1 endpoints)

- `dns`: `.get()`

## emailfilter (1 endpoints)

- `emailfilter`: `.get()`

## event (1 endpoints)

- `event`: `.get()`

## file_filter (1 endpoints)

- `file_filter`: `.get()`

## gtp (1 endpoints)

- `gtp`: `.get()`

## ips (1 endpoints)

- `ips`: `.get()`

## search (1 endpoints)

- `search.search`: `.get()`, `.post()`

## ssh (1 endpoints)

- `ssh`: `.get()`

## ssl (1 endpoints)

- `ssl`: `.get()`

## traffic (1 endpoints)

- `traffic`: `.get()`

## virus (1 endpoints)

- `virus`: `.get()`

## voip (1 endpoints)

- `voip`: `.get()`

## waf (1 endpoints)

- `waf`: `.get()`

## webfilter (1 endpoints)

- `webfilter`: `.get()`

---

# MONITOR API (274 endpoints)


## azure (1 endpoints)

- `azure.application_list`: `.get()`, `.post()`

## casb (1 endpoints)

- `casb.saas_application`: `.get()`

## endpoint_control (5 endpoints)

- `endpoint_control.avatar`: `.get()`
- `endpoint_control.ems`: `.get()`, `.post()`
- `endpoint_control.installer`: `.get()`
- `endpoint_control.record_list`: `.get()`
- `endpoint_control.summary`: `.get()`

## extender_controller (2 endpoints)

- `extender_controller.extender`: `.get()`, `.post()`
- `extender_controller.modem_firmware`: `.get()`

## extension_controller (3 endpoints)

- `extension_controller.fortigate`: `.get()`
- `extension_controller.lan_extension_vdom`: `.get()`
- `extension_controller.lan_extension_vdom_status`: `.get()`

## firewall (44 endpoints)

- `firewall.acl`: `.get()`, `.post()`
- `firewall.acl6`: `.get()`, `.post()`
- `firewall.address6_dynamic`: `.get()`
- `firewall.address_dynamic`: `.get()`
- `firewall.address_fqdns`: `.get()`
- `firewall.address_fqdns6`: `.get()`
- `firewall.central_snat_map`: `.get()`, `.post()`
- `firewall.check_addrgrp_exclude_mac_member`: `.get()`
- `firewall.clearpass_address`: `.post()`
- `firewall.dnat`: `.get()`, `.post()`
- `firewall.gtp`: `.get()`, `.post()`
- `firewall.gtp_runtime_statistics`: `.get()`
- `firewall.gtp_statistics`: `.get()`
- `firewall.health`: `.get()`
- `firewall.internet_service_basic`: `.get()`
- `firewall.internet_service_details`: `.get()`
- `firewall.internet_service_fqdn`: `.get()`
- `firewall.internet_service_fqdn_icon_ids`: `.get()`
- `firewall.internet_service_match`: `.get()`
- `firewall.internet_service_reputation`: `.get()`
- `firewall.ippool`: `.get()`
- `firewall.load_balance`: `.get()`
- `firewall.local_in`: `.get()`
- `firewall.local_in6`: `.get()`
- `firewall.multicast_policy`: `.get()`, `.post()`
- `firewall.multicast_policy6`: `.get()`, `.post()`
- `firewall.network_service_dynamic`: `.get()`
- `firewall.per_ip_shaper`: `.get()`, `.post()`
- `firewall.policy`: `.get()`, `.post()`
- `firewall.policy_lookup`: `.get()`
- `firewall.proxy`: `.get()`
- `firewall.proxy_policy`: `.get()`, `.post()`
- `firewall.saas_application`: `.get()`
- `firewall.sdn_connector_filters`: `.get()`
- `firewall.security_policy`: `.get()`, `.post()`
- `firewall.session`: `.post()`
- `firewall.session6`: `.post()`
- `firewall.sessions`: `.get()`
- `firewall.shaper`: `.get()`, `.post()`
- `firewall.uuid`: `.get()`
- `firewall.uuid_list`: `.get()`
- `firewall.uuid_type_lookup`: `.get()`
- `firewall.vip_overlap`: `.get()`
- `firewall.ztna_firewall_policy`: `.post()`

## firmware (1 endpoints)

- `firmware.extension_device`: `.get()`

## fortiguard (3 endpoints)

- `fortiguard.answers`: `.get()`
- `fortiguard.redirect_portal`: `.get()`
- `fortiguard.service_communication_stats`: `.get()`

## fortiview (4 endpoints)

- `fortiview.historical_statistics`: `.get()`
- `fortiview.realtime_proxy_statistics`: `.get()`
- `fortiview.realtime_statistics`: `.get()`
- `fortiview.session`: `.post()`

## geoip (1 endpoints)

- `geoip.geoip_query`: `.post()`

## ips (5 endpoints)

- `ips.anomaly`: `.get()`
- `ips.hold_signatures`: `.get()`
- `ips.metadata`: `.get()`
- `ips.rate_based`: `.get()`
- `ips.session`: `.get()`

## license (5 endpoints)

- `license.database`: `.post()`
- `license.fortianalyzer_status`: `.get()`
- `license.forticare_org_list`: `.get()`
- `license.forticare_resellers`: `.get()`
- `license.status`: `.get()`

## log (15 endpoints)

- `log.av_archive`: `.get()`
- `log.current_disk_usage`: `.get()`
- `log.device`: `.get()`
- `log.feature_set`: `.get()`
- `log.fortianalyzer`: `.get()`
- `log.fortianalyzer_queue`: `.get()`
- `log.forticloud`: `.get()`
- `log.forticloud_report`: `.get()`
- `log.forticloud_report_list`: `.get()`
- `log.historic_daily_remote_logs`: `.get()`
- `log.hourly_disk_usage`: `.get()`
- `log.local_report`: `.get()`, `.post()`
- `log.local_report_list`: `.get()`
- `log.policy_archive`: `.get()`
- `log.stats`: `.get()`, `.post()`

## network (7 endpoints)

- `network.arp`: `.get()`
- `network.ddns`: `.get()`
- `network.debug_flow`: `.post()`
- `network.dns`: `.get()`
- `network.fortiguard`: `.get()`
- `network.lldp`: `.get()`
- `network.reverse_ip_lookup`: `.get()`

## registration (3 endpoints)

- `registration.forticare`: `.get()`, `.post()`
- `registration.forticloud`: `.get()`, `.post()`
- `registration.vdom`: `.post()`

## router (11 endpoints)

- `router.bgp`: `.get()`, `.post()`
- `router.charts`: `.get()`
- `router.ipv4`: `.get()`
- `router.ipv6`: `.get()`
- `router.lookup`: `.get()`
- `router.lookup_policy`: `.get()`
- `router.ospf`: `.get()`
- `router.policy`: `.get()`
- `router.policy6`: `.get()`
- `router.sdwan`: `.get()`
- `router.statistics`: `.get()`

## sdwan (1 endpoints)

- `sdwan.link_monitor_metrics`: `.post()`

## service (1 endpoints)

- `service.ldap`: `.get()`

## switch_controller (9 endpoints)

- `switch_controller.detected_device`: `.get()`
- `switch_controller.fsw_firmware`: `.get()`, `.post()`
- `switch_controller.isl_lockdown`: `.get()`, `.post()`
- `switch_controller.known_nac_device_criteria_list`: `.get()`
- `switch_controller.managed_switch`: `.get()`, `.post()`
- `switch_controller.matched_devices`: `.get()`
- `switch_controller.mclag_icl`: `.get()`, `.post()`
- `switch_controller.nac_device`: `.get()`
- `switch_controller.recommendation`: `.post()`

## system (83 endpoints)

- `system.3g_modem`: `.get()`
- `system.5g_modem`: `.get()`
- `system.acme_certificate_status`: `.get()`
- `system.acquired_dns`: `.get()`
- `system.admin`: `.post()`
- `system.api_user`: `.post()`
- `system.automation_action`: `.get()`
- `system.automation_stitch`: `.get()`, `.post()`
- `system.available_certificates`: `.get()`
- `system.available_interfaces`: `.get()`
- `system.botnet`: `.get()`
- `system.botnet_domains`: `.get()`
- `system.central_management`: `.get()`
- `system.certificate`: `.get()`, `.post()`
- `system.change_password`: `.post()`
- `system.check_port_availability`: `.get()`
- `system.cluster`: `.get()`
- `system.com_log`: `.get()`, `.post()`
- `system.config`: `.get()`, `.post()`
- `system.config_error_log`: `.get()`
- `system.config_revision`: `.get()`, `.post()`
- `system.config_script`: `.get()`, `.post()`
- `system.config_sync`: `.get()`
- `system.crash_log`: `.get()`, `.post()`
- `system.csf`: `.get()`, `.post()`
- `system.current_admins`: `.get()`
- `system.debug`: `.get()`
- `system.dhcp`: `.get()`, `.post()`
- `system.dhcp6`: `.post()`
- `system.disconnect_admins`: `.post()`
- `system.external_resource`: `.get()`, `.post()`
- `system.firmware`: `.get()`, `.post()`
- `system.fortiguard`: `.get()`, `.post()`
- `system.fortimanager`: `.get()`, `.post()`
- `system.fsck`: `.post()`
- `system.global_resources`: `.get()`
- `system.global_search`: `.get()`
- `system.ha_backup_hb_used`: `.get()`
- `system.ha_checksums`: `.get()`
- `system.ha_history`: `.get()`
- `system.ha_hw_interface`: `.get()`
- `system.ha_nonsync_checksums`: `.get()`
- `system.ha_peer`: `.get()`, `.post()`
- `system.ha_statistics`: `.get()`
- `system.ha_table_checksums`: `.get()`
- `system.hscalefw_license`: `.post()`
- `system.interface`: `.get()`, `.post()`
- `system.interface_connected_admins_info`: `.get()`
- `system.ipam`: `.get()`
- `system.ipconf`: `.get()`
- `system.link_monitor`: `.get()`
- `system.logdisk`: `.post()`
- `system.lte_modem`: `.get()`, `.post()`
- `system.modem`: `.get()`, `.post()`
- `system.modem_3g`: `.get()`
- `system.modem_5g`: `.get()`
- `system.monitor_sensor`: `.get()`
- `system.ntp`: `.get()`
- `system.object`: `.get()`
- `system.os`: `.post()`
- `system.password_policy_conform`: `.post()`
- `system.performance`: `.get()`
- `system.private_data_encryption`: `.post()`
- `system.process`: `.post()`
- `system.resolve_fqdn`: `.get()`
- `system.resource`: `.get()`
- `system.running_processes`: `.get()`
- `system.sandbox`: `.get()`
- `system.sdn_connector`: `.get()`, `.post()`
- `system.sensor_info`: `.get()`
- `system.status`: `.get()`
- `system.storage`: `.get()`
- `system.time`: `.get()`, `.post()`
- `system.timezone`: `.get()`
- `system.traffic_history`: `.get()`, `.post()`
- `system.trusted_cert_authorities`: `.get()`
- `system.upgrade_report`: `.get()`
- `system.usb_device`: `.post()`
- `system.usb_log`: `.get()`, `.post()`
- `system.vdom_link`: `.get()`
- `system.vdom_resource`: `.get()`
- `system.vm_information`: `.get()`
- `system.vmlicense`: `.post()`

## user (16 endpoints)

- `user.banned`: `.get()`, `.post()`
- `user.collected_email`: `.get()`
- `user.device`: `.get()`, `.post()`
- `user.firewall`: `.get()`, `.post()`
- `user.fortitoken`: `.get()`, `.post()`
- `user.fortitoken_cloud`: `.get()`, `.post()`
- `user.fsso`: `.get()`, `.post()`
- `user.guest`: `.post()`
- `user.info`: `.get()`
- `user.local`: `.post()`
- `user.password_policy_conform`: `.post()`
- `user.proxy`: `.get()`
- `user.query`: `.post()`
- `user.radius`: `.get()`, `.post()`
- `user.scim`: `.get()`
- `user.tacacs_plus`: `.post()`

## utm (5 endpoints)

- `utm.antivirus`: `.get()`
- `utm.app_lookup`: `.get()`
- `utm.application_categories`: `.get()`
- `utm.blacklisted_certificates`: `.get()`
- `utm.rating_lookup`: `.post()`

## videofilter (1 endpoints)

- `videofilter.fortiguard_categories`: `.get()`

## virtual_wan (5 endpoints)

- `virtual_wan.health_check`: `.get()`
- `virtual_wan.interface_log`: `.get()`
- `virtual_wan.members`: `.get()`
- `virtual_wan.sla_log`: `.get()`
- `virtual_wan.sladb`: `.get()`

## vpn (3 endpoints)

- `vpn.ike`: `.post()`
- `vpn.ipsec`: `.get()`, `.post()`
- `vpn.ssl`: `.get()`, `.post()`

## vpn_certificate (6 endpoints)

- `vpn_certificate.ca`: `.post()`
- `vpn_certificate.cert_name_available`: `.get()`
- `vpn_certificate.crl`: `.post()`
- `vpn_certificate.csr`: `.post()`
- `vpn_certificate.local`: `.post()`
- `vpn_certificate.remote`: `.post()`

## wanopt (3 endpoints)

- `wanopt.history`: `.get()`, `.post()`
- `wanopt.peer_stats`: `.get()`, `.post()`
- `wanopt.webcache`: `.get()`, `.post()`

## web_ui (2 endpoints)

- `web_ui.custom_language`: `.get()`, `.post()`
- `web_ui.language`: `.post()`

## webcache (1 endpoints)

- `webcache.stats`: `.get()`, `.post()`

## webfilter (5 endpoints)

- `webfilter.category_quota`: `.get()`, `.post()`
- `webfilter.fortiguard_categories`: `.get()`
- `webfilter.malicious_urls`: `.get()`
- `webfilter.override`: `.get()`, `.post()`
- `webfilter.trusted_urls`: `.get()`

## webproxy (1 endpoints)

- `webproxy.pacfile`: `.get()`, `.post()`

## wifi (21 endpoints)

- `wifi.ap_channels`: `.get()`
- `wifi.ap_names`: `.get()`
- `wifi.ap_profile`: `.post()`
- `wifi.ap_status`: `.get()`
- `wifi.client`: `.get()`, `.post()`
- `wifi.euclid`: `.get()`, `.post()`
- `wifi.firmware`: `.get()`, `.post()`
- `wifi.interfering_ap`: `.get()`
- `wifi.managed_ap`: `.get()`, `.post()`
- `wifi.matched_devices`: `.get()`
- `wifi.meta`: `.get()`
- `wifi.nac_device`: `.get()`
- `wifi.network`: `.get()`, `.post()`
- `wifi.region_image`: `.get()`, `.post()`
- `wifi.rogue_ap`: `.get()`, `.post()`
- `wifi.spectrum`: `.get()`, `.post()`
- `wifi.ssid`: `.post()`
- `wifi.station_capability`: `.get()`
- `wifi.statistics`: `.get()`
- `wifi.unassociated_devices`: `.get()`
- `wifi.vlan_probe`: `.get()`, `.post()`

---

# SERVICE API (3 endpoints)


## security_rating (1 endpoints)

- `security_rating.security_rating`: `.get()`

## sniffer (1 endpoints)

- `sniffer.sniffer`: `.delete()`, `.get()`, `.post()`

## system (1 endpoints)

- `system.system`: `.get()`
