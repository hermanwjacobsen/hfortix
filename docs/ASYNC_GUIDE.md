# Async/Await Support Guide

HFortix provides full async/await support for all FortiOS API operations, allowing you to write high-performance concurrent code while maintaining the same simple API interface.

## 🎯 Overview

- **Single Class**: Same `FortiOS` class works in both sync and async modes
- **Mode Parameter**: Simply set `mode="async"` to enable async operations
- **Full Coverage**: All 750+ API methods support async
- **Helper Methods**: All `.exists()` and other helpers work transparently
- **Type Safety**: Full type hints with IDE autocomplete support
- **Zero Breaking Changes**: Existing sync code continues to work unchanged

## 🚀 Quick Start

### Sync Mode (Default)

```python
from hfortix import FortiOS

# Default sync mode
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False
)

# Use normally
addresses = fgt.api.cmdb.firewall.address.list()
print(f"Found {len(addresses)} addresses")

# Check if exists
if fgt.api.cmdb.firewall.address.exists("web-server"):
    print("Address exists!")
```

### Async Mode

```python
import asyncio
from hfortix import FortiOS

async def main():
    # Enable async mode
    fgt = FortiOS(
        host='192.168.1.99',
        token='your-api-token',
        verify=False,
        mode="async"  # 👈 Enable async mode
    )

    # Use async context manager for automatic cleanup
    async with fgt:
        # Use await with all API methods
        addresses = await fgt.api.cmdb.firewall.address.list()
        print(f"Found {len(addresses)} addresses")

        # Helper methods also work with await
        if await fgt.api.cmdb.firewall.address.exists("web-server"):
            print("Address exists!")

# Run async code
asyncio.run(main())
```

## 📖 API Reference

### Mode Parameter

The `FortiOS` class accepts a `mode` parameter:

```python
FortiOS(
    host: str,
    token: str | None = None,
    username: str | None = None,
    password: str | None = None,
    verify: bool = True,
    vdom: str | None = None,
    mode: Literal["sync", "async"] = "sync"  # 👈 New parameter
)
```

**Values:**
- `"sync"` (default): Synchronous mode - methods return results directly
- `"async"`: Asynchronous mode - methods return coroutines that must be awaited

### Async Context Manager

Use `async with` for automatic resource cleanup:

```python
async with FortiOS(..., mode="async") as fgt:
    # API calls here
    result = await fgt.api.cmdb.firewall.address.get("web-server")
# Connection automatically closed when exiting context
```

Manual cleanup is also supported:

```python
fgt = FortiOS(..., mode="async")
try:
    result = await fgt.api.cmdb.firewall.address.get("web-server")
finally:
    await fgt.aclose()  # Manual cleanup
```

## 🔥 Common Patterns

### 1. Concurrent Requests

Fetch multiple resources concurrently:

```python
import asyncio
from hfortix import FortiOS

async def fetch_configs():
    async with FortiOS(..., mode="async") as fgt:
        # Run multiple requests concurrently
        addresses, policies, services = await asyncio.gather(
            fgt.api.cmdb.firewall.address.list(),
            fgt.api.cmdb.firewall.policy.list(),
            fgt.api.cmdb.firewall.service.custom.list()
        )

        print(f"Addresses: {len(addresses)}")
        print(f"Policies: {len(policies)}")
        print(f"Services: {len(services)}")

asyncio.run(fetch_configs())
```

### 2. Bulk Operations

Process multiple items concurrently:

```python
async def create_addresses(names_and_ips):
    async with FortiOS(..., mode="async") as fgt:
        tasks = []
        for name, ip in names_and_ips:
            task = fgt.api.cmdb.firewall.address.create(
                name=name,
                subnet=f"{ip}/32"
            )
            tasks.append(task)

        # Create all addresses concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Check results
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Failed: {names_and_ips[i][0]} - {result}")
            else:
                print(f"Created: {names_and_ips[i][0]}")

# Usage
addresses = [
    ("server1", "10.0.1.10"),
    ("server2", "10.0.1.11"),
    ("server3", "10.0.1.12"),
]
asyncio.run(create_addresses(addresses))
```

### 3. Conditional Operations

Use `.exists()` helper in async mode:

```python
async def update_or_create(name, config):
    async with FortiOS(..., mode="async") as fgt:
        # Check if exists (returns coroutine in async mode)
        exists = await fgt.api.cmdb.firewall.address.exists(name)

        if exists:
            # Update existing
            result = await fgt.api.cmdb.firewall.address.update(
                name=name,
                **config
            )
            print(f"Updated {name}")
        else:
            # Create new
            result = await fgt.api.cmdb.firewall.address.create(
                name=name,
                **config
            )
            print(f"Created {name}")

        return result

asyncio.run(update_or_create("web-server", {"subnet": "10.0.1.50/32"}))
```

### 4. Error Handling

Handle errors in async operations:

```python
from hfortix.FortiOS.exceptions_forti import (
    ResourceNotFoundError,
    ResourceAlreadyExistsError,
    FortiOSAPIError
)

async def safe_create(name, subnet):
    async with FortiOS(..., mode="async") as fgt:
        try:
            result = await fgt.api.cmdb.firewall.address.create(
                name=name,
                subnet=subnet
            )
            print(f"✓ Created {name}")
            return result

        except ResourceAlreadyExistsError:
            print(f"⚠ {name} already exists")
            # Update instead
            return await fgt.api.cmdb.firewall.address.update(
                name=name,
                subnet=subnet
            )

        except FortiOSAPIError as e:
            print(f"✗ Failed: {e}")
            return None

asyncio.run(safe_create("web-server", "10.0.1.50/32"))
```

### 5. Progress Tracking

Track progress of bulk operations:

```python
async def bulk_delete_with_progress(names):
    async with FortiOS(..., mode="async") as fgt:
        total = len(names)

        for i, name in enumerate(names, 1):
            try:
                await fgt.api.cmdb.firewall.address.delete(name)
                print(f"[{i}/{total}] Deleted: {name}")
            except ResourceNotFoundError:
                print(f"[{i}/{total}] Not found: {name}")
            except Exception as e:
                print(f"[{i}/{total}] Error: {name} - {e}")

asyncio.run(bulk_delete_with_progress(["old-server1", "old-server2"]))
```

## 🔄 Migration Guide

### From Sync to Async

Converting sync code to async is straightforward:

**Before (Sync):**

```python
from hfortix import FortiOS

def manage_addresses():
    fgt = FortiOS(host='...', token='...')

    # List addresses
    addresses = fgt.api.cmdb.firewall.address.list()

    # Create address
    if not fgt.api.cmdb.firewall.address.exists("server1"):
        fgt.api.cmdb.firewall.address.create(
            name="server1",
            subnet="10.0.1.10/32"
        )

    return addresses

result = manage_addresses()
```

**After (Async):**

```python
import asyncio
from hfortix import FortiOS

async def manage_addresses():
    async with FortiOS(host='...', token='...', mode="async") as fgt:
        # List addresses (add await)
        addresses = await fgt.api.cmdb.firewall.address.list()

        # Create address (add await)
        if not await fgt.api.cmdb.firewall.address.exists("server1"):
            await fgt.api.cmdb.firewall.address.create(
                name="server1",
                subnet="10.0.1.10/32"
            )

        return addresses

result = asyncio.run(manage_addresses())
```

**Changes needed:**
1. Add `mode="async"` parameter
2. Make function `async def`
3. Add `await` before all API calls
4. Use `async with` for context manager
5. Run with `asyncio.run()`

## ⚡ Performance Benefits

### Concurrent Operations

Async mode shines when performing multiple independent operations:

```python
import time
import asyncio
from hfortix import FortiOS

# Sync mode - Sequential (slower)
def sync_fetch():
    fgt = FortiOS(..., mode="sync")
    start = time.time()

    addr = fgt.api.cmdb.firewall.address.list()
    pol = fgt.api.cmdb.firewall.policy.list()
    svc = fgt.api.cmdb.firewall.service.custom.list()

    elapsed = time.time() - start
    print(f"Sync: {elapsed:.2f}s")
    return addr, pol, svc

# Async mode - Concurrent (faster)
async def async_fetch():
    async with FortiOS(..., mode="async") as fgt:
        start = time.time()

        # All three run concurrently!
        addr, pol, svc = await asyncio.gather(
            fgt.api.cmdb.firewall.address.list(),
            fgt.api.cmdb.firewall.policy.list(),
            fgt.api.cmdb.firewall.service.custom.list()
        )

        elapsed = time.time() - start
        print(f"Async: {elapsed:.2f}s")
        return addr, pol, svc

# Sync: 3.5s (sequential: 1.2s + 1.1s + 1.2s)
sync_fetch()

# Async: 1.2s (concurrent: max(1.2s, 1.1s, 1.2s))
asyncio.run(async_fetch())
```

**Speedup:** ~3x faster for 3 concurrent operations!

## 🛠️ Advanced Usage

### Rate Limiting

Control concurrency to avoid overwhelming the FortiGate:

```python
async def rate_limited_operations(items, max_concurrent=5):
    async with FortiOS(..., mode="async") as fgt:
        semaphore = asyncio.Semaphore(max_concurrent)

        async def limited_create(name, subnet):
            async with semaphore:
                return await fgt.api.cmdb.firewall.address.create(
                    name=name,
                    subnet=subnet
                )

        tasks = [limited_create(n, s) for n, s in items]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        return results
```

### Timeout Handling

Set timeouts for individual operations:

```python
async def fetch_with_timeout():
    async with FortiOS(..., mode="async") as fgt:
        try:
            # 5 second timeout
            result = await asyncio.wait_for(
                fgt.api.cmdb.firewall.address.list(),
                timeout=5.0
            )
            return result
        except asyncio.TimeoutError:
            print("Operation timed out")
            return None
```

### Multiple FortiGates

Manage multiple FortiGates concurrently:

```python
async def manage_multiple_fortigates(hosts_and_tokens):
    async def fetch_from_host(host, token):
        async with FortiOS(host=host, token=token, mode="async") as fgt:
            addresses = await fgt.api.cmdb.firewall.address.list()
            return host, addresses

    tasks = [fetch_from_host(h, t) for h, t in hosts_and_tokens]
    results = await asyncio.gather(*tasks)

    for host, addresses in results:
        print(f"{host}: {len(addresses)} addresses")

    return results

fortigates = [
    ("192.168.1.1", "token1"),
    ("192.168.1.2", "token2"),
    ("192.168.1.3", "token3"),
]
asyncio.run(manage_multiple_fortigates(fortigates))
```

## 📋 Method Reference

### All Methods Support Async

Every API method works in async mode:

**CRUD Methods:**
- `list()` → `await list()`
- `get()` → `await get()`
- `create()` → `await create()`
- `update()` → `await update()`
- `delete()` → `await delete()`

**Helper Methods:**
- `exists()` → `await exists()`

**Examples:**

```python
async with FortiOS(..., mode="async") as fgt:
    # List
    items = await fgt.api.cmdb.firewall.address.list()

    # Get
    item = await fgt.api.cmdb.firewall.address.get("web-server")

    # Create
    result = await fgt.api.cmdb.firewall.address.create(
        name="new-server",
        subnet="10.0.1.100/32"
    )

    # Update
    result = await fgt.api.cmdb.firewall.address.update(
        name="web-server",
        subnet="10.0.1.50/32"
    )

    # Delete
    result = await fgt.api.cmdb.firewall.address.delete("old-server")

    # Exists
    exists = await fgt.api.cmdb.firewall.address.exists("web-server")
```

## 🔍 Type Hints & IDE Support

Full type hints are provided for both modes:

```python
from hfortix import FortiOS

# Sync mode - type checker knows methods return values
fgt_sync: FortiOS = FortiOS(mode="sync")
addresses: dict = fgt_sync.api.cmdb.firewall.address.list()

# Async mode - type checker knows methods return coroutines
fgt_async: FortiOS = FortiOS(mode="async")
addresses_coro = fgt_async.api.cmdb.firewall.address.list()
# Must await coroutines
addresses: dict = await addresses_coro
```

## ⚠️ Important Notes

### 1. Mode Must Be Consistent

Don't mix sync and async calls on the same instance:

```python
# ❌ WRONG - mixing modes
fgt = FortiOS(..., mode="async")
result = fgt.api.cmdb.firewall.address.list()  # Returns coroutine, not data!

# ✓ CORRECT - use await in async mode
fgt = FortiOS(..., mode="async")
result = await fgt.api.cmdb.firewall.address.list()
```

### 2. Always Use Async Context Manager

In async mode, use `async with` or manually call `await fgt.aclose()`:

```python
# ✓ CORRECT - automatic cleanup
async with FortiOS(..., mode="async") as fgt:
    result = await fgt.api.cmdb.firewall.address.list()

# ✓ ALSO CORRECT - manual cleanup
fgt = FortiOS(..., mode="async")
try:
    result = await fgt.api.cmdb.firewall.address.list()
finally:
    await fgt.aclose()

# ❌ WRONG - resource leak
fgt = FortiOS(..., mode="async")
result = await fgt.api.cmdb.firewall.address.list()
# Missing cleanup!
```

### 3. Helper Methods Return Coroutines in Async Mode

The `.exists()` helper returns different types based on mode:

```python
# Sync mode - returns bool directly
fgt_sync = FortiOS(..., mode="sync")
exists: bool = fgt_sync.api.cmdb.firewall.address.exists("test")

# Async mode - returns coroutine
fgt_async = FortiOS(..., mode="async")
exists_coro = fgt_async.api.cmdb.firewall.address.exists("test")
exists: bool = await exists_coro
```

## 🎓 Best Practices

1. **Use async for I/O-bound operations** - Multiple API calls, bulk operations
2. **Use sync for simple scripts** - Single operation, quick tasks
3. **Always use context managers** - Ensures proper cleanup
4. **Handle exceptions properly** - Async errors can be tricky
5. **Limit concurrency** - Use semaphores to avoid overwhelming FortiGate
6. **Set timeouts** - Prevent hanging operations
7. **Test error paths** - Network errors, API errors, timeouts

## 📚 Additional Resources

- **Main README**: [README.md](README.md)
- **Quick Start Guide**: [QUICKSTART.md](QUICKSTART.md)
- **API Coverage**: [API_COVERAGE.md](API_COVERAGE.md)
- **Python asyncio docs**: [docs.python.org/3/library/asyncio](https://docs.python.org/3/library/asyncio.html)

## 🐛 Troubleshooting

### "RuntimeError: This event loop is already running"

If running in Jupyter/IPython, use `await` directly instead of `asyncio.run()`:

```python
# In Jupyter/IPython
async with FortiOS(..., mode="async") as fgt:
    result = await fgt.api.cmdb.firewall.address.list()
```

### "Coroutine was never awaited"

You forgot to `await` an async call:

```python
# ❌ WRONG
fgt = FortiOS(..., mode="async")
result = fgt.api.cmdb.firewall.address.list()  # Missing await!

# ✓ CORRECT
fgt = FortiOS(..., mode="async")
result = await fgt.api.cmdb.firewall.address.list()
```

### "Cannot call 'aclose' in sync mode"

You're trying to use async cleanup in sync mode:

```python
# ❌ WRONG
fgt = FortiOS(..., mode="sync")
await fgt.aclose()  # Can't await in sync mode!

# ✓ CORRECT
fgt = FortiOS(..., mode="sync")
fgt.close()  # Use sync close

# Or use context manager
with FortiOS(..., mode="sync") as fgt:
    result = fgt.api.cmdb.firewall.address.list()
```

---

**Built with ❤️ for the Fortinet community**
