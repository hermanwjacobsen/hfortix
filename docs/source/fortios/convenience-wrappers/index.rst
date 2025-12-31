Convenience Wrappers
====================

High-level wrappers that simplify common FortiOS operations with intuitive methods
like ``get()``, ``create()``, ``update()``, and ``delete()``.

Overview
--------

Convenience wrappers are accessed through the ``firewall`` namespace and provide
object-oriented interfaces for common FortiOS configuration tasks:

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Use high-level wrapper methods
   fgt.firewall.policy.get()           # List all policies
   fgt.firewall.policy.get(policyid=1)  # Get specific policy
   fgt.firewall.policy.create(...)      # Create new policy
   fgt.firewall.policy.update(...)      # Update existing policy
   fgt.firewall.policy.delete(...)      # Delete policy

Firewall & Objects
------------------

.. toctree::
   :maxdepth: 1

   firewall/policy
   firewall/schedule
   firewall/service
   firewall/shaper
   firewall/ipmac-binding

Wrapper vs API Methods
----------------------

**Convenience Wrapper Methods** (High-level, recommended):

- ``get()`` - Retrieve all resources (when called without parameters) or a specific resource (with ID parameter)
- ``create()`` - Create a new resource
- ``update()`` - Update an existing resource
- ``delete()`` - Delete a resource
- Plus helper methods like ``exists()``, ``clone()``, ``get_by_name()``

**API Endpoint Methods** (Low-level):

- ``.get()`` - HTTP GET request
- ``.post()`` - HTTP POST request
- ``.put()`` - HTTP PUT request
- ``.delete()`` - HTTP DELETE request

**When to use each:**

- **Use convenience wrappers** for common tasks (creating policies, schedules, services)
- **Use API endpoints** when you need direct API access or endpoints without wrappers

Example Comparison
------------------

**Using Convenience Wrapper** (Recommended):

.. code-block:: python

   # Simple, intuitive
   policy = fgt.firewall.policy.create(
       name='Allow-Web',
       srcintf=['port1'],
       dstintf=['port2'],
       srcaddr=['all'],
       dstaddr=['all'],
       service=['HTTP', 'HTTPS'],
       action='accept'
   )

**Using API Endpoint** (Low-level):

.. code-block:: python

   # More complex, requires knowing API structure
   policy = fgt.api.cmdb.firewall.policy.post(
       json={
           'name': 'Allow-Web',
           'srcintf': [{'name': 'port1'}],
           'dstintf': [{'name': 'port2'}],
           'srcaddr': [{'name': 'all'}],
           'dstaddr': [{'name': 'all'}],
           'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
           'action': 'accept'
       }
   )

See Also
--------

- :doc:`/fortios/getting-started/quickstart` - Quick start guide
- :doc:`/fortios/api-reference/index` - Low-level API reference
- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide
