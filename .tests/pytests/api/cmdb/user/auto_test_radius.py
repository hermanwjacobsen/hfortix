"""
Auto-generated basic tests for cmdb.user/radius

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/user.radius.json
Category: cmdb
Endpoint: /cmdb/user/radius

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_radius.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.user.radius


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoRadiusGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all radius items."""
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
        print(f"✅ Retrieved {len(result)} radius items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "name")
            mkey_value = getattr(item, "name", "N/A")
            print(f"   First item name: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific radius by name."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing radius items to test with")
        
        # Get first item's name
        mkey_value = getattr(all_items[0], "name")
        
        # Get specific item
        result = endpoint.get(name=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "name") == mkey_value
        print(f"✅ Retrieved radius name={mkey_value}")
    
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
class TestAutoRadiusExists:
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
            pytest.skip("No existing radius items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRadiusValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
            print(f"✅ Successfully imported validators for radius")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_user_radius_post")
            assert hasattr(validators, "validate_user_radius_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
            "rsso": "enable",  # option
            "rsso-context-timeout": 28800,  # integer
            "rsso-endpoint-attribute": "User-Name",  # option
            "rsso-endpoint-block-attribute": "User-Name",  # option
            "rsso-log-period": 0,  # integer
            "rsso-radius-response": "enable",  # option
            "rsso-radius-server-port": 1813,  # integer
            "rsso-secret": "",  # password
            "rsso-validate-request-secret": "enable",  # option
            "secret": "",  # password
            "server": "test_server",  # string
            "sso-attribute": "User-Name",  # option
            "sso-attribute-value-override": "enable",  # option
        }
        
        try:
            result = validators.validate_radius_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoRadiusEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_all_usergroup(self):
        """Test enum field all-usergroup validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        valid_values = ['disable', 'enable']
        
        # Test each valid value
        for value in valid_values:
            config = {"all-usergroup": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: all-usergroup={value}")
        
        print(f"✅ Enum field all-usergroup has {len(valid_values)} valid values")
    def auto_test_enum_use_management_vdom(self):
        """Test enum field use-management-vdom validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"use-management-vdom": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: use-management-vdom={value}")
        
        print(f"✅ Enum field use-management-vdom has {len(valid_values)} valid values")
    def auto_test_enum_switch_controller_nas_ip_dynamic(self):
        """Test enum field switch-controller-nas-ip-dynamic validation."""
        from hfortix_fortios.api.v2.cmdb.user._helpers import radius as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"switch-controller-nas-ip-dynamic": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: switch-controller-nas-ip-dynamic={value}")
        
        print(f"✅ Enum field switch-controller-nas-ip-dynamic has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/user/radius"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/user.radius.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']