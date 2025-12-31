User
====

Configure FSSO groups configuration and management.

Overview
--------

The ``cmdb.user`` category provides configuration management for:

- **Adgrp** - Configure FSSO groups.
- **Certificate** - Configure certificate users.
- **Domain Controller** - Configure domain controller entries.
- **Exchange** - Configure MS Exchange server entries.
- **External Identity Provider** - Configure external identity provider.
- **Fortitoken** - Configure FortiToken.
- **Fsso** - Configure Fortinet Single Sign On (FSSO) agents.
- **Fsso Polling** - Configure FSSO active directory servers for polling mode.
- **Group** - Configure user groups.
- **Krb Keytab** - Configure Kerberos keytab entries.
- **Ldap** - Configure LDAP server entries.
- **Local** - Configure local users.
- **Nac Policy** - Configure NAC policy matching pattern to identify matching NAC devices.
- **Password Policy** - Configure user password policy.
- **Peer** - Configure peer users.
- **Peergrp** - Configure peer groups.
- **Pop3** - POP3 server entry configuration.
- **Quarantine** - Configure quarantine support.
- **Radius** - Configure RADIUS server entries.
- **Saml** - SAML server entry configuration.
- **Scim** - Configure SCIM client entries.
- **Security Exempt List** - Configure security exemption list.
- **Setting** - Configure user authentication setting.
- **Tacacs+** - Configure TACACS+ server entries.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.user

Available Endpoints
-------------------

**adgrp**
   Configure FSSO groups.
   
   .. code-block:: python
   
      # List all adgrp
      items = fgt.api.cmdb.user.adgrp.get()
      
      # Get specific adgrp
      item = fgt.api.cmdb.user.adgrp.get(mkey='name')

**certificate**
   Configure certificate users.
   
   .. code-block:: python
   
      # List all certificate
      items = fgt.api.cmdb.user.certificate.get()
      
      # Get specific certificate
      item = fgt.api.cmdb.user.certificate.get(mkey='name')

**domain-controller**
   Configure domain controller entries.
   
   .. code-block:: python
   
      # List all domain-controller
      items = fgt.api.cmdb.user.domain_controller.get()
      
      # Get specific domain-controller
      item = fgt.api.cmdb.user.domain_controller.get(mkey='name')

**exchange**
   Configure MS Exchange server entries.
   
   .. code-block:: python
   
      # List all exchange
      items = fgt.api.cmdb.user.exchange.get()
      
      # Get specific exchange
      item = fgt.api.cmdb.user.exchange.get(mkey='name')

**external-identity-provider**
   Configure external identity provider.
   
   .. code-block:: python
   
      # List all external-identity-provider
      items = fgt.api.cmdb.user.external_identity_provider.get()
      
      # Get specific external-identity-provider
      item = fgt.api.cmdb.user.external_identity_provider.get(mkey='name')

**fortitoken**
   Configure FortiToken.
   
   .. code-block:: python
   
      # List all fortitoken
      items = fgt.api.cmdb.user.fortitoken.get()
      
      # Get specific fortitoken
      item = fgt.api.cmdb.user.fortitoken.get(mkey='name')

**fsso**
   Configure Fortinet Single Sign On (FSSO) agents.
   
   .. code-block:: python
   
      # List all fsso
      items = fgt.api.cmdb.user.fsso.get()
      
      # Get specific fsso
      item = fgt.api.cmdb.user.fsso.get(mkey='name')

**fsso-polling**
   Configure FSSO active directory servers for polling mode.
   
   .. code-block:: python
   
      # List all fsso-polling
      items = fgt.api.cmdb.user.fsso_polling.get()
      
      # Get specific fsso-polling
      item = fgt.api.cmdb.user.fsso_polling.get(mkey='name')

**group**
   Configure user groups.
   
   .. code-block:: python
   
      # List all group
      items = fgt.api.cmdb.user.group.get()
      
      # Get specific group
      item = fgt.api.cmdb.user.group.get(mkey='name')

**krb-keytab**
   Configure Kerberos keytab entries.
   
   .. code-block:: python
   
      # List all krb-keytab
      items = fgt.api.cmdb.user.krb_keytab.get()
      
      # Get specific krb-keytab
      item = fgt.api.cmdb.user.krb_keytab.get(mkey='name')

**ldap**
   Configure LDAP server entries.
   
   .. code-block:: python
   
      # List all ldap
      items = fgt.api.cmdb.user.ldap.get()
      
      # Get specific ldap
      item = fgt.api.cmdb.user.ldap.get(mkey='name')

**local**
   Configure local users.
   
   .. code-block:: python
   
      # List all local
      items = fgt.api.cmdb.user.local.get()
      
      # Get specific local
      item = fgt.api.cmdb.user.local.get(mkey='name')

**nac-policy**
   Configure NAC policy matching pattern to identify matching NAC devices.
   
   .. code-block:: python
   
      # List all nac-policy
      items = fgt.api.cmdb.user.nac_policy.get()
      
      # Get specific nac-policy
      item = fgt.api.cmdb.user.nac_policy.get(mkey='name')

**password-policy**
   Configure user password policy.
   
   .. code-block:: python
   
      # List all password-policy
      items = fgt.api.cmdb.user.password_policy.get()
      
      # Get specific password-policy
      item = fgt.api.cmdb.user.password_policy.get(mkey='name')

**peer**
   Configure peer users.
   
   .. code-block:: python
   
      # List all peer
      items = fgt.api.cmdb.user.peer.get()
      
      # Get specific peer
      item = fgt.api.cmdb.user.peer.get(mkey='name')

**peergrp**
   Configure peer groups.
   
   .. code-block:: python
   
      # List all peergrp
      items = fgt.api.cmdb.user.peergrp.get()
      
      # Get specific peergrp
      item = fgt.api.cmdb.user.peergrp.get(mkey='name')

**pop3**
   POP3 server entry configuration.
   
   .. code-block:: python
   
      # List all pop3
      items = fgt.api.cmdb.user.pop3.get()
      
      # Get specific pop3
      item = fgt.api.cmdb.user.pop3.get(mkey='name')

**quarantine**
   Configure quarantine support.
   
   .. code-block:: python
   
      # List all quarantine
      items = fgt.api.cmdb.user.quarantine.get()
      
      # Get specific quarantine
      item = fgt.api.cmdb.user.quarantine.get(mkey='name')

**radius**
   Configure RADIUS server entries.
   
   .. code-block:: python
   
      # List all radius
      items = fgt.api.cmdb.user.radius.get()
      
      # Get specific radius
      item = fgt.api.cmdb.user.radius.get(mkey='name')

**saml**
   SAML server entry configuration.
   
   .. code-block:: python
   
      # List all saml
      items = fgt.api.cmdb.user.saml.get()
      
      # Get specific saml
      item = fgt.api.cmdb.user.saml.get(mkey='name')

**scim**
   Configure SCIM client entries.
   
   .. code-block:: python
   
      # List all scim
      items = fgt.api.cmdb.user.scim.get()
      
      # Get specific scim
      item = fgt.api.cmdb.user.scim.get(mkey='name')

**security-exempt-list**
   Configure security exemption list.
   
   .. code-block:: python
   
      # List all security-exempt-list
      items = fgt.api.cmdb.user.security_exempt_list.get()
      
      # Get specific security-exempt-list
      item = fgt.api.cmdb.user.security_exempt_list.get(mkey='name')

**setting**
   Configure user authentication setting.
   
   .. code-block:: python
   
      # List all setting
      items = fgt.api.cmdb.user.setting.get()
      
      # Get specific setting
      item = fgt.api.cmdb.user.setting.get(mkey='name')

**tacacs+**
   Configure TACACS+ server entries.
   
   .. code-block:: python
   
      # List all tacacs+
      items = fgt.api.cmdb.user.tacacs+.get()
      
      # Get specific tacacs+
      item = fgt.api.cmdb.user.tacacs+.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.user.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.user.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.user.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.user.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.user.{endpoint}.delete(mkey='config-name')

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
