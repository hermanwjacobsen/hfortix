# Firewall Policy Management

Complete guide to managing firewall policies using the convenience wrapper.

```{note}
This content will be migrated from `docs/fortios/wrappers/FIREWALL_POLICY_WRAPPER.md`
```

## Overview

The firewall policy wrapper provides simplified syntax for managing FortiGate firewall policies with support for 150+ parameters.

## Quick Example

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create firewall policy
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

# Check if policy exists
if fgt.firewall.policy.exists(policyid='1'):
    print("Policy exists!")

# Clone policy
new_policy = fgt.firewall.policy.clone(
    policyid='1',
    new_name='Allow-Web-Traffic-Copy'
)
```

## Coming Soon

Detailed documentation including:
- All policy parameters
- Address and service object integration
- NAT configuration
- Policy ordering and priorities
- Cloning and templating
- Best practices

## Temporary Reference

For now, see:
- [Convenience Wrappers API Reference](/fortios/api-reference/convenience-wrappers.rst)
- Current docs: `docs/fortios/wrappers/FIREWALL_POLICY_WRAPPER.md` in repository
