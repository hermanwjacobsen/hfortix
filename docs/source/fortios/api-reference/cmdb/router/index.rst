Router
======

Overview
--------

The ``cmdb.router`` namespace provides configuration management for:

- :doc:`Access List <access_list>` - Access List configuration endpoint.
- :doc:`Access List6 <access_list6>` - Access List6 configuration endpoint.
- :doc:`Aspath List <aspath_list>` - Aspath List configuration endpoint.
- :doc:`Auth Path <auth_path>` - Auth Path configuration endpoint.
- :doc:`Bfd <bfd>` - Bfd configuration endpoint.
- :doc:`Bfd6 <bfd6>` - Bfd6 configuration endpoint.
- :doc:`Bgp <bgp>` - Bgp configuration endpoint.
- :doc:`Community List <community_list>` - Community List configuration endpoint.
- :doc:`Extcommunity List <extcommunity_list>` - Extcommunity List configuration endpoint.
- :doc:`Isis <isis>` - Isis configuration endpoint.
- :doc:`Key Chain <key_chain>` - Key Chain configuration endpoint.
- :doc:`Multicast <multicast>` - Multicast configuration endpoint.
- :doc:`Multicast6 <multicast6>` - Multicast6 configuration endpoint.
- :doc:`Multicast Flow <multicast_flow>` - Multicast Flow configuration endpoint.
- :doc:`Ospf <ospf>` - Ospf configuration endpoint.
- :doc:`Ospf6 <ospf6>` - Ospf6 configuration endpoint.
- :doc:`Policy <policy>` - Policy configuration endpoint.
- :doc:`Policy6 <policy6>` - Policy6 configuration endpoint.
- :doc:`Prefix List <prefix_list>` - Prefix List configuration endpoint.
- :doc:`Prefix List6 <prefix_list6>` - Prefix List6 configuration endpoint.
- :doc:`Rip <rip>` - Rip configuration endpoint.
- :doc:`Ripng <ripng>` - Ripng configuration endpoint.
- :doc:`Route Map <route_map>` - Route Map configuration endpoint.
- :doc:`Setting <setting>` - Setting configuration endpoint.
- :doc:`Static <static>` - Static configuration endpoint.
- :doc:`Static6 <static6>` - Static6 configuration endpoint.


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
   
   access_list
   access_list6
   aspath_list
   auth_path
   bfd
   bfd6
   bgp
   community_list
   extcommunity_list
   isis
   key_chain
   multicast
   multicast6
   multicast_flow
   ospf
   ospf6
   policy
   policy6
   prefix_list
   prefix_list6
   rip
   ripng
   route_map
   setting
   static
   static6

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
