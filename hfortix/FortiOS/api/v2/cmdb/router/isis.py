"""FortiOS CMDB - Router ISIS - IS-IS configuration"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Isis:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client
    def get(self, datasource: Optional[bool] = None, with_meta: Optional[bool] = None, skip: Optional[bool] = None, format: Optional[str] = None, action: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        params = {}
        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if action is not None:
            params["action"] = action
        params.update(kwargs)
        return self._client.get("cmdb", "router/isis", params=params if params else None, vdom=vdom)
    def put(self, data_dict: Optional[dict[str, Any]] = None, is_type: Optional[str] = None, adv_passive_only: Optional[str] = None, adv_passive_only6: Optional[str] = None, auth_mode_l1: Optional[str] = None, auth_mode_l2: Optional[str] = None, auth_password_l1: Optional[str] = None, auth_password_l2: Optional[str] = None, auth_keychain_l1: Optional[str] = None, auth_keychain_l2: Optional[str] = None, auth_sendonly_l1: Optional[str] = None, auth_sendonly_l2: Optional[str] = None, ignore_lsp_errors: Optional[str] = None, lsp_gen_interval_l1: Optional[int] = None, lsp_gen_interval_l2: Optional[int] = None, lsp_refresh_interval: Optional[int] = None, max_lsp_lifetime: Optional[int] = None, spf_interval_exp_l1: Optional[str] = None, spf_interval_exp_l2: Optional[str] = None, dynamic_hostname: Optional[str] = None, adjacency_check: Optional[str] = None, adjacency_check6: Optional[str] = None, overload_bit: Optional[str] = None, overload_bit_suppress: Optional[str] = None, overload_bit_on_startup: Optional[int] = None, default_originate: Optional[str] = None, default_originate6: Optional[str] = None, metric_style: Optional[str] = None, redistribute_l1: Optional[str] = None, redistribute_l1_list: Optional[str] = None, redistribute_l2: Optional[str] = None, redistribute_l2_list: Optional[str] = None, redistribute6_l1: Optional[str] = None, redistribute6_l1_list: Optional[str] = None, redistribute6_l2: Optional[str] = None, redistribute6_l2_list: Optional[str] = None, isis_net: Optional[list] = None, isis_interface: Optional[list] = None, summary_address: Optional[list] = None, summary_address6: Optional[list] = None, redistribute: Optional[list] = None, redistribute6: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"is_type": "is-type", "adv_passive_only": "adv-passive-only", "adv_passive_only6": "adv-passive-only6", "auth_mode_l1": "auth-mode-l1", "auth_mode_l2": "auth-mode-l2", "auth_password_l1": "auth-password-l1", "auth_password_l2": "auth-password-l2", "auth_keychain_l1": "auth-keychain-l1", "auth_keychain_l2": "auth-keychain-l2", "auth_sendonly_l1": "auth-sendonly-l1", "auth_sendonly_l2": "auth-sendonly-l2", "ignore_lsp_errors": "ignore-lsp-errors", "lsp_gen_interval_l1": "lsp-gen-interval-l1", "lsp_gen_interval_l2": "lsp-gen-interval-l2", "lsp_refresh_interval": "lsp-refresh-interval", "max_lsp_lifetime": "max-lsp-lifetime", "spf_interval_exp_l1": "spf-interval-exp-l1", "spf_interval_exp_l2": "spf-interval-exp-l2", "dynamic_hostname": "dynamic-hostname", "adjacency_check": "adjacency-check", "adjacency_check6": "adjacency-check6", "overload_bit": "overload-bit", "overload_bit_suppress": "overload-bit-suppress", "overload_bit_on_startup": "overload-bit-on-startup", "default_originate": "default-originate", "default_originate6": "default-originate6", "metric_style": "metric-style", "redistribute_l1": "redistribute-l1", "redistribute_l1_list": "redistribute-l1-list", "redistribute_l2": "redistribute-l2", "redistribute_l2_list": "redistribute-l2-list", "redistribute6_l1": "redistribute6-l1", "redistribute6_l1_list": "redistribute6-l1-list", "redistribute6_l2": "redistribute6-l2", "redistribute6_l2_list": "redistribute6-l2-list", "isis_net": "isis-net", "isis_interface": "isis-interface", "summary_address": "summary-address", "summary_address6": "summary-address6"}
        if is_type is not None:
            data[param_map["is_type"]] = is_type
        if adv_passive_only is not None:
            data[param_map["adv_passive_only"]] = adv_passive_only
        if adv_passive_only6 is not None:
            data[param_map["adv_passive_only6"]] = adv_passive_only6
        if auth_mode_l1 is not None:
            data[param_map["auth_mode_l1"]] = auth_mode_l1
        if auth_mode_l2 is not None:
            data[param_map["auth_mode_l2"]] = auth_mode_l2
        if auth_password_l1 is not None:
            data[param_map["auth_password_l1"]] = auth_password_l1
        if auth_password_l2 is not None:
            data[param_map["auth_password_l2"]] = auth_password_l2
        if auth_keychain_l1 is not None:
            data[param_map["auth_keychain_l1"]] = auth_keychain_l1
        if auth_keychain_l2 is not None:
            data[param_map["auth_keychain_l2"]] = auth_keychain_l2
        if auth_sendonly_l1 is not None:
            data[param_map["auth_sendonly_l1"]] = auth_sendonly_l1
        if auth_sendonly_l2 is not None:
            data[param_map["auth_sendonly_l2"]] = auth_sendonly_l2
        if ignore_lsp_errors is not None:
            data[param_map["ignore_lsp_errors"]] = ignore_lsp_errors
        if lsp_gen_interval_l1 is not None:
            data[param_map["lsp_gen_interval_l1"]] = lsp_gen_interval_l1
        if lsp_gen_interval_l2 is not None:
            data[param_map["lsp_gen_interval_l2"]] = lsp_gen_interval_l2
        if lsp_refresh_interval is not None:
            data[param_map["lsp_refresh_interval"]] = lsp_refresh_interval
        if max_lsp_lifetime is not None:
            data[param_map["max_lsp_lifetime"]] = max_lsp_lifetime
        if spf_interval_exp_l1 is not None:
            data[param_map["spf_interval_exp_l1"]] = spf_interval_exp_l1
        if spf_interval_exp_l2 is not None:
            data[param_map["spf_interval_exp_l2"]] = spf_interval_exp_l2
        if dynamic_hostname is not None:
            data[param_map["dynamic_hostname"]] = dynamic_hostname
        if adjacency_check is not None:
            data[param_map["adjacency_check"]] = adjacency_check
        if adjacency_check6 is not None:
            data[param_map["adjacency_check6"]] = adjacency_check6
        if overload_bit is not None:
            data[param_map["overload_bit"]] = overload_bit
        if overload_bit_suppress is not None:
            data[param_map["overload_bit_suppress"]] = overload_bit_suppress
        if overload_bit_on_startup is not None:
            data[param_map["overload_bit_on_startup"]] = overload_bit_on_startup
        if default_originate is not None:
            data[param_map["default_originate"]] = default_originate
        if default_originate6 is not None:
            data[param_map["default_originate6"]] = default_originate6
        if metric_style is not None:
            data[param_map["metric_style"]] = metric_style
        if redistribute_l1 is not None:
            data[param_map["redistribute_l1"]] = redistribute_l1
        if redistribute_l1_list is not None:
            data[param_map["redistribute_l1_list"]] = redistribute_l1_list
        if redistribute_l2 is not None:
            data[param_map["redistribute_l2"]] = redistribute_l2
        if redistribute_l2_list is not None:
            data[param_map["redistribute_l2_list"]] = redistribute_l2_list
        if redistribute6_l1 is not None:
            data[param_map["redistribute6_l1"]] = redistribute6_l1
        if redistribute6_l1_list is not None:
            data[param_map["redistribute6_l1_list"]] = redistribute6_l1_list
        if redistribute6_l2 is not None:
            data[param_map["redistribute6_l2"]] = redistribute6_l2
        if redistribute6_l2_list is not None:
            data[param_map["redistribute6_l2_list"]] = redistribute6_l2_list
        if isis_net is not None:
            data[param_map["isis_net"]] = isis_net
        if isis_interface is not None:
            data[param_map["isis_interface"]] = isis_interface
        if summary_address is not None:
            data[param_map["summary_address"]] = summary_address
        if summary_address6 is not None:
            data[param_map["summary_address6"]] = summary_address6
        if redistribute is not None:
            data["redistribute"] = redistribute
        if redistribute6 is not None:
            data["redistribute6"] = redistribute6
        data.update(kwargs)
        return self._client.put("cmdb", "router/isis", data=data, vdom=vdom)
