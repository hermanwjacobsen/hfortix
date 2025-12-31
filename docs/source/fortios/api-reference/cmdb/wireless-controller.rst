Wireless Controller
===================

Configure 3GPP public land mobile network (PLMN) configuration and management.

Overview
--------

The ``cmdb.wireless-controller`` category provides configuration management for:

- **Access Control List** - Configure WiFi bridge access control list.
- **Ap Status** - Configure access point status (rogue | accepted | suppressed).
- **Apcfg Profile** - Configure AP local configuration profiles.
- **Arrp Profile** - Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
- **Ble Profile** - Configure Bluetooth Low Energy profile.
- **Bonjour Profile** - Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
- **Global** - Configure wireless controller global settings.
- **Inter Controller** - Configure inter wireless controller operation.
- **Log** - Configure wireless controller event log filters.
- **Lw Profile** - Configure LoRaWAN profile.
- **Mpsk Profile** - Configure MPSK profile.
- **Nac Profile** - Configure WiFi network access control (NAC) profiles.
- **Qos Profile** - Configure WiFi quality of service (QoS) profiles.
- **Region** - Configure FortiAP regions (for floor plans and maps).
- **Setting** - VDOM wireless controller configuration.
- **Snmp** - Configure SNMP.
- **Ssid Policy** - Configure WiFi SSID policies.
- **Syslog Profile** - Configure Wireless Termination Points (WTP) system log server profile.
- **Timers** - Configure CAPWAP timers.
- **Utm Profile** - Configure UTM (Unified Threat Management) profile.
- **Vap** - Configure Virtual Access Points (VAPs).
- **Vap Group** - Configure virtual Access Point (VAP) groups.
- **Wag Profile** - Configure wireless access gateway (WAG) profiles used for tunnels on AP.
- **Wids Profile** - Configure wireless intrusion detection system (WIDS) profiles.
- **Wtp** - Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
- **Wtp Group** - Configure WTP groups.
- **Wtp Profile** - Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.wireless-controller

Available Endpoints
-------------------

**access-control-list**
   Configure WiFi bridge access control list.
   
   .. code-block:: python
   
      # List all access-control-list
      items = fgt.api.cmdb.wireless-controller.access_control_list.get()
      
      # Get specific access-control-list
      item = fgt.api.cmdb.wireless-controller.access_control_list.get(mkey='name')

**ap-status**
   Configure access point status (rogue | accepted | suppressed).
   
   .. code-block:: python
   
      # List all ap-status
      items = fgt.api.cmdb.wireless-controller.ap_status.get()
      
      # Get specific ap-status
      item = fgt.api.cmdb.wireless-controller.ap_status.get(mkey='name')

**apcfg-profile**
   Configure AP local configuration profiles.
   
   .. code-block:: python
   
      # List all apcfg-profile
      items = fgt.api.cmdb.wireless-controller.apcfg_profile.get()
      
      # Get specific apcfg-profile
      item = fgt.api.cmdb.wireless-controller.apcfg_profile.get(mkey='name')

**arrp-profile**
   Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
   
   .. code-block:: python
   
      # List all arrp-profile
      items = fgt.api.cmdb.wireless-controller.arrp_profile.get()
      
      # Get specific arrp-profile
      item = fgt.api.cmdb.wireless-controller.arrp_profile.get(mkey='name')

**ble-profile**
   Configure Bluetooth Low Energy profile.
   
   .. code-block:: python
   
      # List all ble-profile
      items = fgt.api.cmdb.wireless-controller.ble_profile.get()
      
      # Get specific ble-profile
      item = fgt.api.cmdb.wireless-controller.ble_profile.get(mkey='name')

**bonjour-profile**
   Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
   
   .. code-block:: python
   
      # List all bonjour-profile
      items = fgt.api.cmdb.wireless-controller.bonjour_profile.get()
      
      # Get specific bonjour-profile
      item = fgt.api.cmdb.wireless-controller.bonjour_profile.get(mkey='name')

**global**
   Configure wireless controller global settings.
   
   .. code-block:: python
   
      # List all global
      items = fgt.api.cmdb.wireless-controller.global.get()
      
      # Get specific global
      item = fgt.api.cmdb.wireless-controller.global.get(mkey='name')

**inter-controller**
   Configure inter wireless controller operation.
   
   .. code-block:: python
   
      # List all inter-controller
      items = fgt.api.cmdb.wireless-controller.inter_controller.get()
      
      # Get specific inter-controller
      item = fgt.api.cmdb.wireless-controller.inter_controller.get(mkey='name')

**log**
   Configure wireless controller event log filters.
   
   .. code-block:: python
   
      # List all log
      items = fgt.api.cmdb.wireless-controller.log.get()
      
      # Get specific log
      item = fgt.api.cmdb.wireless-controller.log.get(mkey='name')

**lw-profile**
   Configure LoRaWAN profile.
   
   .. code-block:: python
   
      # List all lw-profile
      items = fgt.api.cmdb.wireless-controller.lw_profile.get()
      
      # Get specific lw-profile
      item = fgt.api.cmdb.wireless-controller.lw_profile.get(mkey='name')

**mpsk-profile**
   Configure MPSK profile.
   
   .. code-block:: python
   
      # List all mpsk-profile
      items = fgt.api.cmdb.wireless-controller.mpsk_profile.get()
      
      # Get specific mpsk-profile
      item = fgt.api.cmdb.wireless-controller.mpsk_profile.get(mkey='name')

**nac-profile**
   Configure WiFi network access control (NAC) profiles.
   
   .. code-block:: python
   
      # List all nac-profile
      items = fgt.api.cmdb.wireless-controller.nac_profile.get()
      
      # Get specific nac-profile
      item = fgt.api.cmdb.wireless-controller.nac_profile.get(mkey='name')

**qos-profile**
   Configure WiFi quality of service (QoS) profiles.
   
   .. code-block:: python
   
      # List all qos-profile
      items = fgt.api.cmdb.wireless-controller.qos_profile.get()
      
      # Get specific qos-profile
      item = fgt.api.cmdb.wireless-controller.qos_profile.get(mkey='name')

**region**
   Configure FortiAP regions (for floor plans and maps).
   
   .. code-block:: python
   
      # List all region
      items = fgt.api.cmdb.wireless-controller.region.get()
      
      # Get specific region
      item = fgt.api.cmdb.wireless-controller.region.get(mkey='name')

**setting**
   VDOM wireless controller configuration.
   
   .. code-block:: python
   
      # List all setting
      items = fgt.api.cmdb.wireless-controller.setting.get()
      
      # Get specific setting
      item = fgt.api.cmdb.wireless-controller.setting.get(mkey='name')

**snmp**
   Configure SNMP.
   
   .. code-block:: python
   
      # List all snmp
      items = fgt.api.cmdb.wireless-controller.snmp.get()
      
      # Get specific snmp
      item = fgt.api.cmdb.wireless-controller.snmp.get(mkey='name')

**ssid-policy**
   Configure WiFi SSID policies.
   
   .. code-block:: python
   
      # List all ssid-policy
      items = fgt.api.cmdb.wireless-controller.ssid_policy.get()
      
      # Get specific ssid-policy
      item = fgt.api.cmdb.wireless-controller.ssid_policy.get(mkey='name')

**syslog-profile**
   Configure Wireless Termination Points (WTP) system log server profile.
   
   .. code-block:: python
   
      # List all syslog-profile
      items = fgt.api.cmdb.wireless-controller.syslog_profile.get()
      
      # Get specific syslog-profile
      item = fgt.api.cmdb.wireless-controller.syslog_profile.get(mkey='name')

**timers**
   Configure CAPWAP timers.
   
   .. code-block:: python
   
      # List all timers
      items = fgt.api.cmdb.wireless-controller.timers.get()
      
      # Get specific timers
      item = fgt.api.cmdb.wireless-controller.timers.get(mkey='name')

**utm-profile**
   Configure UTM (Unified Threat Management) profile.
   
   .. code-block:: python
   
      # List all utm-profile
      items = fgt.api.cmdb.wireless-controller.utm_profile.get()
      
      # Get specific utm-profile
      item = fgt.api.cmdb.wireless-controller.utm_profile.get(mkey='name')

**vap**
   Configure Virtual Access Points (VAPs).
   
   .. code-block:: python
   
      # List all vap
      items = fgt.api.cmdb.wireless-controller.vap.get()
      
      # Get specific vap
      item = fgt.api.cmdb.wireless-controller.vap.get(mkey='name')

**vap-group**
   Configure virtual Access Point (VAP) groups.
   
   .. code-block:: python
   
      # List all vap-group
      items = fgt.api.cmdb.wireless-controller.vap_group.get()
      
      # Get specific vap-group
      item = fgt.api.cmdb.wireless-controller.vap_group.get(mkey='name')

**wag-profile**
   Configure wireless access gateway (WAG) profiles used for tunnels on AP.
   
   .. code-block:: python
   
      # List all wag-profile
      items = fgt.api.cmdb.wireless-controller.wag_profile.get()
      
      # Get specific wag-profile
      item = fgt.api.cmdb.wireless-controller.wag_profile.get(mkey='name')

**wids-profile**
   Configure wireless intrusion detection system (WIDS) profiles.
   
   .. code-block:: python
   
      # List all wids-profile
      items = fgt.api.cmdb.wireless-controller.wids_profile.get()
      
      # Get specific wids-profile
      item = fgt.api.cmdb.wireless-controller.wids_profile.get(mkey='name')

**wtp**
   Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
   
   .. code-block:: python
   
      # List all wtp
      items = fgt.api.cmdb.wireless-controller.wtp.get()
      
      # Get specific wtp
      item = fgt.api.cmdb.wireless-controller.wtp.get(mkey='name')

**wtp-group**
   Configure WTP groups.
   
   .. code-block:: python
   
      # List all wtp-group
      items = fgt.api.cmdb.wireless-controller.wtp_group.get()
      
      # Get specific wtp-group
      item = fgt.api.cmdb.wireless-controller.wtp_group.get(mkey='name')

**wtp-profile**
   Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
   
   .. code-block:: python
   
      # List all wtp-profile
      items = fgt.api.cmdb.wireless-controller.wtp_profile.get()
      
      # Get specific wtp-profile
      item = fgt.api.cmdb.wireless-controller.wtp_profile.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.wireless-controller.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.wireless-controller.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.wireless-controller.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.wireless-controller.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.wireless-controller.{endpoint}.delete(mkey='config-name')

HTTP Methods
------------

All CMDB endpoints support standard HTTP methods:

**.get()**
   HTTP GET - Retrieve configuration(s)

**.post()**
   HTTP POST - Create new configuration

**.put()**
   HTTP PUT - Update existing configuration

**.delete()**
   HTTP DELETE - Remove configuration

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
