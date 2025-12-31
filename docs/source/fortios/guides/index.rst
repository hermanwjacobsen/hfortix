Topic Guides
============

In-depth guides for specific features and use cases.

.. toctree::
   :maxdepth: 2
   :caption: Convenience Wrappers

   firewall-policies
   schedules
   shapers
   services
   ipmac-binding

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics

   filtering
   validation
   performance

Overview
--------

Topic guides provide detailed, task-oriented documentation for specific features:

Convenience Wrapper Guides
---------------------------

**Firewall Policies**
   Complete guide to managing firewall policies using the high-level wrapper.
   Covers creation, updates, cloning, and all 150+ policy parameters.

**Schedules**
   Guide to schedule management including recurring schedules, one-time schedules,
   and schedule groups. Includes examples for business hours, maintenance windows, etc.

**Traffic Shapers**
   Guide to traffic shaping with per-IP shapers and traffic shapers. Covers bandwidth
   limits, concurrent sessions, and traffic management.

**Services**
   Guide to managing custom services, service groups, and service categories for
   firewall policy matching.

**IP/MAC Binding**
   Guide to IP/MAC binding settings and table management for controlling network
   access based on MAC addresses.

Advanced Topics
---------------

**Filtering**
   Complete guide to filtering and querying API results. 50+ examples covering
   simple filters, complex queries, logical operators, and performance optimization.

**Validation**
   Guide to the validation framework with 832 auto-generated validators. Covers
   enum validation, length limits, range checks, pattern matching, and type validation.

**Performance**
   Performance testing guide and optimization strategies. Includes connection pool
   tuning, timeout configuration, and device-specific recommendations.

See Also
--------

- :doc:`../user-guide/index` - Core concepts and essential features
- :doc:`../api-reference/convenience-wrappers` - API reference for wrappers
- :doc:`../examples/index` - Practical code examples
