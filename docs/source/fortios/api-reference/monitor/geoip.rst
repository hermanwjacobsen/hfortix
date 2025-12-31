GeoIP
=====

GeoIP information.

.. automodule:: hfortix_fortios.api.v2.monitor.geoip
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS GeoIP configuration through
   the ``fgt.api.monitor.geoip`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access GeoIP endpoints
   result = fgt.api.monitor.geoip.<endpoint>.list()

See Also
--------

- :doc:`index` - MONITOR API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
