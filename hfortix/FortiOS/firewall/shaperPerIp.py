"""
Per-IP Traffic Shaper Convenience Wrapper

Provides simplified syntax for per-IP traffic shaper operations with
full parameter support.
Instead of: fgt.api.cmdb.firewall.shaper_per_ip_shaper.post(data)
Use: fgt.firewall.shaper_per_ip.create(name='shaper1',
    max_bandwidth=1000, ...)
"""

import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Coroutine,
    Dict,
    Literal,
    Optional,
    Union,
)

from ..api._helpers import build_cmdb_payload_normalized

if TYPE_CHECKING:
    from ..fortios import FortiOS


def validate_shaper_name(
    name: Optional[str], operation: str = "operation"
) -> None:
    """Validate per-IP shaper name."""
    if not name:
        raise ValueError(f"Per-IP shaper name is required for {operation}")
    if isinstance(name, str) and len(name) > 35:
        raise ValueError(
            f"Per-IP shaper name cannot exceed 35 characters, "
            f"got {len(name)}"
        )


def validate_bandwidth(
    bandwidth: Optional[int], param_name: str = "bandwidth"
) -> None:
    """Validate bandwidth parameter."""
    if bandwidth is not None:
        if not isinstance(bandwidth, int):
            raise ValueError(
                f"{param_name} must be an integer, got {type(bandwidth)}"
            )
        if not 0 <= bandwidth <= 80000000:
            raise ValueError(
                f"{param_name} must be between 0 and 80000000, "
                f"got {bandwidth}"
            )


def validate_bandwidth_unit(bandwidth_unit: Optional[str]) -> None:
    """Validate bandwidth-unit parameter."""
    valid_units = ["kbps", "mbps", "gbps"]
    if bandwidth_unit is not None and bandwidth_unit not in valid_units:
        raise ValueError(
            f"Invalid bandwidth-unit '{bandwidth_unit}'. "
            f"Must be one of: {', '.join(valid_units)}"
        )


def validate_concurrent_sessions(
    sessions: Optional[int], param_name: str = "sessions"
) -> None:
    """Validate concurrent session parameters."""
    if sessions is not None:
        if not isinstance(sessions, int):
            raise ValueError(
                f"{param_name} must be an integer, got {type(sessions)}"
            )
        if not 0 <= sessions <= 2097000:
            raise ValueError(
                f"{param_name} must be between 0 and 2097000, "
                f"got {sessions}"
            )


def validate_diffserv(diffserv: Optional[str]) -> None:
    """Validate diffserv enable/disable parameter."""
    if diffserv is not None and diffserv not in ["enable", "disable"]:
        raise ValueError(
            f"Invalid diffserv value '{diffserv}'. "
            f"Must be 'enable' or 'disable'"
        )


class ShaperPerIp:
    """
    Convenience wrapper for per-IP traffic shaper operations with full
    parameter support.
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """Initialize the ShaperPerIp wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.shaper.per_ip_shaper
        self._logger = logging.getLogger("hfortix.firewall.shaper_per_ip")

    def create(
        self,
        # Required parameters
        name: str,
        # Bandwidth parameters
        max_bandwidth: Optional[int] = None,
        bandwidth_unit: Optional[Literal["kbps", "mbps", "gbps"]] = None,
        # Session limits
        max_concurrent_session: Optional[int] = None,
        max_concurrent_tcp_session: Optional[int] = None,
        max_concurrent_udp_session: Optional[int] = None,
        # DiffServ parameters
        diffserv_forward: Optional[Literal["enable", "disable"]] = None,
        diffserv_reverse: Optional[Literal["enable", "disable"]] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Create a new per-IP traffic shaper.

        Args:
            name: Traffic shaper name (max 35 chars, required)
            max_bandwidth: Upper bandwidth limit (0-80000000).
                0 means no limit. Units depend on bandwidth-unit setting
            bandwidth_unit: Unit of measurement (kbps, mbps, gbps)
            max_concurrent_session: Maximum concurrent sessions (0-2097000).
                0 means no limit
            max_concurrent_tcp_session: Maximum concurrent TCP sessions
                (0-2097000). 0 means no limit
            max_concurrent_udp_session: Maximum concurrent UDP sessions
                (0-2097000). 0 means no limit
            diffserv_forward: Enable/disable changing the Forward
                (original) DiffServ setting
            diffserv_reverse: Enable/disable changing the Reverse
                (reply) DiffServ setting
            diffservcode_forward: Forward (original) DiffServ setting
            diffservcode_rev: Reverse (reply) DiffServ setting
            vdom: Virtual domain name
            data: Additional fields as dictionary

        Returns:
            API response dictionary

        Example:
            >>> # Create per-IP shaper with bandwidth limit
            >>> result = fgt.firewall.shaper_per_ip.create(
            ...     name="per-ip-shaper-1",
            ...     max_bandwidth=5000,
            ...     bandwidth_unit="kbps",
            ...     max_concurrent_session=100
            ... )
            >>>
            >>> # Create with DiffServ settings
            >>> result = fgt.firewall.shaper_per_ip.create(
            ...     name="per-ip-shaper-2",
            ...     max_bandwidth=10000,
            ...     bandwidth_unit="mbps",
            ...     diffserv_forward="enable",
            ...     diffservcode_forward="0x28"
            ... )
        """
        validate_shaper_name(name, "create")
        validate_bandwidth(max_bandwidth, "max_bandwidth")
        validate_bandwidth_unit(bandwidth_unit)
        validate_concurrent_sessions(
            max_concurrent_session, "max_concurrent_session"
        )
        validate_concurrent_sessions(
            max_concurrent_tcp_session, "max_concurrent_tcp_session"
        )
        validate_concurrent_sessions(
            max_concurrent_udp_session, "max_concurrent_udp_session"
        )
        validate_diffserv(diffserv_forward)
        validate_diffserv(diffserv_reverse)

        payload = build_cmdb_payload_normalized(
            name=name,
            max_bandwidth=max_bandwidth,
            bandwidth_unit=bandwidth_unit,
            max_concurrent_session=max_concurrent_session,
            max_concurrent_tcp_session=max_concurrent_tcp_session,
            max_concurrent_udp_session=max_concurrent_udp_session,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            data=data,
        )

        self._logger.debug(f"Creating per-IP shaper: {name}")
        return self._api.post(payload_dict=payload, vdom=vdom)

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Retrieve per-IP shaper configuration.

        Args:
            name: Shaper name (if None, returns all shapers)
            vdom: Virtual domain name
            **kwargs: Additional query parameters

        Returns:
            API response dictionary
        """
        return self._api.get(name=name, vdom=vdom, **kwargs)

    def update(
        self,
        # Required parameter
        name: str,
        # Bandwidth parameters
        max_bandwidth: Optional[int] = None,
        bandwidth_unit: Optional[Literal["kbps", "mbps", "gbps"]] = None,
        # Session limits
        max_concurrent_session: Optional[int] = None,
        max_concurrent_tcp_session: Optional[int] = None,
        max_concurrent_udp_session: Optional[int] = None,
        # DiffServ parameters
        diffserv_forward: Optional[Literal["enable", "disable"]] = None,
        diffserv_reverse: Optional[Literal["enable", "disable"]] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Update an existing per-IP traffic shaper.

        Args:
            name: Traffic shaper name (required)
            max_bandwidth: Upper bandwidth limit (0-80000000)
            bandwidth_unit: Unit of measurement (kbps, mbps, gbps)
            max_concurrent_session: Maximum concurrent sessions (0-2097000)
            max_concurrent_tcp_session: Maximum concurrent TCP sessions
                (0-2097000)
            max_concurrent_udp_session: Maximum concurrent UDP sessions
                (0-2097000)
            diffserv_forward: Enable/disable Forward DiffServ setting
            diffserv_reverse: Enable/disable Reverse DiffServ setting
            diffservcode_forward: Forward DiffServ setting
            diffservcode_rev: Reverse DiffServ setting
            vdom: Virtual domain name
            data: Additional fields as dictionary

        Returns:
            API response dictionary
        """
        validate_shaper_name(name, "update")
        validate_bandwidth(max_bandwidth, "max_bandwidth")
        validate_bandwidth_unit(bandwidth_unit)
        validate_concurrent_sessions(
            max_concurrent_session, "max_concurrent_session"
        )
        validate_concurrent_sessions(
            max_concurrent_tcp_session, "max_concurrent_tcp_session"
        )
        validate_concurrent_sessions(
            max_concurrent_udp_session, "max_concurrent_udp_session"
        )
        validate_diffserv(diffserv_forward)
        validate_diffserv(diffserv_reverse)

        payload = build_cmdb_payload_normalized(
            max_bandwidth=max_bandwidth,
            bandwidth_unit=bandwidth_unit,
            max_concurrent_session=max_concurrent_session,
            max_concurrent_tcp_session=max_concurrent_tcp_session,
            max_concurrent_udp_session=max_concurrent_udp_session,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            data=data,
        )

        self._logger.debug(f"Updating per-IP shaper: {name}")
        return self._api.put(name=name, payload_dict=payload, vdom=vdom)

    def rename(
        self, name: str, new_name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Rename operation is NOT supported by FortiOS for per-IP shapers.

        The 'name' field serves as the immutable primary key for per-IP
        shapers. FortiOS does not support renaming shaper objects after
        creation.

        To rename a shaper, you must:
        1. Create a new shaper with the desired name
        2. Update any policies/rules that reference the old shaper
        3. Delete the old shaper

        Args:
            name: Current shaper name
            new_name: New shaper name
            vdom: Virtual domain name

        Raises:
            NotImplementedError: Always raised as rename is not supported by
                the FortiOS API

        Note:
            This is a limitation of the FortiOS API, not the wrapper.
            The per-ip-shaper endpoint uses name-based URLs
            (/firewall.shaper/per-ip-shaper/{name}) where the name is the
            primary key and cannot be changed.
        """
        raise NotImplementedError(
            "FortiOS does not support renaming per-IP shapers. "
            "The 'name' field is immutable after creation. "
            "To rename, you must delete the old shaper and create a new one "
            "with the desired name. Note: this will break any policies that "
            "reference the old shaper name."
        )

    def delete(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Delete a per-IP traffic shaper.

        Args:
            name: Shaper name
            vdom: Virtual domain name

        Returns:
            API response dictionary
        """
        validate_shaper_name(name, "delete")
        return self._api.delete(name=name, vdom=vdom)

    def exists(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if a per-IP traffic shaper exists.

        Args:
            name: Shaper name
            vdom: Virtual domain name

        Returns:
            True if shaper exists, False otherwise
        """
        validate_shaper_name(name, "exists")
        return self._api.exists(name=name, vdom=vdom)
