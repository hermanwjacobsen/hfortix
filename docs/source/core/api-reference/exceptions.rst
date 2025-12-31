Exception Hierarchy
===================

All HFortix exceptions inherit from ``FortinetError``.

Exception Classes
-----------------

.. automodule:: hfortix_core.exceptions
   :members:
   :undoc-members:
   :show-inheritance:
   :member-order: bysource

Exception Hierarchy
-------------------

.. code-block:: text

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

Usage Examples
--------------

Basic Exception Handling
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS
   from hfortix_core import (
       APIError,
       ResourceNotFoundError,
       DuplicateEntryError
   )

   fgt = FortiOS(host='192.168.1.99', token='your-token')

   try:
       fgt.api.cmdb.firewall.address.create(
           name='test-server',
           subnet='10.0.0.1/32'
       )
   except DuplicateEntryError:
       print("Address already exists!")
   except ValidationError as e:
       print(f"Invalid input: {e.message}")
   except APIError as e:
       print(f"API error: {e.message}")

Specific HTTP Errors
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_core import (
       ResourceNotFoundError,
       UnauthorizedError,
       ForbiddenError
   )

   try:
       result = fgt.api.cmdb.firewall.address.get(name='missing')
   except ResourceNotFoundError:
       print("Address not found")
   except UnauthorizedError:
       print("Invalid credentials")
   except ForbiddenError:
       print("Insufficient permissions")

FortiOS-Specific Errors
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_core import DuplicateEntryError, EntryInUseError

   # Handle duplicate entries
   try:
       fgt.api.cmdb.firewall.address.create(name='existing', ...)
   except DuplicateEntryError:
       # Update instead
       fgt.api.cmdb.firewall.address.update(name='existing', ...)

   # Handle in-use objects
   try:
       fgt.api.cmdb.firewall.address.delete(name='in-use-address')
   except EntryInUseError as e:
       print(f"Cannot delete: {e.message}")
       print("Remove from policies first")

Connection and Timeout Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_core import ConnectionError, TimeoutError

   try:
       fgt = FortiOS(
           host='unreachable-host',
           token='token',
           connect_timeout=5.0
       )
       result = fgt.api.monitor.system.status.get()
   except ConnectionError:
       print("Cannot connect to FortiGate")
   except TimeoutError:
       print("Request timed out")

Error Attributes
----------------

All exceptions include helpful attributes:

.. code-block:: python

   try:
       result = fgt.api.cmdb.firewall.address.create(...)
   except APIError as e:
       print(f"Message: {e.message}")
       print(f"Error Code: {e.error_code}")
       print(f"HTTP Status: {e.http_status}")
       print(f"Details: {e.details}")

See Also
--------

- :doc:`../user-guide/error-handling` - Comprehensive error handling guide
- :doc:`client` - FortiOS client reference
- :doc:`core` - Core package reference
