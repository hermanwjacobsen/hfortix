Vpn
===

CA certificate configuration and management.

Overview
--------

The ``cmdb.vpn`` category provides configuration management for:

- :doc:`Kmip Server <kmip-server>` - KMIP server entry configuration.
- :doc:`L2Tp <l2tp>` - Configure L2TP.
- :doc:`Pptp <pptp>` - Configure PPTP.
- :doc:`Qkd <qkd>` - Configure Quantum Key Distribution servers


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.cmdb.vpn.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   kmip-server
   l2tp
   pptp
   qkd

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
