"""
FortiOS profile-group API wrapper.
Provides access to /api/v2/cmdb/firewall/profile-group endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class ProfileGroup:
    """
    Wrapper for firewall profile-group API endpoint.

    Manages profile-group configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the ProfileGroup wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/profile-group"


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
        Retrieve a specific profile-group entry by its name.

        Args:
            mkey: The name (primary key)
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
        application_list: Optional[str] = None,
        av_profile: Optional[str] = None,
        casb_profile: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        icap_profile: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        name: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        ssh_filter_profile: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        voip_profile: Optional[str] = None,
        waf_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create profile-group entry.

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

            application-list (string) (max_len: 47):
                Name of an existing Application list.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            diameter-filter-profile (string) (max_len: 47):
                Name of an existing Diameter filter profile.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            icap-profile (string) (max_len: 47):
                Name of an existing ICAP profile.
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            name (string) (max_len: 47):
                Profile group name.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            ssh-filter-profile (string) (max_len: 47):
                Name of an existing SSH filter profile.
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            virtual-patch-profile (string) (max_len: 47):
                Name of an existing virtual-patch profile.
            voip-profile (string) (max_len: 47):
                Name of an existing VoIP (voipd) profile.
            waf-profile (string) (max_len: 47):
                Name of an existing Web application firewall profile.
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if application_list is not None:
            payload_dict["application-list"] = application_list
        if av_profile is not None:
            payload_dict["av-profile"] = av_profile
        if casb_profile is not None:
            payload_dict["casb-profile"] = casb_profile
        if diameter_filter_profile is not None:
            payload_dict["diameter-filter-profile"] = diameter_filter_profile
        if dlp_profile is not None:
            payload_dict["dlp-profile"] = dlp_profile
        if dnsfilter_profile is not None:
            payload_dict["dnsfilter-profile"] = dnsfilter_profile
        if emailfilter_profile is not None:
            payload_dict["emailfilter-profile"] = emailfilter_profile
        if file_filter_profile is not None:
            payload_dict["file-filter-profile"] = file_filter_profile
        if icap_profile is not None:
            payload_dict["icap-profile"] = icap_profile
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if ips_voip_filter is not None:
            payload_dict["ips-voip-filter"] = ips_voip_filter
        if name is not None:
            payload_dict["name"] = name
        if profile_protocol_options is not None:
            payload_dict["profile-protocol-options"] = profile_protocol_options
        if sctp_filter_profile is not None:
            payload_dict["sctp-filter-profile"] = sctp_filter_profile
        if ssh_filter_profile is not None:
            payload_dict["ssh-filter-profile"] = ssh_filter_profile
        if ssl_ssh_profile is not None:
            payload_dict["ssl-ssh-profile"] = ssl_ssh_profile
        if videofilter_profile is not None:
            payload_dict["videofilter-profile"] = videofilter_profile
        if virtual_patch_profile is not None:
            payload_dict["virtual-patch-profile"] = virtual_patch_profile
        if voip_profile is not None:
            payload_dict["voip-profile"] = voip_profile
        if waf_profile is not None:
            payload_dict["waf-profile"] = waf_profile
        if webfilter_profile is not None:
            payload_dict["webfilter-profile"] = webfilter_profile

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
        application_list: Optional[str] = None,
        av_profile: Optional[str] = None,
        casb_profile: Optional[str] = None,
        diameter_filter_profile: Optional[str] = None,
        dlp_profile: Optional[str] = None,
        dnsfilter_profile: Optional[str] = None,
        emailfilter_profile: Optional[str] = None,
        file_filter_profile: Optional[str] = None,
        icap_profile: Optional[str] = None,
        ips_sensor: Optional[str] = None,
        ips_voip_filter: Optional[str] = None,
        name: Optional[str] = None,
        profile_protocol_options: Optional[str] = None,
        sctp_filter_profile: Optional[str] = None,
        ssh_filter_profile: Optional[str] = None,
        ssl_ssh_profile: Optional[str] = None,
        videofilter_profile: Optional[str] = None,
        virtual_patch_profile: Optional[str] = None,
        voip_profile: Optional[str] = None,
        waf_profile: Optional[str] = None,
        webfilter_profile: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update profile-group entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The name (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            application-list (string) (max_len: 47):
                Name of an existing Application list.
            av-profile (string) (max_len: 47):
                Name of an existing Antivirus profile.
            casb-profile (string) (max_len: 47):
                Name of an existing CASB profile.
            diameter-filter-profile (string) (max_len: 47):
                Name of an existing Diameter filter profile.
            dlp-profile (string) (max_len: 47):
                Name of an existing DLP profile.
            dnsfilter-profile (string) (max_len: 47):
                Name of an existing DNS filter profile.
            emailfilter-profile (string) (max_len: 47):
                Name of an existing email filter profile.
            file-filter-profile (string) (max_len: 47):
                Name of an existing file-filter profile.
            icap-profile (string) (max_len: 47):
                Name of an existing ICAP profile.
            ips-sensor (string) (max_len: 47):
                Name of an existing IPS sensor.
            ips-voip-filter (string) (max_len: 47):
                Name of an existing VoIP (ips) profile.
            name (string) (max_len: 47):
                Profile group name.
            profile-protocol-options (string) (max_len: 47):
                Name of an existing Protocol options profile.
            sctp-filter-profile (string) (max_len: 47):
                Name of an existing SCTP filter profile.
            ssh-filter-profile (string) (max_len: 47):
                Name of an existing SSH filter profile.
            ssl-ssh-profile (string) (max_len: 47):
                Name of an existing SSL SSH profile.
            videofilter-profile (string) (max_len: 47):
                Name of an existing VideoFilter profile.
            virtual-patch-profile (string) (max_len: 47):
                Name of an existing virtual-patch profile.
            voip-profile (string) (max_len: 47):
                Name of an existing VoIP (voipd) profile.
            waf-profile (string) (max_len: 47):
                Name of an existing Web application firewall profile.
            webfilter-profile (string) (max_len: 47):
                Name of an existing Web filter profile.

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
        if application_list is not None:
            payload_dict["application-list"] = application_list
        if av_profile is not None:
            payload_dict["av-profile"] = av_profile
        if casb_profile is not None:
            payload_dict["casb-profile"] = casb_profile
        if diameter_filter_profile is not None:
            payload_dict["diameter-filter-profile"] = diameter_filter_profile
        if dlp_profile is not None:
            payload_dict["dlp-profile"] = dlp_profile
        if dnsfilter_profile is not None:
            payload_dict["dnsfilter-profile"] = dnsfilter_profile
        if emailfilter_profile is not None:
            payload_dict["emailfilter-profile"] = emailfilter_profile
        if file_filter_profile is not None:
            payload_dict["file-filter-profile"] = file_filter_profile
        if icap_profile is not None:
            payload_dict["icap-profile"] = icap_profile
        if ips_sensor is not None:
            payload_dict["ips-sensor"] = ips_sensor
        if ips_voip_filter is not None:
            payload_dict["ips-voip-filter"] = ips_voip_filter
        if name is not None:
            payload_dict["name"] = name
        if profile_protocol_options is not None:
            payload_dict["profile-protocol-options"] = profile_protocol_options
        if sctp_filter_profile is not None:
            payload_dict["sctp-filter-profile"] = sctp_filter_profile
        if ssh_filter_profile is not None:
            payload_dict["ssh-filter-profile"] = ssh_filter_profile
        if ssl_ssh_profile is not None:
            payload_dict["ssl-ssh-profile"] = ssl_ssh_profile
        if videofilter_profile is not None:
            payload_dict["videofilter-profile"] = videofilter_profile
        if virtual_patch_profile is not None:
            payload_dict["virtual-patch-profile"] = virtual_patch_profile
        if voip_profile is not None:
            payload_dict["voip-profile"] = voip_profile
        if waf_profile is not None:
            payload_dict["waf-profile"] = waf_profile
        if webfilter_profile is not None:
            payload_dict["webfilter-profile"] = webfilter_profile

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
        Delete a profile-group entry.

        Args:
            mkey: The name (primary key)
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
