Service Management
==================

High-level wrappers for managing FortiOS services (custom services, groups, and categories).

Overview
--------

Service wrappers provide an intuitive interface for creating and managing network services
used in firewall policies for traffic matching.

Service Types
-------------

FortiOS supports three types of services:

1. **Custom Services** - Define specific protocols and ports
2. **Service Groups** - Combine multiple services
3. **Service Categories** - Predefined service categories

Service Custom
--------------

Create custom network services with specific protocols and ports.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create TCP service
   web_service = fgt.firewall.service_custom.create(
       name='Custom-Web',
       protocol='TCP/UDP/SCTP',
       tcp_portrange='8080-8090',
       udp_portrange='8080-8090'
   )
   
   # Create ICMP service
   ping = fgt.firewall.service_custom.create(
       name='Custom-Ping',
       protocol='ICMP',
       icmptype=8,
       icmpcode=0
   )
   
   # List all custom services
   services = fgt.firewall.service_custom.list()
   
   # Clone and modify
   new_service = fgt.firewall.service_custom.clone(
       name='Custom-Web',
       new_name='Custom-Web-Alt',
       tcp_portrange='9080-9090'
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ServiceCustom
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Service Group
-------------

Combine multiple services into logical groups.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   # Create service group
   web_services = fgt.firewall.service_group.create(
       name='Web-Services',
       member=['HTTP', 'HTTPS', 'Custom-Web']
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ServiceGroup
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Service Category
----------------

Manage service categories for grouping related services.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   # Create service category
   category = fgt.firewall.service_category.create(
       name='Business-Apps',
       comment='Business application services'
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ServiceCategory
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

See Also
--------

- :doc:`/fortios/guides/services` - Complete service guide with examples
- :doc:`/fortios/api-reference/cmdb/firewall` - Low-level firewall API
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
