HTTP Client
===========

The HTTP client provides both synchronous and asynchronous interfaces for making requests to Fortinet APIs.

.. currentmodule:: hfortix_core.http

HTTPClient
----------

.. autoclass:: client.HTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__

Base Client
-----------

.. autoclass:: base.BaseHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

Async Client
------------

.. autoclass:: async_client.AsyncHTTPClient
   :members:
   :undoc-members:
   :show-inheritance:

   .. automethod:: __init__

Client Interface
----------------

.. autoclass:: interface.HTTPClientInterface
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Synchronous Client
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_core.http import HTTPClient

   # Create client
   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="your-api-token",
       verify_ssl=True,
       timeout=30
   )

   try:
       # Make GET request
       response = client.get("/api/v2/monitor/system/status")
       print(response)

       # Make POST request
       data = {"name": "test", "subnet": "10.0.1.0/24"}
       response = client.post("/api/v2/cmdb/firewall/address", json=data)
       
   finally:
       client.close()

Context Manager
^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_core.http import HTTPClient

   with HTTPClient(base_url="https://192.168.1.99", token="token") as client:
       response = client.get("/api/v2/monitor/system/status")
       print(response)

Async Client
^^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from hfortix_core.http import AsyncHTTPClient

   async def main():
       async with AsyncHTTPClient(
           base_url="https://192.168.1.99",
           token="your-token"
       ) as client:
           response = await client.get("/api/v2/monitor/system/status")
           print(response)

   asyncio.run(main())

Configuration
-------------

Connection Pooling
^^^^^^^^^^^^^^^^^^

The HTTP client uses connection pooling for improved performance:

.. code-block:: python

   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       max_connections=100,  # Max total connections
       max_keepalive=20      # Max keepalive connections
   )

Timeouts
^^^^^^^^

Configure request timeouts:

.. code-block:: python

   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       timeout=30,           # Default timeout in seconds
       connect_timeout=10    # Connection timeout
   )

SSL/TLS
^^^^^^^

Control SSL verification:

.. code-block:: python

   # Verify SSL (production)
   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       verify_ssl=True
   )

   # Disable SSL verification (testing only)
   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       verify_ssl=False
   )

   # Custom CA bundle
   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       verify_ssl="/path/to/ca-bundle.crt"
   )

Retry Logic
^^^^^^^^^^^

Built-in retry with exponential backoff:

.. code-block:: python

   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       max_retries=3,           # Number of retries
       retry_backoff_factor=2.0 # Exponential backoff factor
   )

Advanced Features
-----------------

Circuit Breaker
^^^^^^^^^^^^^^^

Automatic circuit breaker for fault tolerance:

.. code-block:: python

   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       circuit_breaker_threshold=5,  # Failures before opening
       circuit_breaker_timeout=60     # Seconds before retry
   )

Request Hooks
^^^^^^^^^^^^^

Add hooks for logging or debugging:

.. code-block:: python

   def log_request(request):
       print(f"Request: {request.method} {request.url}")

   def log_response(response):
       print(f"Response: {response.status_code}")

   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       request_hooks=[log_request],
       response_hooks=[log_response]
   )

Custom Headers
^^^^^^^^^^^^^^

Add custom headers to all requests:

.. code-block:: python

   client = HTTPClient(
       base_url="https://192.168.1.99",
       token="token",
       headers={
           "X-Custom-Header": "value",
           "User-Agent": "MyApp/1.0"
       }
   )

See Also
--------

- :doc:`/core/api-reference/exceptions` - Exception handling
- :doc:`/core/index` - Core package overview
