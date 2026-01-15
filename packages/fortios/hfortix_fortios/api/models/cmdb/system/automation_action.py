"""
Pydantic Models for CMDB - system/automation_action

Runtime validation models for system/automation_action configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class AutomationActionEmailTo(BaseModel):
    """
    Child table model for email-to.
    
    Email addresses.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=255, default="", description="Email address.")
class AutomationActionHttpHeaders(BaseModel):
    """
    Child table model for http-headers.
    
    Request headers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    key: str = Field(max_length=1023, description="Request header key.")    
    value: str = Field(max_length=4095, description="Request header value.")
class AutomationActionFormData(BaseModel):
    """
    Child table model for form-data.
    
    Form data parts for content type multipart/form-data.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    key: str = Field(max_length=1023, description="Key of the part of Multipart/form-data.")    
    value: str = Field(max_length=4095, description="Value of the part of Multipart/form-data.")
class AutomationActionSdnConnector(BaseModel):
    """
    Child table model for sdn-connector.
    
    NSX SDN connector names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="SDN connector name.")  # datasource: ['system.sdn-connector.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class AutomationActionAction_typeEnum(str, Enum):
    """Allowed values for action_type field."""
    EMAIL = "email"    FORTIEXPLORER_NOTIFICATION = "fortiexplorer-notification"    ALERT = "alert"    DISABLE_SSID = "disable-ssid"    SYSTEM_ACTIONS = "system-actions"    QUARANTINE = "quarantine"    QUARANTINE_FORTICLIENT = "quarantine-forticlient"    QUARANTINE_NSX = "quarantine-nsx"    QUARANTINE_FORTINAC = "quarantine-fortinac"    BAN_IP = "ban-ip"    AWS_LAMBDA = "aws-lambda"    AZURE_FUNCTION = "azure-function"    GOOGLE_CLOUD_FUNCTION = "google-cloud-function"    ALICLOUD_FUNCTION = "alicloud-function"    WEBHOOK = "webhook"    CLI_SCRIPT = "cli-script"    DIAGNOSE_SCRIPT = "diagnose-script"    REGULAR_EXPRESSION = "regular-expression"    SLACK_NOTIFICATION = "slack-notification"    MICROSOFT_TEAMS_NOTIFICATION = "microsoft-teams-notification"
class AutomationActionMethodEnum(str, Enum):
    """Allowed values for method field."""
    POST = "post"    PUT = "put"    GET = "get"    PATCH = "patch"    DELETE = "delete"

# ============================================================================
# Main Model
# ============================================================================

class AutomationActionModel(BaseModel):
    """
    Pydantic model for system/automation_action configuration.
    
    Action for automation stitches.
    
    Validation Rules:        - name: max_length=64 pattern=        - description: max_length=255 pattern=        - action_type: pattern=        - system_action: pattern=        - tls_certificate: max_length=35 pattern=        - forticare_email: pattern=        - email_to: pattern=        - email_from: max_length=127 pattern=        - email_subject: max_length=511 pattern=        - minimum_interval: min=0 max=2592000 pattern=        - aws_api_key: max_length=123 pattern=        - azure_function_authorization: pattern=        - azure_api_key: max_length=123 pattern=        - alicloud_function_authorization: pattern=        - alicloud_access_key_id: max_length=35 pattern=        - alicloud_access_key_secret: max_length=59 pattern=        - message_type: pattern=        - message: max_length=4095 pattern=        - replacement_message: pattern=        - replacemsg_group: max_length=35 pattern=        - protocol: pattern=        - method: pattern=        - uri: max_length=1023 pattern=        - http_body: max_length=4095 pattern=        - port: min=1 max=65535 pattern=        - http_headers: pattern=        - form_data: pattern=        - verify_host_cert: pattern=        - script: max_length=1023 pattern=        - output_size: min=1 max=1024 pattern=        - timeout: min=0 max=300 pattern=        - duration: min=1 max=36000 pattern=        - output_interval: min=0 max=36000 pattern=        - file_only: pattern=        - execute_security_fabric: pattern=        - accprofile: max_length=35 pattern=        - regular_expression: max_length=1023 pattern=        - log_debug_print: pattern=        - security_tag: max_length=255 pattern=        - sdn_connector: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=64, default="", description="Name.")    
    description: str | None = Field(max_length=255, default=None, description="Description.")    
    action_type: ActionTypeEnum | None = Field(default="alert", description="Action type.")    
    system_action: Literal["reboot", "shutdown", "backup-config"] = Field(default="", description="System action type.")    
    tls_certificate: str | None = Field(max_length=35, default="", description="Custom TLS certificate for API request.")  # datasource: ['certificate.local.name']    
    forticare_email: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable use of your FortiCare email address as the email-to address.")    
    email_to: list[EmailTo] = Field(default=None, description="Email addresses.")    
    email_from: str | None = Field(max_length=127, default=None, description="Email sender name.")    
    email_subject: str | None = Field(max_length=511, default=None, description="Email subject.")    
    minimum_interval: int | None = Field(ge=0, le=2592000, default=0, description="Limit execution to no more than once in this interval (in seconds).")    
    aws_api_key: Any = Field(max_length=123, description="AWS API Gateway API key.")    
    azure_function_authorization: Literal["anonymous", "function", "admin"] = Field(default="anonymous", description="Azure function authorization level.")    
    azure_api_key: Any = Field(max_length=123, default=None, description="Azure function API key.")    
    alicloud_function_authorization: Literal["anonymous", "function"] = Field(default="anonymous", description="AliCloud function authorization type.")    
    alicloud_access_key_id: str = Field(max_length=35, default="", description="AliCloud AccessKey ID.")    
    alicloud_access_key_secret: Any = Field(max_length=59, description="AliCloud AccessKey secret.")    
    message_type: Literal["text", "json", "form-data"] = Field(default="text", description="Message type.")    
    message: str = Field(max_length=4095, default="Time: %%log.date%% %%log.time%%
Device: %%log.devid%% (%%log.vd%%)
Level: %%log.level%%
Event: %%log.logdesc%%
Raw log:
%%log%%", description="Message content.")    
    replacement_message: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable replacement message.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    protocol: Literal["http", "https"] = Field(default="http", description="Request protocol.")    
    method: MethodEnum = Field(default="post", description="Request method (POST, PUT, GET, PATCH or DELETE).")    
    uri: str = Field(max_length=1023, description="Request API URI.")    
    http_body: str | None = Field(max_length=4095, default=None, description="Request body (if necessary). Should be serialized json string.")    
    port: int | None = Field(ge=1, le=65535, default=0, description="Protocol port.")    
    http_headers: list[HttpHeaders] = Field(default=None, description="Request headers.")    
    form_data: list[FormData] = Field(default=None, description="Form data parts for content type multipart/form-data.")    
    verify_host_cert: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable verification of the remote host certificate.")    
    script: str = Field(max_length=1023, description="CLI script.")    
    output_size: int | None = Field(ge=1, le=1024, default=10, description="Number of megabytes to limit script output to (1 - 1024, default = 10).")    
    timeout: int | None = Field(ge=0, le=300, default=0, description="Maximum running time for this script in seconds (0 = no timeout).")    
    duration: int | None = Field(ge=1, le=36000, default=5, description="Maximum running time for this script in seconds.")    
    output_interval: int | None = Field(ge=0, le=36000, default=0, description="Collect the outputs for each output-interval in seconds (0 = no intermediate output).")    
    file_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the output in files only.")    
    execute_security_fabric: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable execution of CLI script on all or only one FortiGate unit in the Security Fabric.")    
    accprofile: str | None = Field(max_length=35, default="", description="Access profile for CLI script action to access FortiGate features.")  # datasource: ['system.accprofile.name']    
    regular_expression: str = Field(max_length=1023, description="Regular expression string.")    
    log_debug_print: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging debug print output from diagnose action.")    
    security_tag: str = Field(max_length=255, default="", description="NSX security tag.")    
    sdn_connector: list[SdnConnector] = Field(default=None, description="NSX SDN connector names.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('tls_certificate')
    @classmethod
    def validate_tls_certificate(cls, v: Any) -> Any:
        """
        Validate tls_certificate field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    @field_validator('accprofile')
    @classmethod
    def validate_accprofile(cls, v: Any) -> Any:
        """
        Validate accprofile field.
        
        Datasource: ['system.accprofile.name']
        
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
    async def validate_tls_certificate_references(self, client: Any) -> list[str]:
        """
        Validate tls_certificate references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationActionModel(
            ...     tls_certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tls_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_action.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "tls_certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Tls-Certificate '{value}' not found in "
                "certificate/local"
            )        
        return errors    
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
            >>> policy = AutomationActionModel(
            ...     replacemsg_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_action.post(policy.to_fortios_dict())
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
    async def validate_accprofile_references(self, client: Any) -> list[str]:
        """
        Validate accprofile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/accprofile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationActionModel(
            ...     accprofile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_accprofile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_action.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "accprofile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Accprofile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_sdn_connector_references(self, client: Any) -> list[str]:
        """
        Validate sdn_connector references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdn-connector        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationActionModel(
            ...     sdn_connector=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sdn_connector_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_action.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "sdn_connector", [])
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
            if await client.api.cmdb.system.sdn-connector.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Sdn-Connector '{value}' not found in "
                    "system/sdn-connector"
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
        
        errors = await self.validate_tls_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_replacemsg_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_accprofile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sdn_connector_references(client)
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
    "AutomationActionModel",    "AutomationActionEmailTo",    "AutomationActionHttpHeaders",    "AutomationActionFormData",    "AutomationActionSdnConnector",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.025267Z
# ============================================================================