VPN Certificate
===============

Overview
--------

The ``monitor.vpn_certificate`` namespace provides configuration management for:

- :doc:`Ca <ca>` - Ca configuration endpoint.
- :doc:`Cert Name Available <cert_name_available>` - Cert Name Available configuration endpoint.
- :doc:`Crl <crl>` - Crl configuration endpoint.
- :doc:`Csr <csr>` - Csr configuration endpoint.
- :doc:`Local <local>` - Local configuration endpoint.
- :doc:`Remote <remote>` - Remote configuration endpoint.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.monitor.vpn_certificate.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   ca
   cert_name_available
   crl
   csr
   local
   remote

See Also
--------

- :doc:`/api-reference/api-reference/monitor/index` - MONITOR API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
