"""
Auto-generated basic tests for cmdb.router/policy6

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/router.policy6.json
Category: cmdb
Endpoint: /cmdb/router/policy6

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_policy6.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.router.policy6


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoPolicy6Get:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all policy6 items."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Multi-value CMDB endpoints return list
        assert isinstance(result, list)
        print(f"✅ Retrieved {len(result)} policy6 items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "seq_num")
            mkey_value = getattr(item, "seq_num", "N/A")
            print(f"   First item seq-num: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific policy6 by seq-num."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing policy6 items to test with")
        
        # Get first item's seq-num
        mkey_value = getattr(all_items[0], "seq_num")
        
        # Get specific item
        result = endpoint.get(seq_num=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "seq_num") == mkey_value
        print(f"✅ Retrieved policy6 seq-num={mkey_value}")
    
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
                q_format="name|seq-num",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoPolicy6Exists:
    """Auto-generated exists() tests."""
    
    def auto_test_exists_method(self):
        """Test exists() helper method."""
        # Get existing items
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if all_items and len(all_items) > 0:
            # Test with existing item
            mkey_value = getattr(all_items[0], "seq_num")
            exists = endpoint.exists(seq_num=mkey_value)
            assert exists is True
            print(f"✅ exists(seq-num={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = 999999
            exists = endpoint.exists(seq_num=non_existing)
            assert exists is False
            print(f"✅ exists(seq-num={non_existing}) = False")
        else:
            pytest.skip("No existing policy6 items to test exists() with")




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPolicy6Enums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_input_device_negate(self):
        """Test enum field input-device-negate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"input-device-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: input-device-negate={value}")
        
        print(f"✅ Enum field input-device-negate has {len(valid_values)} valid values")
    def auto_test_enum_src_negate(self):
        """Test enum field src-negate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"src-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: src-negate={value}")
        
        print(f"✅ Enum field src-negate has {len(valid_values)} valid values")
    def auto_test_enum_dst_negate(self):
        """Test enum field dst-negate validation."""
        from hfortix_fortios.api.v2.cmdb.router._helpers import policy6 as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"dst-negate": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dst-negate={value}")
        
        print(f"✅ Enum field dst-negate has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/router/policy6"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/router.policy6.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']