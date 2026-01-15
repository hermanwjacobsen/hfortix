import sys
from pathlib import Path

# Add local packages to path FIRST (before pip installed versions)
# This ensures we test against local development code, not installed packages
# Path: .tests/__client__.py -> parent = workspace root
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root / "packages" / "core"))
sys.path.insert(0, str(repo_root / "packages" / "fortios"))

from hfortix_fortios import FortiOS

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")

# Disable circuit breaker for testing by setting a very high threshold
# This allows tests to run without being blocked by protective circuit breaker
fgt: FortiOS = FortiOS(
    host="192.168.1.99", 
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1", 
    port=443, 
    verify=False, 
    error_mode="return", 
    vdom="test",  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1  # Short timeout if it does trigger
)
fgt_ResponseModeObject: FortiOS = FortiOS(
    host="192.168.1.99", 
    token="3f8a1c9d2e7b40561938c7f2d0e5b6a1", 
    port=443, 
    verify=False, 
    error_mode="return", 
    vdom="test",  # Use test VDOM for testing (super_admin token has access to all VDOMs)
    circuit_breaker_threshold=99999999,  # Effectively disable circuit breaker for tests
    circuit_breaker_timeout=1,  # Short timeout if it does trigger
    response_mode="object",
)