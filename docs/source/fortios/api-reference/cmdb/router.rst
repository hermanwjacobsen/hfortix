Router
======

Configure access lists configuration and management.

Overview
--------

The ``cmdb.router`` category provides configuration management for:

- **Access List** - Configure access lists.
- **Access List6** - Configure IPv6 access lists.
- **Aspath List** - Configure Autonomous System (AS) path lists.
- **Auth Path** - Configure authentication based routing.
- **Bfd** - Configure BFD.
- **Bfd6** - Configure IPv6 BFD.
- **Bgp** - Configure BGP.
- **Community List** - Configure community lists.
- **Extcommunity List** - Configure extended community lists.
- **Isis** - Configure IS-IS.
- **Key Chain** - Configure key-chain.
- **Multicast** - Configure router multicast.
- **Multicast Flow** - Configure multicast-flow.
- **Multicast6** - Configure IPv6 multicast.
- **Ospf** - Configure OSPF.
- **Ospf6** - Configure IPv6 OSPF.
- **Policy** - Configure IPv4 routing policies.
- **Policy6** - Configure IPv6 routing policies.
- **Prefix List** - Configure IPv4 prefix lists.
- **Prefix List6** - Configure IPv6 prefix lists.
- **Rip** - Configure RIP.
- **Ripng** - Configure RIPng.
- **Route Map** - Configure route maps.
- **Setting** - Configure router settings.
- **Static** - Configure IPv4 static routing tables.
- **Static6** - Configure IPv6 static routing tables.


Endpoint
--------

.. code-block:: python

   fgt.api.cmdb.router

Available Endpoints
-------------------

**access-list**
   Configure access lists.
   
   .. code-block:: python
   
      # List all access-list
      items = fgt.api.cmdb.router.access_list.get()
      
      # Get specific access-list
      item = fgt.api.cmdb.router.access_list.get(mkey='name')

**access-list6**
   Configure IPv6 access lists.
   
   .. code-block:: python
   
      # List all access-list6
      items = fgt.api.cmdb.router.access_list6.get()
      
      # Get specific access-list6
      item = fgt.api.cmdb.router.access_list6.get(mkey='name')

**aspath-list**
   Configure Autonomous System (AS) path lists.
   
   .. code-block:: python
   
      # List all aspath-list
      items = fgt.api.cmdb.router.aspath_list.get()
      
      # Get specific aspath-list
      item = fgt.api.cmdb.router.aspath_list.get(mkey='name')

**auth-path**
   Configure authentication based routing.
   
   .. code-block:: python
   
      # List all auth-path
      items = fgt.api.cmdb.router.auth_path.get()
      
      # Get specific auth-path
      item = fgt.api.cmdb.router.auth_path.get(mkey='name')

**bfd**
   Configure BFD.
   
   .. code-block:: python
   
      # List all bfd
      items = fgt.api.cmdb.router.bfd.get()
      
      # Get specific bfd
      item = fgt.api.cmdb.router.bfd.get(mkey='name')

**bfd6**
   Configure IPv6 BFD.
   
   .. code-block:: python
   
      # List all bfd6
      items = fgt.api.cmdb.router.bfd6.get()
      
      # Get specific bfd6
      item = fgt.api.cmdb.router.bfd6.get(mkey='name')

**bgp**
   Configure BGP.
   
   .. code-block:: python
   
      # List all bgp
      items = fgt.api.cmdb.router.bgp.get()
      
      # Get specific bgp
      item = fgt.api.cmdb.router.bgp.get(mkey='name')

**community-list**
   Configure community lists.
   
   .. code-block:: python
   
      # List all community-list
      items = fgt.api.cmdb.router.community_list.get()
      
      # Get specific community-list
      item = fgt.api.cmdb.router.community_list.get(mkey='name')

**extcommunity-list**
   Configure extended community lists.
   
   .. code-block:: python
   
      # List all extcommunity-list
      items = fgt.api.cmdb.router.extcommunity_list.get()
      
      # Get specific extcommunity-list
      item = fgt.api.cmdb.router.extcommunity_list.get(mkey='name')

**isis**
   Configure IS-IS.
   
   .. code-block:: python
   
      # List all isis
      items = fgt.api.cmdb.router.isis.get()
      
      # Get specific isis
      item = fgt.api.cmdb.router.isis.get(mkey='name')

**key-chain**
   Configure key-chain.
   
   .. code-block:: python
   
      # List all key-chain
      items = fgt.api.cmdb.router.key_chain.get()
      
      # Get specific key-chain
      item = fgt.api.cmdb.router.key_chain.get(mkey='name')

**multicast**
   Configure router multicast.
   
   .. code-block:: python
   
      # List all multicast
      items = fgt.api.cmdb.router.multicast.get()
      
      # Get specific multicast
      item = fgt.api.cmdb.router.multicast.get(mkey='name')

**multicast-flow**
   Configure multicast-flow.
   
   .. code-block:: python
   
      # List all multicast-flow
      items = fgt.api.cmdb.router.multicast_flow.get()
      
      # Get specific multicast-flow
      item = fgt.api.cmdb.router.multicast_flow.get(mkey='name')

**multicast6**
   Configure IPv6 multicast.
   
   .. code-block:: python
   
      # List all multicast6
      items = fgt.api.cmdb.router.multicast6.get()
      
      # Get specific multicast6
      item = fgt.api.cmdb.router.multicast6.get(mkey='name')

**ospf**
   Configure OSPF.
   
   .. code-block:: python
   
      # List all ospf
      items = fgt.api.cmdb.router.ospf.get()
      
      # Get specific ospf
      item = fgt.api.cmdb.router.ospf.get(mkey='name')

**ospf6**
   Configure IPv6 OSPF.
   
   .. code-block:: python
   
      # List all ospf6
      items = fgt.api.cmdb.router.ospf6.get()
      
      # Get specific ospf6
      item = fgt.api.cmdb.router.ospf6.get(mkey='name')

**policy**
   Configure IPv4 routing policies.
   
   .. code-block:: python
   
      # List all policy
      items = fgt.api.cmdb.router.policy.get()
      
      # Get specific policy
      item = fgt.api.cmdb.router.policy.get(mkey='name')

**policy6**
   Configure IPv6 routing policies.
   
   .. code-block:: python
   
      # List all policy6
      items = fgt.api.cmdb.router.policy6.get()
      
      # Get specific policy6
      item = fgt.api.cmdb.router.policy6.get(mkey='name')

**prefix-list**
   Configure IPv4 prefix lists.
   
   .. code-block:: python
   
      # List all prefix-list
      items = fgt.api.cmdb.router.prefix_list.get()
      
      # Get specific prefix-list
      item = fgt.api.cmdb.router.prefix_list.get(mkey='name')

**prefix-list6**
   Configure IPv6 prefix lists.
   
   .. code-block:: python
   
      # List all prefix-list6
      items = fgt.api.cmdb.router.prefix_list6.get()
      
      # Get specific prefix-list6
      item = fgt.api.cmdb.router.prefix_list6.get(mkey='name')

**rip**
   Configure RIP.
   
   .. code-block:: python
   
      # List all rip
      items = fgt.api.cmdb.router.rip.get()
      
      # Get specific rip
      item = fgt.api.cmdb.router.rip.get(mkey='name')

**ripng**
   Configure RIPng.
   
   .. code-block:: python
   
      # List all ripng
      items = fgt.api.cmdb.router.ripng.get()
      
      # Get specific ripng
      item = fgt.api.cmdb.router.ripng.get(mkey='name')

**route-map**
   Configure route maps.
   
   .. code-block:: python
   
      # List all route-map
      items = fgt.api.cmdb.router.route_map.get()
      
      # Get specific route-map
      item = fgt.api.cmdb.router.route_map.get(mkey='name')

**setting**
   Configure router settings.
   
   .. code-block:: python
   
      # List all setting
      items = fgt.api.cmdb.router.setting.get()
      
      # Get specific setting
      item = fgt.api.cmdb.router.setting.get(mkey='name')

**static**
   Configure IPv4 static routing tables.
   
   .. code-block:: python
   
      # List all static
      items = fgt.api.cmdb.router.static.get()
      
      # Get specific static
      item = fgt.api.cmdb.router.static.get(mkey='name')

**static6**
   Configure IPv6 static routing tables.
   
   .. code-block:: python
   
      # List all static6
      items = fgt.api.cmdb.router.static6.get()
      
      # Get specific static6
      item = fgt.api.cmdb.router.static6.get(mkey='name')

Common Operations
-----------------

Create Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create new configuration
   result = fgt.api.cmdb.router.{endpoint}.post(json={
       'name': 'config-name',
       # Add configuration parameters
   })

Update Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Update existing configuration
   result = fgt.api.cmdb.router.{endpoint}.put(
       mkey='config-name',
       json={
           # Updated parameters
       }
   )

Get Configuration
^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Get all configurations
   items = fgt.api.cmdb.router.{endpoint}.get()
   
   # Get specific configuration
   item = fgt.api.cmdb.router.{endpoint}.get(mkey='config-name')

Delete Configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # Delete configuration
   result = fgt.api.cmdb.router.{endpoint}.delete(mkey='config-name')

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
