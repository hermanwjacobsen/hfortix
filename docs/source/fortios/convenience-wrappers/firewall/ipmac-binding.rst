IP/MAC Binding
==============

High-level wrappers for managing FortiOS IP/MAC binding settings and tables.

Overview
--------

IP/MAC binding wrappers provide an intuitive interface for controlling network access
based on MAC addresses and managing IP/MAC binding tables.

Binding Types
-------------

FortiOS provides two components for IP/MAC binding:

1. **IP/MAC Binding Settings** - Global configuration for IP/MAC binding
2. **IP/MAC Binding Table** - Specific IP/MAC address associations

IP/MAC Binding Setting
----------------------

Configure global IP/MAC binding settings.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Configure IP/MAC binding settings
   setting = fgt.firewall.ipmac_binding_setting.create(
       bindthroughfw='enable',
       bindtofw='enable',
       undefinedhost='block'
   )
   
   # Update settings
   fgt.firewall.ipmac_binding_setting.update(
       undefinedhost='allow'
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.IPMACBindingSetting
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

IP/MAC Binding Table
--------------------

Manage specific IP/MAC address bindings.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   # Add IP/MAC binding
   binding = fgt.firewall.ipmac_binding_table.create(
       ip='10.0.0.100',
       mac='00:11:22:33:44:55',
       name='workstation-01',
       status='enable'
   )
   
   # List all bindings
   bindings = fgt.firewall.ipmac_binding_table.list()
   
   # Get specific binding
   binding = fgt.firewall.ipmac_binding_table.get(seq_num=1)
   
   # Update binding
   fgt.firewall.ipmac_binding_table.update(
       seq_num=1,
       name='workstation-01-updated'
   )
   
   # Delete binding
   fgt.firewall.ipmac_binding_table.delete(seq_num=1)

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.IPMACBindingTable
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

See Also
--------

- :doc:`/fortios/guides/ipmac-binding` - Complete IP/MAC binding guide with examples
- :doc:`/fortios/api-reference/cmdb/firewall` - Low-level firewall API
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
