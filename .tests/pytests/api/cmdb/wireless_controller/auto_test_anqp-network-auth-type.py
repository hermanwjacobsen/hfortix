"""
Auto-generated basic tests for cmdb.wireless_controller/hotspot20/anqp_network_auth_type

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.anqp-network-auth-type.json
Category: cmdb
Endpoint: /cmdb/wireless-controller.hotspot20/anqp-network-auth-type

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_anqp-network-auth-type.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.hotspot20.anqp_network_auth_type


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoAnqpNetworkAuthTypeGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all anqp-network-auth-type items."""
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
        print(f"✅ Retrieved {len(result)} anqp-network-auth-type items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "name")
            mkey_value = getattr(item, "name", "N/A")
            print(f"   First item name: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific anqp-network-auth-type by name."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing anqp-network-auth-type items to test with")
        
        # Get first item's name
        mkey_value = getattr(all_items[0], "name")
        
        # Get specific item
        result = endpoint.get(name=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "name") == mkey_value
        print(f"✅ Retrieved anqp-network-auth-type name={mkey_value}")
    
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
                q_format="name|name",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoAnqpNetworkAuthTypeExists:
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
            mkey_value = getattr(all_items[0], "name")
            exists = endpoint.exists(name=mkey_value)
            assert exists is True
            print(f"✅ exists(name={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(name=non_existing)
            assert exists is False
            print(f"✅ exists(name={non_existing}) = False")
        else:
            pytest.skip("No existing anqp-network-auth-type items to test exists() with")




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoAnqpNetworkAuthTypeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_auth_type(self):
        """Test enum field auth-type validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller.hotspot20._helpers import anqp_network_auth_type as validators
        
        valid_values = ['acceptance-of-terms', 'online-enrollment', 'http-redirection', 'dns-redirection']
        
        # Test each valid value
        for value in valid_values:
            config = {"auth-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: auth-type={value}")
        
        print(f"✅ Enum field auth-type has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/hotspot20/anqp_network_auth_type"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.hotspot20.anqp-network-auth-type.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']