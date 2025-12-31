# Filtering and Queries

Complete guide to filtering API results with 50+ examples.

```{note}
This content will be migrated from `docs/fortios/FILTERING_GUIDE.md`
```

## Overview

HFortix supports powerful filtering for list operations:
- Simple field filters
- Complex queries with logical operators
- Pattern matching
- Range queries

## Quick Examples

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Simple filter
addresses = fgt.api.cmdb.firewall.address.list(
    filter='name==web-server'
)

# Complex filter with AND
policies = fgt.api.cmdb.firewall.policy.list(
    filter='srcintf==port1&action==accept'
)

# OR operator
policies = fgt.api.cmdb.firewall.policy.list(
    filter='srcintf==port1|srcintf==port2'
)

# Contains
addresses = fgt.api.cmdb.firewall.address.list(
    filter='name=@server'
)

# Limit results
addresses = fgt.api.cmdb.firewall.address.list(
    filter='subnet=@192.168',
    count=10
)
```

## Coming Soon

Detailed documentation including:
- Filter syntax and operators
- 50+ filtering examples
- Performance considerations
- Log filtering
- Complex query patterns
- Best practices

## Temporary Reference

For now, see:
- Current docs: `docs/fortios/FILTERING_GUIDE.md` in repository
