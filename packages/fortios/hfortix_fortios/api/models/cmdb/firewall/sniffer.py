"""
Pydantic Models for CMDB - firewall/sniffer

Runtime validation models for firewall/sniffer configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class SnifferIpThreatfeed(BaseModel):
    """
    Child table model for ip-threatfeed.
    
    Name of an existing IP threat feed.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Threat feed name.")  # datasource: ['system.external-resource.name']
class SnifferAnomaly(BaseModel):
    """
    Child table model for anomaly.
    
    Configuration method to edit Denial of Service (DoS) anomaly settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Anomaly name.")    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable this anomaly.")    
    log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable anomaly logging.")    
    action: Literal["pass", "block"] | None = Field(default="pass", description="Action taken when the threshold is reached.")    
    quarantine: Literal["none", "attacker"] | None = Field(default="none", description="Quarantine method.")    
    quarantine_expiry: str | None = Field(default="5m", description="Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.")    
    quarantine_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable quarantine logging.")    
    threshold: int | None = Field(ge=1, le=2147483647, default=0, description="Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action.")    
    threshold(default): int | None = Field(ge=0, le=4294967295, default=0, description="Number of detected instances (packets per second or concurrent session number) which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SnifferModel(BaseModel):
    """
    Pydantic model for firewall/sniffer configuration.
    
    Configure sniffer.
    
    Validation Rules:        - id: min=0 max=9999 pattern=        - uuid: pattern=        - status: pattern=        - logtraffic: pattern=        - ipv6: pattern=        - non_ip: pattern=        - interface: max_length=35 pattern=        - host: max_length=63 pattern=        - port: max_length=63 pattern=        - protocol: max_length=63 pattern=        - vlan: max_length=63 pattern=        - application_list_status: pattern=        - application_list: max_length=47 pattern=        - ips_sensor_status: pattern=        - ips_sensor: max_length=47 pattern=        - dsri: pattern=        - av_profile_status: pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile_status: pattern=        - webfilter_profile: max_length=47 pattern=        - emailfilter_profile_status: pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile_status: pattern=        - dlp_profile: max_length=47 pattern=        - ip_threatfeed_status: pattern=        - ip_threatfeed: pattern=        - file_filter_profile_status: pattern=        - file_filter_profile: max_length=47 pattern=        - ips_dos_status: pattern=        - anomaly: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=9999, default=0, description="Sniffer ID (0 - 9999).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of the sniffer.")    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy.")    
    ipv6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sniffing IPv6 packets.")    
    non_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sniffing non-IP packets.")    
    interface: str | None = Field(max_length=35, default="", description="Interface name that traffic sniffing will take place on.")  # datasource: ['system.interface.name']    
    host: str | None = Field(max_length=63, default="", description="Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240).")    
    port: str | None = Field(max_length=63, default="", description="Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200).")    
    protocol: str | None = Field(max_length=63, default="", description="Integer value for the protocol type as defined by IANA (0 - 255).")    
    vlan: str | None = Field(max_length=63, default="", description="List of VLANs to sniff.")    
    application_list_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application control profile.")    
    application_list: str = Field(max_length=47, default="", description="Name of an existing application list.")  # datasource: ['application.list.name']    
    ips_sensor_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS sensor.")    
    ips_sensor: str = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    dsri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DSRI.")    
    av_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable antivirus profile.")    
    av_profile: str = Field(max_length=47, default="", description="Name of an existing antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web filter profile.")    
    webfilter_profile: str = Field(max_length=47, default="", description="Name of an existing web filter profile.")  # datasource: ['webfilter.profile.name']    
    emailfilter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable emailfilter.")    
    emailfilter_profile: str = Field(max_length=47, default="", description="Name of an existing email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DLP profile.")    
    dlp_profile: str = Field(max_length=47, default="", description="Name of an existing DLP profile.")  # datasource: ['dlp.profile.name']    
    ip_threatfeed_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IP threat feed.")    
    ip_threatfeed: list[IpThreatfeed] = Field(default=None, description="Name of an existing IP threat feed.")    
    file_filter_profile_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable file filter.")    
    file_filter_profile: str = Field(max_length=47, default="", description="Name of an existing file-filter profile.")  # datasource: ['file-filter.profile.name']    
    ips_dos_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS DoS anomaly detection.")    
    anomaly: list[Anomaly] = Field(default=None, description="Configuration method to edit Denial of Service (DoS) anomaly settings.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SnifferModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
            >>> policy = SnifferModel(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
            >>> policy = SnifferModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
            >>> policy = SnifferModel(
            ...     av_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_av_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
            >>> policy = SnifferModel(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
            >>> policy = SnifferModel(
            ...     emailfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_emailfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
            >>> policy = SnifferModel(
            ...     dlp_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dlp_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
    async def validate_ip_threatfeed_references(self, client: Any) -> list[str]:
        """
        Validate ip_threatfeed references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SnifferModel(
            ...     ip_threatfeed=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ip_threatfeed_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ip_threatfeed", [])
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
            if await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ip-Threatfeed '{value}' not found in "
                    "system/external-resource"
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
            >>> policy = SnifferModel(
            ...     file_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_file_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.sniffer.post(policy.to_fortios_dict())
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
        errors = await self.validate_application_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_sensor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_av_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_emailfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dlp_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ip_threatfeed_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_file_filter_profile_references(client)
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
    "SnifferModel",    "SnifferIpThreatfeed",    "SnifferAnomaly",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.857882Z
# ============================================================================