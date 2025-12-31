Wireless Controller
===================

Configure 3GPP public land mobile network (PLMN) configuration and management.

Overview
--------

The ``cmdb.wireless-controller`` category provides configuration management for:

- :ref:`Access Control List <wireless-controller-access-control-list>` - Configure WiFi bridge access control list.
- :ref:`Ap Status <wireless-controller-ap-status>` - Configure access point status (rogue | accepted | suppressed).
- :ref:`Apcfg Profile <wireless-controller-apcfg-profile>` - Configure AP local configuration profiles.
- :ref:`Arrp Profile <wireless-controller-arrp-profile>` - Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
- :ref:`Ble Profile <wireless-controller-ble-profile>` - Configure Bluetooth Low Energy profile.
- :ref:`Bonjour Profile <wireless-controller-bonjour-profile>` - Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.
- :ref:`Global <wireless-controller-global>` - Configure wireless controller global settings.
- :ref:`Inter Controller <wireless-controller-inter-controller>` - Configure inter wireless controller operation.
- :ref:`Log <wireless-controller-log>` - Configure wireless controller event log filters.
- :ref:`Lw Profile <wireless-controller-lw-profile>` - Configure LoRaWAN profile.
- :ref:`Mpsk Profile <wireless-controller-mpsk-profile>` - Configure MPSK profile.
- :ref:`Nac Profile <wireless-controller-nac-profile>` - Configure WiFi network access control (NAC) profiles.
- :ref:`Qos Profile <wireless-controller-qos-profile>` - Configure WiFi quality of service (QoS) profiles.
- :ref:`Region <wireless-controller-region>` - Configure FortiAP regions (for floor plans and maps).
- :ref:`Setting <wireless-controller-setting>` - VDOM wireless controller configuration.
- :ref:`Snmp <wireless-controller-snmp>` - Configure SNMP.
- :ref:`Ssid Policy <wireless-controller-ssid-policy>` - Configure WiFi SSID policies.
- :ref:`Syslog Profile <wireless-controller-syslog-profile>` - Configure Wireless Termination Points (WTP) system log server profile.
- :ref:`Timers <wireless-controller-timers>` - Configure CAPWAP timers.
- :ref:`Utm Profile <wireless-controller-utm-profile>` - Configure UTM (Unified Threat Management) profile.
- :ref:`Vap <wireless-controller-vap>` - Configure Virtual Access Points (VAPs).
- :ref:`Vap Group <wireless-controller-vap-group>` - Configure virtual Access Point (VAP) groups.
- :ref:`Wag Profile <wireless-controller-wag-profile>` - Configure wireless access gateway (WAG) profiles used for tunnels on AP.
- :ref:`Wids Profile <wireless-controller-wids-profile>` - Configure wireless intrusion detection system (WIDS) profiles.
- :ref:`Wtp <wireless-controller-wtp>` - Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
- :ref:`Wtp Group <wireless-controller-wtp-group>` - Configure WTP groups.
- :ref:`Wtp Profile <wireless-controller-wtp-profile>` - Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.wireless-controller

Available Endpoints
-------------------

.. _wireless-controller-access-control-list:

access-control-list
~~~~~~~~~~~~~~~~~~~

Configure WiFi bridge access control list.

**Python attribute:** ``access_control_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.access_control_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.access_control_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.access_control_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.access_control_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.access_control_list.delete(mkey='item-name')

.. _wireless-controller-ap-status:

ap-status
~~~~~~~~~

Configure access point status (rogue | accepted | suppressed).

**Python attribute:** ``ap_status``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.ap_status.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.ap_status.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.ap_status.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.ap_status.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.ap_status.delete(mkey='item-name')

.. _wireless-controller-apcfg-profile:

apcfg-profile
~~~~~~~~~~~~~

Configure AP local configuration profiles.

**Python attribute:** ``apcfg_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.apcfg_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.apcfg_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.apcfg_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.apcfg_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.apcfg_profile.delete(mkey='item-name')

.. _wireless-controller-arrp-profile:

arrp-profile
~~~~~~~~~~~~

Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.

**Python attribute:** ``arrp_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.arrp_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.arrp_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.arrp_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.arrp_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.arrp_profile.delete(mkey='item-name')

.. _wireless-controller-ble-profile:

ble-profile
~~~~~~~~~~~

Configure Bluetooth Low Energy profile.

**Python attribute:** ``ble_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.ble_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.ble_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.ble_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.ble_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.ble_profile.delete(mkey='item-name')

.. _wireless-controller-bonjour-profile:

bonjour-profile
~~~~~~~~~~~~~~~

Configure Bonjour profiles. Bonjour is Apple's zero configuration networking protocol. Bonjour profiles allow APs and FortiAPs to connect to networks using Bonjour.

**Python attribute:** ``bonjour_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.bonjour_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.bonjour_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.bonjour_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.bonjour_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.bonjour_profile.delete(mkey='item-name')

.. _wireless-controller-global:

global
~~~~~~

Configure wireless controller global settings.

**Python attribute:** ``global``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.global.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.global.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.global.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.global.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.global.delete(mkey='item-name')

.. _wireless-controller-inter-controller:

inter-controller
~~~~~~~~~~~~~~~~

Configure inter wireless controller operation.

**Python attribute:** ``inter_controller``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.inter_controller.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.inter_controller.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.inter_controller.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.inter_controller.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.inter_controller.delete(mkey='item-name')

.. _wireless-controller-log:

log
~~~

Configure wireless controller event log filters.

**Python attribute:** ``log``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.log.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.log.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.log.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.log.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.log.delete(mkey='item-name')

.. _wireless-controller-lw-profile:

lw-profile
~~~~~~~~~~

Configure LoRaWAN profile.

**Python attribute:** ``lw_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.lw_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.lw_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.lw_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.lw_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.lw_profile.delete(mkey='item-name')

.. _wireless-controller-mpsk-profile:

mpsk-profile
~~~~~~~~~~~~

Configure MPSK profile.

**Python attribute:** ``mpsk_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.mpsk_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.mpsk_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.mpsk_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.mpsk_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.mpsk_profile.delete(mkey='item-name')

.. _wireless-controller-nac-profile:

nac-profile
~~~~~~~~~~~

Configure WiFi network access control (NAC) profiles.

**Python attribute:** ``nac_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.nac_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.nac_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.nac_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.nac_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.nac_profile.delete(mkey='item-name')

.. _wireless-controller-qos-profile:

qos-profile
~~~~~~~~~~~

Configure WiFi quality of service (QoS) profiles.

**Python attribute:** ``qos_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.qos_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.qos_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.qos_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.qos_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.qos_profile.delete(mkey='item-name')

.. _wireless-controller-region:

region
~~~~~~

Configure FortiAP regions (for floor plans and maps).

**Python attribute:** ``region``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.region.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.region.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.region.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.region.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.region.delete(mkey='item-name')

.. _wireless-controller-setting:

setting
~~~~~~~

VDOM wireless controller configuration.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.setting.delete(mkey='item-name')

.. _wireless-controller-snmp:

snmp
~~~~

Configure SNMP.

**Python attribute:** ``snmp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.snmp.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.snmp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.snmp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.snmp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.snmp.delete(mkey='item-name')

.. _wireless-controller-ssid-policy:

ssid-policy
~~~~~~~~~~~

Configure WiFi SSID policies.

**Python attribute:** ``ssid_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.ssid_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.ssid_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.ssid_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.ssid_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.ssid_policy.delete(mkey='item-name')

.. _wireless-controller-syslog-profile:

syslog-profile
~~~~~~~~~~~~~~

Configure Wireless Termination Points (WTP) system log server profile.

**Python attribute:** ``syslog_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.syslog_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.syslog_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.syslog_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.syslog_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.syslog_profile.delete(mkey='item-name')

.. _wireless-controller-timers:

timers
~~~~~~

Configure CAPWAP timers.

**Python attribute:** ``timers``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.timers.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.timers.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.timers.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.timers.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.timers.delete(mkey='item-name')

.. _wireless-controller-utm-profile:

utm-profile
~~~~~~~~~~~

Configure UTM (Unified Threat Management) profile.

**Python attribute:** ``utm_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.utm_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.utm_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.utm_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.utm_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.utm_profile.delete(mkey='item-name')

.. _wireless-controller-vap:

vap
~~~

Configure Virtual Access Points (VAPs).

**Python attribute:** ``vap``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.vap.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.vap.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.vap.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.vap.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.vap.delete(mkey='item-name')

.. _wireless-controller-vap-group:

vap-group
~~~~~~~~~

Configure virtual Access Point (VAP) groups.

**Python attribute:** ``vap_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.vap_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.vap_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.vap_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.vap_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.vap_group.delete(mkey='item-name')

.. _wireless-controller-wag-profile:

wag-profile
~~~~~~~~~~~

Configure wireless access gateway (WAG) profiles used for tunnels on AP.

**Python attribute:** ``wag_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.wag_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.wag_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.wag_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.wag_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.wag_profile.delete(mkey='item-name')

.. _wireless-controller-wids-profile:

wids-profile
~~~~~~~~~~~~

Configure wireless intrusion detection system (WIDS) profiles.

**Python attribute:** ``wids_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.wids_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.wids_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.wids_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.wids_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.wids_profile.delete(mkey='item-name')

.. _wireless-controller-wtp:

wtp
~~~

Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

**Python attribute:** ``wtp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.wtp.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.wtp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.wtp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.wtp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.wtp.delete(mkey='item-name')

.. _wireless-controller-wtp-group:

wtp-group
~~~~~~~~~

Configure WTP groups.

**Python attribute:** ``wtp_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.wtp_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.wtp_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.wtp_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.wtp_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.wtp_group.delete(mkey='item-name')

.. _wireless-controller-wtp-profile:

wtp-profile
~~~~~~~~~~~

Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

**Python attribute:** ``wtp_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.wireless-controller.wtp_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.wireless-controller.wtp_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.wireless-controller.wtp_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.wireless-controller.wtp_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.wireless-controller.wtp_profile.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.wireless-controller.access_control_list.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.wireless-controller.access_control_list.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.wireless-controller.access_control_list.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.wireless-controller.access_control_list.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.wireless-controller.access_control_list.delete(mkey='config-name')

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
