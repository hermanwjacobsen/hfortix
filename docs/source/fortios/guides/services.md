# Service Management

Guide to managing custom services, service groups, and service categories.

## Overview

HFortix provides wrappers for three types of service objects:
- **Custom Services** - User-defined services
- **Service Groups** - Collections of services
- **Service Categories** - Service categorization

## Quick Examples

### Custom Service

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create custom TCP service
service = fgt.firewall.service_custom.create(
    name='custom-app',
    protocol='TCP',
    tcp_portrange='8080-8090',
    comment='Custom application service'
)

# Create UDP service
dns_service = fgt.firewall.service_custom.create(
    name='custom-dns',
    protocol='UDP',
    udp_portrange='5353',
    comment='Custom DNS service'
)
```

### Service Group

```python
# Create service group
web_services = fgt.firewall.service_group.create(
    name='web-services',
    member=['HTTP', 'HTTPS', 'custom-app'],
    comment='All web-related services'
)
```

### Service Category

```python
# Manage service categories
categories = fgt.firewall.service_category.list()
```

## Coming Soon

Detailed documentation including:
- Protocol types (TCP, UDP, ICMP, etc.)
- Port range configuration
- Service groups and nesting
- Integration with policies
- Cloning and templating
- Best practices

## Temporary Reference

For now, see:
- [Convenience Wrappers API Reference](/fortios/api-reference/convenience-wrappers.rst)
