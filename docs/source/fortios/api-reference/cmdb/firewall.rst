Firewall
========

Configure IP to MAC binding settings configuration and management.

Overview
--------

The ``cmdb.firewall`` category provides configuration management for:

- :ref:`Dos Policy <firewall-DoS-policy>` - Configure IPv4 DoS policies.
- :ref:`Dos Policy6 <firewall-DoS-policy6>` - Configure IPv6 DoS policies.
- :ref:`Access Proxy <firewall-access-proxy>` - Configure IPv4 access proxy.
- :ref:`Access Proxy Ssh Client Cert <firewall-access-proxy-ssh-client-cert>` - Configure Access Proxy SSH client certificate.
- :ref:`Access Proxy Virtual Host <firewall-access-proxy-virtual-host>` - Configure Access Proxy virtual hosts.
- :ref:`Access Proxy6 <firewall-access-proxy6>` - Configure IPv6 access proxy.
- :ref:`Address <firewall-address>` - Configure IPv4 addresses.
- :ref:`Address6 <firewall-address6>` - Configure IPv6 firewall addresses.
- :ref:`Address6 Template <firewall-address6-template>` - Configure IPv6 address templates.
- :ref:`Addrgrp <firewall-addrgrp>` - Configure IPv4 address groups.
- :ref:`Addrgrp6 <firewall-addrgrp6>` - Configure IPv6 address groups.
- :ref:`Auth Portal <firewall-auth-portal>` - Configure firewall authentication portals.
- :ref:`Central Snat Map <firewall-central-snat-map>` - Configure IPv4 and IPv6 central SNAT policies.
- :ref:`City <firewall-city>` - Define city table.
- :ref:`Country <firewall-country>` - Define country table.
- :ref:`Decrypted Traffic Mirror <firewall-decrypted-traffic-mirror>` - Configure decrypted traffic mirror.
- :ref:`Dnstranslation <firewall-dnstranslation>` - Configure DNS translation.
- :ref:`Global <firewall-global>` - Global firewall settings.
- :ref:`Identity Based Route <firewall-identity-based-route>` - Configure identity based routing.
- :ref:`Interface Policy <firewall-interface-policy>` - Configure IPv4 interface policies.
- :ref:`Interface Policy6 <firewall-interface-policy6>` - Configure IPv6 interface policies.
- :ref:`Internet Service <firewall-internet-service>` - Show Internet Service application.
- :ref:`Internet Service Addition <firewall-internet-service-addition>` - Configure Internet Services Addition.
- :ref:`Internet Service Append <firewall-internet-service-append>` - Configure additional port mappings for Internet Services.
- :ref:`Internet Service Botnet <firewall-internet-service-botnet>` - Show Internet Service botnet.
- :ref:`Internet Service Custom <firewall-internet-service-custom>` - Configure custom Internet Services.
- :ref:`Internet Service Custom Group <firewall-internet-service-custom-group>` - Configure custom Internet Service group.
- :ref:`Internet Service Definition <firewall-internet-service-definition>` - Configure Internet Service definition.
- :ref:`Internet Service Extension <firewall-internet-service-extension>` - Configure Internet Services Extension.
- :ref:`Internet Service Fortiguard <firewall-internet-service-fortiguard>` - Configure FortiGuard Internet Services.
- :ref:`Internet Service Group <firewall-internet-service-group>` - Configure group of Internet Service.
- :ref:`Internet Service Ipbl Reason <firewall-internet-service-ipbl-reason>` - IP block list reason.
- :ref:`Internet Service Ipbl Vendor <firewall-internet-service-ipbl-vendor>` - IP block list vendor.
- :ref:`Internet Service List <firewall-internet-service-list>` - Internet Service list.
- :ref:`Internet Service Name <firewall-internet-service-name>` - Define internet service names.
- :ref:`Internet Service Owner <firewall-internet-service-owner>` - Internet Service owner.
- :ref:`Internet Service Reputation <firewall-internet-service-reputation>` - Show Internet Service reputation.
- :ref:`Internet Service Sld <firewall-internet-service-sld>` - Internet Service Second Level Domain.
- :ref:`Internet Service Subapp <firewall-internet-service-subapp>` - Show Internet Service sub app ID.
- :ref:`Ip Translation <firewall-ip-translation>` - Configure firewall IP-translation.
- :ref:`Ippool <firewall-ippool>` - Configure IPv4 IP pools.
- :ref:`Ippool6 <firewall-ippool6>` - Configure IPv6 IP pools.
- :ref:`Ldb Monitor <firewall-ldb-monitor>` - Configure server load balancing health monitors.
- :ref:`Local In Policy <firewall-local-in-policy>` - Configure user defined IPv4 local-in policies.
- :ref:`Local In Policy6 <firewall-local-in-policy6>` - Configure user defined IPv6 local-in policies.
- :ref:`Multicast Address <firewall-multicast-address>` - Configure multicast addresses.
- :ref:`Multicast Address6 <firewall-multicast-address6>` - Configure IPv6 multicast address.
- :ref:`Multicast Policy <firewall-multicast-policy>` - Configure multicast NAT policies.
- :ref:`Multicast Policy6 <firewall-multicast-policy6>` - Configure IPv6 multicast NAT policies.
- :ref:`Network Service Dynamic <firewall-network-service-dynamic>` - Configure Dynamic Network Services.
- :ref:`On Demand Sniffer <firewall-on-demand-sniffer>` - Configure on-demand packet sniffer.
- :ref:`Policy <firewall-policy>` - Configure IPv4/IPv6 policies.
- :ref:`Profile Group <firewall-profile-group>` - Configure profile groups.
- :ref:`Profile Protocol Options <firewall-profile-protocol-options>` - Configure protocol options.
- :ref:`Proxy Address <firewall-proxy-address>` - Configure web proxy address.
- :ref:`Proxy Addrgrp <firewall-proxy-addrgrp>` - Configure web proxy address group.
- :ref:`Proxy Policy <firewall-proxy-policy>` - Configure proxy policies.
- :ref:`Region <firewall-region>` - Define region table.
- :ref:`Security Policy <firewall-security-policy>` - Configure NGFW IPv4/IPv6 application policies.
- :ref:`Shaping Policy <firewall-shaping-policy>` - Configure shaping policies.
- :ref:`Shaping Profile <firewall-shaping-profile>` - Configure shaping profiles.
- :ref:`Sniffer <firewall-sniffer>` - Configure sniffer.
- :ref:`Ssl Server <firewall-ssl-server>` - Configure SSL servers.
- :ref:`Ssl Ssh Profile <firewall-ssl-ssh-profile>` - Configure SSL/SSH protocol options.
- :ref:`Traffic Class <firewall-traffic-class>` - Configure names for shaping classes.
- :ref:`Ttl Policy <firewall-ttl-policy>` - Configure TTL policies.
- :ref:`Vendor Mac <firewall-vendor-mac>` - Show vendor and the MAC address they have.
- :ref:`Vendor Mac Summary <firewall-vendor-mac-summary>` - Vendor MAC database summary.
- :ref:`Vip <firewall-vip>` - Configure virtual IP for IPv4.
- :ref:`Vip6 <firewall-vip6>` - Configure virtual IP for IPv6.
- :ref:`Vipgrp <firewall-vipgrp>` - Configure IPv4 virtual IP groups.
- :ref:`Vipgrp6 <firewall-vipgrp6>` - Configure IPv6 virtual IP groups.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.firewall

Available Endpoints
-------------------

.. _firewall-DoS-policy:

DoS-policy
~~~~~~~~~~

Configure IPv4 DoS policies.

**Python attribute:** ``DoS_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.DoS_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.DoS_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.DoS_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.DoS_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.DoS_policy.delete(mkey='item-name')

.. _firewall-DoS-policy6:

DoS-policy6
~~~~~~~~~~~

Configure IPv6 DoS policies.

**Python attribute:** ``DoS_policy6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.DoS_policy6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.DoS_policy6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.DoS_policy6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.DoS_policy6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.DoS_policy6.delete(mkey='item-name')

.. _firewall-access-proxy:

access-proxy
~~~~~~~~~~~~

Configure IPv4 access proxy.

**Python attribute:** ``access_proxy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.access_proxy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.access_proxy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy.delete(mkey='item-name')

.. _firewall-access-proxy-ssh-client-cert:

access-proxy-ssh-client-cert
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Access Proxy SSH client certificate.

**Python attribute:** ``access_proxy_ssh_client_cert``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.delete(mkey='item-name')

.. _firewall-access-proxy-virtual-host:

access-proxy-virtual-host
~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Access Proxy virtual hosts.

**Python attribute:** ``access_proxy_virtual_host``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.access_proxy_virtual_host.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.access_proxy_virtual_host.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy_virtual_host.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy_virtual_host.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy_virtual_host.delete(mkey='item-name')

.. _firewall-access-proxy6:

access-proxy6
~~~~~~~~~~~~~

Configure IPv6 access proxy.

**Python attribute:** ``access_proxy6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.access_proxy6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.access_proxy6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.access_proxy6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.access_proxy6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.access_proxy6.delete(mkey='item-name')

.. _firewall-address:

address
~~~~~~~

Configure IPv4 addresses.

**Python attribute:** ``address``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.address.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.address.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.address.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.address.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.address.delete(mkey='item-name')

.. _firewall-address6:

address6
~~~~~~~~

Configure IPv6 firewall addresses.

**Python attribute:** ``address6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.address6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.address6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.address6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.address6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.address6.delete(mkey='item-name')

.. _firewall-address6-template:

address6-template
~~~~~~~~~~~~~~~~~

Configure IPv6 address templates.

**Python attribute:** ``address6_template``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.address6_template.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.address6_template.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.address6_template.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.address6_template.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.address6_template.delete(mkey='item-name')

.. _firewall-addrgrp:

addrgrp
~~~~~~~

Configure IPv4 address groups.

**Python attribute:** ``addrgrp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.addrgrp.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.addrgrp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.addrgrp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.addrgrp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.addrgrp.delete(mkey='item-name')

.. _firewall-addrgrp6:

addrgrp6
~~~~~~~~

Configure IPv6 address groups.

**Python attribute:** ``addrgrp6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.addrgrp6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.addrgrp6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.addrgrp6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.addrgrp6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.addrgrp6.delete(mkey='item-name')

.. _firewall-auth-portal:

auth-portal
~~~~~~~~~~~

Configure firewall authentication portals.

**Python attribute:** ``auth_portal``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.auth_portal.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.auth_portal.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.auth_portal.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.auth_portal.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.auth_portal.delete(mkey='item-name')

.. _firewall-central-snat-map:

central-snat-map
~~~~~~~~~~~~~~~~

Configure IPv4 and IPv6 central SNAT policies.

**Python attribute:** ``central_snat_map``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.central_snat_map.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.central_snat_map.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.central_snat_map.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.central_snat_map.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.central_snat_map.delete(mkey='item-name')

.. _firewall-city:

city
~~~~

Define city table.

**Python attribute:** ``city``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.city.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.city.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.city.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.city.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.city.delete(mkey='item-name')

.. _firewall-country:

country
~~~~~~~

Define country table.

**Python attribute:** ``country``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.country.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.country.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.country.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.country.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.country.delete(mkey='item-name')

.. _firewall-decrypted-traffic-mirror:

decrypted-traffic-mirror
~~~~~~~~~~~~~~~~~~~~~~~~

Configure decrypted traffic mirror.

**Python attribute:** ``decrypted_traffic_mirror``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.decrypted_traffic_mirror.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.decrypted_traffic_mirror.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.decrypted_traffic_mirror.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.decrypted_traffic_mirror.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.decrypted_traffic_mirror.delete(mkey='item-name')

.. _firewall-dnstranslation:

dnstranslation
~~~~~~~~~~~~~~

Configure DNS translation.

**Python attribute:** ``dnstranslation``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.dnstranslation.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.dnstranslation.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.dnstranslation.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.dnstranslation.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.dnstranslation.delete(mkey='item-name')

.. _firewall-global:

global
~~~~~~

Global firewall settings.

**Python attribute:** ``global``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.global.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.global.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.global.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.global.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.global.delete(mkey='item-name')

.. _firewall-identity-based-route:

identity-based-route
~~~~~~~~~~~~~~~~~~~~

Configure identity based routing.

**Python attribute:** ``identity_based_route``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.identity_based_route.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.identity_based_route.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.identity_based_route.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.identity_based_route.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.identity_based_route.delete(mkey='item-name')

.. _firewall-interface-policy:

interface-policy
~~~~~~~~~~~~~~~~

Configure IPv4 interface policies.

**Python attribute:** ``interface_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.interface_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.interface_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.interface_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.interface_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.interface_policy.delete(mkey='item-name')

.. _firewall-interface-policy6:

interface-policy6
~~~~~~~~~~~~~~~~~

Configure IPv6 interface policies.

**Python attribute:** ``interface_policy6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.interface_policy6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.interface_policy6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.interface_policy6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.interface_policy6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.interface_policy6.delete(mkey='item-name')

.. _firewall-internet-service:

internet-service
~~~~~~~~~~~~~~~~

Show Internet Service application.

**Python attribute:** ``internet_service``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service.delete(mkey='item-name')

.. _firewall-internet-service-addition:

internet-service-addition
~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Internet Services Addition.

**Python attribute:** ``internet_service_addition``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_addition.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_addition.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_addition.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_addition.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_addition.delete(mkey='item-name')

.. _firewall-internet-service-append:

internet-service-append
~~~~~~~~~~~~~~~~~~~~~~~

Configure additional port mappings for Internet Services.

**Python attribute:** ``internet_service_append``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_append.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_append.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_append.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_append.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_append.delete(mkey='item-name')

.. _firewall-internet-service-botnet:

internet-service-botnet
~~~~~~~~~~~~~~~~~~~~~~~

Show Internet Service botnet.

**Python attribute:** ``internet_service_botnet``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_botnet.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_botnet.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_botnet.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_botnet.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_botnet.delete(mkey='item-name')

.. _firewall-internet-service-custom:

internet-service-custom
~~~~~~~~~~~~~~~~~~~~~~~

Configure custom Internet Services.

**Python attribute:** ``internet_service_custom``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_custom.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_custom.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_custom.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_custom.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_custom.delete(mkey='item-name')

.. _firewall-internet-service-custom-group:

internet-service-custom-group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure custom Internet Service group.

**Python attribute:** ``internet_service_custom_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_custom_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_custom_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_custom_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_custom_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_custom_group.delete(mkey='item-name')

.. _firewall-internet-service-definition:

internet-service-definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Internet Service definition.

**Python attribute:** ``internet_service_definition``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_definition.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_definition.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_definition.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_definition.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_definition.delete(mkey='item-name')

.. _firewall-internet-service-extension:

internet-service-extension
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Internet Services Extension.

**Python attribute:** ``internet_service_extension``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_extension.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_extension.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_extension.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_extension.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_extension.delete(mkey='item-name')

.. _firewall-internet-service-fortiguard:

internet-service-fortiguard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure FortiGuard Internet Services.

**Python attribute:** ``internet_service_fortiguard``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_fortiguard.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_fortiguard.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_fortiguard.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_fortiguard.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_fortiguard.delete(mkey='item-name')

.. _firewall-internet-service-group:

internet-service-group
~~~~~~~~~~~~~~~~~~~~~~

Configure group of Internet Service.

**Python attribute:** ``internet_service_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_group.delete(mkey='item-name')

.. _firewall-internet-service-ipbl-reason:

internet-service-ipbl-reason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IP block list reason.

**Python attribute:** ``internet_service_ipbl_reason``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_ipbl_reason.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_ipbl_reason.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_ipbl_reason.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_ipbl_reason.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_ipbl_reason.delete(mkey='item-name')

.. _firewall-internet-service-ipbl-vendor:

internet-service-ipbl-vendor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IP block list vendor.

**Python attribute:** ``internet_service_ipbl_vendor``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_ipbl_vendor.delete(mkey='item-name')

.. _firewall-internet-service-list:

internet-service-list
~~~~~~~~~~~~~~~~~~~~~

Internet Service list.

**Python attribute:** ``internet_service_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_list.delete(mkey='item-name')

.. _firewall-internet-service-name:

internet-service-name
~~~~~~~~~~~~~~~~~~~~~

Define internet service names.

**Python attribute:** ``internet_service_name``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_name.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_name.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_name.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_name.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_name.delete(mkey='item-name')

.. _firewall-internet-service-owner:

internet-service-owner
~~~~~~~~~~~~~~~~~~~~~~

Internet Service owner.

**Python attribute:** ``internet_service_owner``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_owner.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_owner.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_owner.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_owner.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_owner.delete(mkey='item-name')

.. _firewall-internet-service-reputation:

internet-service-reputation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show Internet Service reputation.

**Python attribute:** ``internet_service_reputation``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_reputation.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_reputation.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_reputation.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_reputation.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_reputation.delete(mkey='item-name')

.. _firewall-internet-service-sld:

internet-service-sld
~~~~~~~~~~~~~~~~~~~~

Internet Service Second Level Domain.

**Python attribute:** ``internet_service_sld``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_sld.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_sld.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_sld.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_sld.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_sld.delete(mkey='item-name')

.. _firewall-internet-service-subapp:

internet-service-subapp
~~~~~~~~~~~~~~~~~~~~~~~

Show Internet Service sub app ID.

**Python attribute:** ``internet_service_subapp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.internet_service_subapp.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.internet_service_subapp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.internet_service_subapp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.internet_service_subapp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.internet_service_subapp.delete(mkey='item-name')

.. _firewall-ip-translation:

ip-translation
~~~~~~~~~~~~~~

Configure firewall IP-translation.

**Python attribute:** ``ip_translation``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ip_translation.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ip_translation.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ip_translation.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ip_translation.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ip_translation.delete(mkey='item-name')

.. _firewall-ippool:

ippool
~~~~~~

Configure IPv4 IP pools.

**Python attribute:** ``ippool``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ippool.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ippool.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ippool.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ippool.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ippool.delete(mkey='item-name')

.. _firewall-ippool6:

ippool6
~~~~~~~

Configure IPv6 IP pools.

**Python attribute:** ``ippool6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ippool6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ippool6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ippool6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ippool6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ippool6.delete(mkey='item-name')

.. _firewall-ldb-monitor:

ldb-monitor
~~~~~~~~~~~

Configure server load balancing health monitors.

**Python attribute:** ``ldb_monitor``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ldb_monitor.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ldb_monitor.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ldb_monitor.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ldb_monitor.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ldb_monitor.delete(mkey='item-name')

.. _firewall-local-in-policy:

local-in-policy
~~~~~~~~~~~~~~~

Configure user defined IPv4 local-in policies.

**Python attribute:** ``local_in_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.local_in_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.local_in_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.local_in_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.local_in_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.local_in_policy.delete(mkey='item-name')

.. _firewall-local-in-policy6:

local-in-policy6
~~~~~~~~~~~~~~~~

Configure user defined IPv6 local-in policies.

**Python attribute:** ``local_in_policy6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.local_in_policy6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.local_in_policy6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.local_in_policy6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.local_in_policy6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.local_in_policy6.delete(mkey='item-name')

.. _firewall-multicast-address:

multicast-address
~~~~~~~~~~~~~~~~~

Configure multicast addresses.

**Python attribute:** ``multicast_address``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.multicast_address.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.multicast_address.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.multicast_address.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.multicast_address.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.multicast_address.delete(mkey='item-name')

.. _firewall-multicast-address6:

multicast-address6
~~~~~~~~~~~~~~~~~~

Configure IPv6 multicast address.

**Python attribute:** ``multicast_address6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.multicast_address6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.multicast_address6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.multicast_address6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.multicast_address6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.multicast_address6.delete(mkey='item-name')

.. _firewall-multicast-policy:

multicast-policy
~~~~~~~~~~~~~~~~

Configure multicast NAT policies.

**Python attribute:** ``multicast_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.multicast_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.multicast_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.multicast_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.multicast_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.multicast_policy.delete(mkey='item-name')

.. _firewall-multicast-policy6:

multicast-policy6
~~~~~~~~~~~~~~~~~

Configure IPv6 multicast NAT policies.

**Python attribute:** ``multicast_policy6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.multicast_policy6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.multicast_policy6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.multicast_policy6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.multicast_policy6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.multicast_policy6.delete(mkey='item-name')

.. _firewall-network-service-dynamic:

network-service-dynamic
~~~~~~~~~~~~~~~~~~~~~~~

Configure Dynamic Network Services.

**Python attribute:** ``network_service_dynamic``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.network_service_dynamic.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.network_service_dynamic.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.network_service_dynamic.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.network_service_dynamic.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.network_service_dynamic.delete(mkey='item-name')

.. _firewall-on-demand-sniffer:

on-demand-sniffer
~~~~~~~~~~~~~~~~~

Configure on-demand packet sniffer.

**Python attribute:** ``on_demand_sniffer``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.on_demand_sniffer.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.on_demand_sniffer.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.on_demand_sniffer.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.on_demand_sniffer.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.on_demand_sniffer.delete(mkey='item-name')

.. _firewall-policy:

policy
~~~~~~

Configure IPv4/IPv6 policies.

**Python attribute:** ``policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.policy.delete(mkey='item-name')

.. _firewall-profile-group:

profile-group
~~~~~~~~~~~~~

Configure profile groups.

**Python attribute:** ``profile_group``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.profile_group.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.profile_group.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.profile_group.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.profile_group.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.profile_group.delete(mkey='item-name')

.. _firewall-profile-protocol-options:

profile-protocol-options
~~~~~~~~~~~~~~~~~~~~~~~~

Configure protocol options.

**Python attribute:** ``profile_protocol_options``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.profile_protocol_options.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.profile_protocol_options.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.profile_protocol_options.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.profile_protocol_options.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.profile_protocol_options.delete(mkey='item-name')

.. _firewall-proxy-address:

proxy-address
~~~~~~~~~~~~~

Configure web proxy address.

**Python attribute:** ``proxy_address``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.proxy_address.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.proxy_address.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.proxy_address.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.proxy_address.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.proxy_address.delete(mkey='item-name')

.. _firewall-proxy-addrgrp:

proxy-addrgrp
~~~~~~~~~~~~~

Configure web proxy address group.

**Python attribute:** ``proxy_addrgrp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.proxy_addrgrp.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.proxy_addrgrp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.proxy_addrgrp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.proxy_addrgrp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.proxy_addrgrp.delete(mkey='item-name')

.. _firewall-proxy-policy:

proxy-policy
~~~~~~~~~~~~

Configure proxy policies.

**Python attribute:** ``proxy_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.proxy_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.proxy_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.proxy_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.proxy_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.proxy_policy.delete(mkey='item-name')

.. _firewall-region:

region
~~~~~~

Define region table.

**Python attribute:** ``region``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.region.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.region.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.region.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.region.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.region.delete(mkey='item-name')

.. _firewall-security-policy:

security-policy
~~~~~~~~~~~~~~~

Configure NGFW IPv4/IPv6 application policies.

**Python attribute:** ``security_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.security_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.security_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.security_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.security_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.security_policy.delete(mkey='item-name')

.. _firewall-shaping-policy:

shaping-policy
~~~~~~~~~~~~~~

Configure shaping policies.

**Python attribute:** ``shaping_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.shaping_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.shaping_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.shaping_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.shaping_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.shaping_policy.delete(mkey='item-name')

.. _firewall-shaping-profile:

shaping-profile
~~~~~~~~~~~~~~~

Configure shaping profiles.

**Python attribute:** ``shaping_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.shaping_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.shaping_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.shaping_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.shaping_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.shaping_profile.delete(mkey='item-name')

.. _firewall-sniffer:

sniffer
~~~~~~~

Configure sniffer.

**Python attribute:** ``sniffer``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.sniffer.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.sniffer.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.sniffer.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.sniffer.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.sniffer.delete(mkey='item-name')

.. _firewall-ssl-server:

ssl-server
~~~~~~~~~~

Configure SSL servers.

**Python attribute:** ``ssl_server``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ssl_server.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ssl_server.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ssl_server.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ssl_server.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ssl_server.delete(mkey='item-name')

.. _firewall-ssl-ssh-profile:

ssl-ssh-profile
~~~~~~~~~~~~~~~

Configure SSL/SSH protocol options.

**Python attribute:** ``ssl_ssh_profile``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ssl_ssh_profile.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ssl_ssh_profile.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ssl_ssh_profile.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ssl_ssh_profile.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ssl_ssh_profile.delete(mkey='item-name')

.. _firewall-traffic-class:

traffic-class
~~~~~~~~~~~~~

Configure names for shaping classes.

**Python attribute:** ``traffic_class``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.traffic_class.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.traffic_class.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.traffic_class.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.traffic_class.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.traffic_class.delete(mkey='item-name')

.. _firewall-ttl-policy:

ttl-policy
~~~~~~~~~~

Configure TTL policies.

**Python attribute:** ``ttl_policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.ttl_policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.ttl_policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.ttl_policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.ttl_policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.ttl_policy.delete(mkey='item-name')

.. _firewall-vendor-mac:

vendor-mac
~~~~~~~~~~

Show vendor and the MAC address they have.

**Python attribute:** ``vendor_mac``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.vendor_mac.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.vendor_mac.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.vendor_mac.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.vendor_mac.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.vendor_mac.delete(mkey='item-name')

.. _firewall-vendor-mac-summary:

vendor-mac-summary
~~~~~~~~~~~~~~~~~~

Vendor MAC database summary.

**Python attribute:** ``vendor_mac_summary``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.vendor_mac_summary.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.vendor_mac_summary.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.vendor_mac_summary.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.vendor_mac_summary.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.vendor_mac_summary.delete(mkey='item-name')

.. _firewall-vip:

vip
~~~

Configure virtual IP for IPv4.

**Python attribute:** ``vip``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.vip.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.vip.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.vip.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.vip.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.vip.delete(mkey='item-name')

.. _firewall-vip6:

vip6
~~~~

Configure virtual IP for IPv6.

**Python attribute:** ``vip6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.vip6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.vip6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.vip6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.vip6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.vip6.delete(mkey='item-name')

.. _firewall-vipgrp:

vipgrp
~~~~~~

Configure IPv4 virtual IP groups.

**Python attribute:** ``vipgrp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.vipgrp.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.vipgrp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.vipgrp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.vipgrp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.vipgrp.delete(mkey='item-name')

.. _firewall-vipgrp6:

vipgrp6
~~~~~~~

Configure IPv6 virtual IP groups.

**Python attribute:** ``vipgrp6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.firewall.vipgrp6.get()
   
   # Get specific item
   item = fgt.api.cmdb.firewall.vipgrp6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.firewall.vipgrp6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.firewall.vipgrp6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.firewall.vipgrp6.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.firewall.DoS_policy.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.firewall.DoS_policy.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.firewall.DoS_policy.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.firewall.DoS_policy.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.firewall.DoS_policy.delete(mkey='config-name')

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
