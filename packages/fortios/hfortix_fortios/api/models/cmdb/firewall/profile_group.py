"""
Pydantic Models for CMDB - firewall/profile_group

Runtime validation models for firewall/profile_group configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileGroupModel(BaseModel):
    """
    Pydantic model for firewall/profile_group configuration.
    
    Configure profile groups.
    
    Validation Rules:        - name: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - voip_profile: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - diameter_filter_profile: max_length=47 pattern=        - virtual_patch_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - waf_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Profile group name.")    
    profile_protocol_options: str | None = Field(max_length=47, default="default", description="Name of an existing Protocol options profile.")  # datasource: ['firewall.profile-protocol-options.name']    
    ssl_ssh_profile: str | None = Field(max_length=47, default="certificate-inspection", description="Name of an existing SSL SSH profile.")  # datasource: ['firewall.ssl-ssh-profile.name']    
    av_profile: str | None = Field(max_length=47, default="", description="Name of an existing Antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web filter profile.")  # datasource: ['webfilter.profile.name']    
    dnsfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing DNS filter profile.")  # datasource: ['dnsfilter.profile.name']    
    emailfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile: str | None = Field(max_length=47, default="", description="Name of an existing DLP profile.")  # datasource: ['dlp.profile.name']    
    file_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing file-filter profile.")  # datasource: ['file-filter.profile.name']    
    ips_sensor: str | None = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    application_list: str | None = Field(max_length=47, default="", description="Name of an existing Application list.")  # datasource: ['application.list.name']    
    voip_profile: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (voipd) profile.")  # datasource: ['voip.profile.name']    
    ips_voip_filter: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (ips) profile.")  # datasource: ['voip.profile.name']    
    sctp_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SCTP filter profile.")  # datasource: ['sctp-filter.profile.name']    
    diameter_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing Diameter filter profile.")  # datasource: ['diameter-filter.profile.name']    
    virtual_patch_profile: str | None = Field(max_length=47, default="", description="Name of an existing virtual-patch profile.")  # datasource: ['virtual-patch.profile.name']    
    icap_profile: str | None = Field(max_length=47, default="", description="Name of an existing ICAP profile.")  # datasource: ['icap.profile.name']    
    videofilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing VideoFilter profile.")  # datasource: ['videofilter.profile.name']    
    waf_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web application firewall profile.")  # datasource: ['waf.profile.name']    
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('profile_protocol_options')
    @classmethod
    def validate_profile_protocol_options(cls, v: Any) -> Any:
        """
        Validate profile_protocol_options field.
        
        Datasource: ['firewall.profile-protocol-options.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssl_ssh_profile')
    @classmethod
    def validate_ssl_ssh_profile(cls, v: Any) -> Any:
        """
        Validate ssl_ssh_profile field.
        
        Datasource: ['firewall.ssl-ssh-profile.name']
        
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
    @field_validator('dnsfilter_profile')
    @classmethod
    def validate_dnsfilter_profile(cls, v: Any) -> Any:
        """
        Validate dnsfilter_profile field.
        
        Datasource: ['dnsfilter.profile.name']
        
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
    @field_validator('file_filter_profile')
    @classmethod
    def validate_file_filter_profile(cls, v: Any) -> Any:
        """
        Validate file_filter_profile field.
        
        Datasource: ['file-filter.profile.name']
        
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
    @field_validator('voip_profile')
    @classmethod
    def validate_voip_profile(cls, v: Any) -> Any:
        """
        Validate voip_profile field.
        
        Datasource: ['voip.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_voip_filter')
    @classmethod
    def validate_ips_voip_filter(cls, v: Any) -> Any:
        """
        Validate ips_voip_filter field.
        
        Datasource: ['voip.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sctp_filter_profile')
    @classmethod
    def validate_sctp_filter_profile(cls, v: Any) -> Any:
        """
        Validate sctp_filter_profile field.
        
        Datasource: ['sctp-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('diameter_filter_profile')
    @classmethod
    def validate_diameter_filter_profile(cls, v: Any) -> Any:
        """
        Validate diameter_filter_profile field.
        
        Datasource: ['diameter-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('virtual_patch_profile')
    @classmethod
    def validate_virtual_patch_profile(cls, v: Any) -> Any:
        """
        Validate virtual_patch_profile field.
        
        Datasource: ['virtual-patch.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('icap_profile')
    @classmethod
    def validate_icap_profile(cls, v: Any) -> Any:
        """
        Validate icap_profile field.
        
        Datasource: ['icap.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('videofilter_profile')
    @classmethod
    def validate_videofilter_profile(cls, v: Any) -> Any:
        """
        Validate videofilter_profile field.
        
        Datasource: ['videofilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('waf_profile')
    @classmethod
    def validate_waf_profile(cls, v: Any) -> Any:
        """
        Validate waf_profile field.
        
        Datasource: ['waf.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_filter_profile')
    @classmethod
    def validate_ssh_filter_profile(cls, v: Any) -> Any:
        """
        Validate ssh_filter_profile field.
        
        Datasource: ['ssh-filter.profile.name']
        
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
    async def validate_profile_protocol_options_references(self, client: Any) -> list[str]:
        """
        Validate profile_protocol_options references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/profile-protocol-options        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     profile_protocol_options="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_protocol_options_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "profile_protocol_options", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.profile-protocol-options.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Profile-Protocol-Options '{value}' not found in "
                "firewall/profile-protocol-options"
            )        
        return errors    
    async def validate_ssl_ssh_profile_references(self, client: Any) -> list[str]:
        """
        Validate ssl_ssh_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssl-ssh-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     ssl_ssh_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_ssh_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_ssh_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssl-ssh-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssl-Ssh-Profile '{value}' not found in "
                "firewall/ssl-ssh-profile"
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
            >>> policy = ProfileGroupModel(
            ...     av_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_av_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
            >>> policy = ProfileGroupModel(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
    async def validate_dnsfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate dnsfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dnsfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     dnsfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dnsfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dnsfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dnsfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dnsfilter-Profile '{value}' not found in "
                "dnsfilter/profile"
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
            >>> policy = ProfileGroupModel(
            ...     emailfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_emailfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
            >>> policy = ProfileGroupModel(
            ...     dlp_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dlp_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
    async def validate_file_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate file_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - file-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     file_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_file_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "file_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.file-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"File-Filter-Profile '{value}' not found in "
                "file-filter/profile"
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
            >>> policy = ProfileGroupModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
            >>> policy = ProfileGroupModel(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
    async def validate_voip_profile_references(self, client: Any) -> list[str]:
        """
        Validate voip_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - voip/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     voip_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_voip_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "voip_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.voip.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Voip-Profile '{value}' not found in "
                "voip/profile"
            )        
        return errors    
    async def validate_ips_voip_filter_references(self, client: Any) -> list[str]:
        """
        Validate ips_voip_filter references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - voip/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     ips_voip_filter="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_voip_filter_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ips_voip_filter", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.voip.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ips-Voip-Filter '{value}' not found in "
                "voip/profile"
            )        
        return errors    
    async def validate_sctp_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate sctp_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - sctp-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     sctp_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sctp_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sctp_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.sctp-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sctp-Filter-Profile '{value}' not found in "
                "sctp-filter/profile"
            )        
        return errors    
    async def validate_diameter_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate diameter_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - diameter-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     diameter_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_diameter_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "diameter_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.diameter-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Diameter-Filter-Profile '{value}' not found in "
                "diameter-filter/profile"
            )        
        return errors    
    async def validate_virtual_patch_profile_references(self, client: Any) -> list[str]:
        """
        Validate virtual_patch_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - virtual-patch/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     virtual_patch_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_virtual_patch_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "virtual_patch_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.virtual-patch.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Virtual-Patch-Profile '{value}' not found in "
                "virtual-patch/profile"
            )        
        return errors    
    async def validate_icap_profile_references(self, client: Any) -> list[str]:
        """
        Validate icap_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - icap/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     icap_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_icap_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "icap_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.icap.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Icap-Profile '{value}' not found in "
                "icap/profile"
            )        
        return errors    
    async def validate_videofilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate videofilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - videofilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     videofilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_videofilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "videofilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.videofilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Videofilter-Profile '{value}' not found in "
                "videofilter/profile"
            )        
        return errors    
    async def validate_waf_profile_references(self, client: Any) -> list[str]:
        """
        Validate waf_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - waf/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     waf_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_waf_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "waf_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.waf.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Waf-Profile '{value}' not found in "
                "waf/profile"
            )        
        return errors    
    async def validate_ssh_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate ssh_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ssh-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileGroupModel(
            ...     ssh_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssh_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssh_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.ssh-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssh-Filter-Profile '{value}' not found in "
                "ssh-filter/profile"
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
            >>> policy = ProfileGroupModel(
            ...     casb_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_casb_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_group.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_profile_protocol_options_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssl_ssh_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_av_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dnsfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_emailfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dlp_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_file_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_sensor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_application_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_voip_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_voip_filter_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sctp_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_diameter_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_virtual_patch_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_icap_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_videofilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_waf_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssh_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_casb_profile_references(client)
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
    "ProfileGroupModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.383683Z
# ============================================================================