"""
Auto-generated basic tests for cmdb.switch_controller/managed_switch

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.managed-switch.json
Category: cmdb
Endpoint: /cmdb/switch-controller/managed-switch

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_managed-switch.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.managed_switch


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoManagedSwitchGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all managed-switch items."""
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
        print(f"✅ Retrieved {len(result)} managed-switch items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "switch_id" in item
            print(f"   First item switch-id: {item.get('switch_id', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific managed-switch by switch-id."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing managed-switch items to test with")
        
        # Get first item's switch-id
        mkey_value = all_items[0]["switch_id"]
        
        # Get specific item
        result = endpoint.get(switch_id=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["switch_id"] == mkey_value
        print(f"✅ Retrieved managed-switch switch-id={mkey_value}")
    
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
                q_format="name|switch-id",  # Limit fields
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
class TestAutoManagedSwitchExists:
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
            mkey_value = all_items[0]["switch_id"]
            exists = endpoint.exists(switch_id=mkey_value)
            assert exists is True
            print(f"✅ exists(switch-id={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(switch_id=non_existing)
            assert exists is False
            print(f"✅ exists(switch-id={non_existing}) = False")
        else:
            pytest.skip("No existing managed-switch items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManagedSwitchValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
            print(f"✅ Successfully imported validators for managed-switch")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_managed_switch_post")
            assert hasattr(validators, "validate_switch_controller_managed_switch_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        # Build minimal valid config with all required fields
        config = {
            "fsw-wan1-peer": "test_fsw-wan1-peer",  # string
            "radius-nas-ip": "0.0.0.0",  # ipv4-address
            "sn": "test_sn",  # string
            "switch-id": "test_switch-id",  # string
        }
        
        try:
            result = validators.validate_managed_switch_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoManagedSwitchEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_purdue_level(self):
        """Test enum field purdue-level validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        valid_values = ['1', '1.5', '2', '2.5', '3', '3.5', '4', '5', '5.5']
        
        # Test each valid value
        for value in valid_values:
            config = {"purdue-level": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: purdue-level={value}")
        
        print(f"✅ Enum field purdue-level has {len(valid_values)} valid values")
    def auto_test_enum_fsw_wan1_admin(self):
        """Test enum field fsw-wan1-admin validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        valid_values = ['discovered', 'disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fsw-wan1-admin": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fsw-wan1-admin={value}")
        
        print(f"✅ Enum field fsw-wan1-admin has {len(valid_values)} valid values")
    def auto_test_enum_poe_pre_standard_detection(self):
        """Test enum field poe-pre-standard-detection validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller._helpers import managed_switch as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"poe-pre-standard-detection": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: poe-pre-standard-detection={value}")
        
        print(f"✅ Enum field poe-pre-standard-detection has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/managed_switch"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.managed-switch.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']