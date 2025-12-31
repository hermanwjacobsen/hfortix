Schedule Management
===================

High-level wrappers for managing FortiOS schedules (recurring, one-time, and groups).

Overview
--------

Schedule wrappers provide an intuitive interface for creating and managing time-based
schedules used in firewall policies and other FortiOS features.

Schedule Types
--------------

FortiOS supports three types of schedules:

1. **Recurring Schedules** - Repeat on specific days/times (e.g., business hours)
2. **One-time Schedules** - Single time window (e.g., maintenance window)
3. **Schedule Groups** - Combine multiple schedules with OR logic

Schedule Recurring
------------------

Create schedules that repeat on specific days and times.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Create business hours schedule
   schedule = fgt.firewall.schedule_recurring.create(
       name='business-hours',
       day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
       start='08:00',
       end='18:00'
   )
   
   # Create weekend schedule
   weekend = fgt.firewall.schedule_recurring.create(
       name='weekends',
       day=['saturday', 'sunday'],
       start='00:00',
       end='23:59'
   )
   
   # Clone and modify
   extended = fgt.firewall.schedule_recurring.clone(
       name='business-hours',
       new_name='extended-hours',
       end='20:00'
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ScheduleRecurring
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Schedule Onetime
----------------

Create single-occurrence schedules for maintenance windows or special events.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   # Create one-time maintenance window
   maintenance = fgt.firewall.schedule_onetime.create(
       name='weekend-maintenance',
       start='2024-01-15 02:00',
       end='2024-01-15 06:00'
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ScheduleOnetime
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Schedule Group
--------------

Combine multiple schedules with OR logic.

Quick Start
^^^^^^^^^^^

.. code-block:: python

   # Create schedule group combining business hours and weekends
   group = fgt.firewall.schedule_group.create(
       name='business-and-weekends',
       member=['business-hours', 'weekends']
   )

API Reference
^^^^^^^^^^^^^

.. autoclass:: hfortix_fortios.firewall.ScheduleGroup
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

See Also
--------

- :doc:`/fortios/guides/schedules` - Complete schedule guide with examples
- :doc:`/fortios/api-reference/cmdb/firewall` - Low-level firewall API
- :doc:`/fortios/getting-started/quickstart` - Quick start guide
