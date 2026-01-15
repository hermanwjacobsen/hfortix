from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SshConfigPayload(TypedDict, total=False):
    """
    Type hints for system/ssh_config payload fields.
    
    Configure SSH config.
    
    **Usage:**
        payload: SshConfigPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"]  # Select one or more SSH kex algorithms. | Default: diffie-hellman-group14-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group-exchange-sha256 curve25519-sha256@libssh.org ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521
    ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"]  # Select one or more SSH ciphers. | Default: aes256-ctr aes256-gcm@openssh.com
    ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"]  # Select one or more SSH MAC algorithms. | Default: hmac-sha2-256 hmac-sha2-256-etm@openssh.com hmac-sha2-512 hmac-sha2-512-etm@openssh.com
    ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"]  # Select one or more SSH hostkey algorithms. | Default: ecdsa-sha2-nistp521 ecdsa-sha2-nistp384 ecdsa-sha2-nistp256 rsa-sha2-256 rsa-sha2-512 ssh-ed25519
    ssh_hsk_override: Literal["disable", "enable"]  # Enable/disable SSH host key override in SSH daemon | Default: disable
    ssh_hsk_password: str  # Password for ssh-hostkey. | MaxLen: 128
    ssh_hsk: str  # Config SSH host key.

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SshConfigResponse(TypedDict):
    """
    Type hints for system/ssh_config API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"]  # Select one or more SSH kex algorithms. | Default: diffie-hellman-group14-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group-exchange-sha256 curve25519-sha256@libssh.org ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521
    ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"]  # Select one or more SSH ciphers. | Default: aes256-ctr aes256-gcm@openssh.com
    ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"]  # Select one or more SSH MAC algorithms. | Default: hmac-sha2-256 hmac-sha2-256-etm@openssh.com hmac-sha2-512 hmac-sha2-512-etm@openssh.com
    ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"]  # Select one or more SSH hostkey algorithms. | Default: ecdsa-sha2-nistp521 ecdsa-sha2-nistp384 ecdsa-sha2-nistp256 rsa-sha2-256 rsa-sha2-512 ssh-ed25519
    ssh_hsk_override: Literal["disable", "enable"]  # Enable/disable SSH host key override in SSH daemon | Default: disable
    ssh_hsk_password: str  # Password for ssh-hostkey. | MaxLen: 128
    ssh_hsk: str  # Config SSH host key.


@final
class SshConfigObject:
    """Typed FortiObject for system/ssh_config with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Select one or more SSH kex algorithms. | Default: diffie-hellman-group14-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group-exchange-sha256 curve25519-sha256@libssh.org ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521
    ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"]
    # Select one or more SSH ciphers. | Default: aes256-ctr aes256-gcm@openssh.com
    ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"]
    # Select one or more SSH MAC algorithms. | Default: hmac-sha2-256 hmac-sha2-256-etm@openssh.com hmac-sha2-512 hmac-sha2-512-etm@openssh.com
    ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"]
    # Select one or more SSH hostkey algorithms. | Default: ecdsa-sha2-nistp521 ecdsa-sha2-nistp384 ecdsa-sha2-nistp256 rsa-sha2-256 rsa-sha2-512 ssh-ed25519
    ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"]
    # Enable/disable SSH host key override in SSH daemon. | Default: disable
    ssh_hsk_override: Literal["disable", "enable"]
    # Password for ssh-hostkey. | MaxLen: 128
    ssh_hsk_password: str
    # Config SSH host key.
    ssh_hsk: str
    
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
    def to_dict(self) -> SshConfigPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SshConfig:
    """
    Configure SSH config.
    
    Path: system/ssh_config
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject: ...
    
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
    ) -> SshConfigObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | list[str] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | list[str] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | list[str] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | list[str] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SshConfigObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | list[str] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | list[str] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | list[str] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | list[str] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | list[str] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | list[str] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | list[str] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | list[str] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | list[str] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | list[str] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | list[str] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | list[str] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SshConfigPayload | None = ...,
        ssh_kex_algo: Literal["diffie-hellman-group1-sha1", "diffie-hellman-group14-sha1", "diffie-hellman-group14-sha256", "diffie-hellman-group16-sha512", "diffie-hellman-group18-sha512", "diffie-hellman-group-exchange-sha1", "diffie-hellman-group-exchange-sha256", "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256", "ecdh-sha2-nistp384", "ecdh-sha2-nistp521"] | list[str] | None = ...,
        ssh_enc_algo: Literal["chacha20-poly1305@openssh.com", "aes128-ctr", "aes192-ctr", "aes256-ctr", "arcfour256", "arcfour128", "aes128-cbc", "3des-cbc", "blowfish-cbc", "cast128-cbc", "aes192-cbc", "aes256-cbc", "arcfour", "rijndael-cbc@lysator.liu.se", "aes128-gcm@openssh.com", "aes256-gcm@openssh.com"] | list[str] | None = ...,
        ssh_mac_algo: Literal["hmac-md5", "hmac-md5-etm@openssh.com", "hmac-md5-96", "hmac-md5-96-etm@openssh.com", "hmac-sha1", "hmac-sha1-etm@openssh.com", "hmac-sha2-256", "hmac-sha2-256-etm@openssh.com", "hmac-sha2-512", "hmac-sha2-512-etm@openssh.com", "hmac-ripemd160", "hmac-ripemd160@openssh.com", "hmac-ripemd160-etm@openssh.com", "umac-64@openssh.com", "umac-128@openssh.com", "umac-64-etm@openssh.com", "umac-128-etm@openssh.com"] | list[str] | None = ...,
        ssh_hsk_algo: Literal["ssh-rsa", "ecdsa-sha2-nistp521", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp256", "rsa-sha2-256", "rsa-sha2-512", "ssh-ed25519"] | list[str] | None = ...,
        ssh_hsk_override: Literal["disable", "enable"] | None = ...,
        ssh_hsk_password: str | None = ...,
        ssh_hsk: str | None = ...,
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
    "SshConfig",
    "SshConfigPayload",
    "SshConfigResponse",
    "SshConfigObject",
]