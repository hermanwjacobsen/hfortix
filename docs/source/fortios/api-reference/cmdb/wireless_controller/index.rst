Wireless Controller
===================

Overview
--------

The ``cmdb.wireless_controller`` namespace provides configuration management for:

- :doc:`Access Control List <access_control_list>` - Access Control List configuration endpoint.
- :doc:`Ap Status <ap_status>` - Ap Status configuration endpoint.
- :doc:`Apcfg Profile <apcfg_profile>` - Apcfg Profile configuration endpoint.
- :doc:`Arrp Profile <arrp_profile>` - Arrp Profile configuration endpoint.
- :doc:`Ble Profile <ble_profile>` - Ble Profile configuration endpoint.
- :doc:`Bonjour Profile <bonjour_profile>` - Bonjour Profile configuration endpoint.
- :doc:`Global <global_>` - Global configuration endpoint.
- :doc:`Hotspot20 Anqp 3gpp Cellular <hotspot20_anqp_3gpp_cellular>` - Hotspot20 Anqp 3gpp Cellular configuration endpoint.
- :doc:`Hotspot20 Anqp IP Address Type <hotspot20_anqp_ip_address_type>` - Hotspot20 Anqp IP Address Type configuration endpoint.
- :doc:`Hotspot20 Anqp Nai Realm <hotspot20_anqp_nai_realm>` - Hotspot20 Anqp Nai Realm configuration endpoint.
- :doc:`Hotspot20 Anqp Network Auth Type <hotspot20_anqp_network_auth_type>` - Hotspot20 Anqp Network Auth Type configuration endpoint.
- :doc:`Hotspot20 Anqp Roaming Consortium <hotspot20_anqp_roaming_consortium>` - Hotspot20 Anqp Roaming Consortium configuration endpoint.
- :doc:`Hotspot20 Anqp Venue Name <hotspot20_anqp_venue_name>` - Hotspot20 Anqp Venue Name configuration endpoint.
- :doc:`Hotspot20 Anqp Venue Url <hotspot20_anqp_venue_url>` - Hotspot20 Anqp Venue Url configuration endpoint.
- :doc:`Hotspot20 H2qp Advice Of Charge <hotspot20_h2qp_advice_of_charge>` - Hotspot20 H2qp Advice Of Charge configuration endpoint.
- :doc:`Hotspot20 H2qp Conn Capability <hotspot20_h2qp_conn_capability>` - Hotspot20 H2qp Conn Capability configuration endpoint.
- :doc:`Hotspot20 H2qp Operator Name <hotspot20_h2qp_operator_name>` - Hotspot20 H2qp Operator Name configuration endpoint.
- :doc:`Hotspot20 H2qp Osu Provider <hotspot20_h2qp_osu_provider>` - Hotspot20 H2qp Osu Provider configuration endpoint.
- :doc:`Hotspot20 H2qp Osu Provider Nai <hotspot20_h2qp_osu_provider_nai>` - Hotspot20 H2qp Osu Provider Nai configuration endpoint.
- :doc:`Hotspot20 H2qp Terms And Conditions <hotspot20_h2qp_terms_and_conditions>` - Hotspot20 H2qp Terms And Conditions configuration endpoint.
- :doc:`Hotspot20 H2qp Wan Metric <hotspot20_h2qp_wan_metric>` - Hotspot20 H2qp Wan Metric configuration endpoint.
- :doc:`Hotspot20 Hs Profile <hotspot20_hs_profile>` - Hotspot20 Hs Profile configuration endpoint.
- :doc:`Hotspot20 Icon <hotspot20_icon>` - Hotspot20 Icon configuration endpoint.
- :doc:`Hotspot20 Qos Map <hotspot20_qos_map>` - Hotspot20 Qos Map configuration endpoint.
- :doc:`Inter Controller <inter_controller>` - Inter Controller configuration endpoint.
- :doc:`Log <log>` - Log configuration endpoint.
- :doc:`Lw Profile <lw_profile>` - Lw Profile configuration endpoint.
- :doc:`Mpsk Profile <mpsk_profile>` - Mpsk Profile configuration endpoint.
- :doc:`Nac Profile <nac_profile>` - Nac Profile configuration endpoint.
- :doc:`Qos Profile <qos_profile>` - Qos Profile configuration endpoint.
- :doc:`Region <region>` - Region configuration endpoint.
- :doc:`Setting <setting>` - Setting configuration endpoint.
- :doc:`SNMP <snmp>` - SNMP configuration endpoint.
- :doc:`Ssid Policy <ssid_policy>` - Ssid Policy configuration endpoint.
- :doc:`Syslog Profile <syslog_profile>` - Syslog Profile configuration endpoint.
- :doc:`Timers <timers>` - Timers configuration endpoint.
- :doc:`UTM Profile <utm_profile>` - UTM Profile configuration endpoint.
- :doc:`Vap <vap>` - Vap configuration endpoint.
- :doc:`Vap Group <vap_group>` - Vap Group configuration endpoint.
- :doc:`Wag Profile <wag_profile>` - Wag Profile configuration endpoint.
- :doc:`Wids Profile <wids_profile>` - Wids Profile configuration endpoint.
- :doc:`Wtp <wtp>` - Wtp configuration endpoint.
- :doc:`Wtp Group <wtp_group>` - Wtp Group configuration endpoint.
- :doc:`Wtp Profile <wtp_profile>` - Wtp Profile configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.wireless_controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   access_control_list
   ap_status
   apcfg_profile
   arrp_profile
   ble_profile
   bonjour_profile
   global_
   hotspot20_anqp_3gpp_cellular
   hotspot20_anqp_ip_address_type
   hotspot20_anqp_nai_realm
   hotspot20_anqp_network_auth_type
   hotspot20_anqp_roaming_consortium
   hotspot20_anqp_venue_name
   hotspot20_anqp_venue_url
   hotspot20_h2qp_advice_of_charge
   hotspot20_h2qp_conn_capability
   hotspot20_h2qp_operator_name
   hotspot20_h2qp_osu_provider
   hotspot20_h2qp_osu_provider_nai
   hotspot20_h2qp_terms_and_conditions
   hotspot20_h2qp_wan_metric
   hotspot20_hs_profile
   hotspot20_icon
   hotspot20_qos_map
   inter_controller
   log
   lw_profile
   mpsk_profile
   nac_profile
   qos_profile
   region
   setting
   snmp
   ssid_policy
   syslog_profile
   timers
   utm_profile
   vap
   vap_group
   wag_profile
   wids_profile
   wtp
   wtp_group
   wtp_profile

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
