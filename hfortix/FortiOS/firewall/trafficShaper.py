"""
Traffic Shaper Convenience Wrapper

Provides simplified syntax for shared traffic shaper operations with
full parameter support.
Instead of: fgt.api.cmdb.firewall.shaper_traffic_shaper.post(data)
Use: fgt.firewall.traffic_shaper.create(name='shaper1',
    guaranteed_bandwidth=1000, maximum_bandwidth=5000, ...)
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
    """Validate traffic shaper name."""
    if not name:
        raise ValueError(f"Traffic shaper name is required for {operation}")
    if isinstance(name, str) and len(name) > 35:
        raise ValueError(
            f"Traffic shaper name cannot exceed 35 characters, "
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


def validate_priority(priority: Optional[str]) -> None:
    """Validate priority parameter."""
    valid_priorities = ["low", "medium", "high"]
    if priority is not None and priority not in valid_priorities:
        raise ValueError(
            f"Invalid priority '{priority}'. "
            f"Must be one of: {', '.join(valid_priorities)}"
        )


def validate_enable_disable(
    value: Optional[str], param_name: str = "parameter"
) -> None:
    """Validate enable/disable parameter."""
    if value is not None and value not in ["enable", "disable"]:
        raise ValueError(
            f"Invalid {param_name} value '{value}'. "
            f"Must be 'enable' or 'disable'"
        )


def validate_dscp_marking_method(method: Optional[str]) -> None:
    """Validate DSCP marking method parameter."""
    valid_methods = ["multi-stage", "static"]
    if method is not None and method not in valid_methods:
        raise ValueError(
            f"Invalid dscp-marking-method '{method}'. "
            f"Must be one of: {', '.join(valid_methods)}"
        )


def validate_cos_marking_method(method: Optional[str]) -> None:
    """Validate CoS marking method parameter."""
    valid_methods = ["multi-stage", "static"]
    if method is not None and method not in valid_methods:
        raise ValueError(
            f"Invalid cos-marking-method '{method}'. "
            f"Must be one of: {', '.join(valid_methods)}"
        )


def validate_overhead(overhead: Optional[int]) -> None:
    """Validate overhead parameter."""
    if overhead is not None:
        if not isinstance(overhead, int):
            raise ValueError(
                f"overhead must be an integer, got {type(overhead)}"
            )
        if not 0 <= overhead <= 100:
            raise ValueError(
                f"overhead must be between 0 and 100, got {overhead}"
            )


def validate_class_id(class_id: Optional[int]) -> None:
    """Validate class ID parameter."""
    if class_id is not None:
        if not isinstance(class_id, int):
            raise ValueError(
                f"class_id must be an integer, got {type(class_id)}"
            )
        if not 0 <= class_id <= 4294967295:
            raise ValueError(
                f"class_id must be between 0 and 4294967295, "
                f"got {class_id}"
            )


class TrafficShaper:
    """
    Convenience wrapper for shared traffic shaper operations with full
    parameter support.
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """Initialize the TrafficShaper wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.shaper.traffic_shaper
        self._logger = logging.getLogger("hfortix.firewall.traffic_shaper")

    def create(
        self,
        # Required parameters
        name: str,
        # Bandwidth parameters
        guaranteed_bandwidth: Optional[int] = None,
        maximum_bandwidth: Optional[int] = None,
        bandwidth_unit: Optional[Literal["kbps", "mbps", "gbps"]] = None,
        # Priority and policy parameters
        priority: Optional[Literal["low", "medium", "high"]] = None,
        per_policy: Optional[Literal["disable", "enable"]] = None,
        # DiffServ parameters
        diffserv: Optional[Literal["enable", "disable"]] = None,
        diffservcode: Optional[str] = None,
        dscp_marking_method: Optional[Literal["multi-stage", "static"]] = None,
        exceed_bandwidth: Optional[int] = None,
        exceed_dscp: Optional[str] = None,
        maximum_dscp: Optional[str] = None,
        # CoS parameters
        cos_marking: Optional[Literal["enable", "disable"]] = None,
        cos_marking_method: Optional[Literal["multi-stage", "static"]] = None,
        cos: Optional[str] = None,
        exceed_cos: Optional[str] = None,
        maximum_cos: Optional[str] = None,
        # Advanced parameters
        overhead: Optional[int] = None,
        exceed_class_id: Optional[int] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Create a new shared traffic shaper.

        Args:
            name: Traffic shaper name (max 35 chars, required)
            guaranteed_bandwidth: Amount of bandwidth guaranteed
                (0-80000000). Units depend on bandwidth-unit setting
            maximum_bandwidth: Upper bandwidth limit (0-80000000).
                0 means no limit. Units depend on bandwidth-unit setting
            bandwidth_unit: Unit of measurement (kbps, mbps, gbps)
            priority: Traffic priority (low, medium, high).
                Higher priority traffic is more likely to be forwarded
                without delays
            per_policy: Enable/disable applying a separate shaper
                for each policy
            diffserv: Enable/disable changing the DiffServ setting
            diffservcode: DiffServ setting to be applied
            dscp_marking_method: DSCP marking method
                (multi-stage, static)
            exceed_bandwidth: Exceed bandwidth used for DSCP/VLAN CoS
                multi-stage marking
            exceed_dscp: DSCP mark for traffic in guaranteed-bandwidth
                and exceed-bandwidth
            maximum_dscp: DSCP mark for traffic in exceed-bandwidth
                and maximum-bandwidth
            cos_marking: Enable/disable VLAN CoS marking
            cos_marking_method: VLAN CoS marking method
                (multi-stage, static)
            cos: VLAN CoS mark
            exceed_cos: VLAN CoS mark for traffic in
                [guaranteed-bandwidth, exceed-bandwidth]
            maximum_cos: VLAN CoS mark for traffic in
                [exceed-bandwidth, maximum-bandwidth]
            overhead: Per-packet size overhead (0-100)
            exceed_class_id: Class ID for traffic in guaranteed-bandwidth
                and maximum-bandwidth (0-4294967295)
            vdom: Virtual domain name
            data: Additional fields as dictionary

        Returns:
            API response dictionary

        Example:
            >>> # Create traffic shaper with guaranteed and max bandwidth
            >>> result = fgt.firewall.traffic_shaper.create(
            ...     name="traffic-shaper-1",
            ...     guaranteed_bandwidth=1000,
            ...     maximum_bandwidth=5000,
            ...     bandwidth_unit="kbps",
            ...     priority="high"
            ... )
            >>>
            >>> # Create with DiffServ and CoS settings
            >>> result = fgt.firewall.traffic_shaper.create(
            ...     name="traffic-shaper-2",
            ...     guaranteed_bandwidth=10000,
            ...     maximum_bandwidth=50000,
            ...     bandwidth_unit="mbps",
            ...     diffserv="enable",
            ...     diffservcode="0x28",
            ...     cos_marking="enable",
            ...     cos="5"
            ... )
        """
        validate_shaper_name(name, "create")
        validate_bandwidth(guaranteed_bandwidth, "guaranteed_bandwidth")
        validate_bandwidth(maximum_bandwidth, "maximum_bandwidth")
        validate_bandwidth(exceed_bandwidth, "exceed_bandwidth")
        validate_bandwidth_unit(bandwidth_unit)
        validate_priority(priority)
        validate_enable_disable(per_policy, "per_policy")
        validate_enable_disable(diffserv, "diffserv")
        validate_dscp_marking_method(dscp_marking_method)
        validate_enable_disable(cos_marking, "cos_marking")
        validate_cos_marking_method(cos_marking_method)
        validate_overhead(overhead)
        validate_class_id(exceed_class_id)

        payload = build_cmdb_payload_normalized(
            name=name,
            guaranteed_bandwidth=guaranteed_bandwidth,
            maximum_bandwidth=maximum_bandwidth,
            bandwidth_unit=bandwidth_unit,
            priority=priority,
            per_policy=per_policy,
            diffserv=diffserv,
            diffservcode=diffservcode,
            dscp_marking_method=dscp_marking_method,
            exceed_bandwidth=exceed_bandwidth,
            exceed_dscp=exceed_dscp,
            maximum_dscp=maximum_dscp,
            cos_marking=cos_marking,
            cos_marking_method=cos_marking_method,
            cos=cos,
            exceed_cos=exceed_cos,
            maximum_cos=maximum_cos,
            overhead=overhead,
            exceed_class_id=exceed_class_id,
            data=data,
        )

        self._logger.debug(f"Creating traffic shaper: {name}")
        return self._api.post(payload_dict=payload, vdom=vdom)

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Retrieve traffic shaper configuration.

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
        guaranteed_bandwidth: Optional[int] = None,
        maximum_bandwidth: Optional[int] = None,
        bandwidth_unit: Optional[Literal["kbps", "mbps", "gbps"]] = None,
        # Priority and policy parameters
        priority: Optional[Literal["low", "medium", "high"]] = None,
        per_policy: Optional[Literal["disable", "enable"]] = None,
        # DiffServ parameters
        diffserv: Optional[Literal["enable", "disable"]] = None,
        diffservcode: Optional[str] = None,
        dscp_marking_method: Optional[Literal["multi-stage", "static"]] = None,
        exceed_bandwidth: Optional[int] = None,
        exceed_dscp: Optional[str] = None,
        maximum_dscp: Optional[str] = None,
        # CoS parameters
        cos_marking: Optional[Literal["enable", "disable"]] = None,
        cos_marking_method: Optional[Literal["multi-stage", "static"]] = None,
        cos: Optional[str] = None,
        exceed_cos: Optional[str] = None,
        maximum_cos: Optional[str] = None,
        # Advanced parameters
        overhead: Optional[int] = None,
        exceed_class_id: Optional[int] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Update an existing shared traffic shaper.

        Args:
            name: Traffic shaper name (required)
            guaranteed_bandwidth: Amount of bandwidth guaranteed
                (0-80000000)
            maximum_bandwidth: Upper bandwidth limit (0-80000000)
            bandwidth_unit: Unit of measurement (kbps, mbps, gbps)
            priority: Traffic priority (low, medium, high)
            per_policy: Enable/disable per-policy shaping
            diffserv: Enable/disable DiffServ
            diffservcode: DiffServ setting
            dscp_marking_method: DSCP marking method
                (multi-stage, static)
            exceed_bandwidth: Exceed bandwidth for multi-stage marking
            exceed_dscp: DSCP mark for guaranteed-exceed range
            maximum_dscp: DSCP mark for exceed-maximum range
            cos_marking: Enable/disable VLAN CoS marking
            cos_marking_method: CoS marking method (multi-stage, static)
            cos: VLAN CoS mark
            exceed_cos: CoS mark for guaranteed-exceed range
            maximum_cos: CoS mark for exceed-maximum range
            overhead: Per-packet size overhead (0-100)
            exceed_class_id: Class ID (0-4294967295)
            vdom: Virtual domain name
            data: Additional fields as dictionary

        Returns:
            API response dictionary
        """
        validate_shaper_name(name, "update")
        validate_bandwidth(guaranteed_bandwidth, "guaranteed_bandwidth")
        validate_bandwidth(maximum_bandwidth, "maximum_bandwidth")
        validate_bandwidth(exceed_bandwidth, "exceed_bandwidth")
        validate_bandwidth_unit(bandwidth_unit)
        validate_priority(priority)
        validate_enable_disable(per_policy, "per_policy")
        validate_enable_disable(diffserv, "diffserv")
        validate_dscp_marking_method(dscp_marking_method)
        validate_enable_disable(cos_marking, "cos_marking")
        validate_cos_marking_method(cos_marking_method)
        validate_overhead(overhead)
        validate_class_id(exceed_class_id)

        payload = build_cmdb_payload_normalized(
            guaranteed_bandwidth=guaranteed_bandwidth,
            maximum_bandwidth=maximum_bandwidth,
            bandwidth_unit=bandwidth_unit,
            priority=priority,
            per_policy=per_policy,
            diffserv=diffserv,
            diffservcode=diffservcode,
            dscp_marking_method=dscp_marking_method,
            exceed_bandwidth=exceed_bandwidth,
            exceed_dscp=exceed_dscp,
            maximum_dscp=maximum_dscp,
            cos_marking=cos_marking,
            cos_marking_method=cos_marking_method,
            cos=cos,
            exceed_cos=exceed_cos,
            maximum_cos=maximum_cos,
            overhead=overhead,
            exceed_class_id=exceed_class_id,
            data=data,
        )

        self._logger.debug(f"Updating traffic shaper: {name}")
        return self._api.put(name=name, payload_dict=payload, vdom=vdom)

    def rename(
        self, name: str, new_name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Rename operation is NOT supported by FortiOS for traffic shapers.

        The 'name' field serves as the immutable primary key for traffic
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
            The traffic-shaper endpoint uses name-based URLs
            (/firewall.shaper/traffic-shaper/{name}) where the name is the
            primary key and cannot be changed.

            Shaping policies (firewall/shaping-policy) use ID-based URLs and
            DO support renaming.
        """
        raise NotImplementedError(
            "FortiOS does not support renaming traffic shapers. "
            "The 'name' field is immutable after creation. "
            "To rename, you must delete the old shaper and create a new one "
            "with the desired name. Note: this will break any policies that "
            "reference the old shaper name."
        )

    def delete(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Delete a shared traffic shaper.

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
        Check if a shared traffic shaper exists.

        Args:
            name: Shaper name
            vdom: Virtual domain name

        Returns:
            True if shaper exists, False otherwise
        """
        validate_shaper_name(name, "exists")
        return self._api.exists(name=name, vdom=vdom)
