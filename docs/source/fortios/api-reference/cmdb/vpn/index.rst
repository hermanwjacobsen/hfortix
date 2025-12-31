VPN
===

Overview
--------

The ``cmdb.vpn`` namespace provides configuration management for:

- :doc:`Certificate Ca <certificate_ca>` - Certificate Ca configuration endpoint.
- :doc:`Certificate Crl <certificate_crl>` - Certificate Crl configuration endpoint.
- :doc:`Certificate Hsm Local <certificate_hsm_local>` - Certificate Hsm Local configuration endpoint.
- :doc:`Certificate Local <certificate_local>` - Certificate Local configuration endpoint.
- :doc:`Certificate Ocsp Server <certificate_ocsp_server>` - Certificate Ocsp Server configuration endpoint.
- :doc:`Certificate Remote <certificate_remote>` - Certificate Remote configuration endpoint.
- :doc:`Certificate Setting <certificate_setting>` - Certificate Setting configuration endpoint.
- :doc:`Ipsec Concentrator <ipsec_concentrator>` - Ipsec Concentrator configuration endpoint.
- :doc:`Ipsec Fec <ipsec_fec>` - Ipsec Fec configuration endpoint.
- :doc:`Ipsec Manualkey <ipsec_manualkey>` - Ipsec Manualkey configuration endpoint.
- :doc:`Ipsec Manualkey Interface <ipsec_manualkey_interface>` - Ipsec Manualkey Interface configuration endpoint.
- :doc:`Ipsec Phase1 <ipsec_phase1>` - Ipsec Phase1 configuration endpoint.
- :doc:`Ipsec Phase1 Interface <ipsec_phase1_interface>` - Ipsec Phase1 Interface configuration endpoint.
- :doc:`Ipsec Phase2 <ipsec_phase2>` - Ipsec Phase2 configuration endpoint.
- :doc:`Ipsec Phase2 Interface <ipsec_phase2_interface>` - Ipsec Phase2 Interface configuration endpoint.
- :doc:`Kmip Server <kmip_server>` - Kmip Server configuration endpoint.
- :doc:`L2tp <l2tp>` - L2tp configuration endpoint.
- :doc:`Pptp <pptp>` - Pptp configuration endpoint.
- :doc:`Qkd <qkd>` - Qkd configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.vpn.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   certificate_ca
   certificate_crl
   certificate_hsm_local
   certificate_local
   certificate_ocsp_server
   certificate_remote
   certificate_setting
   ipsec_concentrator
   ipsec_fec
   ipsec_manualkey
   ipsec_manualkey_interface
   ipsec_phase1
   ipsec_phase1_interface
   ipsec_phase2
   ipsec_phase2_interface
   kmip_server
   l2tp
   pptp
   qkd

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
