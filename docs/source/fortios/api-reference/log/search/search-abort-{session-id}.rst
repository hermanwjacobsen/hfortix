.. _search_search_abort_{session_id}:

Search_Abort_{Session_Id}
=========================

Abort a running log search session.

Python Attribute
----------------

.. code-block:: python

   fgt.api.log.search.search_abort_{session_id}

Quick Examples
--------------

**Query Logs (GET)**

.. code-block:: python

   # Query logs
   response = fgt.api.log.search.search_abort_{session_id}.get()
   
   # With filters
   response = fgt.api.log.search.search_abort_{session_id}.get(
       rows=100,
       start=0
   )


Parameters
----------

**session_id** (path) - **Required**
   Type: ``integer``
   
   Provide the session ID for the request

**session_id** (path) - **Required**
   Type: ``integer``
   
   Provide the session ID for the request


HTTP Methods
------------

- **POST**: Abort a running log search session.
- **GET**: Returns status of log search session, if it is active or not. This is only applicable for disk log search.


See Also
--------

- :doc:`index` - Search overview
- :doc:`/fortios/api-reference/log/index` - Log API reference
- :doc:`/fortios/guides/filtering` - Filtering guide
