Router
======

Configure access lists configuration and management.

Overview
--------

The ``cmdb.router`` category provides configuration management for:

- :doc:`Access List <access-list>` - Configure access lists.
- :doc:`Access List6 <access-list6>` - Configure IPv6 access lists.
- :doc:`Aspath List <aspath-list>` - Configure Autonomous System (AS) path lists.
- :doc:`Auth Path <auth-path>` - Configure authentication based routing.
- :doc:`Bfd <bfd>` - Configure BFD.
- :doc:`Bfd6 <bfd6>` - Configure IPv6 BFD.
- :doc:`Bgp <bgp>` - Configure BGP.
- :doc:`Community List <community-list>` - Configure community lists.
- :doc:`Extcommunity List <extcommunity-list>` - Configure extended community lists.
- :doc:`Isis <isis>` - Configure IS-IS.
- :doc:`Key Chain <key-chain>` - Configure key-chain.
- :doc:`Multicast <multicast>` - Configure router multicast.
- :doc:`Multicast Flow <multicast-flow>` - Configure multicast-flow.
- :doc:`Multicast6 <multicast6>` - Configure IPv6 multicast.
- :doc:`Ospf <ospf>` - Configure OSPF.
- :doc:`Ospf6 <ospf6>` - Configure IPv6 OSPF.
- :doc:`Policy <policy>` - Configure IPv4 routing policies.
- :doc:`Policy6 <policy6>` - Configure IPv6 routing policies.
- :doc:`Prefix List <prefix-list>` - Configure IPv4 prefix lists.
- :doc:`Prefix List6 <prefix-list6>` - Configure IPv6 prefix lists.
- :doc:`Rip <rip>` - Configure RIP.
- :doc:`Ripng <ripng>` - Configure RIPng.
- :doc:`Route Map <route-map>` - Configure route maps.
- :doc:`Setting <setting>` - Configure router settings.
- :doc:`Static <static>` - Configure IPv4 static routing tables.
- :doc:`Static6 <static6>` - Configure IPv6 static routing tables.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.router.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   access-list
   access-list6
   aspath-list
   auth-path
   bfd
   bfd6
   bgp
   community-list
   extcommunity-list
   isis
   key-chain
   multicast
   multicast-flow
   multicast6
   ospf
   ospf6
   policy
   policy6
   prefix-list
   prefix-list6
   rip
   ripng
   route-map
   setting
   static
   static6

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
