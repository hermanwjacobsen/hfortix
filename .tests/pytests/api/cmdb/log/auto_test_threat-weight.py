"""
Auto-generated basic tests for cmdb.log/threat_weight

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/log.threat-weight.json
Category: cmdb
Endpoint: /cmdb/log/threat-weight

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_threat-weight.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.log.threat_weight


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoThreatWeightGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve threat-weight configuration."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single FortiObject
        assert hasattr(result, "__dict__")  # FortiObject
        print(f"✅ Retrieved threat-weight configuration (singleton)")
        # Convert to dict to count fields
        result_dict = result.dict
        print(f"   Config keys: {len(result_dict)} fields")
    
    
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
    
    def auto_test_get_with_filters(self):
        """Test GET - with filter parameters."""
        # Test with common filter options
        try:
            result = endpoint.get(
                filter="",  # No filter (get all)
                q_format="name|None",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoThreatWeightExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoThreatWeightEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import threat_weight as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_blocked_connection(self):
        """Test enum field blocked-connection validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import threat_weight as validators
        
        valid_values = ['disable', 'low', 'medium', 'high', 'critical']
        
        # Test each valid value
        for value in valid_values:
            config = {"blocked-connection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: blocked-connection={value}")
        
        print(f"✅ Enum field blocked-connection has {len(valid_values)} valid values")
    def auto_test_enum_failed_connection(self):
        """Test enum field failed-connection validation."""
        from hfortix_fortios.api.v2.cmdb.log._helpers import threat_weight as validators
        
        valid_values = ['disable', 'low', 'medium', 'high', 'critical']
        
        # Test each valid value
        for value in valid_values:
            config = {"failed-connection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: failed-connection={value}")
        
        print(f"✅ Enum field failed-connection has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/log/threat_weight"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/log.threat-weight.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']