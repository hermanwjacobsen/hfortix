"""
FortiOS CMDB - DLP Sensor

Configure sensors used by DLP blocking.

API Endpoints:
    GET    /dlp/sensor           - List all / Get specific
    POST   /dlp/sensor           - Create
    PUT    /dlp/sensor/{name}   - Update
    DELETE /dlp/sensor/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Sensor:
    """DLP sensor endpoint"""

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
        Get DLP sensor(s) - List all or get specific.

        Args:
            name: Name of specific sensor to retrieve
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
            API response dictionary with sensor configuration(s)

        Examples:
            >>> # Get all sensors
            >>> result = fgt.cmdb.dlp.sensor.get()
            >>> print(f"Total sensors: {len(result['results'])}")

            >>> # Get specific sensor
            >>> result = fgt.cmdb.dlp.sensor.get('credit-card-sensor')
            >>> print(f"Match type: {result['results']['match-type']}")
        """
        # Build path
        path = "dlp/sensor"
        if name:
            path = f"dlp/sensor/{encode_path_component(name)}"

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

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Sensor configuration
        match_type: str | None = None,
        eval: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Create DLP sensor.

        Args:
            name: Name of the sensor (max 35 chars)
            match_type: Logical relation between entries - 'match-all', 'match-any', or 'match-eval'
            eval: Expression to evaluate (max 255 chars, used with match-eval)
            comment: Optional comments (max 255 chars)
            entries: List of sensor entries. Each entry is a dict with:
                - id (int): Entry ID (1-32)
                - dictionary (str): DLP dictionary or exact-data-match name (max 35 chars)
                - count (int): Count of dictionary matches to trigger (1-255, default 1)
                - status (str): Enable/disable this entry - 'enable' or 'disable'
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # POST - Create sensor with match-any
            >>> result = fgt.cmdb.dlp.sensor.create(
            ...     name='pii-sensor',
            ...     match_type='match-any',
            ...     comment='Detects PII data',
            ...     entries=[
            ...         {
            ...             'id': 1,
            ...             'dictionary': 'ssn-dict',
            ...             'count': 1,
            ...             'status': 'enable'
            ...         },
            ...         {
            ...             'id': 2,
            ...             'dictionary': 'credit-card-dict',
            ...             'count': 1,
            ...             'status': 'enable'
            ...         }
            ...     ]
            ... )

            >>> # POST - Create sensor with match-all
            >>> result = fgt.cmdb.dlp.sensor.create(
            ...     name='multi-match-sensor',
            ...     match_type='match-all',
            ...     comment='Requires all dictionaries to match',
            ...     entries=[
            ...         {'id': 1, 'dictionary': 'dict1', 'count': 2},
            ...         {'id': 2, 'dictionary': 'dict2', 'count': 1}
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            "name": name,
            "match_type": match_type,
            "eval": eval,
            "comment": comment,
            "entries": entries,
        }

        # Map to API field names
        api_field_map = {
            "name": "name",
            "match_type": "match-type",
            "eval": "eval",
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

        return self._client.post("cmdb", "dlp/sensor", data, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Sensor configuration
        match_type: str | None = None,
        eval: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update DLP sensor.

        Args:
            name: Name of the sensor to update
            match_type: Logical relation between entries - 'match-all', 'match-any', or 'match-eval'
            eval: Expression to evaluate (max 255 chars, used with match-eval)
            comment: Optional comments (max 255 chars)
            entries: List of sensor entries (see create() for structure)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters

        Returns:
            API response dictionary

        Examples:
            >>> # PUT - Update comment
            >>> result = fgt.cmdb.dlp.sensor.update(
            ...     name='pii-sensor',
            ...     comment='Updated PII detection sensor'
            ... )

            >>> # PUT - Update entries
            >>> result = fgt.cmdb.dlp.sensor.update(
            ...     name='pii-sensor',
            ...     entries=[
            ...         {
            ...             'id': 1,
            ...             'dictionary': 'ssn-dict',
            ...             'count': 2,
            ...             'status': 'enable'
            ...         },
            ...         {
            ...             'id': 2,
            ...             'dictionary': 'credit-card-dict',
            ...             'count': 1,
            ...             'status': 'enable'
            ...         },
            ...         {
            ...             'id': 3,
            ...             'dictionary': 'passport-dict',
            ...             'count': 1,
            ...             'status': 'enable'
            ...         }
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            "match_type": match_type,
            "eval": eval,
            "comment": comment,
            "entries": entries,
        }

        # Map to API field names
        api_field_map = {
            "match_type": "match-type",
            "eval": "eval",
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

        return self._client.put("cmdb", f"dlp/sensor/{name}", data, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a DLP sensor.

        Args:
            name: Name of the sensor to delete
            vdom: Virtual Domain(s)

        Returns:
            API response dictionary

        Examples:
            >>> # Delete a sensor
            >>> result = fgt.cmdb.dlp.sensor.delete('pii-sensor')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete("cmdb", f"dlp/sensor/{name}", vdom=vdom, raw_json=raw_json)
