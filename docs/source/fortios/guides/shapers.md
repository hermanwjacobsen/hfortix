# Traffic Shaping

Guide to traffic shaping with per-IP shapers and traffic shapers.

```{note}
This content will be migrated from `docs/fortios/wrappers/SHAPER_WRAPPERS.md`
```

## Overview

HFortix provides wrappers for two types of traffic shapers:
- **Traffic Shaper** - Shared bandwidth pools
- **Per-IP Shaper** - Per-user/IP bandwidth limits

## Quick Examples

### Traffic Shaper

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create shared bandwidth pool
shaper = fgt.firewall.traffic_shaper.create(
    name='shared-pool',
    guaranteed_bandwidth=50000,  # 50 Mbps guaranteed
    maximum_bandwidth=100000      # 100 Mbps maximum
)
```

### Per-IP Shaper

```python
# Create per-user bandwidth limit
user_limit = fgt.firewall.shaper_per_ip.create(
    name='user-bandwidth-limit',
    max_bandwidth=10000,          # 10 Mbps per user
    max_concurrent_session=100
)
```

## Coming Soon

Detailed documentation including:
- Traffic shaper types
- Bandwidth configuration
- Guaranteed vs maximum bandwidth
- Concurrent session limits
- Integration with policies
- Best practices

## Temporary Reference

For now, see:
- [Convenience Wrappers API Reference](../api-reference/convenience-wrappers.rst)
- Current docs: `docs/fortios/wrappers/SHAPER_WRAPPERS.md` in repository
