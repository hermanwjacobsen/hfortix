"""
FortiOS shaping-policy API wrapper.
Provides access to /api/v2/cmdb/firewall/shaping-policy endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class ShapingPolicy:
    """
    Wrapper for firewall shaping-policy API endpoint.

    Manages shaping-policy configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the ShapingPolicy wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/shaping-policy"


    def get(
        self,
        mkey: Optional[Union[str, int]] = None,
        attr: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to_datasource: Optional[Any] = None,
        acs: Optional[Any] = None,
        search: Optional[Any] = None,
        scope: Optional[Any] = None,
        datasource: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a specific shaping-policy entry by its id.

        Args:
            mkey: The id (primary key)
            attr: Attribute name that references other table
            count: Maximum number of entries to return.
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address
            acs: If true, returned result are in ascending order.
            search: If present, the objects will be filtered by the search value.
            scope: Scope [global|vdom|both*]
            datasource: Enable to include datasource information for each linked object.
            with_meta: Enable to include meta information about each object (type id, referen
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            action: datasource: Return all applicable datasource entries for a specific at
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with entry details
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if attr is not None:
            params["attr"] = attr
        if count is not None:
            params["count"] = count
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        if scope is not None:
            params["scope"] = scope
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
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        app_category: Optional[list] = None,
        app_group: Optional[list] = None,
        application: Optional[list] = None,
        class_id: Optional[int] = None,
        comment: Optional[str] = None,
        cos: Optional[str] = None,
        cos_mask: Optional[str] = None,
        diffserv_forward: Optional[str] = None,
        diffserv_reverse: Optional[str] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr6: Optional[list] = None,
        dstintf: Optional[list] = None,
        groups: Optional[list] = None,
        id: Optional[int] = None,
        internet_service: Optional[str] = None,
        internet_service_custom: Optional[list] = None,
        internet_service_custom_group: Optional[list] = None,
        internet_service_fortiguard: Optional[list] = None,
        internet_service_group: Optional[list] = None,
        internet_service_name: Optional[list] = None,
        internet_service_src: Optional[str] = None,
        internet_service_src_custom: Optional[list] = None,
        internet_service_src_custom_group: Optional[list] = None,
        internet_service_src_fortiguard: Optional[list] = None,
        internet_service_src_group: Optional[list] = None,
        internet_service_src_name: Optional[list] = None,
        ip_version: Optional[str] = None,
        name: Optional[str] = None,
        per_ip_shaper: Optional[str] = None,
        schedule: Optional[str] = None,
        service: Optional[list] = None,
        srcaddr: Optional[list] = None,
        srcaddr6: Optional[list] = None,
        srcintf: Optional[list] = None,
        status: Optional[str] = None,
        tos: Optional[str] = None,
        tos_mask: Optional[str] = None,
        tos_negate: Optional[str] = None,
        traffic_shaper: Optional[str] = None,
        traffic_shaper_reverse: Optional[str] = None,
        traffic_type: Optional[str] = None,
        url_category: Optional[list] = None,
        users: Optional[list] = None,
        uuid: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create shaping-policy entry.

        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: create(key="value", vdom="root")

        Args:
            payload_dict: The configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            app-category (list[object]):
                IDs of one or more application categories that this shaper a...
            app-group (list[object]):
                One or more application group names.
            application (list[object]):
                IDs of one or more applications that this shaper applies app...
            class-id (integer) (range: 0-4294967295):
                Traffic class ID.
            comment (string) (max_len: 255):
                Comments.
            cos (string):
                VLAN CoS bit pattern.
            cos-mask (string):
                VLAN CoS evaluated bits.
            diffserv-forward (string) (enum: ['enable', 'disable']):
                Enable to change packet's DiffServ values to the specified d...
            diffserv-reverse (string) (enum: ['enable', 'disable']):
                Enable to change packet's reverse (reply) DiffServ values to...
            diffservcode-forward (string):
                Change packet's DiffServ to this value.
            diffservcode-rev (string):
                Change packet's reverse (reply) DiffServ to this value.
            dstaddr (list[object]):
                IPv4 destination address and address group names.
            dstaddr6 (list[object]):
                IPv6 destination address and address group names.
            dstintf (list[object]):
                One or more outgoing (egress) interfaces.
            groups (list[object]):
                Apply this traffic shaping policy to user groups that have a...
            id (integer) (range: 0-4294967295):
                Shaping policy ID (0 - 4294967295).
            internet-service (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services for this policy. If ...
            internet-service-custom (list[object]):
                Custom Internet Service name.
            internet-service-custom-group (list[object]):
                Custom Internet Service group name.
            internet-service-fortiguard (list[object]):
                FortiGuard Internet Service name.
            internet-service-group (list[object]):
                Internet Service group name.
            internet-service-name (list[object]):
                Internet Service ID.
            internet-service-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services in source for this p...
            internet-service-src-custom (list[object]):
                Custom Internet Service source name.
            internet-service-src-custom-group (list[object]):
                Custom Internet Service source group name.
            internet-service-src-fortiguard (list[object]):
                FortiGuard Internet Service source name.
            internet-service-src-group (list[object]):
                Internet Service source group name.
            internet-service-src-name (list[object]):
                Internet Service source name.
            ip-version (string) (enum: ['4', '6']):
                Apply this traffic shaping policy to IPv4 or IPv6 traffic.
            name (string) (max_len: 35):
                Shaping policy name.
            per-ip-shaper (string) (max_len: 35):
                Per-IP traffic shaper to apply with this policy.
            schedule (string) (max_len: 35):
                Schedule name.
            service (list[object]):
                Service and service group names.
            srcaddr (list[object]):
                IPv4 source address and address group names.
            srcaddr6 (list[object]):
                IPv6 source address and address group names.
            srcintf (list[object]):
                One or more incoming (ingress) interfaces.
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this traffic shaping policy.
            tos (string):
                ToS (Type of Service) value used for comparison.
            tos-mask (string):
                Non-zero bit positions are used for comparison while zero bi...
            tos-negate (string) (enum: ['enable', 'disable']):
                Enable negated TOS match.
            traffic-shaper (string) (max_len: 35):
                Traffic shaper to apply to traffic forwarded by the firewall...
            traffic-shaper-reverse (string) (max_len: 35):
                Traffic shaper to apply to response traffic received by the ...
            traffic-type (string) (enum: ['forwarding', 'local-in', 'local-out']):
                Traffic type.
            url-category (list[object]):
                IDs of one or more FortiGuard Web Filtering categories that ...
            users (list[object]):
                Apply this traffic shaping policy to individual users that h...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if app_category is not None:
            payload_dict["app-category"] = app_category
        if app_group is not None:
            payload_dict["app-group"] = app_group
        if application is not None:
            payload_dict["application"] = application
        if class_id is not None:
            payload_dict["class-id"] = class_id
        if comment is not None:
            payload_dict["comment"] = comment
        if cos is not None:
            payload_dict["cos"] = cos
        if cos_mask is not None:
            payload_dict["cos-mask"] = cos_mask
        if diffserv_forward is not None:
            payload_dict["diffserv-forward"] = diffserv_forward
        if diffserv_reverse is not None:
            payload_dict["diffserv-reverse"] = diffserv_reverse
        if diffservcode_forward is not None:
            payload_dict["diffservcode-forward"] = diffservcode_forward
        if diffservcode_rev is not None:
            payload_dict["diffservcode-rev"] = diffservcode_rev
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr6 is not None:
            payload_dict["dstaddr6"] = dstaddr6
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if groups is not None:
            payload_dict["groups"] = groups
        if id is not None:
            payload_dict["id"] = id
        if internet_service is not None:
            payload_dict["internet-service"] = internet_service
        if internet_service_custom is not None:
            payload_dict["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            payload_dict["internet-service-custom-group"] = internet_service_custom_group
        if internet_service_fortiguard is not None:
            payload_dict["internet-service-fortiguard"] = internet_service_fortiguard
        if internet_service_group is not None:
            payload_dict["internet-service-group"] = internet_service_group
        if internet_service_name is not None:
            payload_dict["internet-service-name"] = internet_service_name
        if internet_service_src is not None:
            payload_dict["internet-service-src"] = internet_service_src
        if internet_service_src_custom is not None:
            payload_dict["internet-service-src-custom"] = internet_service_src_custom
        if internet_service_src_custom_group is not None:
            payload_dict["internet-service-src-custom-group"] = internet_service_src_custom_group
        if internet_service_src_fortiguard is not None:
            payload_dict["internet-service-src-fortiguard"] = internet_service_src_fortiguard
        if internet_service_src_group is not None:
            payload_dict["internet-service-src-group"] = internet_service_src_group
        if internet_service_src_name is not None:
            payload_dict["internet-service-src-name"] = internet_service_src_name
        if ip_version is not None:
            payload_dict["ip-version"] = ip_version
        if name is not None:
            payload_dict["name"] = name
        if per_ip_shaper is not None:
            payload_dict["per-ip-shaper"] = per_ip_shaper
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if service is not None:
            payload_dict["service"] = service
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr6 is not None:
            payload_dict["srcaddr6"] = srcaddr6
        if srcintf is not None:
            payload_dict["srcintf"] = srcintf
        if status is not None:
            payload_dict["status"] = status
        if tos is not None:
            payload_dict["tos"] = tos
        if tos_mask is not None:
            payload_dict["tos-mask"] = tos_mask
        if tos_negate is not None:
            payload_dict["tos-negate"] = tos_negate
        if traffic_shaper is not None:
            payload_dict["traffic-shaper"] = traffic_shaper
        if traffic_shaper_reverse is not None:
            payload_dict["traffic-shaper-reverse"] = traffic_shaper_reverse
        if traffic_type is not None:
            payload_dict["traffic-type"] = traffic_type
        if url_category is not None:
            payload_dict["url-category"] = url_category
        if users is not None:
            payload_dict["users"] = users
        if uuid is not None:
            payload_dict["uuid"] = uuid

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if nkey is not None:
            params["nkey"] = nkey
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.post(
            "cmdb", self.path, data=payload_dict, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        mkey: Optional[Union[str, int]] = None,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        app_category: Optional[list] = None,
        app_group: Optional[list] = None,
        application: Optional[list] = None,
        class_id: Optional[int] = None,
        comment: Optional[str] = None,
        cos: Optional[str] = None,
        cos_mask: Optional[str] = None,
        diffserv_forward: Optional[str] = None,
        diffserv_reverse: Optional[str] = None,
        diffservcode_forward: Optional[str] = None,
        diffservcode_rev: Optional[str] = None,
        dstaddr: Optional[list] = None,
        dstaddr6: Optional[list] = None,
        dstintf: Optional[list] = None,
        groups: Optional[list] = None,
        id: Optional[int] = None,
        internet_service: Optional[str] = None,
        internet_service_custom: Optional[list] = None,
        internet_service_custom_group: Optional[list] = None,
        internet_service_fortiguard: Optional[list] = None,
        internet_service_group: Optional[list] = None,
        internet_service_name: Optional[list] = None,
        internet_service_src: Optional[str] = None,
        internet_service_src_custom: Optional[list] = None,
        internet_service_src_custom_group: Optional[list] = None,
        internet_service_src_fortiguard: Optional[list] = None,
        internet_service_src_group: Optional[list] = None,
        internet_service_src_name: Optional[list] = None,
        ip_version: Optional[str] = None,
        name: Optional[str] = None,
        per_ip_shaper: Optional[str] = None,
        schedule: Optional[str] = None,
        service: Optional[list] = None,
        srcaddr: Optional[list] = None,
        srcaddr6: Optional[list] = None,
        srcintf: Optional[list] = None,
        status: Optional[str] = None,
        tos: Optional[str] = None,
        tos_mask: Optional[str] = None,
        tos_negate: Optional[str] = None,
        traffic_shaper: Optional[str] = None,
        traffic_shaper_reverse: Optional[str] = None,
        traffic_type: Optional[str] = None,
        url_category: Optional[list] = None,
        users: Optional[list] = None,
        uuid: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update shaping-policy entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The id (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            app-category (list[object]):
                IDs of one or more application categories that this shaper a...
            app-group (list[object]):
                One or more application group names.
            application (list[object]):
                IDs of one or more applications that this shaper applies app...
            class-id (integer) (range: 0-4294967295):
                Traffic class ID.
            comment (string) (max_len: 255):
                Comments.
            cos (string):
                VLAN CoS bit pattern.
            cos-mask (string):
                VLAN CoS evaluated bits.
            diffserv-forward (string) (enum: ['enable', 'disable']):
                Enable to change packet's DiffServ values to the specified d...
            diffserv-reverse (string) (enum: ['enable', 'disable']):
                Enable to change packet's reverse (reply) DiffServ values to...
            diffservcode-forward (string):
                Change packet's DiffServ to this value.
            diffservcode-rev (string):
                Change packet's reverse (reply) DiffServ to this value.
            dstaddr (list[object]):
                IPv4 destination address and address group names.
            dstaddr6 (list[object]):
                IPv6 destination address and address group names.
            dstintf (list[object]):
                One or more outgoing (egress) interfaces.
            groups (list[object]):
                Apply this traffic shaping policy to user groups that have a...
            id (integer) (range: 0-4294967295):
                Shaping policy ID (0 - 4294967295).
            internet-service (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services for this policy. If ...
            internet-service-custom (list[object]):
                Custom Internet Service name.
            internet-service-custom-group (list[object]):
                Custom Internet Service group name.
            internet-service-fortiguard (list[object]):
                FortiGuard Internet Service name.
            internet-service-group (list[object]):
                Internet Service group name.
            internet-service-name (list[object]):
                Internet Service ID.
            internet-service-src (string) (enum: ['enable', 'disable']):
                Enable/disable use of Internet Services in source for this p...
            internet-service-src-custom (list[object]):
                Custom Internet Service source name.
            internet-service-src-custom-group (list[object]):
                Custom Internet Service source group name.
            internet-service-src-fortiguard (list[object]):
                FortiGuard Internet Service source name.
            internet-service-src-group (list[object]):
                Internet Service source group name.
            internet-service-src-name (list[object]):
                Internet Service source name.
            ip-version (string) (enum: ['4', '6']):
                Apply this traffic shaping policy to IPv4 or IPv6 traffic.
            name (string) (max_len: 35):
                Shaping policy name.
            per-ip-shaper (string) (max_len: 35):
                Per-IP traffic shaper to apply with this policy.
            schedule (string) (max_len: 35):
                Schedule name.
            service (list[object]):
                Service and service group names.
            srcaddr (list[object]):
                IPv4 source address and address group names.
            srcaddr6 (list[object]):
                IPv6 source address and address group names.
            srcintf (list[object]):
                One or more incoming (ingress) interfaces.
            status (string) (enum: ['enable', 'disable']):
                Enable/disable this traffic shaping policy.
            tos (string):
                ToS (Type of Service) value used for comparison.
            tos-mask (string):
                Non-zero bit positions are used for comparison while zero bi...
            tos-negate (string) (enum: ['enable', 'disable']):
                Enable negated TOS match.
            traffic-shaper (string) (max_len: 35):
                Traffic shaper to apply to traffic forwarded by the firewall...
            traffic-shaper-reverse (string) (max_len: 35):
                Traffic shaper to apply to response traffic received by the ...
            traffic-type (string) (enum: ['forwarding', 'local-in', 'local-out']):
                Traffic type.
            url-category (list[object]):
                IDs of one or more FortiGuard Web Filtering categories that ...
            users (list[object]):
                Apply this traffic shaping policy to individual users that h...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if app_category is not None:
            payload_dict["app-category"] = app_category
        if app_group is not None:
            payload_dict["app-group"] = app_group
        if application is not None:
            payload_dict["application"] = application
        if class_id is not None:
            payload_dict["class-id"] = class_id
        if comment is not None:
            payload_dict["comment"] = comment
        if cos is not None:
            payload_dict["cos"] = cos
        if cos_mask is not None:
            payload_dict["cos-mask"] = cos_mask
        if diffserv_forward is not None:
            payload_dict["diffserv-forward"] = diffserv_forward
        if diffserv_reverse is not None:
            payload_dict["diffserv-reverse"] = diffserv_reverse
        if diffservcode_forward is not None:
            payload_dict["diffservcode-forward"] = diffservcode_forward
        if diffservcode_rev is not None:
            payload_dict["diffservcode-rev"] = diffservcode_rev
        if dstaddr is not None:
            payload_dict["dstaddr"] = dstaddr
        if dstaddr6 is not None:
            payload_dict["dstaddr6"] = dstaddr6
        if dstintf is not None:
            payload_dict["dstintf"] = dstintf
        if groups is not None:
            payload_dict["groups"] = groups
        if id is not None:
            payload_dict["id"] = id
        if internet_service is not None:
            payload_dict["internet-service"] = internet_service
        if internet_service_custom is not None:
            payload_dict["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            payload_dict["internet-service-custom-group"] = internet_service_custom_group
        if internet_service_fortiguard is not None:
            payload_dict["internet-service-fortiguard"] = internet_service_fortiguard
        if internet_service_group is not None:
            payload_dict["internet-service-group"] = internet_service_group
        if internet_service_name is not None:
            payload_dict["internet-service-name"] = internet_service_name
        if internet_service_src is not None:
            payload_dict["internet-service-src"] = internet_service_src
        if internet_service_src_custom is not None:
            payload_dict["internet-service-src-custom"] = internet_service_src_custom
        if internet_service_src_custom_group is not None:
            payload_dict["internet-service-src-custom-group"] = internet_service_src_custom_group
        if internet_service_src_fortiguard is not None:
            payload_dict["internet-service-src-fortiguard"] = internet_service_src_fortiguard
        if internet_service_src_group is not None:
            payload_dict["internet-service-src-group"] = internet_service_src_group
        if internet_service_src_name is not None:
            payload_dict["internet-service-src-name"] = internet_service_src_name
        if ip_version is not None:
            payload_dict["ip-version"] = ip_version
        if name is not None:
            payload_dict["name"] = name
        if per_ip_shaper is not None:
            payload_dict["per-ip-shaper"] = per_ip_shaper
        if schedule is not None:
            payload_dict["schedule"] = schedule
        if service is not None:
            payload_dict["service"] = service
        if srcaddr is not None:
            payload_dict["srcaddr"] = srcaddr
        if srcaddr6 is not None:
            payload_dict["srcaddr6"] = srcaddr6
        if srcintf is not None:
            payload_dict["srcintf"] = srcintf
        if status is not None:
            payload_dict["status"] = status
        if tos is not None:
            payload_dict["tos"] = tos
        if tos_mask is not None:
            payload_dict["tos-mask"] = tos_mask
        if tos_negate is not None:
            payload_dict["tos-negate"] = tos_negate
        if traffic_shaper is not None:
            payload_dict["traffic-shaper"] = traffic_shaper
        if traffic_shaper_reverse is not None:
            payload_dict["traffic-shaper-reverse"] = traffic_shaper_reverse
        if traffic_type is not None:
            payload_dict["traffic-type"] = traffic_type
        if url_category is not None:
            payload_dict["url-category"] = url_category
        if users is not None:
            payload_dict["users"] = users
        if uuid is not None:
            payload_dict["uuid"] = uuid

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.put(
            "cmdb",
            f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path,
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Optional[Union[str, int]] = None,
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a shaping-policy entry.

        Args:
            mkey: The id (primary key)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.delete(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )
