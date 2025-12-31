Emailfilter
===========

Overview
--------

The ``cmdb.emailfilter`` namespace provides configuration management for:

- :doc:`Block Allow List <block_allow_list>` - Block Allow List configuration endpoint.
- :doc:`Bword <bword>` - Bword configuration endpoint.
- :doc:`Dnsbl <dnsbl>` - Dnsbl configuration endpoint.
- :doc:`Fortishield <fortishield>` - Fortishield configuration endpoint.
- :doc:`Iptrust <iptrust>` - Iptrust configuration endpoint.
- :doc:`Mheader <mheader>` - Mheader configuration endpoint.
- :doc:`Options <options>` - Options configuration endpoint.
- :doc:`Profile <profile>` - Profile configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.emailfilter.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   block_allow_list
   bword
   dnsbl
   fortishield
   iptrust
   mheader
   options
   profile

See Also
--------

- :doc:`/api-reference/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
