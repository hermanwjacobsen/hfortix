"""
Pydantic Models for CMDB - report/layout

Runtime validation models for report/layout configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class LayoutPage(BaseModel):
    """
    Child table model for page.
    
    Configure report page.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    paper: Literal["a4", "letter"] | None = Field(default="a4", description="Report page paper.")    
    column_break_before: list[ColumnBreakBefore] = Field(default="", description="Report page auto column break before heading.")    
    page_break_before: list[PageBreakBefore] = Field(default="", description="Report page auto page break before heading.")    
    options: list[Options] = Field(default="", description="Report page options.")    
    header: list[Header] = Field(default=None, description="Configure report page header.")    
    footer: list[Footer] = Field(default=None, description="Configure report page footer.")
class LayoutBodyItem(BaseModel):
    """
    Child table model for body-item.
    
    Configure report body item.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Report item ID.")    
    description: str | None = Field(max_length=63, default="", description="Description.")    
    type: TypeEnum | None = Field(default="text", description="Report item type.")    
    style: str | None = Field(max_length=71, default="", description="Report item style.")    
    top_n: int | None = Field(ge=0, le=4294967295, default=0, description="Value of top.")    
    parameters: list[Parameters] = Field(default=None, description="Parameters.")    
    text_component: TextComponentEnum | None = Field(default="text", description="Report item text component.")    
    content: str | None = Field(max_length=511, default="", description="Report item text content.")    
    img_src: str | None = Field(max_length=127, default="", description="Report item image file name.")    
    chart: str | None = Field(max_length=71, default="", description="Report item chart name.")    
    chart_options: list[ChartOptions] = Field(default="include-no-data hide-title show-caption", description="Report chart options.")    
    misc_component: MiscComponentEnum | None = Field(default="hline", description="Report item miscellaneous component.")    
    title: str | None = Field(max_length=511, default="", description="Report section title.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LayoutOptionsEnum(str, Enum):
    """Allowed values for options field."""
    INCLUDE_TABLE_OF_CONTENT = "include-table-of-content"    AUTO_NUMBERING_HEADING = "auto-numbering-heading"    VIEW_CHART_AS_HEADING = "view-chart-as-heading"    SHOW_HTML_NAVBAR_BEFORE_HEADING = "show-html-navbar-before-heading"    DUMMY_OPTION = "dummy-option"
class LayoutDayEnum(str, Enum):
    """Allowed values for day field."""
    SUNDAY = "sunday"    MONDAY = "monday"    TUESDAY = "tuesday"    WEDNESDAY = "wednesday"    THURSDAY = "thursday"    FRIDAY = "friday"    SATURDAY = "saturday"

# ============================================================================
# Main Model
# ============================================================================

class LayoutModel(BaseModel):
    """
    Pydantic model for report/layout configuration.
    
    Report layout configuration.
    
    Validation Rules:        - name: max_length=35 pattern=        - title: max_length=127 pattern=        - subtitle: max_length=127 pattern=        - description: max_length=127 pattern=        - style_theme: max_length=35 pattern=        - options: pattern=        - format: pattern=        - schedule_type: pattern=        - day: pattern=        - time: pattern=        - cutoff_option: pattern=        - cutoff_time: pattern=        - email_send: pattern=        - email_recipients: max_length=511 pattern=        - max_pdf_report: min=1 max=365 pattern=        - page: pattern=        - body_item: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Report layout name.")    
    title: str | None = Field(max_length=127, default="", description="Report title.")    
    subtitle: str | None = Field(max_length=127, default="", description="Report subtitle.")    
    description: str | None = Field(max_length=127, default="", description="Description.")    
    style_theme: str = Field(max_length=35, default="", description="Report style theme.")    
    options: list[Options] = Field(default="include-table-of-content auto-numbering-heading view-chart-as-heading", description="Report layout options.")    
    format: list[Format] = Field(default="pdf", description="Report format.")    
    schedule_type: Literal["demand", "daily", "weekly"] | None = Field(default="daily", description="Report schedule type.")    
    day: DayEnum | None = Field(default="sunday", description="Schedule days of week to generate report.")    
    time: str | None = Field(default="", description="Schedule time to generate report (format = hh:mm).")    
    cutoff_option: Literal["run-time", "custom"] | None = Field(default="run-time", description="Cutoff-option is either run-time or custom.")    
    cutoff_time: str | None = Field(default="", description="Custom cutoff time to generate report (format = hh:mm).")    
    email_send: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending emails after reports are generated.")    
    email_recipients: str | None = Field(max_length=511, default="", description="Email recipients for generated reports.")    
    max_pdf_report: int | None = Field(ge=1, le=365, default=31, description="Maximum number of PDF reports to keep at one time (oldest report is overwritten).")    
    page: list[Page] = Field(default=None, description="Configure report page.")    
    body_item: list[BodyItem] = Field(default=None, description="Configure report body item.")    
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

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "LayoutModel",    "LayoutPage",    "LayoutBodyItem",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.249725Z
# ============================================================================