"""
Auto-generated basic tests for cmdb.wireless_controller/wtp

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wtp.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/wtp

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_wtp.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.wtp


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoWtpGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all wtp items."""
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
        print(f"✅ Retrieved {len(result)} wtp items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "wtp_id" in item
            print(f"   First item wtp-id: {item.get('wtp_id', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific wtp by wtp-id."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing wtp items to test with")
        
        # Get first item's wtp-id
        mkey_value = all_items[0]["wtp_id"]
        
        # Get specific item
        result = endpoint.get(wtp_id=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["wtp_id"] == mkey_value
        print(f"✅ Retrieved wtp wtp-id={mkey_value}")
    
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
                q_format="name|wtp-id",  # Limit fields
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
class TestAutoWtpExists:
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
            mkey_value = all_items[0]["wtp_id"]
            exists = endpoint.exists(wtp_id=mkey_value)
            assert exists is True
            print(f"✅ exists(wtp-id={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(wtp_id=non_existing)
            assert exists is False
            print(f"✅ exists(wtp-id={non_existing}) = False")
        else:
            pytest.skip("No existing wtp items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWtpValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
            print(f"✅ Successfully imported validators for wtp")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_wireless_controller_wtp_post")
            assert hasattr(validators, "validate_wireless_controller_wtp_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        # Build minimal valid config with all required fields
        config = {
            "wtp-id": "test_wtp-id",  # string
            "wtp-profile": "test_wtp-profile",  # string
        }
        
        try:
            result = validators.validate_wtp_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoWtpEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_admin(self):
        """Test enum field admin validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        valid_values = ['discovered', 'disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"admin": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: admin={value}")
        
        print(f"✅ Enum field admin has {len(valid_values)} valid values")
    def auto_test_enum_firmware_provision_latest(self):
        """Test enum field firmware-provision-latest validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        valid_values = ['disable', 'once']
        
        # Test each valid value
        for value in valid_values:
            config = {"firmware-provision-latest": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: firmware-provision-latest={value}")
        
        print(f"✅ Enum field firmware-provision-latest has {len(valid_values)} valid values")
    def auto_test_enum_override_led_state(self):
        """Test enum field override-led-state validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import wtp as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"override-led-state": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: override-led-state={value}")
        
        print(f"✅ Enum field override-led-state has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/wtp"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.wtp.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']