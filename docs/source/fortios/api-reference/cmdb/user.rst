User
====

Configure FSSO groups configuration and management.

Overview
--------

The ``cmdb.user`` category provides configuration management for:

- :ref:`Adgrp <user-adgrp>` - Configure FSSO groups.
- :ref:`Certificate <user-certificate>` - Configure certificate users.
- :ref:`Domain Controller <user-domain-controller>` - Configure domain controller entries.
- :ref:`Exchange <user-exchange>` - Configure MS Exchange server entries.
- :ref:`External Identity Provider <user-external-identity-provider>` - Configure external identity provider.
- :ref:`Fortitoken <user-fortitoken>` - Configure FortiToken.
- :ref:`Fsso <user-fsso>` - Configure Fortinet Single Sign On (FSSO) agents.
- :ref:`Fsso Polling <user-fsso-polling>` - Configure FSSO active directory servers for polling mode.
- :ref:`Group <user-group>` - Configure user groups.
- :ref:`Krb Keytab <user-krb-keytab>` - Configure Kerberos keytab entries.
- :ref:`Ldap <user-ldap>` - Configure LDAP server entries.
- :ref:`Local <user-local>` - Configure local users.
- :ref:`Nac Policy <user-nac-policy>` - Configure NAC policy matching pattern to identify matching NAC devices.
- :ref:`Password Policy <user-password-policy>` - Configure user password policy.
- :ref:`Peer <user-peer>` - Configure peer users.
- :ref:`Peergrp <user-peergrp>` - Configure peer groups.
- :ref:`Pop3 <user-pop3>` - POP3 server entry configuration.
- :ref:`Quarantine <user-quarantine>` - Configure quarantine support.
- :ref:`Radius <user-radius>` - Configure RADIUS server entries.
- :ref:`Saml <user-saml>` - SAML server entry configuration.
- :ref:`Scim <user-scim>` - Configure SCIM client entries.
- :ref:`Security Exempt List <user-security-exempt-list>` - Configure security exemption list.
- :ref:`Setting <user-setting>` - Configure user authentication setting.
- :ref:`Tacacs+ <user-tacacs+>` - Configure TACACS+ server entries.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.user

Available Endpoints
-------------------

.. _user-adgrp:

adgrp
~~~~~

Configure FSSO groups.

**Python attribute:** ``adgrp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.adgrp.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.adgrp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.adgrp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.adgrp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.adgrp.delete(mkey='item-name')

.. _user-certificate:

certificate
~~~~~~~~~~~

Configure certificate users.

**Python attribute:** ``certificate``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.certificate.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.certificate.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.certificate.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.certificate.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.certificate.delete(mkey='item-name')

.. _user-domain-controller:

domain-controller
~~~~~~~~~~~~~~~~~

Configure domain controller entries.

**Python attribute:** ``domain_controller``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.domain_controller.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.domain_controller.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.domain_controller.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.domain_controller.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.domain_controller.delete(mkey='item-name')

.. _user-exchange:

exchange
~~~~~~~~

Configure MS Exchange server entries.

**Python attribute:** ``exchange``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.exchange.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.exchange.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.exchange.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.exchange.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.exchange.delete(mkey='item-name')

.. _user-external-identity-provider:

external-identity-provider
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure external identity provider.

**Python attribute:** ``external_identity_provider``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.external_identity_provider.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.external_identity_provider.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.external_identity_provider.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.external_identity_provider.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.external_identity_provider.delete(mkey='item-name')

.. _user-fortitoken:

fortitoken
~~~~~~~~~~

Configure FortiToken.

**Python attribute:** ``fortitoken``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.fortitoken.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.fortitoken.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.fortitoken.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.fortitoken.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.fortitoken.delete(mkey='item-name')

.. _user-fsso:

fsso
~~~~

Configure Fortinet Single Sign On (FSSO) agents.

**Python attribute:** ``fsso``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.fsso.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.fsso.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.fsso.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.fsso.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.fsso.delete(mkey='item-name')

.. _user-fsso-polling:

fsso-polling
~~~~~~~~~~~~

Configure FSSO active directory servers for polling mode.

**Python attribute:** ``fsso_polling``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.fsso_polling.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.fsso_polling.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.fsso_polling.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.fsso_polling.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.fsso_polling.delete(mkey='item-name')

.. _user-group:

group
~~~~~

Configure user groups.

**Python attribute:** ``group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.group.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.group.delete(mkey='item-name')

.. _user-krb-keytab:

krb-keytab
~~~~~~~~~~

Configure Kerberos keytab entries.

**Python attribute:** ``krb_keytab``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.krb_keytab.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.krb_keytab.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.krb_keytab.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.krb_keytab.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.krb_keytab.delete(mkey='item-name')

.. _user-ldap:

ldap
~~~~

Configure LDAP server entries.

**Python attribute:** ``ldap``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.ldap.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.ldap.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.ldap.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.ldap.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.ldap.delete(mkey='item-name')

.. _user-local:

local
~~~~~

Configure local users.

**Python attribute:** ``local``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.local.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.local.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.local.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.local.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.local.delete(mkey='item-name')

.. _user-nac-policy:

nac-policy
~~~~~~~~~~

Configure NAC policy matching pattern to identify matching NAC devices.

**Python attribute:** ``nac_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.nac_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.nac_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.nac_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.nac_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.nac_policy.delete(mkey='item-name')

.. _user-password-policy:

password-policy
~~~~~~~~~~~~~~~

Configure user password policy.

**Python attribute:** ``password_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.password_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.password_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.password_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.password_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.password_policy.delete(mkey='item-name')

.. _user-peer:

peer
~~~~

Configure peer users.

**Python attribute:** ``peer``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.peer.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.peer.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.peer.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.peer.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.peer.delete(mkey='item-name')

.. _user-peergrp:

peergrp
~~~~~~~

Configure peer groups.

**Python attribute:** ``peergrp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.peergrp.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.peergrp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.peergrp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.peergrp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.peergrp.delete(mkey='item-name')

.. _user-pop3:

pop3
~~~~

POP3 server entry configuration.

**Python attribute:** ``pop3``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.pop3.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.pop3.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.pop3.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.pop3.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.pop3.delete(mkey='item-name')

.. _user-quarantine:

quarantine
~~~~~~~~~~

Configure quarantine support.

**Python attribute:** ``quarantine``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.quarantine.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.quarantine.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.quarantine.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.quarantine.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.quarantine.delete(mkey='item-name')

.. _user-radius:

radius
~~~~~~

Configure RADIUS server entries.

**Python attribute:** ``radius``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.radius.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.radius.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.radius.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.radius.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.radius.delete(mkey='item-name')

.. _user-saml:

saml
~~~~

SAML server entry configuration.

**Python attribute:** ``saml``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.saml.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.saml.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.saml.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.saml.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.saml.delete(mkey='item-name')

.. _user-scim:

scim
~~~~

Configure SCIM client entries.

**Python attribute:** ``scim``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.scim.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.scim.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.scim.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.scim.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.scim.delete(mkey='item-name')

.. _user-security-exempt-list:

security-exempt-list
~~~~~~~~~~~~~~~~~~~~

Configure security exemption list.

**Python attribute:** ``security_exempt_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.security_exempt_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.security_exempt_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.security_exempt_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.security_exempt_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.security_exempt_list.delete(mkey='item-name')

.. _user-setting:

setting
~~~~~~~

Configure user authentication setting.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.setting.delete(mkey='item-name')

.. _user-tacacs+:

tacacs+
~~~~~~~

Configure TACACS+ server entries.

**Python attribute:** ``tacacs+``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.user.tacacs+.get()
   
   # Get specific item
   item = fgt.api.cmdb.user.tacacs+.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.user.tacacs+.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.user.tacacs+.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.user.tacacs+.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.user.adgrp.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.user.adgrp.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.user.adgrp.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.user.adgrp.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.user.adgrp.delete(mkey='config-name')

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
