"""
FortiOS profile-protocol-options API wrapper.
Provides access to /api/v2/cmdb/firewall/profile-protocol-options endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class ProfileProtocolOptions:
    """
    Wrapper for firewall profile-protocol-options API endpoint.

    Manages profile-protocol-options configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the ProfileProtocolOptions wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/profile-protocol-options"

    def list(
        self,
        datasource: Optional[Any] = None,
        start: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        with_contents_hash: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        filter: Optional[Any] = None,
        key: Optional[Any] = None,
        pattern: Optional[Any] = None,
        scope: Optional[Any] = None,
        exclude_default_values: Optional[Any] = None,
        datasource_format: Optional[Any] = None,
        unfiltered_count: Optional[Any] = None,
        stat_items: Optional[Any] = None,
        primary_keys: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all profile-protocol-options entries.

        Args:
            datasource: Enable to include datasource information for each linked object.
            start: Starting entry index.
            count: Maximum number of entries to return.
            skip_to: Skip to Nth CMDB entry.
            with_meta: Enable to include meta information about each object (type id, referen
            with_contents_hash: Enable to include a checksum of each object's contents.
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            filter: Filtering multiple key/value pairs
            key: If present, objects will be filtered on property with this name.
            pattern: If present, objects will be filtered on property with this value.
            scope: Scope [global|vdom|both*]
            exclude_default_values: Exclude properties/objects with default value
            datasource_format: A map of datasources to a string of attributes, separated by | (ie: po
            unfiltered_count: Maximum number of unfiltered entries to interate through.
            stat_items: Items to count occurrence in entire response (multiple items should be
            primary_keys: The primary key to find indexes for.
            action: default: Return the CLI default values for entire CLI tree.
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with results list
        """
        params = {}

        if datasource is not None:
            params["datasource"] = datasource
        if start is not None:
            params["start"] = start
        if count is not None:
            params["count"] = count
        if skip_to is not None:
            params["skip_to"] = skip_to
        if with_meta is not None:
            params["with_meta"] = with_meta
        if with_contents_hash is not None:
            params["with_contents_hash"] = with_contents_hash
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if filter is not None:
            params["filter"] = filter
        if key is not None:
            params["key"] = key
        if pattern is not None:
            params["pattern"] = pattern
        if scope is not None:
            params["scope"] = scope
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if datasource_format is not None:
            params["datasource_format"] = datasource_format
        if unfiltered_count is not None:
            params["unfiltered_count"] = unfiltered_count
        if stat_items is not None:
            params["stat-items"] = stat_items
        if primary_keys is not None:
            params["primary_keys"] = primary_keys
        if action is not None:
            params["action"] = action
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get("cmdb", self.path, params=params, vdom=vdom, raw_json=raw_json)

    def get(
        self,
        mkey: Union[str, int],
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
        Retrieve a specific profile-protocol-options entry by its name.

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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        cifs: Optional[list] = None,
        comment: Optional[str] = None,
        dns: Optional[list] = None,
        ftp: Optional[list] = None,
        http: Optional[list] = None,
        imap: Optional[list] = None,
        mail_signature: Optional[list] = None,
        mapi: Optional[list] = None,
        name: Optional[str] = None,
        nntp: Optional[list] = None,
        oversize_log: Optional[str] = None,
        pop3: Optional[list] = None,
        replacemsg_group: Optional[str] = None,
        rpc_over_http: Optional[str] = None,
        smtp: Optional[list] = None,
        ssh: Optional[list] = None,
        switching_protocols_log: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create profile-protocol-options entry.

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

            cifs (list[object]):
                Configure CIFS protocol options.
            comment (string) (max_len: 255):
                Optional comments.
            dns (list[object]):
                Configure DNS protocol options.
            ftp (list[object]):
                Configure FTP protocol options.
            http (list[object]):
                Configure HTTP protocol options.
            imap (list[object]):
                Configure IMAP protocol options.
            mail-signature (list[object]):
                Configure Mail signature.
            mapi (list[object]):
                Configure MAPI protocol options.
            name (string) (max_len: 47):
                Name.
            nntp (list[object]):
                Configure NNTP protocol options.
            oversize-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging for antivirus oversize file blocking.
            pop3 (list[object]):
                Configure POP3 protocol options.
            replacemsg-group (string) (max_len: 35):
                Name of the replacement message group to be used.
            rpc-over-http (string) (enum: ['enable', 'disable']):
                Enable/disable inspection of RPC over HTTP.
            smtp (list[object]):
                Configure SMTP protocol options.
            ssh (list[object]):
                Configure SFTP and SCP protocol options.
            switching-protocols-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging for HTTP/HTTPS switching protocols.

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if cifs is not None:
            payload_dict["cifs"] = cifs
        if comment is not None:
            payload_dict["comment"] = comment
        if dns is not None:
            payload_dict["dns"] = dns
        if ftp is not None:
            payload_dict["ftp"] = ftp
        if http is not None:
            payload_dict["http"] = http
        if imap is not None:
            payload_dict["imap"] = imap
        if mail_signature is not None:
            payload_dict["mail-signature"] = mail_signature
        if mapi is not None:
            payload_dict["mapi"] = mapi
        if name is not None:
            payload_dict["name"] = name
        if nntp is not None:
            payload_dict["nntp"] = nntp
        if oversize_log is not None:
            payload_dict["oversize-log"] = oversize_log
        if pop3 is not None:
            payload_dict["pop3"] = pop3
        if replacemsg_group is not None:
            payload_dict["replacemsg-group"] = replacemsg_group
        if rpc_over_http is not None:
            payload_dict["rpc-over-http"] = rpc_over_http
        if smtp is not None:
            payload_dict["smtp"] = smtp
        if ssh is not None:
            payload_dict["ssh"] = ssh
        if switching_protocols_log is not None:
            payload_dict["switching-protocols-log"] = switching_protocols_log

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
        mkey: Union[str, int],
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        cifs: Optional[list] = None,
        comment: Optional[str] = None,
        dns: Optional[list] = None,
        ftp: Optional[list] = None,
        http: Optional[list] = None,
        imap: Optional[list] = None,
        mail_signature: Optional[list] = None,
        mapi: Optional[list] = None,
        name: Optional[str] = None,
        nntp: Optional[list] = None,
        oversize_log: Optional[str] = None,
        pop3: Optional[list] = None,
        replacemsg_group: Optional[str] = None,
        rpc_over_http: Optional[str] = None,
        smtp: Optional[list] = None,
        ssh: Optional[list] = None,
        switching_protocols_log: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update profile-protocol-options entry.

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

            cifs (list[object]):
                Configure CIFS protocol options.
            comment (string) (max_len: 255):
                Optional comments.
            dns (list[object]):
                Configure DNS protocol options.
            ftp (list[object]):
                Configure FTP protocol options.
            http (list[object]):
                Configure HTTP protocol options.
            imap (list[object]):
                Configure IMAP protocol options.
            mail-signature (list[object]):
                Configure Mail signature.
            mapi (list[object]):
                Configure MAPI protocol options.
            name (string) (max_len: 47):
                Name.
            nntp (list[object]):
                Configure NNTP protocol options.
            oversize-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging for antivirus oversize file blocking.
            pop3 (list[object]):
                Configure POP3 protocol options.
            replacemsg-group (string) (max_len: 35):
                Name of the replacement message group to be used.
            rpc-over-http (string) (enum: ['enable', 'disable']):
                Enable/disable inspection of RPC over HTTP.
            smtp (list[object]):
                Configure SMTP protocol options.
            ssh (list[object]):
                Configure SFTP and SCP protocol options.
            switching-protocols-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging for HTTP/HTTPS switching protocols.

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
        if cifs is not None:
            payload_dict["cifs"] = cifs
        if comment is not None:
            payload_dict["comment"] = comment
        if dns is not None:
            payload_dict["dns"] = dns
        if ftp is not None:
            payload_dict["ftp"] = ftp
        if http is not None:
            payload_dict["http"] = http
        if imap is not None:
            payload_dict["imap"] = imap
        if mail_signature is not None:
            payload_dict["mail-signature"] = mail_signature
        if mapi is not None:
            payload_dict["mapi"] = mapi
        if name is not None:
            payload_dict["name"] = name
        if nntp is not None:
            payload_dict["nntp"] = nntp
        if oversize_log is not None:
            payload_dict["oversize-log"] = oversize_log
        if pop3 is not None:
            payload_dict["pop3"] = pop3
        if replacemsg_group is not None:
            payload_dict["replacemsg-group"] = replacemsg_group
        if rpc_over_http is not None:
            payload_dict["rpc-over-http"] = rpc_over_http
        if smtp is not None:
            payload_dict["smtp"] = smtp
        if ssh is not None:
            payload_dict["ssh"] = ssh
        if switching_protocols_log is not None:
            payload_dict["switching-protocols-log"] = switching_protocols_log

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
            f"{self.path}/{mkey_str}",
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Union[str, int],
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a profile-protocol-options entry.

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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )
