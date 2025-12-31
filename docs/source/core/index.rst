Core Package
============

Documentation for the ``hfortix-core`` package - the foundation for all HFortix packages.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   http-client
   exceptions
   utilities

Overview
--------

The ``hfortix-core`` package provides the foundational components used by all HFortix packages:

**HTTP Client**
   Synchronous and asynchronous HTTP client with connection pooling, retry logic,
   and circuit breaker support.

**Exception Handling**
   Comprehensive exception hierarchy for handling API errors, network issues,
   and validation errors.

**Utilities**
   Common utilities and helpers shared across HFortix packages.

Installation
------------

.. code-block:: bash

   pip install hfortix-core

The core package is automatically installed as a dependency when you install
any HFortix package (``hfortix-fortios``, etc.).

Quick Example
-------------

.. code-block:: python

   from hfortix_core.http.client import HTTPClient
   from hfortix_core.exceptions import APIError

   # Create HTTP client
   client = HTTPClient(
       base_url='https://api.example.com',
       verify=True
   )

   # Make request
   try:
       response = client.get('/endpoint')
   except APIError as e:
       print(f"Error: {e.message}")

API Reference
-------------

For complete API documentation, see:

- :doc:`/api-reference/core` - Complete API reference
- :doc:`/api-reference/exceptions` - Exception hierarchy

Components
----------

HTTP Client
^^^^^^^^^^^

See: :doc:`/core/http-client`

- Synchronous and asynchronous support
- Connection pooling
- Automatic retries with exponential backoff
- Circuit breaker pattern
- Custom timeout configuration

Exception Handling
^^^^^^^^^^^^^^^^^^

See: :doc:`/core/exceptions`

- Comprehensive exception hierarchy
- FortiOS-specific exceptions
- HTTP error mapping
- Validation errors

See Also
--------

- :doc:`/fortios/index` - FortiOS package documentation
- :doc:`/getting-started/installation` - Installation guide
