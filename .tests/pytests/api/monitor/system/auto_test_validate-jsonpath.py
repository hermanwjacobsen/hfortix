"""
Auto-generated basic tests for monitor.system/external_resource/validate_jsonpath

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/monitor/system.external-resource.validate-jsonpath.json
Category: monitor
Endpoint: /monitor/system/external-resource/validate-jsonpath

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_validate-jsonpath.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.monitor.system.external_resource.validate_jsonpath


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoValidateJsonpathGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve validate-jsonpath configuration."""
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
TEST_ENDPOINT = "monitor/system/external_resource/validate_jsonpath"
TEST_CATEGORY = "monitor"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/monitor/system.external-resource.validate-jsonpath.json"
TEST_HTTP_METHODS = ['GET']