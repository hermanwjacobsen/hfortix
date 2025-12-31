User
====

Overview
--------

The ``cmdb.user`` namespace provides configuration management for:

- :doc:`Adgrp <adgrp>` - Adgrp configuration endpoint.
- :doc:`Certificate <certificate>` - Certificate configuration endpoint.
- :doc:`Domain Controller <domain_controller>` - Domain Controller configuration endpoint.
- :doc:`Exchange <exchange>` - Exchange configuration endpoint.
- :doc:`External Identity Provider <external_identity_provider>` - External Identity Provider configuration endpoint.
- :doc:`Fortitoken <fortitoken>` - Fortitoken configuration endpoint.
- :doc:`FSSO <fsso>` - FSSO configuration endpoint.
- :doc:`FSSO Polling <fsso_polling>` - FSSO Polling configuration endpoint.
- :doc:`Group <group>` - Group configuration endpoint.
- :doc:`Krb Keytab <krb_keytab>` - Krb Keytab configuration endpoint.
- :doc:`Ldap <ldap>` - Ldap configuration endpoint.
- :doc:`Local <local>` - Local configuration endpoint.
- :doc:`Nac Policy <nac_policy>` - Nac Policy configuration endpoint.
- :doc:`Password Policy <password_policy>` - Password Policy configuration endpoint.
- :doc:`Peer <peer>` - Peer configuration endpoint.
- :doc:`Peergrp <peergrp>` - Peergrp configuration endpoint.
- :doc:`Pop3 <pop3>` - Pop3 configuration endpoint.
- :doc:`Quarantine <quarantine>` - Quarantine configuration endpoint.
- :doc:`Radius <radius>` - Radius configuration endpoint.
- :doc:`Saml <saml>` - Saml configuration endpoint.
- :doc:`Scim <scim>` - Scim configuration endpoint.
- :doc:`Security Exempt List <security_exempt_list>` - Security Exempt List configuration endpoint.
- :doc:`Setting <setting>` - Setting configuration endpoint.
- :doc:`Tacacs Plus <tacacs_plus_>` - Tacacs Plus configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.user.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   adgrp
   certificate
   domain_controller
   exchange
   external_identity_provider
   fortitoken
   fsso
   fsso_polling
   group
   krb_keytab
   ldap
   local
   nac_policy
   password_policy
   peer
   peergrp
   pop3
   quarantine
   radius
   saml
   scim
   security_exempt_list
   setting
   tacacs_plus_

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
