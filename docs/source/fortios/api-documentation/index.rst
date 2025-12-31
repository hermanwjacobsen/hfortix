API Documentation
=================

Complete API documentation for FortiOS including high-level convenience wrappers and low-level endpoint reference.

Choose Your Interface
---------------------

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: 🎯 Convenience Wrappers
        :link: convenience-wrappers
        :link-type: doc

        **Start here!** High-level wrappers with intuitive methods.
        
        Use ``get()``, ``create()``, ``update()``, ``delete()``

    .. grid-item-card:: 📚 API Reference
        :link: api-reference
        :link-type: doc

        Low-level endpoint documentation (750+ endpoints).
        
        Direct HTTP methods: GET, POST, PUT, DELETE

Quick Comparison
----------------

**Convenience Wrappers** - High-level, Pythonic interface:

.. code-block:: python

   # Simple and intuitive
   fgt.firewall.policy.create(
       name='Allow-Web',
       srcintf=['port1'],
       dstintf=['port2'],
       service=['HTTP', 'HTTPS'],
       action='accept'
   )

**API Reference** - Low-level, direct API access:

.. code-block:: python

   # More control, requires API knowledge
   fgt.api.cmdb.firewall.policy.post(
       json={
           'name': 'Allow-Web',
           'srcintf': [{'name': 'port1'}],
           'dstintf': [{'name': 'port2'}],
           'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
           'action': 'accept'
       }
   )

Documentation Sections
----------------------

.. toctree::
   :maxdepth: 2

   convenience-wrappers
   api-reference

Convenience Wrappers
--------------------

High-level wrappers for common operations:

- **Firewall Policies** - Create, update, delete policies with validation
- **Schedules** - One-time, recurring, and group schedules
- **Services** - Custom services and service groups
- **Traffic Shapers** - Bandwidth control and QoS
- **IP/MAC Binding** - Static IP-MAC assignments

See :doc:`convenience-wrappers` for detailed documentation.

API Reference
-------------

Complete endpoint documentation organized by category:

- **CMDB API** - 37 configuration categories (500+ endpoints)
- **Monitor API** - 32 status/statistics categories (200+ endpoints)
- **Log API** - 5 log categories
- **Service API** - 3 service categories (21 methods)

See :doc:`api-reference` for complete endpoint documentation.
