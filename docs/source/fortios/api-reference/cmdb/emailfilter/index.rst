Emailfilter
===========

Configure anti-spam block/allow list configuration and management.

Overview
--------

The ``cmdb.emailfilter`` category provides configuration management for:

- :doc:`Block Allow List <block-allow-list>` - Configure anti-spam block/allow list.
- :doc:`Bword <bword>` - Configure AntiSpam banned word list.
- :doc:`Dnsbl <dnsbl>` - Configure AntiSpam DNSBL/ORBL.
- :doc:`Fortishield <fortishield>` - Configure FortiGuard - AntiSpam.
- :doc:`Iptrust <iptrust>` - Configure AntiSpam IP trust.
- :doc:`Mheader <mheader>` - Configure AntiSpam MIME header.
- :doc:`Options <options>` - Configure AntiSpam options.
- :doc:`Profile <profile>` - Configure Email Filter profiles.


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
   
   block-allow-list
   bword
   dnsbl
   fortishield
   iptrust
   mheader
   options
   profile

See Also
--------

- :doc:`/fortios/api-reference/cmdb/index` - CMDB API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
