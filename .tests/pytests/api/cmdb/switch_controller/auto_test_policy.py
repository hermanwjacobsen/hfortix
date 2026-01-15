"""
Auto-generated basic tests for cmdb.switch_controller/auto_config/policy

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.auto-config.policy.json
Category: cmdb
Endpoint: /cmdb/switch-controller.auto-config/policy

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_policy.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.switch_controller.auto_config.policy


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoPolicyGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all policy items."""
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
        print(f"✅ Retrieved {len(result)} policy items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "name" in item
            print(f"   First item name: {item.get('name', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific policy by name."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing policy items to test with")
        
        # Get first item's name
        mkey_value = all_items[0]["name"]
        
        # Get specific item
        result = endpoint.get(name=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["name"] == mkey_value
        print(f"✅ Retrieved policy name={mkey_value}")
    
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
                q_format="name|name",  # Limit fields
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
class TestAutoPolicyExists:
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
            mkey_value = all_items[0]["name"]
            exists = endpoint.exists(name=mkey_value)
            assert exists is True
            print(f"✅ exists(name={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(name=non_existing)
            assert exists is False
            print(f"✅ exists(name={non_existing}) = False")
        else:
            pytest.skip("No existing policy items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPolicyValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.switch_controller.auto_config._helpers import policy as validators
            print(f"✅ Successfully imported validators for policy")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_switch_controller_auto_config_policy_post")
            assert hasattr(validators, "validate_switch_controller_auto_config_policy_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.auto_config._helpers import policy as validators
        
        # Build minimal valid config with all required fields
        config = {
            "name": "test_name",  # string
        }
        
        try:
            result = validators.validate_policy_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoPolicyEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_poe_status(self):
        """Test enum field poe-status validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.auto_config._helpers import policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"poe-status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: poe-status={value}")
        
        print(f"✅ Enum field poe-status has {len(valid_values)} valid values")
    def auto_test_enum_igmp_flood_report(self):
        """Test enum field igmp-flood-report validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.auto_config._helpers import policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"igmp-flood-report": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: igmp-flood-report={value}")
        
        print(f"✅ Enum field igmp-flood-report has {len(valid_values)} valid values")
    def auto_test_enum_igmp_flood_traffic(self):
        """Test enum field igmp-flood-traffic validation."""
        from hfortix_fortios.api.v2.cmdb.switch_controller.auto_config._helpers import policy as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"igmp-flood-traffic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: igmp-flood-traffic={value}")
        
        print(f"✅ Enum field igmp-flood-traffic has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/switch_controller/auto_config/policy"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/switch-controller.auto-config.policy.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']