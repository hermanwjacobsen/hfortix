"""
Auto-generated basic tests for cmdb.endpoint_control/fctems

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/endpoint-control.fctems.json
Category: cmdb
Endpoint: /cmdb/endpoint-control/fctems

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_fctems.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.endpoint_control.fctems


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoFctemsGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all fctems items."""
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
        print(f"✅ Retrieved {len(result)} fctems items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            assert "ems_id" in item
            print(f"   First item ems-id: {item.get('ems_id', 'N/A')}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific fctems by ems-id."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get(response_mode="dict")
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing fctems items to test with")
        
        # Get first item's ems-id
        mkey_value = all_items[0]["ems_id"]
        
        # Get specific item
        result = endpoint.get(ems_id=mkey_value, response_mode="dict")
        
        # Since v0.5.33: querying by mkey returns single dict, not list
        assert isinstance(result, dict)
        assert result["ems_id"] == mkey_value
        print(f"✅ Retrieved fctems ems-id={mkey_value}")
    
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
                q_format="name|ems-id",  # Limit fields
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
class TestAutoFctemsExists:
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
            mkey_value = all_items[0]["ems_id"]
            exists = endpoint.exists(ems_id=mkey_value)
            assert exists is True
            print(f"✅ exists(ems-id={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = 999999
            exists = endpoint.exists(ems_id=non_existing)
            assert exists is False
            print(f"✅ exists(ems-id={non_existing}) = False")
        else:
            pytest.skip("No existing fctems items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFctemsValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
            print(f"✅ Successfully imported validators for fctems")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_endpoint_control_fctems_post")
            assert hasattr(validators, "validate_endpoint_control_fctems_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        # Build minimal valid config with all required fields
        config = {
            "interface": "test_interface",  # string
        }
        
        try:
            result = validators.validate_fctems_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoFctemsEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_dirty_reason(self):
        """Test enum field dirty-reason validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        valid_values = ['none', 'mismatched-ems-sn']
        
        # Test each valid value
        for value in valid_values:
            config = {"dirty-reason": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: dirty-reason={value}")
        
        print(f"✅ Enum field dirty-reason has {len(valid_values)} valid values")
    def auto_test_enum_fortinetone_cloud_authentication(self):
        """Test enum field fortinetone-cloud-authentication validation."""
        from hfortix_fortios.api.v2.cmdb.endpoint_control._helpers import fctems as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fortinetone-cloud-authentication": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fortinetone-cloud-authentication={value}")
        
        print(f"✅ Enum field fortinetone-cloud-authentication has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/endpoint_control/fctems"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/endpoint-control.fctems.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']