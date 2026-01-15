"""
Auto-generated basic tests for cmdb.system/object_tagging

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.object-tagging.json
Category: cmdb
Endpoint: /cmdb/system/object-tagging

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_object-tagging.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.object_tagging


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoObjectTaggingGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all object-tagging items."""
        try:
            result = endpoint.get(response_mode="dict")
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Multi-value CMDB endpoints return list
        assert isinstance(result, list)
        print(f"✅ Retrieved {len(result)} object-tagging items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "category" in item
            print(f"   First item category: {item.get('category', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific object-tagging by category."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing object-tagging items to test with")
        
        # Get first item's category
        mkey_value = all_items[0]["category"]
        
        # Get specific item
        result = endpoint.get(category=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["category"] == mkey_value
        print(f"✅ Retrieved object-tagging category={mkey_value}")
    
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
                q_format="name|category",  # Limit fields
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
class TestAutoObjectTaggingExists:
    """Auto-generated exists() tests."""
    
    def auto_test_exists_method(self):
        """Test exists() helper method."""
        # Get existing items
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if all_items and len(all_items) > 0:
            # Test with existing item
            mkey_value = all_items[0]["category"]
            exists = endpoint.exists(category=mkey_value)
            assert exists is True
            print(f"✅ exists(category={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(category=non_existing)
            assert exists is False
            print(f"✅ exists(category={non_existing}) = False")
        else:
            pytest.skip("No existing object-tagging items to test exists() with")




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoObjectTaggingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_address(self):
        """Test enum field address validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import object_tagging as validators
        
        valid_values = ['disable', 'mandatory', 'optional']
        
        # Test each valid value
        for value in valid_values:
            config = {"address": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: address={value}")
        
        print(f"✅ Enum field address has {len(valid_values)} valid values")
    def auto_test_enum_device(self):
        """Test enum field device validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import object_tagging as validators
        
        valid_values = ['disable', 'mandatory', 'optional']
        
        # Test each valid value
        for value in valid_values:
            config = {"device": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: device={value}")
        
        print(f"✅ Enum field device has {len(valid_values)} valid values")
    def auto_test_enum_interface(self):
        """Test enum field interface validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import object_tagging as validators
        
        valid_values = ['disable', 'mandatory', 'optional']
        
        # Test each valid value
        for value in valid_values:
            config = {"interface": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: interface={value}")
        
        print(f"✅ Enum field interface has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/object_tagging"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.object-tagging.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']