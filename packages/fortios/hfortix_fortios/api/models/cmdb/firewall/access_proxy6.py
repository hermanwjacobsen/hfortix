"""
Pydantic Models for CMDB - firewall/access_proxy6

Runtime validation models for firewall/access_proxy6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class AccessProxy6ApiGateway(BaseModel):
    """
    Child table model for api-gateway.
    
    Set IPv4 API Gateway.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="API Gateway ID.")    
    url_map: str = Field(max_length=511, default="/", description="URL pattern to match.")    
    service: ServiceEnum = Field(default="https", description="Service.")    
    ldb_method: LdbMethodEnum | None = Field(default="static", description="Method used to distribute sessions to real servers.")    
    virtual_host: str | None = Field(max_length=79, default="", description="Virtual host.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    url_map_type: Literal["sub-string", "wildcard", "regex"] = Field(default="sub-string", description="Type of url-map.")    
    h2_support: Literal["enable", "disable"] = Field(default="enable", description="HTTP2 support, default=Enable.")    
    h3_support: Literal["enable", "disable"] | None = Field(default="disable", description="HTTP3/QUIC support, default=Disable.")    
    quic: list[Quic] = Field(default=None, description="QUIC setting.")    
    realservers: list[Realservers] = Field(default=None, description="Select the real servers that this Access Proxy will distribute traffic to.")    
    application: list[Application] = Field(description="SaaS application controlled by this Access Proxy.")    
    persistence: Literal["none", "http-cookie"] | None = Field(default="none", description="Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.")    
    http_cookie_domain_from_host: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of HTTP cookie domain from host field in HTTP.")    
    http_cookie_domain: str | None = Field(max_length=35, default="", description="Domain that HTTP cookie persistence should apply to.")    
    http_cookie_path: str | None = Field(max_length=35, default="", description="Limit HTTP cookie persistence to the specified path.")    
    http_cookie_generation: int | None = Field(ge=0, le=4294967295, default=0, description="Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.")    
    http_cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    http_cookie_share: Literal["disable", "same-ip"] | None = Field(default="same-ip", description="Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.")    
    https_cookie_secure: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable verification that inserted HTTPS cookies are secure.")    
    saml_server: str | None = Field(max_length=35, default="", description="SAML service provider configuration for VIP authentication.")  # datasource: ['user.saml.name']    
    saml_redirect: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SAML redirection after successful authentication.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.")    
    ssl_cipher_suites: list[SslCipherSuites] = Field(default=None, description="SSL/TLS cipher suites to offer to a server, ordered by priority.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version acceptable from a server.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version acceptable from a server.")    
    ssl_renegotiation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable secure renegotiation to comply with RFC 5746.")    
    ssl_vpn_web_portal: str | None = Field(max_length=35, default="", description="Agentless VPN web portal.")  # datasource: ['vpn.ssl.web.portal.name']
class AccessProxy6ApiGateway6(BaseModel):
    """
    Child table model for api-gateway6.
    
    Set IPv6 API Gateway.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="API Gateway ID.")    
    url_map: str = Field(max_length=511, default="/", description="URL pattern to match.")    
    service: ServiceEnum = Field(default="https", description="Service.")    
    ldb_method: LdbMethodEnum | None = Field(default="static", description="Method used to distribute sessions to real servers.")    
    virtual_host: str | None = Field(max_length=79, default="", description="Virtual host.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    url_map_type: Literal["sub-string", "wildcard", "regex"] = Field(default="sub-string", description="Type of url-map.")    
    h2_support: Literal["enable", "disable"] = Field(default="enable", description="HTTP2 support, default=Enable.")    
    h3_support: Literal["enable", "disable"] | None = Field(default="disable", description="HTTP3/QUIC support, default=Disable.")    
    quic: list[Quic] = Field(default=None, description="QUIC setting.")    
    realservers: list[Realservers] = Field(default=None, description="Select the real servers that this Access Proxy will distribute traffic to.")    
    application: list[Application] = Field(description="SaaS application controlled by this Access Proxy.")    
    persistence: Literal["none", "http-cookie"] | None = Field(default="none", description="Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.")    
    http_cookie_domain_from_host: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of HTTP cookie domain from host field in HTTP.")    
    http_cookie_domain: str | None = Field(max_length=35, default="", description="Domain that HTTP cookie persistence should apply to.")    
    http_cookie_path: str | None = Field(max_length=35, default="", description="Limit HTTP cookie persistence to the specified path.")    
    http_cookie_generation: int | None = Field(ge=0, le=4294967295, default=0, description="Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.")    
    http_cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    http_cookie_share: Literal["disable", "same-ip"] | None = Field(default="same-ip", description="Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.")    
    https_cookie_secure: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable verification that inserted HTTPS cookies are secure.")    
    saml_server: str | None = Field(max_length=35, default="", description="SAML service provider configuration for VIP authentication.")  # datasource: ['user.saml.name']    
    saml_redirect: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SAML redirection after successful authentication.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.")    
    ssl_cipher_suites: list[SslCipherSuites] = Field(default=None, description="SSL/TLS cipher suites to offer to a server, ordered by priority.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version acceptable from a server.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version acceptable from a server.")    
    ssl_renegotiation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable secure renegotiation to comply with RFC 5746.")    
    ssl_vpn_web_portal: str | None = Field(max_length=35, default="", description="Agentless VPN web portal.")  # datasource: ['vpn.ssl.web.portal.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AccessProxy6Model(BaseModel):
    """
    Pydantic model for firewall/access_proxy6 configuration.
    
    Configure IPv6 access proxy.
    
    Validation Rules:        - name: max_length=79 pattern=        - vip: max_length=79 pattern=        - auth_portal: pattern=        - auth_virtual_host: max_length=79 pattern=        - log_blocked_traffic: pattern=        - add_vhost_domain_to_dnsdb: pattern=        - svr_pool_multiplex: pattern=        - svr_pool_ttl: min=0 max=2147483647 pattern=        - svr_pool_server_max_request: min=0 max=2147483647 pattern=        - svr_pool_server_max_concurrent_request: min=0 max=2147483647 pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - api_gateway: pattern=        - api_gateway6: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Access Proxy name.")    
    vip: str = Field(max_length=79, default="", description="Virtual IP name.")  # datasource: ['firewall.vip6.name']    
    auth_portal: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable authentication portal.")    
    auth_virtual_host: str | None = Field(max_length=79, default="", description="Virtual host for authentication portal.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    log_blocked_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging of blocked traffic.")    
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel.")    
    svr_pool_multiplex: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable server pool multiplexing (default = disable). Share connected server in HTTP, HTTPS, and web-portal api-gateway.")    
    svr_pool_ttl: int | None = Field(ge=0, le=2147483647, default=15, description="Time-to-live in the server pool for idle connections to servers.")    
    svr_pool_server_max_request: int | None = Field(ge=0, le=2147483647, default=0, description="Maximum number of requests that servers in server pool handle before disconnecting (default = unlimited).")    
    svr_pool_server_max_concurrent_request: int | None = Field(ge=0, le=2147483647, default=0, description="Maximum number of concurrent requests that servers in server pool could handle (default = unlimited).")    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    api_gateway: list[ApiGateway] = Field(default=None, description="Set IPv4 API Gateway.")    
    api_gateway6: list[ApiGateway6] = Field(default=None, description="Set IPv6 API Gateway.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vip')
    @classmethod
    def validate_vip(cls, v: Any) -> Any:
        """
        Validate vip field.
        
        Datasource: ['firewall.vip6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_virtual_host')
    @classmethod
    def validate_auth_virtual_host(cls, v: Any) -> Any:
        """
        Validate auth_virtual_host field.
        
        Datasource: ['firewall.access-proxy-virtual-host.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('decrypted_traffic_mirror')
    @classmethod
    def validate_decrypted_traffic_mirror(cls, v: Any) -> Any:
        """
        Validate decrypted_traffic_mirror field.
        
        Datasource: ['firewall.decrypted-traffic-mirror.name']
        
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
    async def validate_vip_references(self, client: Any) -> list[str]:
        """
        Validate vip references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/vip6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AccessProxy6Model(
            ...     vip="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vip_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.access_proxy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vip", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.vip6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vip '{value}' not found in "
                "firewall/vip6"
            )        
        return errors    
    async def validate_auth_virtual_host_references(self, client: Any) -> list[str]:
        """
        Validate auth_virtual_host references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/access-proxy-virtual-host        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AccessProxy6Model(
            ...     auth_virtual_host="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_virtual_host_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.access_proxy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_virtual_host", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.access-proxy-virtual-host.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Virtual-Host '{value}' not found in "
                "firewall/access-proxy-virtual-host"
            )        
        return errors    
    async def validate_decrypted_traffic_mirror_references(self, client: Any) -> list[str]:
        """
        Validate decrypted_traffic_mirror references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/decrypted-traffic-mirror        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AccessProxy6Model(
            ...     decrypted_traffic_mirror="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_decrypted_traffic_mirror_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.access_proxy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "decrypted_traffic_mirror", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.decrypted-traffic-mirror.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Decrypted-Traffic-Mirror '{value}' not found in "
                "firewall/decrypted-traffic-mirror"
            )        
        return errors    
    async def validate_api_gateway_references(self, client: Any) -> list[str]:
        """
        Validate api_gateway references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/ssl/web/portal        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AccessProxy6Model(
            ...     api_gateway=[{"ssl-vpn-web-portal": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_api_gateway_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.access_proxy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "api_gateway", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("ssl-vpn-web-portal")
            else:
                value = getattr(item, "ssl-vpn-web-portal", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.vpn.ssl.web.portal.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Api-Gateway '{value}' not found in "
                    "vpn/ssl/web/portal"
                )        
        return errors    
    async def validate_api_gateway6_references(self, client: Any) -> list[str]:
        """
        Validate api_gateway6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/ssl/web/portal        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AccessProxy6Model(
            ...     api_gateway6=[{"ssl-vpn-web-portal": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_api_gateway6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.access_proxy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "api_gateway6", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("ssl-vpn-web-portal")
            else:
                value = getattr(item, "ssl-vpn-web-portal", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.vpn.ssl.web.portal.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Api-Gateway6 '{value}' not found in "
                    "vpn/ssl/web/portal"
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
        
        errors = await self.validate_vip_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_virtual_host_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_decrypted_traffic_mirror_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_api_gateway_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_api_gateway6_references(client)
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
    "AccessProxy6Model",    "AccessProxy6ApiGateway",    "AccessProxy6ApiGateway6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.120990Z
# ============================================================================