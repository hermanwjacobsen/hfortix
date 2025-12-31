Wireless Controller
===================

Configure 3GPP public land mobile network (PLMN) configuration and management.

Overview
--------

The ``cmdb.wireless-controller`` category provides configuration management for:

- :doc:`Access Control List <access-control-list>` - Configure WiFi bridge access control list.
- :doc:`Ap Status <ap-status>` - Configure access point status (rogue | accepted | suppressed).
- :doc:`Apcfg Profile <apcfg-profile>` - Configure AP local configuration profiles.
- :doc:`Arrp Profile <arrp-profile>` - Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
- :doc:`Ble Profile <ble-profile>` - Configure Bluetooth Low Energy profile.
- :doc:`Bonjour Profile <bonjour-profile>` - Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
- :doc:`Global <global>` - Configure wireless controller global settings.
- :doc:`Inter Controller <inter-controller>` - Configure inter wireless controller operation.
- :doc:`Log <log>` - Configure wireless controller event log filters.
- :doc:`Lw Profile <lw-profile>` - Configure LoRaWAN profile.
- :doc:`Mpsk Profile <mpsk-profile>` - Configure MPSK profile.
- :doc:`Nac Profile <nac-profile>` - Configure WiFi network access control (NAC) profiles.
- :doc:`Qos Profile <qos-profile>` - Configure WiFi quality of service (QoS) profiles.
- :doc:`Region <region>` - Configure FortiAP regions (for floor plans and maps).
- :doc:`Setting <setting>` - VDOM wireless controller configuration.
- :doc:`Snmp <snmp>` - Configure SNMP.
- :doc:`Ssid Policy <ssid-policy>` - Configure WiFi SSID policies.
- :doc:`Syslog Profile <syslog-profile>` - Configure Wireless Termination Points (WTP) system log server profile.
- :doc:`Timers <timers>` - Configure CAPWAP timers.
- :doc:`Utm Profile <utm-profile>` - Configure UTM (Unified Threat Management) profile.
- :doc:`Vap <vap>` - Configure Virtual Access Points (VAPs).
- :doc:`Vap Group <vap-group>` - Configure virtual Access Point (VAP) groups.
- :doc:`Wag Profile <wag-profile>` - Configure wireless access gateway (WAG) profiles used for tunnels on AP.
- :doc:`Wids Profile <wids-profile>` - Configure wireless intrusion detection system (WIDS) profiles.
- :doc:`Wtp <wtp>` - Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
- :doc:`Wtp Group <wtp-group>` - Configure WTP groups.
- :doc:`Wtp Profile <wtp-profile>` - Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.wireless-controller.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   access-control-list
   ap-status
   apcfg-profile
   arrp-profile
   ble-profile
   bonjour-profile
   global
   inter-controller
   log
   lw-profile
   mpsk-profile
   nac-profile
   qos-profile
   region
   setting
   snmp
   ssid-policy
   syslog-profile
   timers
   utm-profile
   vap
   vap-group
   wag-profile
   wids-profile
   wtp
   wtp-group
   wtp-profile

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
