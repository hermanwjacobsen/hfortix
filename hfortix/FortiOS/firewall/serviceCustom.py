"""
Service Custom Convenience Wrapper

Provides simplified syntax for custom service operations with full
parameter support.
Instead of: fgt.api.cmdb.firewall.service_custom.post(data)
Use: fgt.firewall.service_custom.create(name='HTTP-8080',
    tcp_portrange='8080', ...)
"""

import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Coroutine,
    Dict,
    List,
    Literal,
    Optional,
    Union,
)

from ..api._helpers import build_cmdb_payload_normalized, validate_color

if TYPE_CHECKING:
    from ..fortios import FortiOS


def validate_service_custom_name(
    name: Optional[str], operation: str = "operation"
) -> None:
    """Validate service custom name."""
    if not name:
        raise ValueError(f"Service name is required for {operation}")
    if isinstance(name, str) and len(name) > 79:
        raise ValueError(
            f"Service name cannot exceed 79 characters, got {len(name)}"
        )


def validate_category(category: Optional[str]) -> None:
    """Validate service category."""
    if (
        category is not None
        and isinstance(category, str)
        and len(category) > 63
    ):
        raise ValueError(
            f"Service category cannot exceed 63 characters, "
            f"got {len(category)}"
        )


def validate_proxy(proxy: Optional[str]) -> None:
    """Validate proxy parameter."""
    if proxy is not None and proxy not in ["enable", "disable"]:
        raise ValueError(
            f"Invalid proxy value '{proxy}'. Must be 'enable' or 'disable'"
        )


def validate_protocol(protocol: Optional[str]) -> None:
    """Validate protocol parameter."""
    valid_protocols = [
        "TCP/UDP/UDP-Lite/SCTP",
        "ICMP",
        "ICMP6",
        "IP",
        "HTTP",
        "FTP",
        "CONNECT",
        "SOCKS-TCP",
        "SOCKS-UDP",
        "ALL",
    ]
    if protocol is not None and protocol not in valid_protocols:
        raise ValueError(
            f"Invalid protocol '{protocol}'. "
            f"Must be one of: {', '.join(valid_protocols)}"
        )


def validate_helper(helper: Optional[str]) -> None:
    """Validate helper parameter."""
    valid_helpers = [
        "auto",
        "disable",
        "ftp",
        "tftp",
        "ras",
        "h323",
        "tns",
        "mms",
        "sip",
        "pptp",
        "rtsp",
        "dns-udp",
        "dns-tcp",
        "pmap",
        "rsh",
        "dcerpc",
        "mgcp",
    ]
    if helper is not None and helper not in valid_helpers:
        raise ValueError(
            f"Invalid helper '{helper}'. "
            f"Must be one of: {', '.join(valid_helpers)}"
        )


def validate_fqdn(fqdn: Optional[str]) -> None:
    """Validate FQDN parameter."""
    if fqdn is not None and isinstance(fqdn, str) and len(fqdn) > 255:
        raise ValueError(f"FQDN cannot exceed 255 characters, got {len(fqdn)}")


def validate_comment(comment: Optional[str]) -> None:
    """Validate comment parameter."""
    if comment is not None and isinstance(comment, str) and len(comment) > 255:
        raise ValueError(
            f"Comment cannot exceed 255 characters, got {len(comment)}"
        )


def validate_fabric_object(fabric_object: Optional[str]) -> None:
    """Validate fabric-object parameter."""
    if fabric_object is not None and fabric_object not in [
        "enable",
        "disable",
    ]:
        raise ValueError(
            f"Invalid fabric-object value '{fabric_object}'. "
            f"Must be 'enable' or 'disable'"
        )


def validate_check_reset_range(check_reset_range: Optional[str]) -> None:
    """Validate check-reset-range parameter."""
    valid_values = ["disable", "strict", "default"]
    if check_reset_range is not None and check_reset_range not in valid_values:
        raise ValueError(
            f"Invalid check-reset-range '{check_reset_range}'. "
            f"Must be one of: {', '.join(valid_values)}"
        )


def validate_app_service_type(app_service_type: Optional[str]) -> None:
    """Validate app-service-type parameter."""
    valid_values = ["disable", "app-id", "app-category"]
    if app_service_type is not None and app_service_type not in valid_values:
        raise ValueError(
            f"Invalid app-service-type '{app_service_type}'. "
            f"Must be one of: {', '.join(valid_values)}"
        )


class ServiceCustom:
    """
    Convenience wrapper for custom service operations with full
    parameter support.
    """

    def __init__(self, fortios_instance: "FortiOS"):
        """Initialize the ServiceCustom wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.service_custom
        self._logger = logging.getLogger("hfortix.firewall.service_custom")

    def create(
        self,
        # Required parameters
        name: str,
        # Protocol and Port parameters
        protocol: Optional[
            Literal[
                "TCP/UDP/UDP-Lite/SCTP",
                "ICMP",
                "ICMP6",
                "IP",
                "HTTP",
                "FTP",
                "CONNECT",
                "SOCKS-TCP",
                "SOCKS-UDP",
                "ALL",
            ]
        ] = None,
        tcp_portrange: Optional[str] = None,
        udp_portrange: Optional[str] = None,
        udplite_portrange: Optional[str] = None,
        sctp_portrange: Optional[str] = None,
        # ICMP parameters
        icmptype: Optional[int] = None,
        icmpcode: Optional[int] = None,
        # IP protocol
        protocol_number: Optional[int] = None,
        # IP range and FQDN
        iprange: Optional[str] = None,
        fqdn: Optional[str] = None,
        # Optional parameters
        uuid: Optional[str] = None,
        proxy: Optional[Literal["enable", "disable"]] = None,
        category: Optional[str] = None,
        helper: Optional[
            Literal[
                "auto",
                "disable",
                "ftp",
                "tftp",
                "ras",
                "h323",
                "tns",
                "mms",
                "sip",
                "pptp",
                "rtsp",
                "dns-udp",
                "dns-tcp",
                "pmap",
                "rsh",
                "dcerpc",
                "mgcp",
            ]
        ] = None,
        # Timeout parameters
        tcp_halfclose_timer: Optional[int] = None,
        tcp_halfopen_timer: Optional[int] = None,
        tcp_timewait_timer: Optional[int] = None,
        tcp_rst_timer: Optional[int] = None,
        udp_idle_timer: Optional[int] = None,
        session_ttl: Optional[str] = None,
        # Advanced parameters
        check_reset_range: Optional[
            Literal["disable", "strict", "default"]
        ] = None,
        comment: Optional[str] = None,
        color: Optional[int] = None,
        app_service_type: Optional[
            Literal["disable", "app-id", "app-category"]
        ] = None,
        app_category: Optional[List[Dict[str, Any]]] = None,
        application: Optional[List[Dict[str, Any]]] = None,
        fabric_object: Optional[Literal["enable", "disable"]] = None,
        # API parameters
        vdom: Optional[str] = None,
        # Additional fields
        data: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Create a new custom service."""
        validate_service_custom_name(name, "create")
        validate_category(category)
        validate_proxy(proxy)
        validate_protocol(protocol)
        validate_helper(helper)
        validate_fqdn(fqdn)
        validate_comment(comment)
        validate_fabric_object(fabric_object)
        validate_check_reset_range(check_reset_range)
        validate_app_service_type(app_service_type)
        if color is not None:
            validate_color(color)

        payload = build_cmdb_payload_normalized(
            name=name,
            uuid=uuid,
            proxy=proxy,
            category=category,
            protocol=protocol,
            helper=helper,
            iprange=iprange,
            fqdn=fqdn,
            protocol_number=protocol_number,
            icmptype=icmptype,
            icmpcode=icmpcode,
            tcp_portrange=tcp_portrange,
            udp_portrange=udp_portrange,
            udplite_portrange=udplite_portrange,
            sctp_portrange=sctp_portrange,
            tcp_halfclose_timer=tcp_halfclose_timer,
            tcp_halfopen_timer=tcp_halfopen_timer,
            tcp_timewait_timer=tcp_timewait_timer,
            tcp_rst_timer=tcp_rst_timer,
            udp_idle_timer=udp_idle_timer,
            session_ttl=session_ttl,
            check_reset_range=check_reset_range,
            comment=comment,
            color=color,
            app_service_type=app_service_type,
            app_category=app_category,
            application=application,
            fabric_object=fabric_object,
            data=data,
        )

        self._logger.debug(f"Creating custom service: {name}")
        return self._api.post(payload_dict=payload, vdom=vdom)

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Retrieve custom service configuration."""
        return self._api.get(name=name, vdom=vdom, **kwargs)

    def update(
        self, name: str, **params: Any
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Update an existing custom service."""
        validate_service_custom_name(name, "update")
        vdom = params.pop("vdom", None)
        data = params.pop("data", None)

        # Validate parameters
        if "category" in params:
            validate_category(params["category"])
        if "proxy" in params:
            validate_proxy(params["proxy"])
        if "protocol" in params:
            validate_protocol(params["protocol"])
        if "helper" in params:
            validate_helper(params["helper"])
        if "fqdn" in params:
            validate_fqdn(params["fqdn"])
        if "comment" in params:
            validate_comment(params["comment"])
        if "fabric_object" in params:
            validate_fabric_object(params["fabric_object"])
        if "check_reset_range" in params:
            validate_check_reset_range(params["check_reset_range"])
        if "app_service_type" in params:
            validate_app_service_type(params["app_service_type"])
        if "color" in params:
            validate_color(params["color"])

        payload = build_cmdb_payload_normalized(**params, data=data)
        return self._api.put(name=name, payload_dict=payload, vdom=vdom)

    def rename(
        self, name: str, new_name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Rename a custom service."""
        validate_service_custom_name(name, "rename (name)")
        validate_service_custom_name(new_name, "rename (new_name)")
        return self.update(name=name, data={"name": new_name}, vdom=vdom)

    def delete(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """Delete a custom service."""
        validate_service_custom_name(name, "delete")
        return self._api.delete(name=name, vdom=vdom)

    def exists(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """Check if a custom service exists."""
        validate_service_custom_name(name, "exists")
        return self._api.exists(name=name, vdom=vdom)

    def get_by_name(
        self, name: str, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]], None]:
        """Get a custom service by name, returning None if not found."""
        validate_service_custom_name(name, "get_by_name")
        try:
            return self.get(name=name, vdom=vdom)
        except Exception as e:
            self._logger.debug(f"Custom service not found: {name} - {e}")
            return None
