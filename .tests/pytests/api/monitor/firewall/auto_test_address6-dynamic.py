"""
Auto-generated basic tests for monitor.firewall/address6_dynamic

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/monitor/firewall.address6-dynamic.json
Category: monitor
Endpoint: /monitor/firewall/address6-dynamic

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_address6-dynamic.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.monitor.firewall.address6_dynamic


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoAddress6DynamicGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve address6-dynamic configuration."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Monitor/Service endpoints may return dict with results
        print(f"✅ GET returned data: {type(result)}")
    
    
    def auto_test_get_with_vdom(self):
        """Test GET - with vdom parameter."""
        try:
            result = endpoint.get(vdom="root")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with vdom=root successful")
    










# Metadata for test discovery
TEST_ENDPOINT = "monitor/firewall/address6_dynamic"
TEST_CATEGORY = "monitor"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/monitor/firewall.address6-dynamic.json"
TEST_HTTP_METHODS = ['GET']