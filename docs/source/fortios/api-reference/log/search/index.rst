Search
======

Search log query operations.

Overview
--------

The ``log.search`` category provides log query access for:

- :doc:`Search_Abort_{Session_Id} <search-abort-{session-id}>` - Abort a running log search session.
- :doc:`Search_Status_{Session_Id} <search-status-{session-id}>` - Returns status of log search session, if it is active or not. This is only applicable for disk log search.


Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS
   
   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access endpoints via:
   fgt.api.log.search.<endpoint>

Available Endpoints
-------------------

.. toctree::
   :maxdepth: 1
   
   search-abort-{session-id}
   search-status-{session-id}

See Also
--------

- :doc:`/fortios/api-reference/log/index` - Log API overview
- :doc:`/fortios/user-guide/client` - FortiOS client reference
- :doc:`/fortios/guides/filtering` - Filtering guide
