"""
Pydantic Models for CMDB - wireless_controller/setting

Runtime validation models for wireless_controller/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SettingOffendingSsid(BaseModel):
    """
    Child table model for offending-ssid.
    
    Configure offending SSID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=65535, default=0, description="ID.")    
    ssid_pattern: str = Field(max_length=33, default="", description="Define offending SSID pattern (case insensitive). For example, word, word*, *word, wo*rd.")    
    action: list[Action] = Field(default="log", description="Actions taken for detected offending SSID.")
class SettingDarrpOptimizeSchedules(BaseModel):
    """
    Child table model for darrp-optimize-schedules.
    
    Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.group.name', 'firewall.schedule.recurring.name', 'firewall.schedule.onetime.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingCountryEnum(str, Enum):
    """Allowed values for country field."""
    __ = "--"    AF = "AF"    AL = "AL"    DZ = "DZ"    AS = "AS"    AO = "AO"    AR = "AR"    AM = "AM"    AU = "AU"    AT = "AT"    AZ = "AZ"    BS = "BS"    BH = "BH"    BD = "BD"    BB = "BB"    BY = "BY"    BE = "BE"    BZ = "BZ"    BJ = "BJ"    BM = "BM"    BT = "BT"    BO = "BO"    BA = "BA"    BW = "BW"    BR = "BR"    BN = "BN"    BG = "BG"    BF = "BF"    KH = "KH"    CM = "CM"    KY = "KY"    CF = "CF"    TD = "TD"    CL = "CL"    CN = "CN"    CX = "CX"    CO = "CO"    CG = "CG"    CD = "CD"    CR = "CR"    HR = "HR"    CY = "CY"    CZ = "CZ"    DK = "DK"    DJ = "DJ"    DM = "DM"    DO = "DO"    EC = "EC"    EG = "EG"    SV = "SV"    ET = "ET"    EE = "EE"    GF = "GF"    PF = "PF"    FO = "FO"    FJ = "FJ"    FI = "FI"    FR = "FR"    GA = "GA"    GE = "GE"    GM = "GM"    DE = "DE"    GH = "GH"    GI = "GI"    GR = "GR"    GL = "GL"    GD = "GD"    GP = "GP"    GU = "GU"    GT = "GT"    GY = "GY"    HT = "HT"    HN = "HN"    HK = "HK"    HU = "HU"    IS = "IS"    IN = "IN"    ID = "ID"    IQ = "IQ"    IE = "IE"    IM = "IM"    IL = "IL"    IT = "IT"    CI = "CI"    JM = "JM"    JO = "JO"    KZ = "KZ"    KE = "KE"    KR = "KR"    KW = "KW"    LA = "LA"    LV = "LV"    LB = "LB"    LS = "LS"    LR = "LR"    LY = "LY"    LI = "LI"    LT = "LT"    LU = "LU"    MO = "MO"    MK = "MK"    MG = "MG"    MW = "MW"    MY = "MY"    MV = "MV"    ML = "ML"    MT = "MT"    MH = "MH"    MQ = "MQ"    MR = "MR"    MU = "MU"    YT = "YT"    MX = "MX"    FM = "FM"    MD = "MD"    MC = "MC"    MN = "MN"    MA = "MA"    MZ = "MZ"    MM = "MM"    NA = "NA"    NP = "NP"    NL = "NL"    AN = "AN"    AW = "AW"    NZ = "NZ"    NI = "NI"    NE = "NE"    NG = "NG"    NO = "NO"    MP = "MP"    OM = "OM"    PK = "PK"    PW = "PW"    PA = "PA"    PG = "PG"    PY = "PY"    PE = "PE"    PH = "PH"    PL = "PL"    PT = "PT"    PR = "PR"    QA = "QA"    RE = "RE"    RO = "RO"    RU = "RU"    RW = "RW"    BL = "BL"    KN = "KN"    LC = "LC"    MF = "MF"    PM = "PM"    VC = "VC"    SA = "SA"    SN = "SN"    RS = "RS"    ME = "ME"    SL = "SL"    SG = "SG"    SK = "SK"    SI = "SI"    SO = "SO"    ZA = "ZA"    ES = "ES"    LK = "LK"    SR = "SR"    SZ = "SZ"    SE = "SE"    CH = "CH"    TW = "TW"    TZ = "TZ"    TH = "TH"    TL = "TL"    TG = "TG"    TT = "TT"    TN = "TN"    TR = "TR"    TM = "TM"    AE = "AE"    TC = "TC"    UG = "UG"    UA = "UA"    GB = "GB"    US = "US"    PS = "PS"    UY = "UY"    UZ = "UZ"    VU = "VU"    VE = "VE"    VN = "VN"    VI = "VI"    WF = "WF"    YE = "YE"    ZM = "ZM"    ZW = "ZW"    JP = "JP"    CA = "CA"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for wireless_controller/setting configuration.
    
    VDOM wireless controller configuration.
    
    Validation Rules:        - account_id: max_length=63 pattern=        - country: pattern=        - duplicate_ssid: pattern=        - fapc_compatibility: pattern=        - wfa_compatibility: pattern=        - phishing_ssid_detect: pattern=        - fake_ssid_action: pattern=        - offending_ssid: pattern=        - device_weight: min=0 max=255 pattern=        - device_holdoff: min=0 max=60 pattern=        - device_idle: min=0 max=14400 pattern=        - firmware_provision_on_authorization: pattern=        - rolling_wtp_upgrade: pattern=        - darrp_optimize: min=0 max=86400 pattern=        - darrp_optimize_schedules: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    account_id: str | None = Field(max_length=63, default="", description="FortiCloud customer account ID.")    
    country: CountryEnum | None = Field(default="US", description="Country or region in which the FortiGate is located. The country determines the 802.11 bands and channels that are available.")    
    duplicate_ssid: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing Virtual Access Points (VAPs) to use the same SSID name in the same VDOM.")    
    fapc_compatibility: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FAP-C series compatibility.")    
    wfa_compatibility: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WFA compatibility.")    
    phishing_ssid_detect: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable phishing SSID detection.")    
    fake_ssid_action: list[FakeSsidAction] = Field(default="log", description="Actions taken for detected fake SSID.")    
    offending_ssid: list[OffendingSsid] = Field(default=None, description="Configure offending SSID.")    
    device_weight: int | None = Field(ge=0, le=255, default=1, description="Upper limit of confidence of device for identification (0 - 255, default = 1, 0 = disable).")    
    device_holdoff: int | None = Field(ge=0, le=60, default=5, description="Lower limit of creation time of device for identification in minutes (0 - 60, default = 5).")    
    device_idle: int | None = Field(ge=0, le=14400, default=1440, description="Upper limit of idle time of device for identification in minutes (0 - 14400, default = 1440).")    
    firmware_provision_on_authorization: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic provisioning of latest firmware on authorization.")    
    rolling_wtp_upgrade: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable rolling WTP upgrade (default = disable).")    
    darrp_optimize: int | None = Field(ge=0, le=86400, default=86400, description="Time for running Distributed Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default = 86400, 0 = disable).")    
    darrp_optimize_schedules: list[DarrpOptimizeSchedules] = Field(default=None, description="Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    async def validate_darrp_optimize_schedules_references(self, client: Any) -> list[str]:
        """
        Validate darrp_optimize_schedules references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/schedule/group        - firewall/schedule/recurring        - firewall/schedule/onetime        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     darrp_optimize_schedules=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_darrp_optimize_schedules_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "darrp_optimize_schedules", [])
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
            if await client.api.cmdb.firewall.schedule.group.exists(value):
                found = True
            elif await client.api.cmdb.firewall.schedule.recurring.exists(value):
                found = True
            elif await client.api.cmdb.firewall.schedule.onetime.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Darrp-Optimize-Schedules '{value}' not found in "
                    "firewall/schedule/group or firewall/schedule/recurring or firewall/schedule/onetime"
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
        
        errors = await self.validate_darrp_optimize_schedules_references(client)
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
    "SettingModel",    "SettingOffendingSsid",    "SettingDarrpOptimizeSchedules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.554046Z
# ============================================================================