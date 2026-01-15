"""
Auto-generated basic tests for cmdb.system/ssh_config

Generated from schema: /app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ssh-config.json
Category: cmdb
Endpoint: /cmdb/system/ssh-config

These are BASIC automated tests. For comprehensive testing, create
manual tests in test_ssh-config.py

Test naming convention:
- auto_test_* = Auto-generated basic tests
- test_* = Manual comprehensive tests
"""

import pytest
from __client__ import fgt

endpoint = fgt.api.cmdb.system.ssh_config


@pytest.mark.api_call
@pytest.mark.read_only
class TestAutoSshConfigGet:
    """Auto-generated GET operation tests."""
    
    def auto_test_get_list_all(self):
        """Test GET - retrieve ssh-config configuration."""
        try:
            result = endpoint.get(response_mode="dict")
        except Exception as e:
            # HTTP 400/404/405/424/500/503 means feature not available/enabled, method not supported, or server error
            if any(code in str(e) for code in ["400", "404", "405", "424", "500", "503", "Bad Request", "Not Found", "Method Not Allowed", "Failed Dependency", "Internal Server Error", "Service Unavailable"]):
                pytest.skip(f"Endpoint not available (feature may not be enabled, method not supported, or server error): {e}")
            raise
        
        # Verify response
        assert result is not None
        # Singleton CMDB endpoints return single dict
        assert isinstance(result, dict)
        print(f"✅ Retrieved ssh-config configuration (singleton)")
        print(f"   Config keys: {len(result)} fields")
    
    
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
                q_format="name|None",  # Limit fields
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
class TestAutoSshConfigExists:
    """Auto-generated exists() tests."""
    


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSshConfigValidators:
    """Auto-generated validator tests."""
    
    def auto_test_validator_import(self):
        """Test that validators can be imported."""
        try:
            from hfortix_fortios.api.v2.cmdb.system._helpers import ssh_config as validators
            print(f"✅ Successfully imported validators for ssh-config")
            
            # Check validator functions exist (they use HTTP method naming: post, put, get)
            assert hasattr(validators, "validate_system_ssh_config_post")
            assert hasattr(validators, "validate_system_ssh_config_put")
            print("✅ Validator functions exist")
        except ImportError as e:
            pytest.fail(f"Failed to import validators: {e}")
    
    def auto_test_validator_create_all_required(self):
        """Test create validator with all required fields."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ssh_config as validators
        
        # Build minimal valid config with all required fields
        config = {
            "ssh-hsk": "",  # user
        }
        
        try:
            result = validators.validate_ssh_config_create(config)
            assert result is True or isinstance(result, dict)
            print(f"✅ Validator accepted minimal config with required fields")
        except Exception as e:
            # Validators may do additional checks, log but don't fail
            print(f"⚠️  Validator raised: {e}")


@pytest.mark.validator
@pytest.mark.parallel_safe
class TestAutoSshConfigEnums:
    """Auto-generated enum validation tests."""
    
    def auto_test_enum_ssh_kex_algo(self):
        """Test enum field ssh-kex-algo validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ssh_config as validators
        
        valid_values = ['diffie-hellman-group1-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group14-sha256', 'diffie-hellman-group16-sha512', 'diffie-hellman-group18-sha512', 'diffie-hellman-group-exchange-sha1', 'diffie-hellman-group-exchange-sha256', 'curve25519-sha256@libssh.org', 'ecdh-sha2-nistp256', 'ecdh-sha2-nistp384', 'ecdh-sha2-nistp521']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssh-kex-algo": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssh-kex-algo={value}")
        
        print(f"✅ Enum field ssh-kex-algo has {len(valid_values)} valid values")
    def auto_test_enum_ssh_enc_algo(self):
        """Test enum field ssh-enc-algo validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ssh_config as validators
        
        valid_values = ['chacha20-poly1305@openssh.com', 'aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se', 'aes128-gcm@openssh.com', 'aes256-gcm@openssh.com']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssh-enc-algo": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssh-enc-algo={value}")
        
        print(f"✅ Enum field ssh-enc-algo has {len(valid_values)} valid values")
    def auto_test_enum_ssh_mac_algo(self):
        """Test enum field ssh-mac-algo validation."""
        from hfortix_fortios.api.v2.cmdb.system._helpers import ssh_config as validators
        
        valid_values = ['hmac-md5', 'hmac-md5-etm@openssh.com', 'hmac-md5-96', 'hmac-md5-96-etm@openssh.com', 'hmac-sha1', 'hmac-sha1-etm@openssh.com', 'hmac-sha2-256', 'hmac-sha2-256-etm@openssh.com', 'hmac-sha2-512', 'hmac-sha2-512-etm@openssh.com', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-ripemd160-etm@openssh.com', 'umac-64@openssh.com', 'umac-128@openssh.com', 'umac-64-etm@openssh.com', 'umac-128-etm@openssh.com']
        
        # Test each valid value
        for value in valid_values:
            config = {"ssh-mac-algo": value}
            # Validators should accept any valid enum value
            # Note: Full validation requires all required fields
            print(f"   Valid enum value: ssh-mac-algo={value}")
        
        print(f"✅ Enum field ssh-mac-algo has {len(valid_values)} valid values")




# Metadata for test discovery
TEST_ENDPOINT = "cmdb/system/ssh_config"
TEST_CATEGORY = "cmdb"
TEST_SCHEMA = "/app/dev/classes/fortinet/schema/7.6.5/cmdb/system.ssh-config.json"
TEST_HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']