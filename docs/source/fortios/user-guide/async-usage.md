# Async Usage

Guide to asynchronous programming with HFortix using async/await.

```{note}
This content will be migrated from `docs/fortios/ASYNC_GUIDE.md`
```

## Overview

All HFortix API methods support asynchronous execution by appending `_async` to the method name.

## Quick Example

```python
import asyncio
from hfortix import FortiOS

async def main():
    fgt = FortiOS(host='192.168.1.99', token='token')
    
    # Async API calls
    addresses = await fgt.api.cmdb.firewall.address.list_async()
    
    result = await fgt.api.cmdb.firewall.address.create_async(
        name='server-1',
        subnet='10.0.0.1/32'
    )
    
    # Concurrent operations
    results = await asyncio.gather(
        fgt.api.cmdb.firewall.address.list_async(),
        fgt.api.cmdb.firewall.policy.list_async(),
        fgt.api.monitor.system.status.get_async()
    )

asyncio.run(main())
```

## Coming Soon

Detailed documentation including:
- Async/await basics
- Concurrent operations
- Connection pooling
- Error handling in async code
- Performance benefits
- Best practices

## Temporary Reference

For now, see:
- Current docs: `docs/fortios/ASYNC_GUIDE.md` in repository
