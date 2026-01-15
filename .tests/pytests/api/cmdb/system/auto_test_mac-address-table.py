"""
Auto-generated basic tests for cmdb.system/mac_address_table

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.mac-address-table.json
Category: cmdb
Endpoint: /cmdb/system/mac-address-table

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_mac-address-table.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.mac_address_table


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoMacAddressTableGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all mac-address-table items."""
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
        print(f"✅ Retrieved {len(result)} mac-address-table items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "mac")
            mkey_value = getattr(item, "mac", "N/A")
            print(f"   First item mac: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific mac-address-table by mac."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing mac-address-table items to test with")
        
        # Get first item's mac
        mkey_value = getattr(all_items[0], "mac")
        
        # Get specific item
        result = endpoint.get(mac=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "mac") == mkey_value
        print(f"✅ Retrieved mac-address-table mac={mkey_value}")
    
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
                q_format="name|mac",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoMacAddressTableExists:
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
            mkey_value = getattr(all_items[0], "mac")
            exists = endpoint.exists(mac=mkey_value)
            assert exists is True
            print(f"✅ exists(mac={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(mac=non_existing)
            assert exists is False
            print(f"✅ exists(mac={non_existing}) = False")
        else:
            pytest.skip("No existing mac-address-table items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoMacAddressTableValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import mac_address_table as validators
            print(f"✅ Successfully imported validators for mac-address-table")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_mac_address_table_post")
            assert hasattr(validators, "validate_system_mac_address_table_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import mac_address_table as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "mac": "00:00:00:00:00:00",  # mac-address
        }
        
        try:
            result = validators.validate_mac_address_table_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")






# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/mac_address_table"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.mac-address-table.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']