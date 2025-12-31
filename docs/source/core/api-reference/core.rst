Core Package API Reference
==========================

The ``hfortix-core`` package provides the foundation for all HFortix packages,
including HTTP client functionality, exception handling, and retry logic.

Installation
------------

.. code-block:: bash

   pip install hfortix-core

Core Modules
------------

Exceptions
^^^^^^^^^^

.. automodule:: hfortix_core.exceptions
   :members:
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

Exception Hierarchy
~~~~~~~~~~~~~~~~~~~

All HFortix exceptions inherit from ``FortinetError``::

   FortinetError (Base exception)
   ├── APIError (Base for all API errors)
   │   ├── HTTPError (Base for HTTP errors)
   │   │   ├── BadRequestError (400)
   │   │   ├── UnauthorizedError (401)
   │   │   ├── ForbiddenError (403)
   │   │   ├── ResourceNotFoundError (404)
   │   │   ├── MethodNotAllowedError (405)
   │   │   ├── RateLimitError (429)
   │   │   └── ServerError (500+)
   │   ├── DuplicateEntryError (FortiOS: object exists)
   │   ├── EntryInUseError (FortiOS: object in use)
   │   └── ValidationError (Invalid input)
   ├── ConnectionError (Network/connection issues)
   ├── TimeoutError (Request timeout)
   └── ConfigurationError (Invalid configuration)

HTTP Client
^^^^^^^^^^^

Base HTTP Client Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: hfortix_core.http.interface
   :members:
   :undoc-members:
   :show-inheritance:

Synchronous HTTP Client
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: hfortix_core.http.client
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Asynchronous HTTP Client
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: hfortix_core.http.async_client
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Base HTTP Classes
~~~~~~~~~~~~~~~~~

.. automodule:: hfortix_core.http.base
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Basic Exception Handling
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix import FortiOS
   from hfortix_core import (
       APIError,
       ResourceNotFoundError,
       DuplicateEntryError,
       ValidationError
   )

   fgt = FortiOS(host='192.168.1.99', token='your-token')

   try:
       result = fgt.api.cmdb.firewall.address.create(
           name='test-server',
           subnet='10.0.0.1/32'
       )
   except DuplicateEntryError:
       print("Address already exists!")
   except ValidationError as e:
       print(f"Invalid input: {e.message}")
   except ResourceNotFoundError as e:
       print(f"Resource not found: {e.message}")
   except APIError as e:
       print(f"API error: {e.message} (code: {e.error_code})")

Custom HTTP Client
^^^^^^^^^^^^^^^^^^

Advanced users can extend the base HTTP client:

.. code-block:: python

   from hfortix_core.http.client import HTTPClient

   class CustomHTTPClient(HTTPClient):
       def __init__(self, *args, custom_header='value', **kwargs):
           super().__init__(*args, **kwargs)
           # Add custom initialization
           self.default_headers['X-Custom-Header'] = custom_header

See Also
--------

- :doc:`fortios` - FortiOS package that uses this core functionality
- :doc:`../user-guide/error-handling` - Error handling guide
- :doc:`../user-guide/async-usage` - Async usage guide
