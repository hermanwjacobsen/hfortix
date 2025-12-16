"""
FortiOS CMDB - DLP Label

Configure labels used by DLP blocking.

API Endpoints:
    GET    /dlp/label       - List all labels
    GET    /dlp/label/{name} - Get specific label
    POST   /dlp/label       - Create new label
    PUT    /dlp/label/{name} - Update label
    DELETE /dlp/label/{name} - Delete label
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Label:
    """DLP label endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: str | None = None,
        # Query parameters
        attr: str | None = None,
        count: int | None = None,
        skip_to_datasource: dict[str, Any] | None = None,
        acs: int | None = None,
        search: str | None = None,
        scope: str | None = None,
        datasource: bool | None = None,
        with_meta: bool | None = None,
        skip: bool | None = None,
        format: str | None = None,
        action: str | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get DLP label(s).

        Args:
            name: Name of specific label to retrieve
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned results are in ascending order
            search: Filter objects by search value
            scope: Scope - 'global', 'vdom', or 'both'
            datasource: Include datasource information for each linked object
            with_meta: Include meta information (type id, references, etc)
            skip: Enable CLI skip operator to hide skipped properties
            format: List of property names to include (pipe-separated)
            action: Special actions - 'default', 'schema', 'revision'
            vdom: Virtual Domain(s). Use 'root' for single VDOM, or '*' for all
            **kwargs: Additional query parameters

        Returns:
            API response dictionary with label configuration(s)

        Examples:
            >>> # Get all labels
            >>> result = fgt.cmdb.dlp.label.get()
            >>> print(f"Total labels: {len(result['results'])}")

            >>> # Get specific label
            >>> result = fgt.cmdb.dlp.label.get('mpip-label1')
            >>> print(f"Type: {result['results']['type']}")
        """
        # Build path
        path = "dlp/label"
        if name:
            path = f"dlp/label/{name}"

        # Build query parameters
        params = {}
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

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def list(self, vdom: str | None = None, **kwargs) -> dict[str, Any]:
        """
        List all DLP labels (convenience method).

        Args:
            vdom: Virtual Domain(s)
            **kwargs: Additional query parameters

        Returns:
            API response dictionary with all labels

        Examples:
            >>> # List all labels
            >>> result = fgt.cmdb.dlp.label.list()
            >>> for lbl in result['results']:
            ...     print(f"{lbl['name']}: {lbl.get('type', 'N/A')}")
        """
        return self.get(vdom=vdom, **kwargs)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Label configuration
        type: str = "mpip",
        mpip_type: str | None = None,
        connector: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Create a new DLP label.

        Args:
            name: Name of the label (max 35 chars)
            type: Label type - 'mpip' (Microsoft Purview Information Protection)
            mpip_type: MPIP label type - 'remote' (remotely fetched) or 'local' (locally configured)
            connector: Name of SDN connector (max 35 chars)
            comment: Optional comments (max 255 chars)
            entries: List of label entries. Each entry is a dict with:
                - id (int): Entry ID (1-32)
                - fortidata_label_name (str): Name of FortiData label (max 127 chars)
                - mpip_label_name (str): Name of MPIP label (max 127 chars)
                - guid (str): MPIP label guid (max 36 chars)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create local MPIP label
            >>> result = fgt.cmdb.dlp.label.create(
            ...     name='mpip-label1',
            ...     type='mpip',
            ...     mpip_type='local',
            ...     comment='Local MPIP labels',
            ...     entries=[
            ...         {
            ...             'id': 1,
            ...             'mpip_label_name': 'Confidential',
            ...             'guid': '12345678-1234-1234-1234-123456789abc'
            ...         }
            ...     ]
            ... )

            >>> # Create remote MPIP label with connector
            >>> result = fgt.cmdb.dlp.label.create(
            ...     name='mpip-remote',
            ...     type='mpip',
            ...     mpip_type='remote',
            ...     connector='azure-connector1',
            ...     comment='Remote Azure labels'
            ... )
        """
        data = {}
        param_map = {
            "name": name,
            "type": type,
            "mpip_type": mpip_type,
            "connector": connector,
            "comment": comment,
            "entries": entries,
        }

        # Map to API field names
        api_field_map = {
            "name": "name",
            "type": "type",
            "mpip_type": "mpip-type",
            "connector": "connector",
            "comment": "comment",
            "entries": "entries",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle entries list - convert snake_case keys to hyphen-case
                if param_name == "entries" and isinstance(value, list):
                    converted_entries = []
                    for entry in value:
                        converted_entry = {}
                        for k, v in entry.items():
                            # Convert snake_case to hyphen-case
                            api_key = k.replace("_", "-")
                            converted_entry[api_key] = v
                        converted_entries.append(converted_entry)
                    data[api_name] = converted_entries
                else:
                    data[api_name] = value

        data.update(kwargs)

        return self._client.post("cmdb", "dlp/label", data, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Label configuration
        type: str | None = None,
        mpip_type: str | None = None,
        connector: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update an existing DLP label.

        Args:
            name: Name of the label to update
            type: Label type - 'mpip' (Microsoft Purview Information Protection)
            mpip_type: MPIP label type - 'remote' or 'local'
            connector: Name of SDN connector (max 35 chars)
            comment: Optional comments (max 255 chars)
            entries: List of label entries. Each entry is a dict with:
                - id (int): Entry ID (1-32)
                - fortidata_label_name (str): Name of FortiData label (max 127 chars)
                - mpip_label_name (str): Name of MPIP label (max 127 chars)
                - guid (str): MPIP label guid (max 36 chars)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update comment
            >>> result = fgt.cmdb.dlp.label.update(
            ...     name='mpip-label1',
            ...     comment='Updated comment'
            ... )

            >>> # Update entries
            >>> result = fgt.cmdb.dlp.label.update(
            ...     name='mpip-label1',
            ...     entries=[
            ...         {
            ...             'id': 1,
            ...             'mpip_label_name': 'Confidential',
            ...             'guid': '12345678-1234-1234-1234-123456789abc'
            ...         },
            ...         {
            ...             'id': 2,
            ...             'mpip_label_name': 'Secret',
            ...             'guid': '87654321-4321-4321-4321-cba987654321'
            ...         }
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            "type": type,
            "mpip_type": mpip_type,
            "connector": connector,
            "comment": comment,
            "entries": entries,
        }

        # Map to API field names
        api_field_map = {
            "type": "type",
            "mpip_type": "mpip-type",
            "connector": "connector",
            "comment": "comment",
            "entries": "entries",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle entries list - convert snake_case keys to hyphen-case
                if param_name == "entries" and isinstance(value, list):
                    converted_entries = []
                    for entry in value:
                        converted_entry = {}
                        for k, v in entry.items():
                            # Convert snake_case to hyphen-case
                            api_key = k.replace("_", "-")
                            converted_entry[api_key] = v
                        converted_entries.append(converted_entry)
                    data[api_name] = converted_entries
                else:
                    data[api_name] = value

        data.update(kwargs)

        return self._client.put("cmdb", f"dlp/label/{name}", data, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a DLP label.

        Args:
            name: Name of the label to delete
            vdom: Virtual Domain(s)

        Returns:
            API response dictionary

        Examples:
            >>> # Delete a label
            >>> result = fgt.cmdb.dlp.label.delete('mpip-label1')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete("cmdb", f"dlp/label/{name}", vdom=vdom, raw_json=raw_json)
