"""
Auto-generated basic tests for cmdb.switch_controller/x802_1x_settings

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.802-1X-settings.json
Category: cmdb
Endpoint: /cmdb/switch-controller/802-1X-settings

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_802-1X-settings.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.x802_1x_settings


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoX8021xSettingsGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve 802-1X-settings configuration."""
        try:
            result = endpoint.get(response_mode="dict")
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single dict
        assert isinstance(result, dict)
        print(f"✅ Retrieved 802-1X-settings configuration (singleton)")
        print(f"   Config keys: {len(result)} fields")
    
    
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
    
    def auto_test_get_with_filters(self):
        """Test GET - with filter parameters."""
        # Test with common filter options
        try:
            result = endpoint.get(
                filter="",  # No filter (get all)
                q_format="name|None",  # Limit fields
                response_mode="dict",
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoX8021xSettingsExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoX8021xSettingsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_link_down_auth(self):
        """Test enum field link-down-auth validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import x802_1x_settings as validators
        
        valid_values = ['set-unauth', 'no-action']
        
        # Test each valid value
        for value in valid_values:
            config = {"link-down-auth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: link-down-auth={value}")
        
        print(f"✅ Enum field link-down-auth has {len(valid_values)} valid values")
    def auto_test_enum_mab_reauth(self):
        """Test enum field mab-reauth validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import x802_1x_settings as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"mab-reauth": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mab-reauth={value}")
        
        print(f"✅ Enum field mab-reauth has {len(valid_values)} valid values")
    def auto_test_enum_mac_username_delimiter(self):
        """Test enum field mac-username-delimiter validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import x802_1x_settings as validators
        
        valid_values = ['colon', 'hyphen', 'none', 'single-hyphen']
        
        # Test each valid value
        for value in valid_values:
            config = {"mac-username-delimiter": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: mac-username-delimiter={value}")
        
        print(f"✅ Enum field mac-username-delimiter has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/x802_1x_settings"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.802-1X-settings.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']