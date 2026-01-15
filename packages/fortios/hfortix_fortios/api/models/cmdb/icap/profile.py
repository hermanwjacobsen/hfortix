"""
Pydantic Models for CMDB - icap/profile

Runtime validation models for icap/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileIcapHeaders(BaseModel):
    """
    Child table model for icap-headers.
    
    Configure ICAP forwarded request headers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="HTTP forwarded header ID.")    
    name: str | None = Field(max_length=79, default="", description="HTTP forwarded header name.")    
    content: str | None = Field(max_length=255, default="", description="HTTP header content.")    
    base64_encoding: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of base64 encoding of HTTP content.")
class ProfileRespmodForwardRules(BaseModel):
    """
    Child table model for respmod-forward-rules.
    
    ICAP response mode forward rules.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Address name.")    
    host: str = Field(max_length=79, default="", description="Address object for the host.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name']    
    header_group: list[HeaderGroup] = Field(default=None, description="HTTP header group.")    
    action: Literal["forward", "bypass"] | None = Field(default="forward", description="Action to be taken for ICAP server.")    
    http_resp_status_code: list[HttpRespStatusCode] = Field(default=None, description="HTTP response status code.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProfileMethodsEnum(str, Enum):
    """Allowed values for methods field."""
    DELETE = "delete"    GET = "get"    HEAD = "head"    OPTIONS = "options"    POST = "post"    PUT = "put"    TRACE = "trace"    CONNECT = "connect"    OTHER = "other"

# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for icap/profile configuration.
    
    Configure ICAP profiles.
    
    Validation Rules:        - replacemsg_group: max_length=35 pattern=        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - request: pattern=        - response: pattern=        - file_transfer: pattern=        - streaming_content_bypass: pattern=        - ocr_only: pattern=        - 204_size_limit: min=1 max=10 pattern=        - 204_response: pattern=        - preview: pattern=        - preview_data_length: min=0 max=4096 pattern=        - request_server: max_length=63 pattern=        - response_server: max_length=63 pattern=        - file_transfer_server: max_length=63 pattern=        - request_failure: pattern=        - response_failure: pattern=        - file_transfer_failure: pattern=        - request_path: max_length=127 pattern=        - response_path: max_length=127 pattern=        - file_transfer_path: max_length=127 pattern=        - methods: pattern=        - response_req_hdr: pattern=        - respmod_default_action: pattern=        - icap_block_log: pattern=        - chunk_encap: pattern=        - extension_feature: pattern=        - scan_progress_interval: min=5 max=30 pattern=        - timeout: min=30 max=3600 pattern=        - icap_headers: pattern=        - respmod_forward_rules: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    name: str | None = Field(max_length=47, default="", description="ICAP profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    request: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable whether an HTTP request is passed to an ICAP server.")    
    response: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable whether an HTTP response is passed to an ICAP server.")    
    file_transfer: list[FileTransfer] = Field(default="", description="Configure the file transfer protocols to pass transferred files to an ICAP server as REQMOD.")    
    streaming_content_bypass: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypassing of ICAP server for streaming content.")    
    ocr_only: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable this FortiGate unit to submit only OCR interested content to the ICAP server.")    
    204_size_limit: int | None = Field(ge=1, le=10, default=1, description="204 response size limit to be saved by ICAP client in megabytes (1 - 10, default = 1 MB).")    
    204_response: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allowance of 204 response from ICAP server.")    
    preview: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable preview of data to ICAP server.")    
    preview_data_length: int | None = Field(ge=0, le=4096, default=0, description="Preview data length to be sent to ICAP server.")    
    request_server: str = Field(max_length=63, default="", description="ICAP server to use for an HTTP request.")  # datasource: ['icap.server.name', 'icap.server-group.name']    
    response_server: str = Field(max_length=63, default="", description="ICAP server to use for an HTTP response.")  # datasource: ['icap.server.name', 'icap.server-group.name']    
    file_transfer_server: str = Field(max_length=63, default="", description="ICAP server to use for a file transfer.")  # datasource: ['icap.server.name', 'icap.server-group.name']    
    request_failure: Literal["error", "bypass"] | None = Field(default="error", description="Action to take if the ICAP server cannot be contacted when processing an HTTP request.")    
    response_failure: Literal["error", "bypass"] | None = Field(default="error", description="Action to take if the ICAP server cannot be contacted when processing an HTTP response.")    
    file_transfer_failure: Literal["error", "bypass"] | None = Field(default="error", description="Action to take if the ICAP server cannot be contacted when processing a file transfer.")    
    request_path: str | None = Field(max_length=127, default="", description="Path component of the ICAP URI that identifies the HTTP request processing service.")    
    response_path: str | None = Field(max_length=127, default="", description="Path component of the ICAP URI that identifies the HTTP response processing service.")    
    file_transfer_path: str | None = Field(max_length=127, default="", description="Path component of the ICAP URI that identifies the file transfer processing service.")    
    methods: list[Methods] = Field(default="delete get head options post put trace connect other", description="The allowed HTTP methods that will be sent to ICAP server for further processing.")    
    response_req_hdr: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable addition of req-hdr for ICAP response modification (respmod) processing.")    
    respmod_default_action: Literal["forward", "bypass"] | None = Field(default="forward", description="Default action to ICAP response modification (respmod) processing.")    
    icap_block_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable UTM log when infection found (default = disable).")    
    chunk_encap: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable chunked encapsulation (default = disable).")    
    extension_feature: list[ExtensionFeature] = Field(default="", description="Enable/disable ICAP extension features.")    
    scan_progress_interval: int | None = Field(ge=5, le=30, default=10, description="Scan progress interval value.")    
    timeout: int | None = Field(ge=30, le=3600, default=30, description="Time (in seconds) that ICAP client waits for the response from ICAP server.")    
    icap_headers: list[IcapHeaders] = Field(default=None, description="Configure ICAP forwarded request headers.")    
    respmod_forward_rules: list[RespmodForwardRules] = Field(default=None, description="ICAP response mode forward rules.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('request_server')
    @classmethod
    def validate_request_server(cls, v: Any) -> Any:
        """
        Validate request_server field.
        
        Datasource: ['icap.server.name', 'icap.server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('response_server')
    @classmethod
    def validate_response_server(cls, v: Any) -> Any:
        """
        Validate response_server field.
        
        Datasource: ['icap.server.name', 'icap.server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('file_transfer_server')
    @classmethod
    def validate_file_transfer_server(cls, v: Any) -> Any:
        """
        Validate file_transfer_server field.
        
        Datasource: ['icap.server.name', 'icap.server-group.name']
        
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
    async def validate_replacemsg_group_references(self, client: Any) -> list[str]:
        """
        Validate replacemsg_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/replacemsg-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     replacemsg_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.icap.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "replacemsg_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.replacemsg-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Replacemsg-Group '{value}' not found in "
                "system/replacemsg-group"
            )        
        return errors    
    async def validate_request_server_references(self, client: Any) -> list[str]:
        """
        Validate request_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - icap/server        - icap/server-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     request_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_request_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.icap.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "request_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.icap.server.exists(value):
            found = True
        elif await client.api.cmdb.icap.server-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Request-Server '{value}' not found in "
                "icap/server or icap/server-group"
            )        
        return errors    
    async def validate_response_server_references(self, client: Any) -> list[str]:
        """
        Validate response_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - icap/server        - icap/server-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     response_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_response_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.icap.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "response_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.icap.server.exists(value):
            found = True
        elif await client.api.cmdb.icap.server-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Response-Server '{value}' not found in "
                "icap/server or icap/server-group"
            )        
        return errors    
    async def validate_file_transfer_server_references(self, client: Any) -> list[str]:
        """
        Validate file_transfer_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - icap/server        - icap/server-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     file_transfer_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_file_transfer_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.icap.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "file_transfer_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.icap.server.exists(value):
            found = True
        elif await client.api.cmdb.icap.server-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"File-Transfer-Server '{value}' not found in "
                "icap/server or icap/server-group"
            )        
        return errors    
    async def validate_respmod_forward_rules_references(self, client: Any) -> list[str]:
        """
        Validate respmod_forward_rules references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - firewall/proxy-address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     respmod_forward_rules=[{"host": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_respmod_forward_rules_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.icap.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "respmod_forward_rules", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("host")
            else:
                value = getattr(item, "host", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp.exists(value):
                found = True
            elif await client.api.cmdb.firewall.proxy-address.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Respmod-Forward-Rules '{value}' not found in "
                    "firewall/address or firewall/addrgrp or firewall/proxy-address"
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
        
        errors = await self.validate_replacemsg_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_request_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_response_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_file_transfer_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_respmod_forward_rules_references(client)
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
    "ProfileModel",    "ProfileIcapHeaders",    "ProfileRespmodForwardRules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.694416Z
# ============================================================================