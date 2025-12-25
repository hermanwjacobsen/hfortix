"""Firewall IP/MAC Binding Setting Convenience Wrapper."""

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from ..fortios import FortiOS


class IPMACBindingSetting:
    """Convenience wrapper for firewall IP/MAC binding settings."""

    def __init__(self, fortios_instance: "FortiOS") -> None:
        """Initialize the IPMACBindingSetting wrapper."""
        self._fgt = fortios_instance
        self._api = fortios_instance.api.cmdb.firewall.ipmacbinding_setting

    def get(
        self, vdom: Optional[str] = None, **kwargs: Any
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Get IP/MAC binding settings."""
        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.get(**api_params)

    def update(
        self,
        bindthroughfw: Optional[str] = None,
        bindtofw: Optional[str] = None,
        undefinedhost: Optional[str] = None,
        vdom: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Update IP/MAC binding settings."""
        data: dict[str, Any] = {}
        if bindthroughfw is not None:
            data["bindthroughfw"] = bindthroughfw
        if bindtofw is not None:
            data["bindtofw"] = bindtofw
        if undefinedhost is not None:
            data["undefinedhost"] = undefinedhost

        api_params: dict[str, Any] = {}
        if vdom:
            api_params["vdom"] = vdom
        api_params.update(kwargs)

        return self._api.put(data, **api_params)

    def enable_binding_through_firewall(
        self, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Enable IP/MAC binding for packets going through firewall."""
        return self.update(bindthroughfw="enable", vdom=vdom)

    def disable_binding_through_firewall(
        self, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Disable IP/MAC binding for packets going through firewall."""
        return self.update(bindthroughfw="disable", vdom=vdom)

    def enable_binding_to_firewall(
        self, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Enable IP/MAC binding for packets going to firewall."""
        return self.update(bindtofw="enable", vdom=vdom)

    def disable_binding_to_firewall(
        self, vdom: Optional[str] = None
    ) -> Union[Dict[str, Any], "Coroutine[Any, Any, Dict[str, Any]]"]:
        """Disable IP/MAC binding for packets going to firewall."""
        return self.update(bindtofw="disable", vdom=vdom)
