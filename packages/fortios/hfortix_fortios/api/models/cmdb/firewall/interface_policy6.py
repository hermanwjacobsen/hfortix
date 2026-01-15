"""
Pydantic Models for CMDB - firewall/interface_policy6

Runtime validation models for firewall/interface_policy6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class InterfacePolicy6Srcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class InterfacePolicy6Dstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class InterfacePolicy6Service6(BaseModel):
    """
    Child table model for service6.
    
    Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class InterfacePolicy6Model(BaseModel):
    """
    Pydantic model for firewall/interface_policy6 configuration.
    
    Configure IPv6 interface policies.
    
    Validation Rules:        - policyid: min=0 max=4294967295 pattern=        - uuid: pattern=        - status: pattern=        - comments: max_length=1023 pattern=        - logtraffic: pattern=        - interface: max_length=35 pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - service6: pattern=        - application_list_status: pattern=        - application_list: max_length=47 pattern=        - ips_sensor_status: pattern=        - ips_sensor: max_length=47 pattern=        - dsri: pattern=        - av_profile_status: pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile_status: pattern=        - webfilter_profile: max_length=47 pattern=        - casb_profile_status: pattern=        - casb_profile: max_length=47 pattern=        - emailfilter_profile_status: pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile_status: pattern=        - dlp_profile: max_length=47 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="Policy ID (0 - 4294967295).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this policy.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comments.")    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Logging type to be used in this policy (Options: all | utm | disable, Default: utm).")    
    interface: str = Field(max_length=35, default="", description="Monitored interface name from available interfaces.")  # datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']    
    srcaddr6: list[Srcaddr6] = Field(description="IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.")    
    dstaddr6: list[Dstaddr6] = Field(description="IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.")    
    service6: list[Service6] = Field(default=None, description="Service name.")    
    application_list_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application control.")    
    application_list: str = Field(max_length=47, default="", description="Application list name.")  # datasource: ['application.list.name']    
    ips_sensor_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS.")    
    ips_sensor: str = Field(max_length=47, default="", description="IPS sensor name.")  # datasource: ['ips.sensor.name']    
    dsri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DSRI.")    
    av_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable antivirus.")    
    av_profile: str = Field(max_length=47, default="", description="Antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web filtering.")    
    webfilter_profile: str = Field(max_length=47, default="", description="Web filter profile.")  # datasource: ['webfilter.profile.name']    
    casb_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable CASB.")    
    casb_profile: str = Field(max_length=47, default="", description="CASB profile.")  # datasource: ['casb.profile.name']    
    emailfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable email filter.")    
    emailfilter_profile: str = Field(max_length=47, default="", description="Email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DLP.")    
    dlp_profile: str = Field(max_length=47, default="", description="DLP profile name.")  # datasource: ['dlp.profile.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('application_list')
    @classmethod
    def validate_application_list(cls, v: Any) -> Any:
        """
        Validate application_list field.
        
        Datasource: ['application.list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_sensor')
    @classmethod
    def validate_ips_sensor(cls, v: Any) -> Any:
        """
        Validate ips_sensor field.
        
        Datasource: ['ips.sensor.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('av_profile')
    @classmethod
    def validate_av_profile(cls, v: Any) -> Any:
        """
        Validate av_profile field.
        
        Datasource: ['antivirus.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webfilter_profile')
    @classmethod
    def validate_webfilter_profile(cls, v: Any) -> Any:
        """
        Validate webfilter_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('casb_profile')
    @classmethod
    def validate_casb_profile(cls, v: Any) -> Any:
        """
        Validate casb_profile field.
        
        Datasource: ['casb.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('emailfilter_profile')
    @classmethod
    def validate_emailfilter_profile(cls, v: Any) -> Any:
        """
        Validate emailfilter_profile field.
        
        Datasource: ['emailfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dlp_profile')
    @classmethod
    def validate_dlp_profile(cls, v: Any) -> Any:
        """
        Validate dlp_profile field.
        
        Datasource: ['dlp.profile.name']
        
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
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/zone        - system/sdwan/zone        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.zone.exists(value):
            found = True
        elif await client.api.cmdb.system.sdwan.zone.exists(value):
            found = True
        elif await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Interface '{value}' not found in "
                "system/zone or system/sdwan/zone or system/interface"
            )        
        return errors    
    async def validate_srcaddr6_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     srcaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcaddr6", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.address6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
                )        
        return errors    
    async def validate_dstaddr6_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     dstaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstaddr6", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.address6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
                )        
        return errors    
    async def validate_service6_references(self, client: Any) -> list[str]:
        """
        Validate service6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/service/custom        - firewall/service/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     service6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "service6", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.service.custom.exists(value):
                found = True
            elif await client.api.cmdb.firewall.service.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Service6 '{value}' not found in "
                    "firewall/service/custom or firewall/service/group"
                )        
        return errors    
    async def validate_application_list_references(self, client: Any) -> list[str]:
        """
        Validate application_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - application/list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "application_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.application.list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Application-List '{value}' not found in "
                "application/list"
            )        
        return errors    
    async def validate_ips_sensor_references(self, client: Any) -> list[str]:
        """
        Validate ips_sensor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ips/sensor        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ips_sensor", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.ips.sensor.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ips-Sensor '{value}' not found in "
                "ips/sensor"
            )        
        return errors    
    async def validate_av_profile_references(self, client: Any) -> list[str]:
        """
        Validate av_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - antivirus/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     av_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_av_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "av_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.antivirus.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Av-Profile '{value}' not found in "
                "antivirus/profile"
            )        
        return errors    
    async def validate_webfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate webfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "webfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.webfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Webfilter-Profile '{value}' not found in "
                "webfilter/profile"
            )        
        return errors    
    async def validate_casb_profile_references(self, client: Any) -> list[str]:
        """
        Validate casb_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - casb/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     casb_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_casb_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "casb_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.casb.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Casb-Profile '{value}' not found in "
                "casb/profile"
            )        
        return errors    
    async def validate_emailfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate emailfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     emailfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_emailfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "emailfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Emailfilter-Profile '{value}' not found in "
                "emailfilter/profile"
            )        
        return errors    
    async def validate_dlp_profile_references(self, client: Any) -> list[str]:
        """
        Validate dlp_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfacePolicy6Model(
            ...     dlp_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dlp_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.interface_policy6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dlp_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dlp.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dlp-Profile '{value}' not found in "
                "dlp/profile"
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
        
        errors = await self.validate_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_service6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_application_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_sensor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_av_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_casb_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_emailfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dlp_profile_references(client)
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
    "InterfacePolicy6Model",    "InterfacePolicy6Srcaddr6",    "InterfacePolicy6Dstaddr6",    "InterfacePolicy6Service6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.406043Z
# ============================================================================