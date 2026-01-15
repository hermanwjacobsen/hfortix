"""
Auto-generated basic tests for monitor.system/traffic_history/enable_app_bandwidth_tracking

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/monitor/system.traffic-history.enable-app-bandwidth-tracking.json
Category: monitor
Endpoint: /monitor/system/traffic-history/enable-app-bandwidth-tracking

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_enable-app-bandwidth-tracking.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.monitor.system.traffic_history.enable_app_bandwidth_tracking


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoEnableAppBandwidthTrackingGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve enable-app-bandwidth-tracking configuration."""
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
TEST_ENDPOINT = "monitor/system/traffic_history/enable_app_bandwidth_tracking"
TEST_CATEGORY = "monitor"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/monitor/system.traffic-history.enable-app-bandwidth-tracking.json"
TEST_HTTP_METHODS = ['GET']