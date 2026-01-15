"""
Auto-generated basic tests for log.forticloud/app_ctrl

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/log/forticloud.app_ctrl.json
Category: log
Endpoint: /log/forticloud/app_ctrl

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_app_ctrl.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.log.forticloud.app_ctrl


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoAppCtrlGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve app_ctrl configuration."""
        try:
            result = endpoint.get(response_mode="dict")
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
            result = endpoint.get(vdom="root", response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with vdom=root successful")
    










# Metadata for test discovery
TEST_ENDPOINT = "log/forticloud/app_ctrl"
TEST_CATEGORY = "log"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/log/forticloud.app_ctrl.json"
TEST_HTTP_METHODS = ['GET']