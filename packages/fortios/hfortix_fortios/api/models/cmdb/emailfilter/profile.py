"""
Pydantic Models for CMDB - emailfilter/profile

Runtime validation models for emailfilter/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileImap(BaseModel):
    """
    Child table model for imap.
    
    IMAP.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")    
    action: Literal["pass", "tag"] | None = Field(default="tag", description="Action for spam email.")    
    tag_type: list[TagType] = Field(default="subject spaminfo", description="Tag subject or header for spam email.")    
    tag_msg: str | None = Field(max_length=63, default="Spam", description="Subject text or header added to spam email.")
class ProfilePop3(BaseModel):
    """
    Child table model for pop3.
    
    POP3.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")    
    action: Literal["pass", "tag"] | None = Field(default="tag", description="Action for spam email.")    
    tag_type: list[TagType] = Field(default="subject spaminfo", description="Tag subject or header for spam email.")    
    tag_msg: str | None = Field(max_length=63, default="Spam", description="Subject text or header added to spam email.")
class ProfileSmtp(BaseModel):
    """
    Child table model for smtp.
    
    SMTP.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")    
    action: Literal["pass", "tag", "discard"] | None = Field(default="discard", description="Action for spam email.")    
    tag_type: list[TagType] = Field(default="subject spaminfo", description="Tag subject or header for spam email.")    
    tag_msg: str | None = Field(max_length=63, default="Spam", description="Subject text or header added to spam email.")    
    hdrip: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable SMTP email header IP checks for spamfsip, spamrbl, and spambal filters.")    
    local_override: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable local filter to override SMTP remote check result.")
class ProfileMapi(BaseModel):
    """
    Child table model for mapi.
    
    MAPI.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")    
    action: Literal["pass", "discard"] | None = Field(default="pass", description="Action for spam email.")
class ProfileMsnHotmail(BaseModel):
    """
    Child table model for msn-hotmail.
    
    MSN Hotmail.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")
class ProfileYahooMail(BaseModel):
    """
    Child table model for yahoo-mail.
    
    Yahoo! Mail.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")
class ProfileGmail(BaseModel):
    """
    Child table model for gmail.
    
    Gmail.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")
class ProfileOtherWebmails(BaseModel):
    """
    Child table model for other-webmails.
    
    Other supported webmails.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    log_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of all email traffic.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProfileOptionsEnum(str, Enum):
    """Allowed values for options field."""
    BANNEDWORD = "bannedword"    SPAMBAL = "spambal"    SPAMFSIP = "spamfsip"    SPAMFSSUBMIT = "spamfssubmit"    SPAMFSCHKSUM = "spamfschksum"    SPAMFSURL = "spamfsurl"    SPAMHELODNS = "spamhelodns"    SPAMRADDRDNS = "spamraddrdns"    SPAMRBL = "spamrbl"    SPAMHDRCHECK = "spamhdrcheck"    SPAMFSPHISH = "spamfsphish"

# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for emailfilter/profile configuration.
    
    Configure Email Filter profiles.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - feature_set: pattern=        - replacemsg_group: max_length=35 pattern=        - spam_log: pattern=        - spam_log_fortiguard_response: pattern=        - spam_filtering: pattern=        - external: pattern=        - options: pattern=        - imap: pattern=        - pop3: pattern=        - smtp: pattern=        - mapi: pattern=        - msn_hotmail: pattern=        - yahoo_mail: pattern=        - gmail: pattern=        - other_webmails: pattern=        - spam_bword_threshold: min=0 max=2147483647 pattern=        - spam_bword_table: min=0 max=4294967295 pattern=        - spam_bal_table: min=0 max=4294967295 pattern=        - spam_mheader_table: min=0 max=4294967295 pattern=        - spam_rbl_table: min=0 max=4294967295 pattern=        - spam_iptrust_table: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    feature_set: Literal["flow", "proxy"] | None = Field(default="flow", description="Flow/proxy feature set.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    spam_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable spam logging for email filtering.")    
    spam_log_fortiguard_response: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging FortiGuard spam response.")    
    spam_filtering: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable spam filtering.")    
    external: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable external Email inspection.")    
    options: list[Options] = Field(default="", description="Options.")    
    imap: list[Imap] = Field(default=None, description="IMAP.")    
    pop3: list[Pop3] = Field(default=None, description="POP3.")    
    smtp: list[Smtp] = Field(default=None, description="SMTP.")    
    mapi: list[Mapi] = Field(default=None, description="MAPI.")    
    msn_hotmail: list[MsnHotmail] = Field(default=None, description="MSN Hotmail.")    
    yahoo_mail: list[YahooMail] = Field(default=None, description="Yahoo! Mail.")    
    gmail: list[Gmail] = Field(default=None, description="Gmail.")    
    other_webmails: list[OtherWebmails] = Field(default=None, description="Other supported webmails.")    
    spam_bword_threshold: int | None = Field(ge=0, le=2147483647, default=10, description="Spam banned word threshold.")    
    spam_bword_table: int | None = Field(ge=0, le=4294967295, default=0, description="Anti-spam banned word table ID.")  # datasource: ['emailfilter.bword.id']    
    spam_bal_table: int | None = Field(ge=0, le=4294967295, default=0, description="Anti-spam block/allow list table ID.")  # datasource: ['emailfilter.block-allow-list.id']    
    spam_mheader_table: int | None = Field(ge=0, le=4294967295, default=0, description="Anti-spam MIME header table ID.")  # datasource: ['emailfilter.mheader.id']    
    spam_rbl_table: int | None = Field(ge=0, le=4294967295, default=0, description="Anti-spam DNSBL table ID.")  # datasource: ['emailfilter.dnsbl.id']    
    spam_iptrust_table: int | None = Field(ge=0, le=4294967295, default=0, description="Anti-spam IP trust table ID.")  # datasource: ['emailfilter.iptrust.id']    
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
    @field_validator('spam_bword_table')
    @classmethod
    def validate_spam_bword_table(cls, v: Any) -> Any:
        """
        Validate spam_bword_table field.
        
        Datasource: ['emailfilter.bword.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('spam_bal_table')
    @classmethod
    def validate_spam_bal_table(cls, v: Any) -> Any:
        """
        Validate spam_bal_table field.
        
        Datasource: ['emailfilter.block-allow-list.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('spam_mheader_table')
    @classmethod
    def validate_spam_mheader_table(cls, v: Any) -> Any:
        """
        Validate spam_mheader_table field.
        
        Datasource: ['emailfilter.mheader.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('spam_rbl_table')
    @classmethod
    def validate_spam_rbl_table(cls, v: Any) -> Any:
        """
        Validate spam_rbl_table field.
        
        Datasource: ['emailfilter.dnsbl.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('spam_iptrust_table')
    @classmethod
    def validate_spam_iptrust_table(cls, v: Any) -> Any:
        """
        Validate spam_iptrust_table field.
        
        Datasource: ['emailfilter.iptrust.id']
        
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
            ...     result = await fgt.api.cmdb.emailfilter.profile.post(policy.to_fortios_dict())
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
    async def validate_spam_bword_table_references(self, client: Any) -> list[str]:
        """
        Validate spam_bword_table references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/bword        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     spam_bword_table="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_spam_bword_table_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.emailfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "spam_bword_table", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.bword.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Spam-Bword-Table '{value}' not found in "
                "emailfilter/bword"
            )        
        return errors    
    async def validate_spam_bal_table_references(self, client: Any) -> list[str]:
        """
        Validate spam_bal_table references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/block-allow-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     spam_bal_table="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_spam_bal_table_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.emailfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "spam_bal_table", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.block-allow-list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Spam-Bal-Table '{value}' not found in "
                "emailfilter/block-allow-list"
            )        
        return errors    
    async def validate_spam_mheader_table_references(self, client: Any) -> list[str]:
        """
        Validate spam_mheader_table references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/mheader        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     spam_mheader_table="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_spam_mheader_table_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.emailfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "spam_mheader_table", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.mheader.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Spam-Mheader-Table '{value}' not found in "
                "emailfilter/mheader"
            )        
        return errors    
    async def validate_spam_rbl_table_references(self, client: Any) -> list[str]:
        """
        Validate spam_rbl_table references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/dnsbl        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     spam_rbl_table="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_spam_rbl_table_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.emailfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "spam_rbl_table", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.dnsbl.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Spam-Rbl-Table '{value}' not found in "
                "emailfilter/dnsbl"
            )        
        return errors    
    async def validate_spam_iptrust_table_references(self, client: Any) -> list[str]:
        """
        Validate spam_iptrust_table references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/iptrust        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     spam_iptrust_table="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_spam_iptrust_table_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.emailfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "spam_iptrust_table", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.iptrust.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Spam-Iptrust-Table '{value}' not found in "
                "emailfilter/iptrust"
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
        errors = await self.validate_spam_bword_table_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_spam_bal_table_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_spam_mheader_table_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_spam_rbl_table_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_spam_iptrust_table_references(client)
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
    "ProfileModel",    "ProfileImap",    "ProfilePop3",    "ProfileSmtp",    "ProfileMapi",    "ProfileMsnHotmail",    "ProfileYahooMail",    "ProfileGmail",    "ProfileOtherWebmails",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.220196Z
# ============================================================================