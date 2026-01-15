"""Type stubs for LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom_field import CustomField
    from .eventfilter import Eventfilter
    from .gui_display import GuiDisplay
    from .setting import Setting
    from .threat_weight import ThreatWeight
    from .disk import Disk
    from .fortianalyzer import Fortianalyzer
    from .fortianalyzer2 import Fortianalyzer2
    from .fortianalyzer3 import Fortianalyzer3
    from .fortianalyzer_cloud import FortianalyzerCloud
    from .fortiguard import Fortiguard
    from .memory import Memory
    from .null_device import NullDevice
    from .syslogd import Syslogd
    from .syslogd2 import Syslogd2
    from .syslogd3 import Syslogd3
    from .syslogd4 import Syslogd4
    from .tacacs_plusaccounting import TacacsPlusaccounting
    from .tacacs_plusaccounting2 import TacacsPlusaccounting2
    from .tacacs_plusaccounting3 import TacacsPlusaccounting3
    from .webtrends import Webtrends

__all__ = [
    "CustomField",
    "Eventfilter",
    "GuiDisplay",
    "Setting",
    "ThreatWeight",
    "Log",
]


class Log:
    """LOG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    disk: Disk
    fortianalyzer: Fortianalyzer
    fortianalyzer2: Fortianalyzer2
    fortianalyzer3: Fortianalyzer3
    fortianalyzer_cloud: FortianalyzerCloud
    fortiguard: Fortiguard
    memory: Memory
    null_device: NullDevice
    syslogd: Syslogd
    syslogd2: Syslogd2
    syslogd3: Syslogd3
    syslogd4: Syslogd4
    tacacs_plusaccounting: TacacsPlusaccounting
    tacacs_plusaccounting2: TacacsPlusaccounting2
    tacacs_plusaccounting3: TacacsPlusaccounting3
    webtrends: Webtrends
    custom_field: CustomField
    eventfilter: Eventfilter
    gui_display: GuiDisplay
    setting: Setting
    threat_weight: ThreatWeight

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize log category with HTTP client."""
        ...
