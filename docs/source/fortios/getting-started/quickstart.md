# Quick Start Guide

Get up and running with HFortix in 5 minutes.

## Prerequisites

Before you begin, ensure you have:

1. Python 3.10 or higher installed
2. A FortiGate device with FortiOS 6.0+ and REST API enabled
3. An API token (see [Authentication](/fortios/getting-started/authentication.md) for setup)

## Installation

Install HFortix from PyPI:

```bash
pip install hfortix[fortios]
```

## Your First Script

Create a file named `test_hfortix.py`:

```python
from hfortix import FortiOS, APIError

# Initialize the client
fgt = FortiOS(
    host='192.168.1.99',           # Your FortiGate IP/hostname
    token='your-api-token-here',   # Your API token
    verify=False                   # Use True in production with valid SSL cert
)

# List all firewall addresses
try:
    addresses = fgt.api.cmdb.firewall.address.get()
    print(f"Found {len(addresses)} firewall addresses")
    
    # Display first few addresses
    for addr in addresses[:5]:
        print(f"  - {addr['name']}: {addr.get('subnet', 'N/A')}")
        
except APIError as e:
    print(f"Error: {e.message} (Code: {e.error_code})")
```

Run it:

```bash
python test_hfortix.py
```

## Common Operations

### List Resources

```python
# List firewall addresses
addresses = fgt.api.cmdb.firewall.address.get()

# List firewall policies
policies = fgt.api.cmdb.firewall.policy.get()

# List configured interfaces
interfaces = fgt.api.cmdb.system.interface.get()
```

### Create a Resource

```python
# Create a firewall address
result = fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.0.2.100/32',
    comment='Production web server'
)

print(f"Created: {result}")
```

### Update a Resource

```python
# Update the address
result = fgt.api.cmdb.firewall.address.update(
    name='web-server',
    comment='Updated web server address'
)
```

### Delete a Resource

```python
# Delete the address
result = fgt.api.cmdb.firewall.address.delete(name='web-server')
print("Address deleted successfully")
```

## Using Convenience Wrappers

HFortix provides high-level wrappers for common tasks:

```python
# Create a firewall policy (simplified)
policy = fgt.firewall.policy.create(
    name='Allow-Web-Traffic',
    srcintf=['port1'],
    dstintf=['port2'],
    srcaddr=['all'],
    dstaddr=['web-server'],
    service=['HTTP', 'HTTPS'],
    action='accept',
    nat=True
)

# Create a schedule
schedule = fgt.firewall.schedule_recurring.create(
    name='business-hours',
    day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
    start='08:00',
    end='18:00'
)

# Create a custom service
service = fgt.firewall.service_custom.create(
    name='custom-app',
    protocol='TCP',
    tcp_portrange='8080-8090',
    comment='Custom application service'
)
```

## Dual-Pattern Interface

HFortix supports both dictionary and keyword-based syntax:

```python
# Method 1: Keyword arguments (recommended for readability)
fgt.api.cmdb.firewall.address.create(
    name='server-1',
    subnet='10.0.1.100/32',
    comment='Server'
)

# Method 2: Dictionary (good for templates/configs)
config = {
    'name': 'server-1',
    'subnet': '10.0.1.100/32',
    'comment': 'Server'
}
fgt.api.cmdb.firewall.address.create(data_dict=config)

# Method 3: Mixed (template + overrides)
base_config = load_from_file('template.json')
fgt.api.cmdb.firewall.address.create(
    data_dict=base_config,
    name='server-2',  # Override template value
    comment='Custom comment'
)
```

## Error Handling

Always wrap API calls in try-except blocks:

```python
from hfortix import (
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError,
    EntryInUseError
)

try:
    result = fgt.api.cmdb.firewall.address.create(
        name='test-addr',
        subnet='10.0.0.1/32'
    )
except DuplicateEntryError:
    print("Address already exists!")
except APIError as e:
    print(f"API Error: {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Optimization

For high-performance scenarios, run a performance test first:

```python
# Run performance test to get optimal settings
results = fgt.api.utils.performance_test()

# Create optimized client with recommended settings
fgt_optimized = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    max_connections=results['recommended']['max_connections'],
    max_keepalive_connections=results['recommended']['max_keepalive']
)
```

## Monitoring

Access real-time monitoring data:

```python
# Get system status
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}")
print(f"Version: {status['version']}")

# Get firewall policy statistics
stats = fgt.api.monitor.firewall.policy.get()

# Get active sessions
sessions = fgt.api.monitor.firewall.session.get()
```

## What's Next?

Now that you're up and running, explore more:

- **[User Guide](/fortios/user-guide/fortios-overview.md)** - Comprehensive documentation
- **[Error Handling](/fortios/user-guide/error-handling.md)** - Advanced error handling patterns
- **[Validation](/fortios/user-guide/validation.md)** - Input validation
- **[Examples](/fortios/examples/index.md)** - More code examples
- **[API Reference](/fortios/api-reference/index.rst)** - Complete API documentation

## Getting Help

- **GitHub Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **Documentation**: https://hfortix.readthedocs.io/
- **Examples**: Check the `examples/` directory in the repository
