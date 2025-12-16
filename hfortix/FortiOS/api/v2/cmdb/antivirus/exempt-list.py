"""
FortiOS CMDB - Antivirus Exempt List
Configure a list of hashes to be exempt from AV scanning

API Endpoints:
    GET    /antivirus/exempt-list       - Get all exempt list entries
    GET    /antivirus/exempt-list/{name} - Get specific exempt list entry
    POST   /antivirus/exempt-list       - Create new exempt list entry
    PUT    /antivirus/exempt-list/{name} - Update exempt list entry
    DELETE /antivirus/exempt-list/{name} - Delete exempt list entry
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ExemptList:
    """Antivirus Exempt List endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        # Query parameters
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        GET /antivirus/exempt-list or /antivirus/exempt-list/{name}
        Get exempt list entries

        Args:
            name: Entry name (if None, returns all entries)
            vdom: Virtual domain (optional)

            Query parameters (all optional):
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned result are in ascending order
            search: Filter objects by search value
            scope: Scope (global|vdom|both)
            datasource: Include datasource information for each linked object
            with_meta: Include meta information about each object (type id, references, etc)
            skip: Enable CLI skip operator to hide skipped properties
            format: List of property names to include (e.g., 'name|hash|status')
            action: Special actions (default, schema, revision)
            **kwargs: Any additional parameters

        Returns:
            Exempt list entry or list of entries

        Examples:
            >>> # Get all entries
            >>> entries = fgt.cmdb.antivirus.exempt_list.get()

            >>> # Get specific entry
            >>> entry = fgt.cmdb.antivirus.exempt_list.get('my_exempt')

            >>> # Get with meta information
            >>> entries = fgt.cmdb.antivirus.exempt_list.get(with_meta=True)

            >>> # Get with filters and format
            >>> entries = fgt.cmdb.antivirus.exempt_list.get(
            ...     format='name|hash|status',
            ...     search='trusted',
            ...     count=10
            ... )

            >>> # Get with datasource info
            >>> entries = fgt.cmdb.antivirus.exempt_list.get(
            ...     datasource=True,
            ...     with_meta=True
            ... )
        """
        # Build params dict from provided parameters
        params = {}

        # Map parameters
        param_map = {
            "attr": attr,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        # Add non-None parameters
        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        # Add any extra kwargs
        params.update(kwargs)

        path = f"antivirus/exempt-list/{name}" if name else "antivirus/exempt-list"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        hash_type: Optional[str] = None,
        hash: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        POST /antivirus/exempt-list
        Create new exempt list entry

        Args:
            name: Table entry name (required, max 35 chars)
            comment: Comment (max 255 chars)
            hash_type: Hash type - 'md5', 'sha1', or 'sha256'
            hash: Hash value to be matched (max 64 chars)
            status: Enable/disable table entry - 'enable' or 'disable'
            vdom: Virtual domain (optional)
            **kwargs: Any additional parameters

        Returns:
            Response dict with status

        Examples:
            >>> # Create with SHA256 hash
            >>> fgt.cmdb.antivirus.exempt_list.create(
            ...     name='trusted_file',
            ...     hash_type='sha256',
            ...     hash='abc123...',
            ...     status='enable',
            ...     comment='Trusted application'
            ... )

            >>> # Create with MD5 hash
            >>> fgt.cmdb.antivirus.exempt_list.create(
            ...     name='safe_file',
            ...     hash_type='md5',
            ...     hash='d41d8cd98f00b204e9800998ecf8427e'
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
        else:
            # Pattern 2: build from kwargs
            payload: Dict[str, Any] = {}
            if name is not None:
                payload["name"] = name

            # Map Python parameter names to API field names
            param_map = {
                "comment": comment,
                "hash_type": hash_type,
                "hash": hash,
                "status": status,
            }

            # API field name mapping
            api_field_map = {
                "comment": "comment",
                "hash_type": "hash-type",
                "hash": "hash",
                "status": "status",
            }

            # Add non-None parameters
            for param_name, value in param_map.items():
                if value is not None:
                    api_name = api_field_map[param_name]
                    payload[api_name] = value

            # Add any extra kwargs
            payload.update(kwargs)

        return self._client.post(
            "cmdb", "antivirus/exempt-list", payload, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        hash_type: Optional[str] = None,
        hash: Optional[str] = None,
        status: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        # Query parameters for actions
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        PUT /antivirus/exempt-list/{name}
        Update exempt list entry

        Args:
            name: Table entry name (required)
            comment: Comment (max 255 chars)
            hash_type: Hash type - 'md5', 'sha1', or 'sha256'
            hash: Hash value to be matched (max 64 chars)
            status: Enable/disable table entry - 'enable' or 'disable'
            vdom: Virtual domain (optional)

            Action parameters (optional):
            action: Action to perform - 'move' to reorder entries
            before: If action=move, move before this entry ID
            after: If action=move, move after this entry ID
            scope: Scope (vdom)
            **kwargs: Any additional parameters

        Returns:
            Response dict with status

        Examples:
            >>> # Update status
            >>> fgt.cmdb.antivirus.exempt_list.update(
            ...     name='trusted_file',
            ...     status='disable'
            ... )

            >>> # Update hash and comment
            >>> fgt.cmdb.antivirus.exempt_list.update(
            ...     name='trusted_file',
            ...     hash='new_hash_value',
            ...     comment='Updated hash for new version'
            ... )

            >>> # Move entry (reorder)
            >>> fgt.cmdb.antivirus.exempt_list.update(
            ...     name='entry1',
            ...     action='move',
            ...     after='entry2'
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
            # Extract name from data if not provided as param
            if name is None:
                name = payload.get("name")
        else:
            # Pattern 2: build from kwargs
            payload: Dict[str, Any] = {}

            # Map data parameters
            data_param_map = {
                "comment": comment,
                "hash_type": hash_type,
                "hash": hash,
                "status": status,
            }

            # API field name mapping for data
            api_field_map = {
                "comment": "comment",
                "hash_type": "hash-type",
                "hash": "hash",
                "status": "status",
            }

            # Add non-None data parameters
            for param_name, value in data_param_map.items():
                if value is not None:
                    api_name = api_field_map[param_name]
                    payload[api_name] = value

            # Add any extra data kwargs
            for key, value in kwargs.items():
                if key not in ["action", "before", "after", "scope"]:
                    payload[key] = value

        # Build query params dict
        params = {}

        # Map query parameters
        query_param_map = {
            "action": action,
            "before": before,
            "after": after,
            "scope": scope,
        }

        # Add non-None query parameters
        for param_name, value in query_param_map.items():
            if value is not None:
                params[param_name] = value

        return self._client.put(
            "cmdb",
            f"antivirus/exempt-list/{name}",
            payload,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        # Action parameters
        mkey: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        DELETE /antivirus/exempt-list/{name}
        Delete exempt list entry

        Args:
            name: Table entry name (required) - the MKEY identifier
            vdom: Virtual domain (optional)

            Action parameters (optional):
            mkey: Filter matching mkey attribute value (if different from name)
            scope: Scope (vdom)
            **kwargs: Any additional parameters

        Returns:
            Response dict with status

        Examples:
            >>> # Simple delete
            >>> fgt.cmdb.antivirus.exempt_list.delete('untrusted_file')

            >>> # Delete with specific vdom
            >>> fgt.cmdb.antivirus.exempt_list.delete(
            ...     name='untrusted_file',
            ...     vdom='root'
            ... )

            >>> # Delete with mkey filter
            >>> fgt.cmdb.antivirus.exempt_list.delete(
            ...     name='entry1',
            ...     mkey='specific_id',
            ...     scope='root'
            ... )
        """
        # Build params dict
        params = {}

        # Map parameters
        param_map = {
            "mkey": mkey,
            "scope": scope,
        }

        # Add non-None parameters
        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        # Add any extra kwargs
        params.update(kwargs)

        return self._client.delete(
            "cmdb",
            f"antivirus/exempt-list/{name}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
