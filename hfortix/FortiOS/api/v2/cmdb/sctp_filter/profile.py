"""
FortiOS CMDB - SCTP Filter Profile

Configure SCTP filter profiles.

API Endpoints:
    GET    /api/v2/cmdb/sctp-filter/profile           - List all / Get specific
    POST   /api/v2/cmdb/sctp-filter/profile           - Create
    PUT    /api/v2/cmdb/sctp-filter/profile/{name}   - Update
    DELETE /api/v2/cmdb/sctp-filter/profile/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Profile:
    """SCTP Filter Profile endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize SCTP Filter Profile endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get SCTP filter profile(s) - List all or get specific.

        Args:
            name: Profile name (if specified, gets single profile)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.sctp_filter.profile.get()
            >>> result = fgt.api.cmdb.sctp_filter.profile.get(name='profile1')
        """
        path = "sctp-filter/profile"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        ppid_filters: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create SCTP filter profile.

        Args:
            data_dict: Complete profile configuration dictionary
            name: Profile name (max 35 chars)
            comment: Optional comment (max 255 chars)
            ppid_filters: List of PPID filter dicts. Each dict contains:
                - id: Filter ID (required)
                - ppid: Payload protocol identifier (0-4294967295)
                - action: Action for matching PPID. Options: 'pass', 'reset', 'replace'
                - comment: Optional comment
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Using data_dict
            >>> data = {
            ...     'name': 'sctp-profile1',
            ...     'comment': 'SCTP filter for M3UA',
            ...     'ppid-filters': [
            ...         {'id': 1, 'ppid': 3, 'action': 'pass'},
            ...         {'id': 2, 'ppid': 4, 'action': 'reset'}
            ...     ]
            ... }
            >>> result = fgt.api.cmdb.sctp_filter.profile.create(data_dict=data)
            >>> 
            >>> # Using explicit parameters
            >>> ppid_list = [
            ...     {'id': 1, 'ppid': 3, 'action': 'pass', 'comment': 'M3UA'},
            ...     {'id': 2, 'ppid': 5, 'action': 'reset'}
            ... ]
            >>> result = fgt.api.cmdb.sctp_filter.profile.create(
            ...     name='sctp-profile1',
            ...     comment='SCTP filter profile',
            ...     ppid_filters=ppid_list
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        
        if name is not None:
            data["name"] = name
        if comment is not None:
            data["comment"] = comment
        if ppid_filters is not None:
            data["ppid-filters"] = ppid_filters
            
        data.update(kwargs)
        return self._client.post("cmdb", "sctp-filter/profile", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        comment: Optional[str] = None,
        ppid_filters: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update SCTP filter profile.

        Args:
            name: Profile name (required)
            data_dict: Complete profile configuration dictionary
            comment: Optional comment (max 255 chars)
            ppid_filters: List of PPID filter dicts. Each dict contains:
                - id: Filter ID (required)
                - ppid: Payload protocol identifier (0-4294967295)
                - action: Action for matching PPID. Options: 'pass', 'reset', 'replace'
                - comment: Optional comment
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters to update

        Returns:
            API response dict

        Examples:
            >>> # Using data_dict
            >>> data = {'comment': 'Updated comment'}
            >>> result = fgt.api.cmdb.sctp_filter.profile.update(
            ...     name='sctp-profile1',
            ...     data_dict=data
            ... )
            >>> 
            >>> # Using explicit parameters
            >>> ppid_list = [
            ...     {'id': 1, 'ppid': 3, 'action': 'pass'},
            ...     {'id': 2, 'ppid': 4, 'action': 'pass'}
            ... ]
            >>> result = fgt.api.cmdb.sctp_filter.profile.update(
            ...     name='sctp-profile1',
            ...     comment='Updated profile',
            ...     ppid_filters=ppid_list
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        
        if comment is not None:
            data["comment"] = comment
        if ppid_filters is not None:
            data["ppid-filters"] = ppid_filters
            
        data.update(kwargs)
        path = f"sctp-filter/profile/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete SCTP filter profile.

        Args:
            name: Profile name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.sctp_filter.profile.delete(name='sctp-profile1')
        """
        path = f"sctp-filter/profile/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if SCTP filter profile exists.

        Args:
            name: Profile name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if profile exists, False otherwise

        Examples:
            >>> if fgt.api.cmdb.sctp_filter.profile.exists(name='sctp-profile1'):
            ...     print("Profile exists")
        """
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False
