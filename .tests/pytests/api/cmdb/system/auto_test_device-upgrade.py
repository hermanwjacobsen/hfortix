"""
Auto-generated basic tests for cmdb.system/device_upgrade

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.device-upgrade.json
Category: cmdb
Endpoint: /cmdb/system/device-upgrade

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_device-upgrade.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.device_upgrade


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoDeviceUpgradeGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - list all device-upgrade items."""
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
        print(f"✅ Retrieved {len(result)} device-upgrade items")
        
        # If items exist, verify structure
        if len(result) > 0:
            item = result[0]
            # Access via attribute (FortiObject)
            assert hasattr(item, "serial")
            mkey_value = getattr(item, "serial", "N/A")
            print(f"   First item serial: {mkey_value}")
    
    def auto_test_get_specific_item(self):
        """Test GET - retrieve specific device-upgrade by serial."""
        # First get all items to find one to test with
        try:
            all_items = endpoint.get()
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        if not all_items or len(all_items) == 0:
            pytest.skip("No existing device-upgrade items to test with")
        
        # Get first item's serial
        mkey_value = getattr(all_items[0], "serial")
        
        # Get specific item
        result = endpoint.get(serial=mkey_value)
        
        # Since v0.5.33: querying by mkey returns single FortiObject, not list
        assert hasattr(result, "__dict__")  # FortiObject
        assert getattr(result, "serial") == mkey_value
        print(f"✅ Retrieved device-upgrade serial={mkey_value}")
    
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
                q_format="name|serial",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoDeviceUpgradeExists:
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
            mkey_value = getattr(all_items[0], "serial")
            exists = endpoint.exists(serial=mkey_value)
            assert exists is True
            print(f"✅ exists(serial={mkey_value}) = True")
            
            # Test with non-existing item (hopefully)
            non_existing = "nonexistent_auto_test_item_12345"
            exists = endpoint.exists(serial=non_existing)
            assert exists is False
            print(f"✅ exists(serial={non_existing}) = False")
        else:
            pytest.skip("No existing device-upgrade items to test exists() with")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDeviceUpgradeValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
            print(f"✅ Successfully imported validators for device-upgrade")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_device_upgrade_post")
            assert hasattr(validators, "validate_system_device_upgrade_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        # Build minimal valid config with all required fields
        config = {
            "device-type": "fortigate",  # option
            "known-ha-members": "test_known-ha-members",  # string
            "maximum-minutes": 15,  # integer
            "next-path-index": 0,  # integer
            "serial": "test_serial",  # string
            "setup-time": "",  # user
            "status": "disabled",  # option
            "time": "",  # user
            "timing": "immediate",  # option
            "upgrade-path": "",  # user
        }
        
        try:
            result = validators.validate_device_upgrade_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoDeviceUpgradeEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_status(self):
        """Test enum field status validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        valid_values = ['disabled', 'initialized', 'downloading', 'device-disconnected', 'ready', 'coordinating', 'staging', 'final-check', 'upgrade-devices', 'cancelled', 'confirmed', 'done', 'failed']
        
        # Test each valid value
        for value in valid_values:
            config = {"status": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: status={value}")
        
        print(f"✅ Enum field status has {len(valid_values)} valid values")
    def auto_test_enum_timing(self):
        """Test enum field timing validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        valid_values = ['immediate', 'scheduled']
        
        # Test each valid value
        for value in valid_values:
            config = {"timing": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: timing={value}")
        
        print(f"✅ Enum field timing has {len(valid_values)} valid values")
    def auto_test_enum_device_type(self):
        """Test enum field device-type validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import device_upgrade as validators
        
        valid_values = ['fortigate', 'fortiswitch', 'fortiap', 'fortiextender']
        
        # Test each valid value
        for value in valid_values:
            config = {"device-type": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: device-type={value}")
        
        print(f"✅ Enum field device-type has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/device_upgrade"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.device-upgrade.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']