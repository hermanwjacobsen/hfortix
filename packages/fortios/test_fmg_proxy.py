#!/usr/bin/env python3
"""
Test FortiManager Proxy functionality.

This script tests that the FMG proxy implementation can:
1. Import correctly
2. Create FortiManagerProxy instances
3. Create ProxiedFortiOS instances
4. Access the API namespace
"""

import sys

def test_imports():
    """Test that all imports work."""
    print("Testing imports...")
    
    from hfortix_fortios import FortiManagerProxy, ProxyResponse, DeviceResult
    from hfortix_fortios.fmg_proxy import FMGProxyClient, ProxiedFortiOS
    
    print("  ✓ All imports successful")
    return True


def test_proxy_creation():
    """Test creating proxy instances."""
    print("\nTesting FortiManagerProxy creation...")
    
    from hfortix_fortios import FortiManagerProxy
    
    # Test creation without connecting
    fmg = FortiManagerProxy(
        host="192.168.1.99",
        username="admin",
        password="password",
        verify=False,
        adom="root",
    )
    
    print(f"  ✓ Created FortiManagerProxy for {fmg.host}")
    print(f"    - Default ADOM: {fmg.adom}")
    print(f"    - Verify SSL: {fmg.verify}")
    return True


def test_proxy_method():
    """Test the proxy() method returns a ProxiedFortiOS instance."""
    print("\nTesting proxy() method...")
    
    from hfortix_fortios import FortiManagerProxy
    from hfortix_fortios.fmg_proxy import ProxiedFortiOS
    
    fmg = FortiManagerProxy(
        host="192.168.1.99",
        username="admin",
        password="password",
        adom="root",  # Set default ADOM
    )
    
    # Get a proxy client for a device (without actually connecting)
    fgt = fmg.proxy(device="firewall-01", vdom="root")
    
    print(f"  ✓ Created ProxiedFortiOS for device")
    print(f"    - Target: {fgt.target}")
    print(f"    - VDOM: {fgt.vdom}")
    
    # Verify it's the right type
    assert isinstance(fgt, ProxiedFortiOS), f"Expected ProxiedFortiOS, got {type(fgt)}"
    print("  ✓ Instance type is correct")
    
    return True


def test_api_namespace_exists():
    """Test that the api namespace exists and has expected structure."""
    print("\nTesting API namespace structure...")
    
    from hfortix_fortios import FortiManagerProxy
    
    fmg = FortiManagerProxy(
        host="192.168.1.99",
        username="admin",
        password="password",
        adom="root",
    )
    
    fgt = fmg.proxy(device="firewall-01")
    
    # Check that api property exists
    api = fgt.api
    print(f"  ✓ API namespace created: {type(api).__name__}")
    
    # Check expected sub-namespaces exist
    assert hasattr(api, 'cmdb'), "API should have 'cmdb' namespace"
    assert hasattr(api, 'monitor'), "API should have 'monitor' namespace"
    print("  ✓ Has cmdb and monitor namespaces")
    
    # Check deeper nesting
    assert hasattr(api.cmdb, 'firewall'), "CMDB should have 'firewall' namespace"
    assert hasattr(api.cmdb.firewall, 'address'), "Firewall should have 'address' endpoint"
    print("  ✓ Has firewall.address endpoint")
    
    return True


def test_proxy_client_methods():
    """Test that FMGProxyClient has expected methods."""
    print("\nTesting FMGProxyClient methods...")
    
    from hfortix_fortios.fmg_proxy import FMGProxyClient
    
    # Create proxy client (needs FMG client but we can test structure)
    from hfortix_fortios import FortiManagerProxy
    
    fmg = FortiManagerProxy(
        host="192.168.1.99",
        username="admin",
        password="password",
        adom="root",
    )
    
    # Access internal proxy client through ProxiedFortiOS
    fgt = fmg.proxy(device="firewall-01")
    
    # Check proxy client has expected methods
    client = fgt._proxy_client
    assert hasattr(client, 'get'), "Proxy client should have 'get' method"
    assert hasattr(client, 'post'), "Proxy client should have 'post' method"
    assert hasattr(client, 'put'), "Proxy client should have 'put' method"
    assert hasattr(client, 'delete'), "Proxy client should have 'delete' method"
    print("  ✓ Has get, post, put, delete methods")
    
    return True


def test_response_models():
    """Test response model creation."""
    print("\nTesting response models...")
    
    from hfortix_fortios import ProxyResponse, DeviceResult
    
    # Create DeviceResult
    result = DeviceResult(
        target="adom/root/device/fw01",
        response={"name": "test"},
        status={"code": 0, "message": "OK"},
    )
    print(f"  ✓ Created DeviceResult: {result.target}")
    
    # Check success/failed detection
    assert result.success == True, "Status code 0 should be success"
    assert result.failed == False, "Status code 0 should not be failed"
    print("  ✓ Success/failed detection works")
    
    # Create ProxyResponse (uses 'data' field)
    response = ProxyResponse(data=[result])
    print(f"  ✓ Created ProxyResponse with {len(response)} results")
    
    # Test iteration
    items = list(response)
    assert len(items) == 1, "Should have 1 item"
    print("  ✓ ProxyResponse iteration works")
    
    # Test stats
    assert response.success_count == 1, "Should have 1 success"
    assert response.failed_count == 0, "Should have 0 failures"
    print("  ✓ Success/failed counts work")
    
    return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("FortiManager Proxy Tests")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_proxy_creation,
        test_proxy_method,
        test_api_namespace_exists,
        test_proxy_client_methods,
        test_response_models,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"\n  ✗ FAILED: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
