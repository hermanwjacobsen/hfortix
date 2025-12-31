# Performance Testing and Optimization

Guide to performance testing and optimizing HFortix for your FortiGate device.

```{note}
This content will be migrated from `docs/fortios/PERFORMANCE_TESTING.md`
```

## Overview

HFortix includes built-in performance testing to determine optimal settings for your FortiGate device.

## Quick Start

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Run performance test
results = fgt.api.utils.performance_test()

print(f"Optimal settings for your device:")
print(f"  max_connections: {results['recommended']['max_connections']}")
print(f"  max_keepalive: {results['recommended']['max_keepalive']}")

# Create optimized client
fgt_optimized = FortiOS(
    host='192.168.1.99',
    token='token',
    max_connections=results['recommended']['max_connections'],
    max_keepalive_connections=results['recommended']['max_keepalive']
)
```

## Configuration Options

### Connection Pool Settings

```python
# Conservative (default)
fgt = FortiOS(
    host='192.168.1.99',
    token='token',
    max_connections=10,
    max_keepalive_connections=5
)

# High-performance (after testing)
fgt = FortiOS(
    host='192.168.1.99',
    token='token',
    max_connections=60,
    max_keepalive_connections=30
)
```

### Timeout Settings

```python
# For slow/unreliable networks
fgt = FortiOS(
    host='remote-site.company.com',
    token='token',
    connect_timeout=30.0,  # 30 seconds to connect
    read_timeout=600.0     # 10 minutes to read
)

# For fast local networks
fgt = FortiOS(
    host='192.168.1.99',
    token='token',
    connect_timeout=5.0,   # 5 seconds
    read_timeout=60.0      # 1 minute
)
```

## Coming Soon

Detailed documentation including:
- Performance testing methodology
- Interpreting test results
- Optimization strategies
- Device-specific recommendations
- Concurrent operations
- Best practices

## Temporary Reference

For now, see:
- Current docs: `docs/fortios/PERFORMANCE_TESTING.md` in repository
