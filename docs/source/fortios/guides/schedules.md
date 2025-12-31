# Schedule Management

Guide to managing schedules (recurring, onetime, and groups).

```{note}
This content will be migrated from `docs/fortios/wrappers/SCHEDULE_WRAPPERS.md`
```

## Overview

HFortix provides wrappers for three types of schedules:
- **Recurring** - Regular schedules (daily, weekly)
- **Onetime** - Single occurrence schedules
- **Groups** - Collections of schedules

## Quick Examples

### Recurring Schedule

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Business hours schedule
schedule = fgt.firewall.schedule_recurring.create(
    name='business-hours',
    day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
    start='08:00',
    end='18:00'
)

# Clone and modify
extended = fgt.firewall.schedule_recurring.clone(
    name='business-hours',
    new_name='extended-hours',
    end='20:00'
)
```

### Onetime Schedule

```python
# Maintenance window
maintenance = fgt.firewall.schedule_onetime.create(
    name='maintenance-window',
    start='2025-12-31 22:00',
    end='2026-01-01 02:00'
)
```

### Schedule Group

```python
# Group multiple schedules
group = fgt.firewall.schedule_group.create(
    name='all-business-hours',
    member=['business-hours', 'extended-hours']
)
```

## Coming Soon

Detailed documentation including:
- All schedule types
- Day and time configurations
- Schedule groups
- Cloning and templating
- Integration with policies
- Best practices

## Temporary Reference

For now, see:
- [Convenience Wrappers API Reference](../api-reference/convenience-wrappers.rst)
- Current docs: `docs/fortios/wrappers/SCHEDULE_WRAPPERS.md` in repository
