# Performance Testing Guide

## Quick Start

Test your FortiGate's performance and get optimal configuration recommendations using the **built-in performance testing function**.

### Method 1: Built-in API Method (Recommended)

Performance testing is now a **built-in function** accessible directly from any FortiOS instance:

```python
from hfortix import FortiOS

# Initialize your client
fgt = FortiOS("192.168.1.99", token="your_token", verify=False)

# Run built-in performance test
results = fgt.api.utils.performance_test()

# Results automatically printed with:
# - Connection pool validation
# - Endpoint performance metrics
# - Device profile identification
# - Recommended settings
```

### Method 2: Standalone Function (Alternative)

For testing without an existing client instance:

```python
from hfortix.FortiOS.performance_test import quick_test

# One-liner performance test
results = quick_test(
    host="192.168.1.99",
    token="your_token",
    verify=False
)
```

### Method 3: Command Line (Alternative)

```bash
python -m hfortix.FortiOS.performance_test 192.168.1.99 your_token
```

## Running Performance Tests

### Option 1: Built-in Method (Recommended)

Use the built-in `performance_test()` method on any FortiOS instance:

```python
from hfortix import FortiOS

# Initialize client
fgt = FortiOS("fw.example.com", token="your_token", verify=True)

# Run quick test (validation + endpoints) using built-in function
results = fgt.api.utils.performance_test(
    test_validation=True,
    test_endpoints=True,
    sequential_count=10,
)

# Results automatically printed
# OR access programmatically:
print(f"Device profile: {results.device_profile}")
print(f"Throughput: {results.sequential_throughput:.2f} req/s")
print(f"Recommended settings: {results.recommended_settings}")

# Test specific endpoints
results = fgt.api.utils.performance_test(
    test_endpoints=True,
    sequential_count=20,
    endpoints=['monitor/system/status', 'cmdb/firewall/policy']
)
```

### Option 2: Standalone Function (Alternative)

For testing without an existing client, import the standalone function:

```python
from hfortix.FortiOS.performance_test import run_performance_test

# Quick test (validation + endpoints)
results = run_performance_test(
    host="fw.example.com",
    token="your_token",
    verify=True,
    test_validation=True,
    test_endpoints=True,
    sequential_count=10,
)

# Print summary
results.print_summary()

# Access results programmatically
print(f"Device profile: {results.device_profile}")
print(f"Throughput: {results.sequential_throughput:.2f} req/s")
print(f"Recommended settings: {results.recommended_settings}")
```

### Option 3: Command Line (Alternative)

```bash
# Quick test
python -m hfortix.FortiOS.performance_test 192.168.1.99 your_token

# With SSL verification
python -m hfortix.FortiOS.performance_test fw.example.com your_token --verify

# Full test with concurrency (slower but comprehensive)
python -m hfortix.FortiOS.performance_test fw.example.com your_token --verify --full
```

## What Gets Tested

### 1. Connection Pool Validation ✓
- Tests that connection pool settings work correctly
- Validates auto-adjustment of `max_keepalive_connections`
- Ensures no errors with edge cases

### 2. Endpoint Performance ✓
Tests common API endpoints:
- `monitor/system/status` - System status
- `monitor/system/resource/usage` - Resource usage
- `cmdb/firewall/address` - Firewall addresses (can be large)
- `cmdb/firewall/policy` - Firewall policies (can be large)
- `cmdb/system/interface` - Network interfaces

For each endpoint, measures:
- Average, median, min, max response times
- P95 response time
- Success rate
- Request count

### 3. Concurrency Testing (Optional)
- Tests concurrent vs sequential performance
- Determines if async mode helps or hurts
- Most FortiGates serialize requests (concurrency doesn't help)

## Understanding Results

### Device Profiles

**High-Performance** (< 50ms avg response)
- Fast local/LAN deployment
- Can benefit from concurrency (20-30)
- Expected throughput: ~30 req/s
- **Settings:** `max_connections=60, max_keepalive_connections=30`

**Fast-LAN** (50-100ms avg response)
- Fast but serialized API processing
- Sequential requests recommended
- Expected throughput: ~5-10 req/s
- **Settings:** `max_connections=20, max_keepalive_connections=10`

**Remote/WAN** (> 100ms avg response)
- Remote deployment with network latency
- Sequential requests recommended
- Expected throughput: ~5 req/s
- **Settings:** `max_connections=20, max_keepalive_connections=10`

### Sample Output

```
======================================================================
FortiGate Performance Test Results
======================================================================

[CONNECTION POOL VALIDATION]
✓ Connection pool validation: PASSED
  ⚠ Auto-adjusted max_keepalive_connections from 20 to 5

[ENDPOINT PERFORMANCE]

monitor_system_status:
  Requests:     10
  Avg Time:     23.4ms
  Median Time:  22.1ms
  Min/Max:      20.5ms / 31.2ms
  P95:          28.7ms
  Success Rate: 100.0%

cmdb_firewall_policy:
  Requests:     10
  Avg Time:     156.3ms
  Median Time:  145.2ms
  Min/Max:      98.4ms / 287.1ms
  P95:          251.4ms
  Success Rate: 100.0%

[THROUGHPUT]
Sequential:   11.24 req/s

[DEVICE PROFILE]
Type: high-performance
  → Fast local/LAN deployment
  → Can benefit from moderate concurrency

[RECOMMENDED SETTINGS]
  max_connections: 60
  max_keepalive_connections: 30
  recommended_concurrency: 20-30
  expected_throughput: ~30 req/s
  use_async: Optional - can help with batches

======================================================================
```

## Applying Results

Use the recommended settings when creating your client. The built-in performance test makes this easy:

```python
from hfortix import FortiOS

# Step 1: Create temporary client to run performance test
temp_fgt = FortiOS("192.168.1.99", token="your_token", verify=False)

# Step 2: Run built-in performance test
test_results = temp_fgt.api.utils.performance_test()

# Step 3: Apply recommended settings to production client
settings = test_results.recommended_settings

fgt = FortiOS(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    max_connections=settings.get('max_connections', 30),
    max_keepalive_connections=settings.get('max_keepalive_connections', 15),
)

# Or use the standalone function if preferred:
from hfortix.FortiOS.performance_test import quick_test

test_results = quick_test("192.168.1.99", "your_token", verify=False)
settings = test_results.recommended_settings

fgt = FortiOS(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    max_connections=settings.get('max_connections', 30),
    max_keepalive_connections=settings.get('max_keepalive_connections', 15),
)
```

## Key Findings from Testing

Based on testing across multiple FortiGate models:

1. **Most FortiGates serialize API requests internally**
   - Concurrent requests don't improve throughput
   - Can actually make things 10-15x slower!
   - Sequential requests are recommended

2. **Performance varies dramatically by model and network**
   - Local high-performance: 2-30ms, 30+ req/s
   - LAN standard: 2-10ms, 5-10 req/s  
   - Remote/WAN: 200-300ms, ~5 req/s

3. **Connection pool defaults are conservative**
   - Default `max_connections=30` works for most deployments
   - Increase to 60+ only for high-performance local devices
   - Auto-adjustment prevents configuration errors

4. **Large endpoints take longer**
   - Simple status: 2-30ms
   - Policy lists (100+ rules): 100-300ms
   - Address lists (1000+ objects): 200-500ms

## Advanced Usage

### Test Specific Endpoints (Built-in Method)

Use the built-in function with custom endpoint list:

```python
from hfortix import FortiOS

fgt = FortiOS("192.168.1.99", token="your_token", verify=False)

# Test only specific endpoints using built-in method
results = fgt.api.utils.performance_test(
    test_endpoints=True,
    sequential_count=20,
    endpoints=[
        'monitor/system/status',
        'cmdb/firewall/policy',
        'cmdb/firewall/address',
    ]
)

# Results automatically printed, or access programmatically:
for endpoint_name, metrics in results.endpoint_results.items():
    print(f"{endpoint_name}: {metrics['avg_ms']:.1f}ms")
```

### Test Specific Endpoints (Standalone Function)

Alternatively, use the standalone function:

```python
from hfortix.FortiOS.performance_test import test_endpoint_performance

results = test_endpoint_performance(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    endpoints=[
        'monitor/system/status',
        'cmdb/firewall/policy',
    ],
    count=20,  # 20 requests per endpoint
)

for endpoint, metrics in results.items():
    print(f"{endpoint}: {metrics['avg_ms']:.1f}ms")
```

### Comprehensive Test with Concurrency (Built-in Method)

```python
from hfortix import FortiOS

fgt = FortiOS("192.168.1.99", token="your_token", verify=False)

# Warning: Can take several minutes
results = fgt.api.utils.performance_test(
    test_validation=True,
    test_endpoints=True,
    test_concurrency=True,  # Enable concurrent testing
    sequential_count=20,
    concurrent_count=100,
    concurrent_level=30,
)

# Check if concurrency helps
if results.concurrent_throughput and results.sequential_throughput:
    if results.concurrent_throughput > results.sequential_throughput * 1.1:
        print("Concurrency helps! Use async mode.")
    else:
        print("Concurrency doesn't help. Use sequential.")
```

### Comprehensive Test with Concurrency (Standalone Function)

### Comprehensive Test with Concurrency (Standalone Function)

```python
from hfortix.FortiOS.performance_test import run_performance_test

# Warning: Can take several minutes
results = run_performance_test(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    test_validation=True,
    test_endpoints=True,
    test_concurrency=True,  # Also test concurrent
    sequential_count=20,
    concurrent_count=100,
    concurrent_level=30,
)

# Check if concurrency helps
if results.concurrent_throughput > results.sequential_throughput * 1.1:
    print("Concurrency helps! Use async mode.")
else:
    print("Concurrency doesn't help. Use sequential.")
```

## See Also

- **Example Code:** `examples/performance_test_examples.py`
- **Performance Testing Module:** `hfortix.FortiOS.performance_test`
- **API Integration:** `fgt.api.utils.performance_test()`

## Tips

1. **Use the built-in method**: `fgt.api.utils.performance_test()` is the easiest way to test your FortiGate
2. Run performance tests when setting up a new integration to get optimal settings
3. Test during normal business hours to get realistic performance metrics
4. Network latency often dominates response times for remote devices
5. Large configurations (1000+ policies/objects) significantly impact performance
6. The defaults work well for most deployments - only tune if testing shows clear benefits
