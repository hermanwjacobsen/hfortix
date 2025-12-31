Firewall Policy
===============

High-level wrapper for managing FortiOS firewall policies.

Overview
--------

The firewall policy wrapper provides an intuitive interface for managing firewall policies
with all 150+ policy parameters supported. It handles complex field transformations and
provides helpful methods like ``exists()``, ``clone()``, and ``get_by_name()``.

Quick Start
-----------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create a policy
   policy = fgt.firewall.policy.create(
       name='Allow-Web-Traffic',
       srcintf=['port1'],
       dstintf=['port2'],
       srcaddr=['internal-network'],
       dstaddr=['web-server'],
       service=['HTTP', 'HTTPS'],
       action='accept',
       schedule='always',
       nat=True
   )
   
   # List all policies
   policies = fgt.firewall.policy.get()
   
   # Get specific policy
   policy = fgt.firewall.policy.get(policyid=1)
   
   # Check if policy exists
   exists = fgt.firewall.policy.exists(policyid=1)
   
   # Get policy by name
   policy = fgt.firewall.policy.get_by_name('Allow-Web-Traffic')
   
   # Clone policy
   new_policy = fgt.firewall.policy.clone(
       policyid=1,
       new_name='Allow-Web-Traffic-Copy'
   )
   
   # Update policy
   fgt.firewall.policy.update(
       policyid=1,
       comments='Updated policy'
   )
   
   # Delete policy
   fgt.firewall.policy.delete(policyid=1)

API Reference
-------------

.. autoclass:: hfortix_fortios.firewall.FirewallPolicy
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Available Methods
-----------------

High-Level Methods
^^^^^^^^^^^^^^^^^^

- ``get()`` - Retrieve all firewall policies (no parameters) or a specific policy by ID (with policyid parameter)
- ``create(**params)`` - Create a new policy
- ``update(policyid, **params)`` - Update an existing policy
- ``delete(policyid)`` - Delete a policy

Helper Methods
^^^^^^^^^^^^^^

- ``exists(policyid)`` - Check if a policy exists
- ``get_by_name(name)`` - Find policy by name
- ``clone(policyid, new_name, **overrides)`` - Clone and modify a policy

See Also
--------

- :doc:`/fortios/guides/firewall-policies` - Complete guide with examples
- :doc:`/fortios/api-reference/cmdb/firewall` - Low-level firewall API
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
