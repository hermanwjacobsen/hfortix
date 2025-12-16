"""
FortiOS CMDB - DLP File Pattern

Configure file patterns used by DLP blocking.

API Endpoints:
    GET    /dlp/filepattern       - List all file patterns
    GET    /dlp/filepattern/{id}  - Get specific file pattern
    POST   /dlp/filepattern       - Create new file pattern
    PUT    /dlp/filepattern/{id}  - Update file pattern
    DELETE /dlp/filepattern/{id}  - Delete file pattern
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Filepattern:
    """DLP filepattern endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        id: int | None = None,
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
        Get DLP file pattern(s).

        Args:
            id: File pattern ID. If provided, gets specific file pattern.
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
            API response dictionary with file pattern configuration(s)

        Examples:
            >>> # Get all file patterns
            >>> result = fgt.cmdb.dlp.filepattern.get()
            >>> print(f"Total patterns: {len(result['results'])}")

            >>> # Get specific file pattern
            >>> result = fgt.cmdb.dlp.filepattern.get(1)
            >>> print(f"Name: {result['results']['name']}")

            >>> # Get with metadata
            >>> result = fgt.cmdb.dlp.filepattern.get(with_meta=True)
        """
        # Build path
        path = "dlp/filepattern"
        if id is not None:
            path = f"dlp/filepattern/{id}"

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
        List all DLP file patterns (convenience method).

        Args:
            vdom: Virtual Domain(s)
            **kwargs: Additional query parameters

        Returns:
            API response dictionary with all file patterns

        Examples:
            >>> # List all file patterns
            >>> result = fgt.cmdb.dlp.filepattern.list()
            >>> for p in result['results']:
            ...     print(f"{p['id']}: {p['name']}")
        """
        return self.get(vdom=vdom, **kwargs)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # File pattern configuration
        id: int | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Create a new DLP file pattern.

        Args:
            name: Name of the file pattern list (max 63 chars)
            id: ID (0-4294967295)
            comment: Optional comments (max 255 chars)
            entries: List of file pattern entries. Each entry is a dict with:
                - filter_type (str): Filter by - 'pattern' (file name) or 'type' (file type)
                - pattern (str): File name pattern (max 79 chars, required if filter_type='pattern')
                - file_type (str): File type (required if filter_type='type')
                  Valid types: '7z', 'zip', 'rar', 'tar', 'pdf', 'exe', 'msoffice', 'msofficex', etc.
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create pattern for executable files
            >>> result = fgt.cmdb.dlp.filepattern.create(
            ...     name='block-executables',
            ...     comment='Block executable file types',
            ...     entries=[
            ...         {'filter_type': 'type', 'file_type': 'exe'},
            ...         {'filter_type': 'type', 'file_type': 'dll'},
            ...         {'filter_type': 'type', 'file_type': 'bat'}
            ...     ]
            ... )

            >>> # Create pattern for file names
            >>> result = fgt.cmdb.dlp.filepattern.create(
            ...     name='confidential-docs',
            ...     entries=[
            ...         {'filter_type': 'pattern', 'pattern': '*confidential*'},
            ...         {'filter_type': 'pattern', 'pattern': '*secret*'}
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            "id": id,
            "name": name,
            "comment": comment,
            "entries": entries,
        }

        # Map to API field names
        api_field_map = {
            "id": "id",
            "name": "name",
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

                        # If filter-type is 'type', set pattern to file-type value
                        if (
                            converted_entry.get("filter-type") == "type"
                            and "file-type" in converted_entry
                        ):
                            converted_entry["pattern"] = converted_entry["file-type"]

                        converted_entries.append(converted_entry)
                    data[api_name] = converted_entries
                else:
                    data[api_name] = value

        data.update(kwargs)

        return self._client.post("cmdb", "dlp/filepattern", data, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        id: Optional[int] = None,
        # File pattern configuration
        name: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update an existing DLP file pattern.

        Args:
            id: ID of the file pattern to update
            name: Name of the file pattern list (max 63 chars)
            comment: Optional comments (max 255 chars)
            entries: List of file pattern entries. Each entry is a dict with:
                - filter_type (str): Filter by - 'pattern' (file name) or 'type' (file type)
                - pattern (str): File name pattern (max 79 chars, required if filter_type='pattern')
                - file_type (str): File type (required if filter_type='type')
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update comment
            >>> result = fgt.cmdb.dlp.filepattern.update(
            ...     id=1,
            ...     comment='Updated block list'
            ... )

            >>> # Update entries
            >>> result = fgt.cmdb.dlp.filepattern.update(
            ...     id=1,
            ...     entries=[
            ...         {'filter_type': 'type', 'file_type': 'exe'},
            ...         {'filter_type': 'type', 'file_type': 'dll'},
            ...         {'filter_type': 'type', 'file_type': 'msi'}
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            "id": id,
            "name": name,
            "comment": comment,
            "entries": entries,
        }

        # Map to API field names
        api_field_map = {
            "id": "id",
            "name": "name",
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

                        # If filter-type is 'type', set pattern to file-type value
                        if (
                            converted_entry.get("filter-type") == "type"
                            and "file-type" in converted_entry
                        ):
                            converted_entry["pattern"] = converted_entry["file-type"]

                        converted_entries.append(converted_entry)
                    data[api_name] = converted_entries
                else:
                    data[api_name] = value

        data.update(kwargs)

        return self._client.put("cmdb", f"dlp/filepattern/{id}", data, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        id: int,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a DLP file pattern.

        Args:
            id: ID of the file pattern to delete
            vdom: Virtual Domain(s)

        Returns:
            API response dictionary

        Examples:
            >>> # Delete file pattern
            >>> result = fgt.cmdb.dlp.filepattern.delete(1)
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete("cmdb", f"dlp/filepattern/{id}", vdom=vdom, raw_json=raw_json)
