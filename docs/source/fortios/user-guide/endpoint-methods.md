# Endpoint Methods

Understanding the difference between convenience wrapper methods and low-level API endpoint methods.

```{note}
**TL;DR**: Use **convenience wrappers** (``list()``, ``create()``, etc.) for common tasks. 
Use **API endpoints** (``.get()``, ``.post()``, etc.) when you need direct API access.
```

## Two Approaches to the FortiOS API

HFortix provides two ways to interact with FortiOS:

### 1. Convenience Wrappers (High-Level, Recommended)

Object-oriented wrappers with intuitive methods:

- ``list()`` - Retrieve all resources
- ``get()`` - Retrieve a specific resource
- ``create()`` - Create a new resource
- ``update()`` - Update an existing resource
- ``delete()`` - Delete a resource
- Plus helpers: ``exists()``, ``clone()``, ``get_by_name()``

**Example:**

```python
fgt = FortiOS(host='192.168.1.99', token='token')

# High-level wrapper methods - simple and intuitive
policies = fgt.firewall.policy.list()
policy = fgt.firewall.policy.get(policyid=1)
fgt.firewall.policy.create(name='Allow-Web', srcintf=['port1'], ...)
fgt.firewall.policy.update(policyid=1, comments='Updated')
fgt.firewall.policy.delete(policyid=1)
```

### 2. API Endpoints (Low-Level)

Direct HTTP method access to the FortiOS REST API:

- ``.get()`` - HTTP GET request
- ``.post()`` - HTTP POST request
- ``.put()`` - HTTP PUT request
- ``.delete()`` - HTTP DELETE request

**Example:**

```python
fgt = FortiOS(host='192.168.1.99', token='token')

# Low-level API methods - direct HTTP access
policies = fgt.api.cmdb.firewall.policy.get()
policy = fgt.api.cmdb.firewall.policy.get(mkey=1)
fgt.api.cmdb.firewall.policy.post(json={...})
fgt.api.cmdb.firewall.policy.put(mkey=1, json={...})
fgt.api.cmdb.firewall.policy.delete(mkey=1)
```

## When to Use Each

### Use Convenience Wrappers When:

- ✅ Creating firewall policies, schedules, services, shapers
- ✅ You want simple, readable code
- ✅ You need helper methods (``exists()``, ``clone()``, ``get_by_name()``)
- ✅ You're new to FortiOS API
- ✅ Field transformation is needed (e.g., ``srcintf=['port1']`` → ``[{'name': 'port1'}]``)

### Use API Endpoints When:

- ✅ Working with endpoints that don't have wrappers
- ✅ You need complete control over the API request
- ✅ Accessing monitor or log APIs
- ✅ Using advanced filtering or parameters
- ✅ Building custom automation tools

## Method Comparison

### Convenience Wrapper Methods

```python
# List all resources
resources = fgt.firewall.policy.list()

# Get specific resource
resource = fgt.firewall.policy.get(policyid=1)

# Create resource
resource = fgt.firewall.policy.create(
    name='test',
    srcintf=['port1'],
    dstintf=['port2'],
    ...
)

# Update resource
fgt.firewall.policy.update(policyid=1, comments='Updated')

# Delete resource
fgt.firewall.policy.delete(policyid=1)

# Helper methods
exists = fgt.firewall.policy.exists(policyid=1)
policy = fgt.firewall.policy.get_by_name('test')
cloned = fgt.firewall.policy.clone(policyid=1, new_name='test2')
```

### API Endpoint Methods

```python
# HTTP GET - retrieve all
response = fgt.api.cmdb.firewall.policy.get()

# HTTP GET - retrieve specific (using mkey parameter)
response = fgt.api.cmdb.firewall.policy.get(mkey=1)

# HTTP POST - create
response = fgt.api.cmdb.firewall.policy.post(
    json={
        'name': 'test',
        'srcintf': [{'name': 'port1'}],
        'dstintf': [{'name': 'port2'}],
        ...
    }
)

# HTTP PUT - update
response = fgt.api.cmdb.firewall.policy.put(
    mkey=1,
    json={'comments': 'Updated'}
)

# HTTP DELETE - delete
response = fgt.api.cmdb.firewall.policy.delete(mkey=1)
```

## Key Differences

| Feature | Convenience Wrappers | API Endpoints |
|---------|---------------------|---------------|
| **Method Names** | ``list()``, ``get()``, ``create()``, ``update()``, ``delete()`` | ``.get()``, ``.post()``, ``.put()``, ``.delete()`` |
| **ID Parameter** | ``policyid=1``, ``name='test'`` | ``mkey=1`` |
| **Field Format** | Simple: ``srcintf=['port1']`` | API format: ``srcintf=[{'name': 'port1'}]`` |
| **Helper Methods** | ``exists()``, ``clone()``, ``get_by_name()`` | Not available |
| **Coverage** | Common objects (policies, schedules, services) | All 750+ endpoints |
| **Ease of Use** | ⭐⭐⭐⭐⭐ Beginner-friendly | ⭐⭐⭐ Requires API knowledge |

## Available Convenience Wrappers

- **Firewall Policy** - ``fgt.firewall.policy.*``
- **Schedule Recurring** - ``fgt.firewall.schedule_recurring.*``
- **Schedule Onetime** - ``fgt.firewall.schedule_onetime.*``
- **Schedule Group** - ``fgt.firewall.schedule_group.*``
- **Service Custom** - ``fgt.firewall.service_custom.*``
- **Service Group** - ``fgt.firewall.service_group.*``
- **Service Category** - ``fgt.firewall.service_category.*``
- **Traffic Shaper** - ``fgt.firewall.traffic_shaper.*``
- **Per-IP Shaper** - ``fgt.firewall.shaper_per_ip.*``
- **IP/MAC Binding Setting** - ``fgt.firewall.ipmac_binding_setting.*``
- **IP/MAC Binding Table** - ``fgt.firewall.ipmac_binding_table.*``

See :doc:`/fortios/convenience-wrappers/index` for complete documentation.

## See Also

- [Convenience Wrappers](/fortios/convenience-wrappers/index.rst) - High-level wrapper documentation
- [API Reference](/fortios/api-reference/index.rst) - Low-level API endpoint documentation
- [Quick Start Guide](/fortios/getting-started/quickstart.md) - Getting started tutorial
