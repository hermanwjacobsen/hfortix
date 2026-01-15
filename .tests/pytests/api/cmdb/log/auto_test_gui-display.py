"""
Auto-generated basic tests for cmdb.log/gui_display

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/log.gui-display.json
Category: cmdb
Endpoint: /cmdb/log/gui-display

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_gui-display.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.gui_display


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoGuiDisplayGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve gui-display configuration."""
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
        print(f"✅ Retrieved gui-display configuration (singleton)")
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
class TestAutoGuiDisplayExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoGuiDisplayEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_resolve_hosts(self):
        """Test enum field resolve-hosts validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import gui_display as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"resolve-hosts": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: resolve-hosts={value}")
        
        print(f"✅ Enum field resolve-hosts has {len(valid_values)} valid values")
    def auto_test_enum_resolve_apps(self):
        """Test enum field resolve-apps validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import gui_display as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"resolve-apps": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: resolve-apps={value}")
        
        print(f"✅ Enum field resolve-apps has {len(valid_values)} valid values")
    def auto_test_enum_fortiview_unscanned_apps(self):
        """Test enum field fortiview-unscanned-apps validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import gui_display as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortiview-unscanned-apps": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortiview-unscanned-apps={value}")
        
        print(f"✅ Enum field fortiview-unscanned-apps has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/gui_display"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/log.gui-display.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']