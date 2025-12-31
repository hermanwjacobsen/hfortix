User
====

Configure FSSO groups configuration and management.

Overview
--------

The ``cmdb.user`` category provides configuration management for:

- :doc:`Adgrp <adgrp>` - Configure FSSO groups.
- :doc:`Certificate <certificate>` - Configure certificate users.
- :doc:`Domain Controller <domain-controller>` - Configure domain controller entries.
- :doc:`Exchange <exchange>` - Configure MS Exchange server entries.
- :doc:`External Identity Provider <external-identity-provider>` - Configure external identity provider.
- :doc:`Fortitoken <fortitoken>` - Configure FortiToken.
- :doc:`Fsso <fsso>` - Configure Fortinet Single Sign On (FSSO) agents.
- :doc:`Fsso Polling <fsso-polling>` - Configure FSSO active directory servers for polling mode.
- :doc:`Group <group>` - Configure user groups.
- :doc:`Krb Keytab <krb-keytab>` - Configure Kerberos keytab entries.
- :doc:`Ldap <ldap>` - Configure LDAP server entries.
- :doc:`Local <local>` - Configure local users.
- :doc:`Nac Policy <nac-policy>` - Configure NAC policy matching pattern to identify matching NAC devices.
- :doc:`Password Policy <password-policy>` - Configure user password policy.
- :doc:`Peer <peer>` - Configure peer users.
- :doc:`Peergrp <peergrp>` - Configure peer groups.
- :doc:`Pop3 <pop3>` - POP3 server entry configuration.
- :doc:`Quarantine <quarantine>` - Configure quarantine support.
- :doc:`Radius <radius>` - Configure RADIUS server entries.
- :doc:`Saml <saml>` - SAML server entry configuration.
- :doc:`Scim <scim>` - Configure SCIM client entries.
- :doc:`Security Exempt List <security-exempt-list>` - Configure security exemption list.
- :doc:`Setting <setting>` - Configure user authentication setting.
- :doc:`Tacacs+ <tacacs+>` - Configure TACACS+ server entries.


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
   domain-controller
   exchange
   external-identity-provider
   fortitoken
   fsso
   fsso-polling
   group
   krb-keytab
   ldap
   local
   nac-policy
   password-policy
   peer
   peergrp
   pop3
   quarantine
   radius
   saml
   scim
   security-exempt-list
   setting
   tacacs+

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
