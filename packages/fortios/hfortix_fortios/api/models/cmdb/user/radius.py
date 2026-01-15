"""
Pydantic Models for CMDB - user/radius

Runtime validation models for user/radius configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class RadiusClass(BaseModel):
    """
    Child table model for class.
    
    Class attribute name(s).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Class name.")
class RadiusAccountingServer(BaseModel):
    """
    Child table model for accounting-server.
    
    Additional accounting servers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID (0 - 4294967295).")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    server: str = Field(max_length=63, default="", description="Server CN domain name or IP address.")    
    secret: Any = Field(max_length=128, description="Secret key.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="RADIUS accounting port number.")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for communications to the RADIUS server.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class RadiusAuth_typeEnum(str, Enum):
    """Allowed values for auth_type field."""
    AUTO = "auto"    MS_CHAP_V2 = "ms_chap_v2"    MS_CHAP = "ms_chap"    CHAP = "chap"    PAP = "pap"
class RadiusMac_username_delimiterEnum(str, Enum):
    """Allowed values for mac_username_delimiter field."""
    HYPHEN = "hyphen"    SINGLE_HYPHEN = "single-hyphen"    COLON = "colon"    NONE = "none"
class RadiusMac_password_delimiterEnum(str, Enum):
    """Allowed values for mac_password_delimiter field."""
    HYPHEN = "hyphen"    SINGLE_HYPHEN = "single-hyphen"    COLON = "colon"    NONE = "none"
class RadiusSwitch_controller_service_typeEnum(str, Enum):
    """Allowed values for switch_controller_service_type field."""
    LOGIN = "login"    FRAMED = "framed"    CALLBACK_LOGIN = "callback-login"    CALLBACK_FRAMED = "callback-framed"    OUTBOUND = "outbound"    ADMINISTRATIVE = "administrative"    NAS_PROMPT = "nas-prompt"    AUTHENTICATE_ONLY = "authenticate-only"    CALLBACK_NAS_PROMPT = "callback-nas-prompt"    CALL_CHECK = "call-check"    CALLBACK_ADMINISTRATIVE = "callback-administrative"
class RadiusTls_min_proto_versionEnum(str, Enum):
    """Allowed values for tls_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"
class RadiusAccount_key_cert_fieldEnum(str, Enum):
    """Allowed values for account_key_cert_field field."""
    OTHERNAME = "othername"    RFC822NAME = "rfc822name"    DNSNAME = "dnsname"    CN = "cn"
class RadiusRsso_endpoint_attributeEnum(str, Enum):
    """Allowed values for rsso_endpoint_attribute field."""
    USER_NAME = "User-Name"    NAS_IP_ADDRESS = "NAS-IP-Address"    FRAMED_IP_ADDRESS = "Framed-IP-Address"    FRAMED_IP_NETMASK = "Framed-IP-Netmask"    FILTER_ID = "Filter-Id"    LOGIN_IP_HOST = "Login-IP-Host"    REPLY_MESSAGE = "Reply-Message"    CALLBACK_NUMBER = "Callback-Number"    CALLBACK_ID = "Callback-Id"    FRAMED_ROUTE = "Framed-Route"    FRAMED_IPX_NETWORK = "Framed-IPX-Network"    CLASS = "Class"    CALLED_STATION_ID = "Called-Station-Id"    CALLING_STATION_ID = "Calling-Station-Id"    NAS_IDENTIFIER = "NAS-Identifier"    PROXY_STATE = "Proxy-State"    LOGIN_LAT_SERVICE = "Login-LAT-Service"    LOGIN_LAT_NODE = "Login-LAT-Node"    LOGIN_LAT_GROUP = "Login-LAT-Group"    FRAMED_APPLETALK_ZONE = "Framed-AppleTalk-Zone"    ACCT_SESSION_ID = "Acct-Session-Id"    ACCT_MULTI_SESSION_ID = "Acct-Multi-Session-Id"
class RadiusRsso_endpoint_block_attributeEnum(str, Enum):
    """Allowed values for rsso_endpoint_block_attribute field."""
    USER_NAME = "User-Name"    NAS_IP_ADDRESS = "NAS-IP-Address"    FRAMED_IP_ADDRESS = "Framed-IP-Address"    FRAMED_IP_NETMASK = "Framed-IP-Netmask"    FILTER_ID = "Filter-Id"    LOGIN_IP_HOST = "Login-IP-Host"    REPLY_MESSAGE = "Reply-Message"    CALLBACK_NUMBER = "Callback-Number"    CALLBACK_ID = "Callback-Id"    FRAMED_ROUTE = "Framed-Route"    FRAMED_IPX_NETWORK = "Framed-IPX-Network"    CLASS = "Class"    CALLED_STATION_ID = "Called-Station-Id"    CALLING_STATION_ID = "Calling-Station-Id"    NAS_IDENTIFIER = "NAS-Identifier"    PROXY_STATE = "Proxy-State"    LOGIN_LAT_SERVICE = "Login-LAT-Service"    LOGIN_LAT_NODE = "Login-LAT-Node"    LOGIN_LAT_GROUP = "Login-LAT-Group"    FRAMED_APPLETALK_ZONE = "Framed-AppleTalk-Zone"    ACCT_SESSION_ID = "Acct-Session-Id"    ACCT_MULTI_SESSION_ID = "Acct-Multi-Session-Id"
class RadiusSso_attributeEnum(str, Enum):
    """Allowed values for sso_attribute field."""
    USER_NAME = "User-Name"    NAS_IP_ADDRESS = "NAS-IP-Address"    FRAMED_IP_ADDRESS = "Framed-IP-Address"    FRAMED_IP_NETMASK = "Framed-IP-Netmask"    FILTER_ID = "Filter-Id"    LOGIN_IP_HOST = "Login-IP-Host"    REPLY_MESSAGE = "Reply-Message"    CALLBACK_NUMBER = "Callback-Number"    CALLBACK_ID = "Callback-Id"    FRAMED_ROUTE = "Framed-Route"    FRAMED_IPX_NETWORK = "Framed-IPX-Network"    CLASS = "Class"    CALLED_STATION_ID = "Called-Station-Id"    CALLING_STATION_ID = "Calling-Station-Id"    NAS_IDENTIFIER = "NAS-Identifier"    PROXY_STATE = "Proxy-State"    LOGIN_LAT_SERVICE = "Login-LAT-Service"    LOGIN_LAT_NODE = "Login-LAT-Node"    LOGIN_LAT_GROUP = "Login-LAT-Group"    FRAMED_APPLETALK_ZONE = "Framed-AppleTalk-Zone"    ACCT_SESSION_ID = "Acct-Session-Id"    ACCT_MULTI_SESSION_ID = "Acct-Multi-Session-Id"
class RadiusRsso_log_flagsEnum(str, Enum):
    """Allowed values for rsso_log_flags field."""
    PROTOCOL_ERROR = "protocol-error"    PROFILE_MISSING = "profile-missing"    ACCOUNTING_STOP_MISSED = "accounting-stop-missed"    ACCOUNTING_EVENT = "accounting-event"    ENDPOINT_BLOCK = "endpoint-block"    RADIUSD_OTHER = "radiusd-other"    NONE = "none"

# ============================================================================
# Main Model
# ============================================================================

class RadiusModel(BaseModel):
    """
    Pydantic model for user/radius configuration.
    
    Configure RADIUS server entries.
    
    Validation Rules:        - name: max_length=35 pattern=        - server: max_length=63 pattern=        - secret: max_length=128 pattern=        - secondary_server: max_length=63 pattern=        - secondary_secret: max_length=128 pattern=        - tertiary_server: max_length=63 pattern=        - tertiary_secret: max_length=128 pattern=        - timeout: min=1 max=300 pattern=        - status_ttl: min=0 max=600 pattern=        - all_usergroup: pattern=        - use_management_vdom: pattern=        - switch_controller_nas_ip_dynamic: pattern=        - nas_ip: pattern=        - nas_id_type: pattern=        - call_station_id_type: pattern=        - nas_id: max_length=255 pattern=        - acct_interim_interval: min=60 max=86400 pattern=        - radius_coa: pattern=        - radius_port: min=0 max=65535 pattern=        - h3c_compatibility: pattern=        - auth_type: pattern=        - source_ip: max_length=63 pattern=        - source_ip_interface: max_length=15 pattern=        - username_case_sensitive: pattern=        - group_override_attr_type: pattern=        - class_: pattern=        - password_renewal: pattern=        - require_message_authenticator: pattern=        - password_encoding: pattern=        - mac_username_delimiter: pattern=        - mac_password_delimiter: pattern=        - mac_case: pattern=        - acct_all_servers: pattern=        - switch_controller_acct_fast_framedip_detect: min=2 max=600 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - switch_controller_service_type: pattern=        - transport_protocol: pattern=        - tls_min_proto_version: pattern=        - ca_cert: max_length=79 pattern=        - client_cert: max_length=35 pattern=        - server_identity_check: pattern=        - account_key_processing: pattern=        - account_key_cert_field: pattern=        - rsso: pattern=        - rsso_radius_server_port: min=0 max=65535 pattern=        - rsso_radius_response: pattern=        - rsso_validate_request_secret: pattern=        - rsso_secret: max_length=31 pattern=        - rsso_endpoint_attribute: pattern=        - rsso_endpoint_block_attribute: pattern=        - sso_attribute: pattern=        - sso_attribute_key: max_length=35 pattern=        - sso_attribute_value_override: pattern=        - rsso_context_timeout: min=0 max=4294967295 pattern=        - rsso_log_period: min=0 max=4294967295 pattern=        - rsso_log_flags: pattern=        - rsso_flush_ip_session: pattern=        - rsso_ep_one_ip_only: pattern=        - delimiter: pattern=        - accounting_server: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="RADIUS server entry name.")    
    server: str = Field(max_length=63, default="", description="Primary RADIUS server CN domain name or IP address.")    
    secret: Any = Field(max_length=128, description="Pre-shared secret key used to access the primary RADIUS server.")    
    secondary_server: str | None = Field(max_length=63, default="", description="Secondary RADIUS CN domain name or IP address.")    
    secondary_secret: Any = Field(max_length=128, default=None, description="Secret key to access the secondary server.")    
    tertiary_server: str | None = Field(max_length=63, default="", description="Tertiary RADIUS CN domain name or IP address.")    
    tertiary_secret: Any = Field(max_length=128, default=None, description="Secret key to access the tertiary server.")    
    timeout: int | None = Field(ge=1, le=300, default=5, description="Time in seconds to retry connecting server.")    
    status_ttl: int | None = Field(ge=0, le=600, default=300, description="Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).")    
    all_usergroup: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable automatically including this RADIUS server in all user groups.")    
    use_management_vdom: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using management VDOM to send requests.")    
    switch_controller_nas_ip_dynamic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/Disable switch-controller nas-ip dynamic to dynamically set nas-ip.")    
    nas_ip: str | None = Field(default="0.0.0.0", description="IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes.")    
    nas_id_type: Literal["legacy", "custom", "hostname"] | None = Field(default="legacy", description="NAS identifier type configuration (default = legacy).")    
    call_station_id_type: Literal["legacy", "IP", "MAC"] | None = Field(default="legacy", description="Calling & Called station identifier type configuration (default = legacy), this option is not available for 802.1x authentication. ")    
    nas_id: str | None = Field(max_length=255, default="", description="Custom NAS identifier.")    
    acct_interim_interval: int | None = Field(ge=60, le=86400, default=0, description="Time in seconds between each accounting interim update message.")    
    radius_coa: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated.")    
    radius_port: int | None = Field(ge=0, le=65535, default=0, description="RADIUS service port number.")    
    h3c_compatibility: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.")    
    auth_type: AuthTypeEnum | None = Field(default="auto", description="Authentication methods/protocols permitted for this RADIUS server.")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for communications to the RADIUS server.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="Source interface for communication with the RADIUS server.")  # datasource: ['system.interface.name']    
    username_case_sensitive: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable case sensitive user names.")    
    group_override_attr_type: Literal["filter-Id", "class"] | None = Field(default="", description="RADIUS attribute type to override user group information.")    
    class_: list[Class] = Field(default=None, description="Class attribute name(s).")    
    password_renewal: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable password renewal.")    
    require_message_authenticator: Literal["enable", "disable"] | None = Field(default="enable", description="Require message authenticator in authentication response.")    
    password_encoding: Literal["auto", "ISO-8859-1"] | None = Field(default="auto", description="Password encoding.")    
    mac_username_delimiter: MacUsernameDelimiterEnum | None = Field(default="hyphen", description="MAC authentication username delimiter (default = hyphen).")    
    mac_password_delimiter: MacPasswordDelimiterEnum | None = Field(default="hyphen", description="MAC authentication password delimiter (default = hyphen).")    
    mac_case: Literal["uppercase", "lowercase"] | None = Field(default="lowercase", description="MAC authentication case (default = lowercase).")    
    acct_all_servers: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending of accounting messages to all configured servers (default = disable).")    
    switch_controller_acct_fast_framedip_detect: int | None = Field(ge=2, le=600, default=2, description="Switch controller accounting message Framed-IP detection from DHCP snooping (seconds, default=2).")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    switch_controller_service_type: list[SwitchControllerServiceType] = Field(default="", description="RADIUS service type.")    
    transport_protocol: Literal["udp", "tcp", "tls"] | None = Field(default="udp", description="Transport protocol to be used (default = udp).")    
    tls_min_proto_version: TlsMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for TLS connections (default is to follow system global setting).")    
    ca_cert: str | None = Field(max_length=79, default="", description="CA of server to trust under TLS.")  # datasource: ['vpn.certificate.ca.name']    
    client_cert: str | None = Field(max_length=35, default="", description="Client certificate to use under TLS.")  # datasource: ['vpn.certificate.local.name']    
    server_identity_check: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable RADIUS server identity check (verify server domain name/IP address against the server certificate).")    
    account_key_processing: Literal["same", "strip"] | None = Field(default="same", description="Account key processing operation. The FortiGate will keep either the whole domain or strip the domain from the subject identity.")    
    account_key_cert_field: AccountKeyCertFieldEnum | None = Field(default="othername", description="Define subject identity field in certificate for user access right checking.")    
    rsso: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable RADIUS based single sign on feature.")    
    rsso_radius_server_port: int = Field(ge=0, le=65535, default=1813, description="UDP port to listen on for RADIUS Start and Stop records.")    
    rsso_radius_response: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable sending RADIUS response packets after receiving Start and Stop records.")    
    rsso_validate_request_secret: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable validating the RADIUS request shared secret in the Start or End record.")    
    rsso_secret: Any = Field(max_length=31, description="RADIUS secret used by the RADIUS accounting server.")    
    rsso_endpoint_attribute: RssoEndpointAttributeEnum = Field(default="Calling-Station-Id", description="RADIUS attributes used to extract the user end point identifier from the RADIUS Start record.")    
    rsso_endpoint_block_attribute: RssoEndpointBlockAttributeEnum = Field(default="", description="RADIUS attributes used to block a user.")    
    sso_attribute: SsoAttributeEnum = Field(default="Class", description="RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.")    
    sso_attribute_key: str | None = Field(max_length=35, default="", description="Key prefix for SSO group value in the SSO attribute.")    
    sso_attribute_value_override: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable override old attribute value with new value for the same endpoint.")    
    rsso_context_timeout: int = Field(ge=0, le=4294967295, default=28800, description="Time in seconds before the logged out user is removed from the \"user context list\" of logged on users.")    
    rsso_log_period: int = Field(ge=0, le=4294967295, default=0, description="Time interval in seconds that group event log messages will be generated for dynamic profile events.")    
    rsso_log_flags: list[RssoLogFlags] = Field(default="protocol-error profile-missing accounting-stop-missed accounting-event endpoint-block radiusd-other", description="Events to log.")    
    rsso_flush_ip_session: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.")    
    rsso_ep_one_ip_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.")    
    delimiter: Literal["plus", "comma"] | None = Field(default="plus", description="Configure delimiter to be used for separating profile group names in the SSO attribute (default = plus character \"+\").")    
    accounting_server: list[AccountingServer] = Field(default=None, description="Additional accounting servers.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('source_ip_interface')
    @classmethod
    def validate_source_ip_interface(cls, v: Any) -> Any:
        """
        Validate source_ip_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ca_cert')
    @classmethod
    def validate_ca_cert(cls, v: Any) -> Any:
        """
        Validate ca_cert field.
        
        Datasource: ['vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('client_cert')
    @classmethod
    def validate_client_cert(cls, v: Any) -> Any:
        """
        Validate client_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    # ========================================================================
    # Helper Methods
    # ========================================================================
    
    def to_fortios_dict(self) -> dict[str, Any]:
        """
        Convert model to FortiOS API payload format.
        
        Returns:
            Dict suitable for POST/PUT operations
        """
        # Export with exclude_none to avoid sending null values
        return self.model_dump(exclude_none=True, by_alias=True)
    
    @classmethod
    def from_fortios_response(cls, data: dict[str, Any]) -> "":
        """
        Create model instance from FortiOS API response.
        
        Args:
            data: Response data from API
            
        Returns:
            Validated model instance
        """
        return cls(**data)
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_source_ip_interface_references(self, client: Any) -> list[str]:
        """
        Validate source_ip_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RadiusModel(
            ...     source_ip_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_source_ip_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.radius.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "source_ip_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Source-Ip-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RadiusModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.radius.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_ca_cert_references(self, client: Any) -> list[str]:
        """
        Validate ca_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RadiusModel(
            ...     ca_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ca_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.radius.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ca_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ca-Cert '{value}' not found in "
                "vpn/certificate/ca"
            )        
        return errors    
    async def validate_client_cert_references(self, client: Any) -> list[str]:
        """
        Validate client_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RadiusModel(
            ...     client_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_client_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.radius.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "client_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Client-Cert '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_accounting_server_references(self, client: Any) -> list[str]:
        """
        Validate accounting_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RadiusModel(
            ...     accounting_server=[{"interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_accounting_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.radius.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "accounting_server", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface")
            else:
                value = getattr(item, "interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Accounting-Server '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_all_references(self, client: Any) -> list[str]:
        """
        Validate ALL datasource references in this model.
        
        Convenience method that runs all validate_*_references() methods
        and aggregates the results.
        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of all validation errors found
            
        Example:
            >>> errors = await policy.validate_all_references(fgt._client)
            >>> if errors:
            ...     for error in errors:
            ...         print(f"  - {error}")
        """
        all_errors = []
        
        errors = await self.validate_source_ip_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ca_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_client_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_accounting_server_references(client)
        all_errors.extend(errors)        
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "RadiusModel",    "RadiusClass",    "RadiusAccountingServer",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.556940Z
# ============================================================================