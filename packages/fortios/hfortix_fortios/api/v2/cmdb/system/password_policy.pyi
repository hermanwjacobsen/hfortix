from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PasswordPolicyPayload(TypedDict, total=False):
    """
    Type hints for system/password_policy payload fields.
    
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    **Usage:**
        payload: PasswordPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable setting a password policy for local | Default: enable
    apply_to: Literal["admin-password", "ipsec-preshared-key"]  # Apply password policy to administrator passwords o | Default: admin-password
    minimum_length: int  # Minimum password length (12 - 128, default = 12). | Default: 12 | Min: 12 | Max: 128
    min_lower_case_letter: int  # Minimum number of lowercase characters in password | Default: 1 | Min: 0 | Max: 128
    min_upper_case_letter: int  # Minimum number of uppercase characters in password | Default: 1 | Min: 0 | Max: 128
    min_non_alphanumeric: int  # Minimum number of non-alphanumeric characters in p | Default: 1 | Min: 0 | Max: 128
    min_number: int  # Minimum number of numeric characters in password | Default: 1 | Min: 0 | Max: 128
    expire_status: Literal["enable", "disable"]  # Enable/disable password expiration. | Default: disable
    expire_day: int  # Number of days after which passwords expire | Default: 90 | Min: 1 | Max: 999
    reuse_password: Literal["enable", "disable"]  # Enable/disable reuse of password. | Default: enable
    reuse_password_limit: int  # Number of times passwords can be reused | Default: 0 | Min: 0 | Max: 20
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"]  # Enable/disable administrative user login lockout u | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class PasswordPolicyResponse(TypedDict):
    """
    Type hints for system/password_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable setting a password policy for local | Default: enable
    apply_to: Literal["admin-password", "ipsec-preshared-key"]  # Apply password policy to administrator passwords o | Default: admin-password
    minimum_length: int  # Minimum password length (12 - 128, default = 12). | Default: 12 | Min: 12 | Max: 128
    min_lower_case_letter: int  # Minimum number of lowercase characters in password | Default: 1 | Min: 0 | Max: 128
    min_upper_case_letter: int  # Minimum number of uppercase characters in password | Default: 1 | Min: 0 | Max: 128
    min_non_alphanumeric: int  # Minimum number of non-alphanumeric characters in p | Default: 1 | Min: 0 | Max: 128
    min_number: int  # Minimum number of numeric characters in password | Default: 1 | Min: 0 | Max: 128
    expire_status: Literal["enable", "disable"]  # Enable/disable password expiration. | Default: disable
    expire_day: int  # Number of days after which passwords expire | Default: 90 | Min: 1 | Max: 999
    reuse_password: Literal["enable", "disable"]  # Enable/disable reuse of password. | Default: enable
    reuse_password_limit: int  # Number of times passwords can be reused | Default: 0 | Min: 0 | Max: 20
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"]  # Enable/disable administrative user login lockout u | Default: disable


@final
class PasswordPolicyObject:
    """Typed FortiObject for system/password_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable setting a password policy for locally defined | Default: enable
    status: Literal["enable", "disable"]
    # Apply password policy to administrator passwords or IPsec pr | Default: admin-password
    apply_to: Literal["admin-password", "ipsec-preshared-key"]
    # Minimum password length (12 - 128, default = 12). | Default: 12 | Min: 12 | Max: 128
    minimum_length: int
    # Minimum number of lowercase characters in password | Default: 1 | Min: 0 | Max: 128
    min_lower_case_letter: int
    # Minimum number of uppercase characters in password | Default: 1 | Min: 0 | Max: 128
    min_upper_case_letter: int
    # Minimum number of non-alphanumeric characters in password | Default: 1 | Min: 0 | Max: 128
    min_non_alphanumeric: int
    # Minimum number of numeric characters in password | Default: 1 | Min: 0 | Max: 128
    min_number: int
    # Enable/disable password expiration. | Default: disable
    expire_status: Literal["enable", "disable"]
    # Number of days after which passwords expire | Default: 90 | Min: 1 | Max: 999
    expire_day: int
    # Enable/disable reuse of password. | Default: enable
    reuse_password: Literal["enable", "disable"]
    # Number of times passwords can be reused | Default: 0 | Min: 0 | Max: 20
    reuse_password_limit: int
    # Enable/disable administrative user login lockout upon downgr | Default: disable
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> PasswordPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PasswordPolicy:
    """
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    Path: system/password_policy
    Category: cmdb
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> dict[str, Any] | FortiObject: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> PasswordPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PasswordPolicyPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        apply_to: Literal["admin-password", "ipsec-preshared-key"] | list[str] | None = ...,
        minimum_length: int | None = ...,
        min_lower_case_letter: int | None = ...,
        min_upper_case_letter: int | None = ...,
        min_non_alphanumeric: int | None = ...,
        min_number: int | None = ...,
        expire_status: Literal["enable", "disable"] | None = ...,
        expire_day: int | None = ...,
        reuse_password: Literal["enable", "disable"] | None = ...,
        reuse_password_limit: int | None = ...,
        login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "PasswordPolicy",
    "PasswordPolicyPayload",
    "PasswordPolicyResponse",
    "PasswordPolicyObject",
]