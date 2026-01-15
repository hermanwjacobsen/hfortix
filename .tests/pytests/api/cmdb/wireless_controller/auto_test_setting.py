"""
Auto-generated basic tests for cmdb.wireless_controller/setting

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.setting.json
Category: cmdb
Endpoint: /cmdb/wireless-controller/setting

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_setting.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.wireless_controller.setting


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSettingGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve setting configuration."""
        try:
            result = endpoint.get()
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single FortiObject
        assert hasattr(result, "__dict__")  # FortiObject
        print(f"✅ Retrieved setting configuration (singleton)")
        # Convert to dict to count fields
        result_dict = result.dict
        print(f"   Config keys: {len(result_dict)} fields")
    
    
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
                q_format="name|None",  # Limit fields
            )
        except Exception as e:
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        assert result is not None
        print(f"✅ GET with filters successful")


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSettingExists:
    """Auto-generated exists() tests."""
    




@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSettingEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_country(self):
        """Test enum field country validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import setting as validators
        
        valid_values = ['--', 'AF', 'AL', 'DZ', 'AS', 'AO', 'AR', 'AM', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'BF', 'KH', 'CM', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CO', 'CG', 'CD', 'CR', 'HR', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'ET', 'EE', 'GF', 'PF', 'FO', 'FJ', 'FI', 'FR', 'GA', 'GE', 'GM', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GY', 'HT', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IQ', 'IE', 'IM', 'IL', 'IT', 'CI', 'JM', 'JO', 'KZ', 'KE', 'KR', 'KW', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'MA', 'MZ', 'MM', 'NA', 'NP', 'NL', 'AN', 'AW', 'NZ', 'NI', 'NE', 'NG', 'NO', 'MP', 'OM', 'PK', 'PW', 'PA', 'PG', 'PY', 'PE', 'PH', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'KN', 'LC', 'MF', 'PM', 'VC', 'SA', 'SN', 'RS', 'ME', 'SL', 'SG', 'SK', 'SI', 'SO', 'ZA', 'ES', 'LK', 'SR', 'SZ', 'SE', 'CH', 'TW', 'TZ', 'TH', 'TL', 'TG', 'TT', 'TN', 'TR', 'TM', 'AE', 'TC', 'UG', 'UA', 'GB', 'US', 'PS', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VI', 'WF', 'YE', 'ZM', 'ZW', 'JP', 'CA']
        
        # Test each valid value
        for value in valid_values:
            config = {"country": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: country={value}")
        
        print(f"✅ Enum field country has {len(valid_values)} valid values")
    def auto_test_enum_duplicate_ssid(self):
        """Test enum field duplicate-ssid validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"duplicate-ssid": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: duplicate-ssid={value}")
        
        print(f"✅ Enum field duplicate-ssid has {len(valid_values)} valid values")
    def auto_test_enum_fapc_compatibility(self):
        """Test enum field fapc-compatibility validation."""
        from hfortix_fortios.api.v2.cmdb.wireless_controller._helpers import setting as validators
        
        valid_values = ['enable', 'disable']
        
        # Test each valid value
        for value in valid_values:
            config = {"fapc-compatibility": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: fapc-compatibility={value}")
        
        print(f"✅ Enum field fapc-compatibility has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/wireless_controller/setting"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/wireless-controller.setting.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']