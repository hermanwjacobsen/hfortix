# Performance Testing Guide

## Table of Contents

1. [Quick Start](#quick-start)
2. [Comprehensive Stress Test (New!)](#comprehensive-stress-test)
3. [Standard Performance Testing](#standard-performance-testing)
4. [Running Performance Tests](#running-performance-tests)

---

## Quick Start

Test your FortiGate's performance and get optimal configuration recommendations using the **built-in performance testing function**.

### Method 1: Comprehensive Stress Test (Find Optimal Settings)

**NEW!** Use the comprehensive stress test to find the absolute maximum capacity and recommended safe values for your FortiGate:

```python
from hfortix.FortiOS.performance_test import comprehensive_stress_test

# Run comprehensive stress test
results = comprehensive_stress_test(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    recovery_sleep=60  # Sleep 60s between test phases
)

# Automatically tests:
# - max_connections (sync & async)
# - max_keepalive_connections
# - max_retries
# - adaptive_retry
# - Compares sync vs async performance

# Results show:
# - MAX values (peak capacity)
# - RECOMMENDED values (80% of max for production)
# - Best mode (sync or async)
```

**What it does:**
- Tests all connection parameters systematically
- Pushes your FortiGate to the limit to find maximum capacity
- Provides safe RECOMMENDED values (80% of max)
- Compares sync vs async modes
- Includes recovery sleep between aggressive tests
- Outputs production-ready configuration

**When to use:**
- Setting up hfortix for the first time
- Optimizing for high-performance environments
- After FortiOS upgrades
- When performance issues occur

### Method 2: Built-in API Method (Quick Validation)

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

---

## Comprehensive Stress Test

### Overview

The **comprehensive stress test** is a powerful tool that systematically tests ALL connection parameters to find the maximum capacity and recommended safe values for your specific FortiGate device.

**Use this when:**
- Setting up hfortix for the first time in production
- Optimizing for high-volume/high-performance requirements
- After FortiOS upgrades (performance characteristics may change)
- When experiencing performance issues or throttling
- When you need to know the absolute limits of your device

### What Gets Tested

The comprehensive stress test evaluates:

1. **max_connections** (SYNC mode) - Tests: 5, 10, 20, 30, 50, 75, 100, 150, 200, 300, 500
2. **max_connections** (ASYNC mode) - Tests same values concurrently
3. **max_keepalive_connections** - Tests: 5, 10, 20, 30, 50
4. **max_retries** - Tests: 0, 1, 3, 5, 10
5. **adaptive_retry** - Tests: False vs True
6. **Mode comparison** - Determines if SYNC or ASYNC is better for your device

**Recovery Sleep:** Between each test phase, the tool sleeps (default 60s) to let the FortiGate recover from stress testing.

### Running the Stress Test

#### Method 1: Python Script

```python
from hfortix.FortiOS.performance_test import comprehensive_stress_test

# Run comprehensive stress test
results = comprehensive_stress_test(
    host="192.168.1.99",
    token="your_token",
    verify=False,
    vdom=None,  # Or specify VDOM name
    port=443,
    recovery_sleep=60  # Sleep 60s between test phases
)

# Results contain:
# - max_values: Maximum tested values that worked
# - recommended_values: Safe values (80% of max)
# - test_results: Detailed results for each parameter test
# - best_mode: "sync" or "async" based on performance

# Access results
print(f"Best mode: {results['best_mode']}")
print(f"Max connections: {results['max_values']['max_connections_sync']}")
print(f"Recommended: {results['recommended_values']['max_connections_sync']}")
```

#### Method 2: Example Script

Use the provided example script:

```bash
cd examples
python stress_test_example.py
```

The script will:
1. Ask for confirmation (stress testing can be aggressive)
2. Run all test phases with progress output
3. Save results to JSON file (timestamped)
4. Display production-ready configuration

#### Method 3: Environment Variables

Configure via environment variables:

```bash
export FORTIGATE_HOST="192.168.1.99"
export FORTIGATE_TOKEN="your-api-token"
export FORTIGATE_VERIFY_SSL="False"
export FORTIGATE_VDOM=""  # Leave empty for default
export RECOVERY_SLEEP="60"

python examples/stress_test_example.py
```

### Understanding Results

The test outputs results in multiple phases:

#### Phase 1: max_connections (SYNC)

```
[PHASE 1] Testing max_connections (SYNC mode)...
--------------------------------------------------------------------------------

Testing max_connections=5...
  ✓ Success: 50/50 (100.0%)
  ⏱ Duration: 12.34s
  📊 Throughput: 4.05 req/s
  📈 Response Times: Avg=246.8ms, Median=240.2ms, Min=201.3ms, Max=356.7ms
  📉 Std Dev: 32.4ms, P95=312.5ms

Testing max_connections=10...
  ✓ Success: 50/50 (100.0%)
  ⏱ Duration: 11.87s
  📊 Throughput: 4.21 req/s
  📈 Response Times: Avg=237.4ms, Median=232.1ms, Min=198.5ms, Max=298.2ms
  📉 Std Dev: 24.7ms, P95=287.9ms

Testing max_connections=150...
  ✓ Success: 50/50 (100.0%)
  ⏱ Duration: 11.45s
  📊 Throughput: 4.37 req/s
  📈 Response Times: Avg=229.0ms, Median=225.6ms, Min=195.2ms, Max=287.1ms
  📉 Std Dev: 19.8ms, P95=265.3ms

Testing max_connections=200...
  ✓ Success: 47/50 (94.0%)
  ⏱ Duration: 15.23s
  📊 Throughput: 3.09 req/s
  📈 Response Times: Avg=323.8ms, Median=298.4ms, Min=201.5ms, Max=987.2ms
  📉 Std Dev: 156.3ms, P95=834.7ms
  ⚠ Error: Connection timeout after 10.0s
  ⚠ Error: Remote end closed connection without response
  ⚠ Failed threshold (95%), stopping at 150

================================================================================
SYNC MODE - max_connections Results:
  MAX: 150
  RECOMMENDED: 120 (80% of MAX)
  Peak Throughput: 4.37 req/s
================================================================================

⏸ Sleeping 60s for FortiGate recovery...
```

#### Phase 2: max_connections (ASYNC)

Similar format to Phase 1, but tests async mode with concurrent requests.

#### Final Summary

```
================================================================================
FINAL RECOMMENDATIONS - Optimal Connection Parameters
================================================================================

For PRODUCTION use, configure FortiOS client with:

  mode: 'async'
  max_connections: 160 (80% of MAX: 200)
  max_keepalive_connections: 16 (80% of MAX: 20)
  max_retries: 3
  adaptive_retry: True
  connect_timeout: 10.0
  read_timeout: 30.0

================================================================================
MAXIMUM TESTED VALUES (not recommended for production)
================================================================================

  max_connections (sync): 150 @ 4.37 req/s
  max_connections (async): 200 @ 8.12 req/s
  max_keepalive_connections: 20

================================================================================
TEST SUMMARY
================================================================================

  Total test phases: 6
  Total tests run: 23
  Best performing mode: ASYNC
  Async vs Sync improvement: +85.8% faster
  Recommendation confidence: HIGH (80% safety margin)
================================================================================
```

**Key Points:**
- **RECOMMENDED = 80% of MAX** - Provides safety margin for production
- **Detailed response time statistics** - Avg, Median, Min, Max, StdDev, P95
- **Throughput tracking** - Shows best-performing values
- **Error visibility** - First 3 errors shown for each test
- **Performance comparison** - Quantified async vs sync improvement

### Production Configuration

After running the stress test, configure your FortiOS client with the **RECOMMENDED** values:

```python
from hfortix import FortiOS

client = FortiOS(
    host="192.168.1.99",
    token="your_token",
    mode="async",  # Based on test results
    max_connections=120,  # RECOMMENDED value
    max_keepalive_connections=16,  # RECOMMENDED value
    max_retries=3,  # RECOMMENDED value
    adaptive_retry=True,  # Based on test results
    connect_timeout=10.0,
    read_timeout=30.0,
    verify=False,
)
```

**Why use RECOMMENDED instead of MAX?**

- **MAX**: Peak capacity where device starts showing errors/throttling
- **RECOMMENDED** (80% of MAX): Safe production value with headroom for:
  - Firmware upgrades changing performance characteristics
  - Other users/applications accessing the FortiGate
  - Burst traffic scenarios
  - Configuration changes affecting performance

### Best Practices

1. **Run on test/lab device first** - Stress testing is aggressive and can impact production
2. **Run during maintenance window** - Testing pushes device to limits
3. **Save results** - Keep JSON output for future reference
4. **Re-test after upgrades** - FortiOS upgrades can change performance
5. **Adjust recovery_sleep if needed**:
   - Increase to 90-120s for slower devices
   - Decrease to 30s for high-performance devices
6. **Test in your actual environment** - Network latency affects results
7. **Monitor FortiGate during test** - Watch CPU/memory via GUI

### Interpreting Throughput

The test measures **throughput** (requests per second) for each configuration:

- **Higher throughput = better** for batch operations
- **Lower latency = better** for interactive use
- **95% success rate threshold** - Test stops when errors exceed 5%

**Typical results:**

- **High-Performance (LAN)**: 10-30 req/s
- **Fast (LAN, serialized)**: 5-10 req/s  
- **Remote/WAN**: 2-5 req/s
- **Overloaded**: < 2 req/s with errors

### Troubleshooting

**Test fails immediately:**
- Check network connectivity
- Verify API token is valid
- Ensure API access is enabled on FortiGate
- Check SSL verification settings

**All tests show low throughput (<2 req/s):**
- FortiGate may be overloaded
- Network latency may be high (test from closer location)
- Device may be low-powered model
- Check FortiGate CPU/memory usage

**Tests never exceed max_connections=10:**
- FortiGate may be rate-limiting API access
- Check `diagnose debug application httpsd 7` on FortiGate
- Device may be under heavy load
- Try increasing recovery_sleep

**Async slower than sync:**
- Normal for FortiGate (most serialize API requests internally)
- Use sync mode for simplicity
- Only use async if test shows clear benefit (>10% faster)

### Advanced Usage

#### Custom Test Values

Modify the test values for your specific needs:

```python
from hfortix.FortiOS.performance_test import comprehensive_stress_test

# Edit the function source to customize test ranges:
# max_conn_values = [5, 10, 20, 30, 50]  # Reduce range for faster testing
# retry_values = [3, 5]  # Only test specific retry values
```

#### Scripted Testing

Automate stress testing across multiple FortiGates:

```python
import json

fortigates = [
    {"host": "fw1.example.com", "token": "token1"},
    {"host": "fw2.example.com", "token": "token2"},
]

all_results = {}

for fg in fortigates:
    print(f"\n Testing {fg['host']}...")
    results = comprehensive_stress_test(
        host=fg['host'],
        token=fg['token'],
        verify=True,
        recovery_sleep=60
    )
    all_results[fg['host']] = results

# Save consolidated results
with open("all_fortigates_stress_test.json", "w") as f:
    json.dump(all_results, f, indent=2)
```

---

## See Also

- **Example Code:** `examples/performance_test_examples.py`
- **Stress Test Example:** `examples/stress_test_example.py`
- **Performance Testing Module:** `hfortix.FortiOS.performance_test`
- **API Integration:** `fgt.api.utils.performance_test()`

## Tips

1. **Use the built-in method**: `fgt.api.utils.performance_test()` is the easiest way to test your FortiGate
2. **Use comprehensive stress test**: When setting up for production or optimizing performance
3. Run performance tests when setting up a new integration to get optimal settings
4. Test during normal business hours to get realistic performance metrics
5. Network latency often dominates response times for remote devices
6. Large configurations (1000+ policies/objects) significantly impact performance
7. The defaults work well for most deployments - only tune if testing shows clear benefits
8. **RECOMMENDED values are safer than MAX** - Always use RECOMMENDED for production
