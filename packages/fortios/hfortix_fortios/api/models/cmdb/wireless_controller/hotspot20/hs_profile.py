"""
Pydantic Models for CMDB - wireless_controller/hotspot20/hs_profile

Runtime validation models for wireless_controller/hotspot20/hs_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class HsProfileOsuProvider(BaseModel):
    """
    Child table model for osu-provider.
    
    Manually selected list of OSU provider(s).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="OSU provider name.")  # datasource: ['wireless-controller.hotspot20.h2qp-osu-provider.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class HsProfileAccess_network_typeEnum(str, Enum):
    """Allowed values for access_network_type field."""
    PRIVATE_NETWORK = "private-network"    PRIVATE_NETWORK_WITH_GUEST_ACCESS = "private-network-with-guest-access"    CHARGEABLE_PUBLIC_NETWORK = "chargeable-public-network"    FREE_PUBLIC_NETWORK = "free-public-network"    PERSONAL_DEVICE_NETWORK = "personal-device-network"    EMERGENCY_SERVICES_ONLY_NETWORK = "emergency-services-only-network"    TEST_OR_EXPERIMENTAL = "test-or-experimental"    WILDCARD = "wildcard"
class HsProfileVenue_groupEnum(str, Enum):
    """Allowed values for venue_group field."""
    UNSPECIFIED = "unspecified"    ASSEMBLY = "assembly"    BUSINESS = "business"    EDUCATIONAL = "educational"    FACTORY = "factory"    INSTITUTIONAL = "institutional"    MERCANTILE = "mercantile"    RESIDENTIAL = "residential"    STORAGE = "storage"    UTILITY = "utility"    VEHICULAR = "vehicular"    OUTDOOR = "outdoor"
class HsProfileVenue_typeEnum(str, Enum):
    """Allowed values for venue_type field."""
    UNSPECIFIED = "unspecified"    ARENA = "arena"    STADIUM = "stadium"    PASSENGER_TERMINAL = "passenger-terminal"    AMPHITHEATER = "amphitheater"    AMUSEMENT_PARK = "amusement-park"    PLACE_OF_WORSHIP = "place-of-worship"    CONVENTION_CENTER = "convention-center"    LIBRARY = "library"    MUSEUM = "museum"    RESTAURANT = "restaurant"    THEATER = "theater"    BAR = "bar"    COFFEE_SHOP = "coffee-shop"    ZOO_OR_AQUARIUM = "zoo-or-aquarium"    EMERGENCY_CENTER = "emergency-center"    DOCTOR_OFFICE = "doctor-office"    BANK = "bank"    FIRE_STATION = "fire-station"    POLICE_STATION = "police-station"    POST_OFFICE = "post-office"    PROFESSIONAL_OFFICE = "professional-office"    RESEARCH_FACILITY = "research-facility"    ATTORNEY_OFFICE = "attorney-office"    PRIMARY_SCHOOL = "primary-school"    SECONDARY_SCHOOL = "secondary-school"    UNIVERSITY_OR_COLLEGE = "university-or-college"    FACTORY = "factory"    HOSPITAL = "hospital"    LONG_TERM_CARE_FACILITY = "long-term-care-facility"    REHAB_CENTER = "rehab-center"    GROUP_HOME = "group-home"    PRISON_OR_JAIL = "prison-or-jail"    RETAIL_STORE = "retail-store"    GROCERY_MARKET = "grocery-market"    AUTO_SERVICE_STATION = "auto-service-station"    SHOPPING_MALL = "shopping-mall"    GAS_STATION = "gas-station"    PRIVATE = "private"    HOTEL_OR_MOTEL = "hotel-or-motel"    DORMITORY = "dormitory"    BOARDING_HOUSE = "boarding-house"    AUTOMOBILE = "automobile"    AIRPLANE = "airplane"    BUS = "bus"    FERRY = "ferry"    SHIP_OR_BOAT = "ship-or-boat"    TRAIN = "train"    MOTOR_BIKE = "motor-bike"    MUNI_MESH_NETWORK = "muni-mesh-network"    CITY_PARK = "city-park"    REST_AREA = "rest-area"    TRAFFIC_CONTROL = "traffic-control"    BUS_STOP = "bus-stop"    KIOSK = "kiosk"

# ============================================================================
# Main Model
# ============================================================================

class HsProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/hotspot20/hs_profile configuration.
    
    Configure hotspot profile.
    
    Validation Rules:        - name: max_length=35 pattern=        - release: min=1 max=3 pattern=        - access_network_type: pattern=        - access_network_internet: pattern=        - access_network_asra: pattern=        - access_network_esr: pattern=        - access_network_uesa: pattern=        - venue_group: pattern=        - venue_type: pattern=        - hessid: pattern=        - proxy_arp: pattern=        - l2tif: pattern=        - pame_bi: pattern=        - anqp_domain_id: min=0 max=65535 pattern=        - domain_name: max_length=255 pattern=        - osu_ssid: max_length=255 pattern=        - gas_comeback_delay: min=100 max=10000 pattern=        - gas_fragmentation_limit: min=512 max=4096 pattern=        - dgaf: pattern=        - deauth_request_timeout: min=30 max=120 pattern=        - wnm_sleep_mode: pattern=        - bss_transition: pattern=        - venue_name: max_length=35 pattern=        - venue_url: max_length=35 pattern=        - roaming_consortium: max_length=35 pattern=        - nai_realm: max_length=35 pattern=        - oper_friendly_name: max_length=35 pattern=        - oper_icon: max_length=35 pattern=        - advice_of_charge: max_length=35 pattern=        - osu_provider_nai: max_length=35 pattern=        - terms_and_conditions: max_length=35 pattern=        - osu_provider: pattern=        - wan_metrics: max_length=35 pattern=        - network_auth: max_length=35 pattern=        - 3gpp_plmn: max_length=35 pattern=        - conn_cap: max_length=35 pattern=        - qos_map: max_length=35 pattern=        - ip_addr_type: max_length=35 pattern=        - wba_open_roaming: pattern=        - wba_financial_clearing_provider: max_length=127 pattern=        - wba_data_clearing_provider: max_length=127 pattern=        - wba_charging_currency: max_length=3 pattern=        - wba_charging_rate: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Hotspot profile name.")    
    release: int | None = Field(ge=1, le=3, default=2, description="Hotspot 2.0 Release number (1, 2, 3, default = 2).")    
    access_network_type: AccessNetworkTypeEnum | None = Field(default="private-network", description="Access network type.")    
    access_network_internet: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable connectivity to the Internet.")    
    access_network_asra: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable additional step required for access (ASRA).")    
    access_network_esr: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable emergency services reachable (ESR).")    
    access_network_uesa: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable unauthenticated emergency service accessible (UESA).")    
    venue_group: VenueGroupEnum | None = Field(default="unspecified", description="Venue group.")    
    venue_type: VenueTypeEnum | None = Field(default="unspecified", description="Venue type.")    
    hessid: str | None = Field(default="00:00:00:00:00:00", description="Homogeneous extended service set identifier (HESSID).")    
    proxy_arp: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Proxy ARP.")    
    l2tif: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Layer 2 traffic inspection and filtering.")    
    pame_bi: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI).")    
    anqp_domain_id: int | None = Field(ge=0, le=65535, default=0, description="ANQP Domain ID (0-65535).")    
    domain_name: str | None = Field(max_length=255, default="", description="Domain name.")    
    osu_ssid: str | None = Field(max_length=255, default="", description="Online sign up (OSU) SSID.")    
    gas_comeback_delay: int | None = Field(ge=100, le=10000, default=500, description="GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).")    
    gas_fragmentation_limit: int | None = Field(ge=512, le=4096, default=1024, description="GAS fragmentation limit (512 - 4096, default = 1024).")    
    dgaf: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable downstream group-addressed forwarding (DGAF).")    
    deauth_request_timeout: int | None = Field(ge=30, le=120, default=60, description="Deauthentication request timeout (in seconds).")    
    wnm_sleep_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable wireless network management (WNM) sleep mode.")    
    bss_transition: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable basic service set (BSS) transition Support.")    
    venue_name: str | None = Field(max_length=35, default="", description="Venue name.")  # datasource: ['wireless-controller.hotspot20.anqp-venue-name.name']    
    venue_url: str | None = Field(max_length=35, default="", description="Venue name.")  # datasource: ['wireless-controller.hotspot20.anqp-venue-url.name']    
    roaming_consortium: str | None = Field(max_length=35, default="", description="Roaming consortium list name.")  # datasource: ['wireless-controller.hotspot20.anqp-roaming-consortium.name']    
    nai_realm: str | None = Field(max_length=35, default="", description="NAI realm list name.")  # datasource: ['wireless-controller.hotspot20.anqp-nai-realm.name']    
    oper_friendly_name: str | None = Field(max_length=35, default="", description="Operator friendly name.")  # datasource: ['wireless-controller.hotspot20.h2qp-operator-name.name']    
    oper_icon: str | None = Field(max_length=35, default="", description="Operator icon.")  # datasource: ['wireless-controller.hotspot20.icon.name']    
    advice_of_charge: str | None = Field(max_length=35, default="", description="Advice of charge.")  # datasource: ['wireless-controller.hotspot20.h2qp-advice-of-charge.name']    
    osu_provider_nai: str | None = Field(max_length=35, default="", description="OSU Provider NAI.")  # datasource: ['wireless-controller.hotspot20.h2qp-osu-provider-nai.name']    
    terms_and_conditions: str | None = Field(max_length=35, default="", description="Terms and conditions.")  # datasource: ['wireless-controller.hotspot20.h2qp-terms-and-conditions.name']    
    osu_provider: list[OsuProvider] = Field(default=None, description="Manually selected list of OSU provider(s).")    
    wan_metrics: str | None = Field(max_length=35, default="", description="WAN metric name.")  # datasource: ['wireless-controller.hotspot20.h2qp-wan-metric.name']    
    network_auth: str | None = Field(max_length=35, default="", description="Network authentication name.")  # datasource: ['wireless-controller.hotspot20.anqp-network-auth-type.name']    
    3gpp_plmn: str | None = Field(max_length=35, default="", description="3GPP PLMN name.")  # datasource: ['wireless-controller.hotspot20.anqp-3gpp-cellular.name']    
    conn_cap: str | None = Field(max_length=35, default="", description="Connection capability name.")  # datasource: ['wireless-controller.hotspot20.h2qp-conn-capability.name']    
    qos_map: str | None = Field(max_length=35, default="", description="QoS MAP set ID.")  # datasource: ['wireless-controller.hotspot20.qos-map.name']    
    ip_addr_type: str | None = Field(max_length=35, default="", description="IP address type name.")  # datasource: ['wireless-controller.hotspot20.anqp-ip-address-type.name']    
    wba_open_roaming: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable WBA open roaming support.")    
    wba_financial_clearing_provider: str | None = Field(max_length=127, default="", description="WBA ID of financial clearing provider.")    
    wba_data_clearing_provider: str | None = Field(max_length=127, default="", description="WBA ID of data clearing provider.")    
    wba_charging_currency: str | None = Field(max_length=3, default="", description="Three letter currency code.")    
    wba_charging_rate: int | None = Field(ge=0, le=4294967295, default=0, description="Number of currency units per kilobyte.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('venue_name')
    @classmethod
    def validate_venue_name(cls, v: Any) -> Any:
        """
        Validate venue_name field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-venue-name.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('venue_url')
    @classmethod
    def validate_venue_url(cls, v: Any) -> Any:
        """
        Validate venue_url field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-venue-url.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('roaming_consortium')
    @classmethod
    def validate_roaming_consortium(cls, v: Any) -> Any:
        """
        Validate roaming_consortium field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-roaming-consortium.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('nai_realm')
    @classmethod
    def validate_nai_realm(cls, v: Any) -> Any:
        """
        Validate nai_realm field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-nai-realm.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('oper_friendly_name')
    @classmethod
    def validate_oper_friendly_name(cls, v: Any) -> Any:
        """
        Validate oper_friendly_name field.
        
        Datasource: ['wireless-controller.hotspot20.h2qp-operator-name.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('oper_icon')
    @classmethod
    def validate_oper_icon(cls, v: Any) -> Any:
        """
        Validate oper_icon field.
        
        Datasource: ['wireless-controller.hotspot20.icon.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('advice_of_charge')
    @classmethod
    def validate_advice_of_charge(cls, v: Any) -> Any:
        """
        Validate advice_of_charge field.
        
        Datasource: ['wireless-controller.hotspot20.h2qp-advice-of-charge.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('osu_provider_nai')
    @classmethod
    def validate_osu_provider_nai(cls, v: Any) -> Any:
        """
        Validate osu_provider_nai field.
        
        Datasource: ['wireless-controller.hotspot20.h2qp-osu-provider-nai.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('terms_and_conditions')
    @classmethod
    def validate_terms_and_conditions(cls, v: Any) -> Any:
        """
        Validate terms_and_conditions field.
        
        Datasource: ['wireless-controller.hotspot20.h2qp-terms-and-conditions.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('wan_metrics')
    @classmethod
    def validate_wan_metrics(cls, v: Any) -> Any:
        """
        Validate wan_metrics field.
        
        Datasource: ['wireless-controller.hotspot20.h2qp-wan-metric.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('network_auth')
    @classmethod
    def validate_network_auth(cls, v: Any) -> Any:
        """
        Validate network_auth field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-network-auth-type.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('3gpp_plmn')
    @classmethod
    def validate_3gpp_plmn(cls, v: Any) -> Any:
        """
        Validate 3gpp_plmn field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-3gpp-cellular.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('conn_cap')
    @classmethod
    def validate_conn_cap(cls, v: Any) -> Any:
        """
        Validate conn_cap field.
        
        Datasource: ['wireless-controller.hotspot20.h2qp-conn-capability.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('qos_map')
    @classmethod
    def validate_qos_map(cls, v: Any) -> Any:
        """
        Validate qos_map field.
        
        Datasource: ['wireless-controller.hotspot20.qos-map.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ip_addr_type')
    @classmethod
    def validate_ip_addr_type(cls, v: Any) -> Any:
        """
        Validate ip_addr_type field.
        
        Datasource: ['wireless-controller.hotspot20.anqp-ip-address-type.name']
        
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
    async def validate_venue_name_references(self, client: Any) -> list[str]:
        """
        Validate venue_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-venue-name        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     venue_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_venue_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "venue_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-venue-name.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Venue-Name '{value}' not found in "
                "wireless-controller/hotspot20/anqp-venue-name"
            )        
        return errors    
    async def validate_venue_url_references(self, client: Any) -> list[str]:
        """
        Validate venue_url references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-venue-url        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     venue_url="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_venue_url_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "venue_url", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-venue-url.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Venue-Url '{value}' not found in "
                "wireless-controller/hotspot20/anqp-venue-url"
            )        
        return errors    
    async def validate_roaming_consortium_references(self, client: Any) -> list[str]:
        """
        Validate roaming_consortium references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-roaming-consortium        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     roaming_consortium="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_roaming_consortium_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "roaming_consortium", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-roaming-consortium.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Roaming-Consortium '{value}' not found in "
                "wireless-controller/hotspot20/anqp-roaming-consortium"
            )        
        return errors    
    async def validate_nai_realm_references(self, client: Any) -> list[str]:
        """
        Validate nai_realm references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-nai-realm        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     nai_realm="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_nai_realm_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "nai_realm", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-nai-realm.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Nai-Realm '{value}' not found in "
                "wireless-controller/hotspot20/anqp-nai-realm"
            )        
        return errors    
    async def validate_oper_friendly_name_references(self, client: Any) -> list[str]:
        """
        Validate oper_friendly_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-operator-name        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     oper_friendly_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_oper_friendly_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "oper_friendly_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.h2qp-operator-name.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Oper-Friendly-Name '{value}' not found in "
                "wireless-controller/hotspot20/h2qp-operator-name"
            )        
        return errors    
    async def validate_oper_icon_references(self, client: Any) -> list[str]:
        """
        Validate oper_icon references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/icon        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     oper_icon="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_oper_icon_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "oper_icon", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.icon.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Oper-Icon '{value}' not found in "
                "wireless-controller/hotspot20/icon"
            )        
        return errors    
    async def validate_advice_of_charge_references(self, client: Any) -> list[str]:
        """
        Validate advice_of_charge references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-advice-of-charge        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     advice_of_charge="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_advice_of_charge_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "advice_of_charge", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.h2qp-advice-of-charge.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Advice-Of-Charge '{value}' not found in "
                "wireless-controller/hotspot20/h2qp-advice-of-charge"
            )        
        return errors    
    async def validate_osu_provider_nai_references(self, client: Any) -> list[str]:
        """
        Validate osu_provider_nai references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-osu-provider-nai        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     osu_provider_nai="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_osu_provider_nai_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "osu_provider_nai", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.h2qp-osu-provider-nai.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Osu-Provider-Nai '{value}' not found in "
                "wireless-controller/hotspot20/h2qp-osu-provider-nai"
            )        
        return errors    
    async def validate_terms_and_conditions_references(self, client: Any) -> list[str]:
        """
        Validate terms_and_conditions references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-terms-and-conditions        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     terms_and_conditions="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_terms_and_conditions_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "terms_and_conditions", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.h2qp-terms-and-conditions.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Terms-And-Conditions '{value}' not found in "
                "wireless-controller/hotspot20/h2qp-terms-and-conditions"
            )        
        return errors    
    async def validate_osu_provider_references(self, client: Any) -> list[str]:
        """
        Validate osu_provider references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-osu-provider        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     osu_provider=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_osu_provider_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "osu_provider", [])
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
            if await client.api.cmdb.wireless-controller.hotspot20.h2qp-osu-provider.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Osu-Provider '{value}' not found in "
                    "wireless-controller/hotspot20/h2qp-osu-provider"
                )        
        return errors    
    async def validate_wan_metrics_references(self, client: Any) -> list[str]:
        """
        Validate wan_metrics references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-wan-metric        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     wan_metrics="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wan_metrics_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "wan_metrics", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.h2qp-wan-metric.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Wan-Metrics '{value}' not found in "
                "wireless-controller/hotspot20/h2qp-wan-metric"
            )        
        return errors    
    async def validate_network_auth_references(self, client: Any) -> list[str]:
        """
        Validate network_auth references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-network-auth-type        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     network_auth="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_network_auth_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "network_auth", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-network-auth-type.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Network-Auth '{value}' not found in "
                "wireless-controller/hotspot20/anqp-network-auth-type"
            )        
        return errors    
    async def validate_3gpp_plmn_references(self, client: Any) -> list[str]:
        """
        Validate 3gpp_plmn references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-3gpp-cellular        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     3gpp_plmn="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_3gpp_plmn_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "3gpp_plmn", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-3gpp-cellular.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"3Gpp-Plmn '{value}' not found in "
                "wireless-controller/hotspot20/anqp-3gpp-cellular"
            )        
        return errors    
    async def validate_conn_cap_references(self, client: Any) -> list[str]:
        """
        Validate conn_cap references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/h2qp-conn-capability        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     conn_cap="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_conn_cap_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "conn_cap", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.h2qp-conn-capability.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Conn-Cap '{value}' not found in "
                "wireless-controller/hotspot20/h2qp-conn-capability"
            )        
        return errors    
    async def validate_qos_map_references(self, client: Any) -> list[str]:
        """
        Validate qos_map references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/qos-map        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     qos_map="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_qos_map_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "qos_map", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.qos-map.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Qos-Map '{value}' not found in "
                "wireless-controller/hotspot20/qos-map"
            )        
        return errors    
    async def validate_ip_addr_type_references(self, client: Any) -> list[str]:
        """
        Validate ip_addr_type references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/anqp-ip-address-type        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsProfileModel(
            ...     ip_addr_type="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ip_addr_type_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.hs_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ip_addr_type", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.anqp-ip-address-type.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ip-Addr-Type '{value}' not found in "
                "wireless-controller/hotspot20/anqp-ip-address-type"
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
        
        errors = await self.validate_venue_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_venue_url_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_roaming_consortium_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_nai_realm_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_oper_friendly_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_oper_icon_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_advice_of_charge_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_osu_provider_nai_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_terms_and_conditions_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_osu_provider_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_wan_metrics_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_network_auth_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_3gpp_plmn_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_conn_cap_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_qos_map_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ip_addr_type_references(client)
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
    "HsProfileModel",    "HsProfileOsuProvider",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.009444Z
# ============================================================================