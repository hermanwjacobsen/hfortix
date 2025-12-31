Router
======

Configure access lists configuration and management.

Overview
--------

The ``cmdb.router`` category provides configuration management for:

- :ref:`Access List <router-access-list>` - Configure access lists.
- :ref:`Access List6 <router-access-list6>` - Configure IPv6 access lists.
- :ref:`Aspath List <router-aspath-list>` - Configure Autonomous System (AS) path lists.
- :ref:`Auth Path <router-auth-path>` - Configure authentication based routing.
- :ref:`Bfd <router-bfd>` - Configure BFD.
- :ref:`Bfd6 <router-bfd6>` - Configure IPv6 BFD.
- :ref:`Bgp <router-bgp>` - Configure BGP.
- :ref:`Community List <router-community-list>` - Configure community lists.
- :ref:`Extcommunity List <router-extcommunity-list>` - Configure extended community lists.
- :ref:`Isis <router-isis>` - Configure IS-IS.
- :ref:`Key Chain <router-key-chain>` - Configure key-chain.
- :ref:`Multicast <router-multicast>` - Configure router multicast.
- :ref:`Multicast Flow <router-multicast-flow>` - Configure multicast-flow.
- :ref:`Multicast6 <router-multicast6>` - Configure IPv6 multicast.
- :ref:`Ospf <router-ospf>` - Configure OSPF.
- :ref:`Ospf6 <router-ospf6>` - Configure IPv6 OSPF.
- :ref:`Policy <router-policy>` - Configure IPv4 routing policies.
- :ref:`Policy6 <router-policy6>` - Configure IPv6 routing policies.
- :ref:`Prefix List <router-prefix-list>` - Configure IPv4 prefix lists.
- :ref:`Prefix List6 <router-prefix-list6>` - Configure IPv6 prefix lists.
- :ref:`Rip <router-rip>` - Configure RIP.
- :ref:`Ripng <router-ripng>` - Configure RIPng.
- :ref:`Route Map <router-route-map>` - Configure route maps.
- :ref:`Setting <router-setting>` - Configure router settings.
- :ref:`Static <router-static>` - Configure IPv4 static routing tables.
- :ref:`Static6 <router-static6>` - Configure IPv6 static routing tables.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.router

Available Endpoints
-------------------

.. _router-access-list:

access-list
~~~~~~~~~~~

Configure access lists.

**Python attribute:** ``access_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.access_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.access_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.access_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.access_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.access_list.delete(mkey='item-name')

.. _router-access-list6:

access-list6
~~~~~~~~~~~~

Configure IPv6 access lists.

**Python attribute:** ``access_list6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.access_list6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.access_list6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.access_list6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.access_list6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.access_list6.delete(mkey='item-name')

.. _router-aspath-list:

aspath-list
~~~~~~~~~~~

Configure Autonomous System (AS) path lists.

**Python attribute:** ``aspath_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.aspath_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.aspath_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.aspath_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.aspath_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.aspath_list.delete(mkey='item-name')

.. _router-auth-path:

auth-path
~~~~~~~~~

Configure authentication based routing.

**Python attribute:** ``auth_path``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.auth_path.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.auth_path.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.auth_path.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.auth_path.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.auth_path.delete(mkey='item-name')

.. _router-bfd:

bfd
~~~

Configure BFD.

**Python attribute:** ``bfd``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.bfd.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.bfd.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.bfd.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.bfd.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.bfd.delete(mkey='item-name')

.. _router-bfd6:

bfd6
~~~~

Configure IPv6 BFD.

**Python attribute:** ``bfd6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.bfd6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.bfd6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.bfd6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.bfd6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.bfd6.delete(mkey='item-name')

.. _router-bgp:

bgp
~~~

Configure BGP.

**Python attribute:** ``bgp``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.bgp.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.bgp.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.bgp.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.bgp.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.bgp.delete(mkey='item-name')

.. _router-community-list:

community-list
~~~~~~~~~~~~~~

Configure community lists.

**Python attribute:** ``community_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.community_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.community_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.community_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.community_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.community_list.delete(mkey='item-name')

.. _router-extcommunity-list:

extcommunity-list
~~~~~~~~~~~~~~~~~

Configure extended community lists.

**Python attribute:** ``extcommunity_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.extcommunity_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.extcommunity_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.extcommunity_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.extcommunity_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.extcommunity_list.delete(mkey='item-name')

.. _router-isis:

isis
~~~~

Configure IS-IS.

**Python attribute:** ``isis``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.isis.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.isis.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.isis.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.isis.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.isis.delete(mkey='item-name')

.. _router-key-chain:

key-chain
~~~~~~~~~

Configure key-chain.

**Python attribute:** ``key_chain``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.key_chain.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.key_chain.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.key_chain.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.key_chain.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.key_chain.delete(mkey='item-name')

.. _router-multicast:

multicast
~~~~~~~~~

Configure router multicast.

**Python attribute:** ``multicast``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.multicast.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.multicast.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.multicast.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.multicast.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.multicast.delete(mkey='item-name')

.. _router-multicast-flow:

multicast-flow
~~~~~~~~~~~~~~

Configure multicast-flow.

**Python attribute:** ``multicast_flow``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.multicast_flow.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.multicast_flow.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.multicast_flow.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.multicast_flow.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.multicast_flow.delete(mkey='item-name')

.. _router-multicast6:

multicast6
~~~~~~~~~~

Configure IPv6 multicast.

**Python attribute:** ``multicast6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.multicast6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.multicast6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.multicast6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.multicast6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.multicast6.delete(mkey='item-name')

.. _router-ospf:

ospf
~~~~

Configure OSPF.

**Python attribute:** ``ospf``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.ospf.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.ospf.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.ospf.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.ospf.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.ospf.delete(mkey='item-name')

.. _router-ospf6:

ospf6
~~~~~

Configure IPv6 OSPF.

**Python attribute:** ``ospf6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.ospf6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.ospf6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.ospf6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.ospf6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.ospf6.delete(mkey='item-name')

.. _router-policy:

policy
~~~~~~

Configure IPv4 routing policies.

**Python attribute:** ``policy``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.policy.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.policy.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.policy.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.policy.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.policy.delete(mkey='item-name')

.. _router-policy6:

policy6
~~~~~~~

Configure IPv6 routing policies.

**Python attribute:** ``policy6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.policy6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.policy6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.policy6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.policy6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.policy6.delete(mkey='item-name')

.. _router-prefix-list:

prefix-list
~~~~~~~~~~~

Configure IPv4 prefix lists.

**Python attribute:** ``prefix_list``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.prefix_list.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.prefix_list.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.prefix_list.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.prefix_list.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.prefix_list.delete(mkey='item-name')

.. _router-prefix-list6:

prefix-list6
~~~~~~~~~~~~

Configure IPv6 prefix lists.

**Python attribute:** ``prefix_list6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.prefix_list6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.prefix_list6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.prefix_list6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.prefix_list6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.prefix_list6.delete(mkey='item-name')

.. _router-rip:

rip
~~~

Configure RIP.

**Python attribute:** ``rip``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.rip.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.rip.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.rip.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.rip.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.rip.delete(mkey='item-name')

.. _router-ripng:

ripng
~~~~~

Configure RIPng.

**Python attribute:** ``ripng``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.ripng.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.ripng.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.ripng.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.ripng.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.ripng.delete(mkey='item-name')

.. _router-route-map:

route-map
~~~~~~~~~

Configure route maps.

**Python attribute:** ``route_map``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.route_map.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.route_map.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.route_map.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.route_map.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.route_map.delete(mkey='item-name')

.. _router-setting:

setting
~~~~~~~

Configure router settings.

**Python attribute:** ``setting``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.setting.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.setting.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.setting.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.setting.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.setting.delete(mkey='item-name')

.. _router-static:

static
~~~~~~

Configure IPv4 static routing tables.

**Python attribute:** ``static``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.static.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.static.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.static.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.static.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.static.delete(mkey='item-name')

.. _router-static6:

static6
~~~~~~~

Configure IPv6 static routing tables.

**Python attribute:** ``static6``

.. code-block:: python

   # Get all items
   items = fgt.api.cmdb.router.static6.get()
   
   # Get specific item
   item = fgt.api.cmdb.router.static6.get(mkey='item-name')
   
   # Create new item
   result = fgt.api.cmdb.router.static6.post(json={
       'name': 'item-name',
       # Additional configuration parameters
   })
   
   # Update existing item
   result = fgt.api.cmdb.router.static6.put(
       mkey='item-name',
       json={'parameter': 'value'}
   )
   
   # Delete item
   result = fgt.api.cmdb.router.static6.delete(mkey='item-name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.router.access_list.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.router.access_list.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.router.access_list.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.router.access_list.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.router.access_list.delete(mkey='config-name')

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
