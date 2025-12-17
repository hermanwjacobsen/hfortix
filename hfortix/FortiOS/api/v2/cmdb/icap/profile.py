"""
FortiOS CMDB - ICAP Profile

Configure ICAP profiles for content inspection.

API Endpoints:
    GET    /api/v2/cmdb/icap/profile        - List all ICAP profiles
    GET    /api/v2/cmdb/icap/profile/{name} - Get specific ICAP profile
    POST   /api/v2/cmdb/icap/profile        - Create ICAP profile
    PUT    /api/v2/cmdb/icap/profile/{name} - Update ICAP profile
    DELETE /api/v2/cmdb/icap/profile/{name} - Delete ICAP profile
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class Profile:
    """ICAP Profile endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all ICAP profiles.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing list of ICAP profiles

        Examples:
            >>> # List all profiles
            >>> profiles = fgt.api.cmdb.icap.profile.list()
            >>> for profile in profiles['results']:
            ...     print(profile['name'])
        """
        path = "icap/profile"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def get(
        self,
        name: str,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get specific ICAP profile.

        Args:
            name: Profile name
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Skip hidden properties
            action: Additional action to perform
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing profile configuration

        Examples:
            >>> # Get specific profile
            >>> profile = fgt.api.cmdb.icap.profile.get('default')
            >>> print(profile['request'])
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with-meta": with_meta,
            "skip": skip,
            "action": action,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        path = f"icap/profile/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def create(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        replacemsg_group: Optional[str] = None,
        comment: Optional[str] = None,
        request: Optional[str] = None,
        response: Optional[str] = None,
        file_transfer: Optional[str] = None,
        streaming_content_bypass: Optional[str] = None,
        ocr_only: Optional[str] = None,
        size_limit_204: Optional[int] = None,
        response_204: Optional[str] = None,
        preview: Optional[str] = None,
        preview_data_length: Optional[int] = None,
        request_server: Optional[str] = None,
        response_server: Optional[str] = None,
        file_transfer_server: Optional[str] = None,
        request_failure: Optional[str] = None,
        response_failure: Optional[str] = None,
        file_transfer_failure: Optional[str] = None,
        request_path: Optional[str] = None,
        response_path: Optional[str] = None,
        file_transfer_path: Optional[str] = None,
        methods: Optional[str] = None,
        response_req_hdr: Optional[str] = None,
        respmod_default_action: Optional[str] = None,
        icap_block_log: Optional[str] = None,
        chunk_encap: Optional[str] = None,
        extension_feature: Optional[str] = None,
        scan_progress_interval: Optional[int] = None,
        timeout: Optional[int] = None,
        icap_headers: Optional[list[dict[str, Any]]] = None,
        respmod_forward_rules: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create ICAP profile.

        Supports three usage patterns:

        1. Dictionary pattern (template-based):
           >>> config = {'name': 'web-filter', 'request': 'enable', 'request-server': 'icap-server1'}
           >>> fgt.api.cmdb.icap.profile.create(data_dict=config)

        2. Keyword pattern (explicit parameters):
           >>> fgt.api.cmdb.icap.profile.create(
           ...     name='web-filter',
           ...     request='enable',
           ...     request_server='icap-server1'
           ... )

        3. Mixed pattern (template + overrides):
           >>> base = {'request': 'enable'}
           >>> fgt.api.cmdb.icap.profile.create(data_dict=base, name='web-filter')

        Args:
            data_dict: Complete configuration dictionary (pattern 1 & 3)
            name: Profile name
            replacemsg_group: Replacement message group
            comment: Comment
            request: Enable/disable ICAP request modification (enable/disable)
            response: Enable/disable ICAP response modification (enable/disable)
            file_transfer: File transfer protocols (ssh/ftp)
            streaming_content_bypass: Enable/disable bypassing ICAP for streaming (enable/disable)
            ocr_only: Enable/disable OCR-only content submission (enable/disable)
            size_limit_204: 204 response size limit in MB (1-10)
            response_204: Enable/disable 204 response allowance (enable/disable)
            preview: Enable/disable preview of data (enable/disable)
            preview_data_length: Preview data length (0-4096)
            request_server: ICAP server for HTTP requests
            response_server: ICAP server for HTTP responses
            file_transfer_server: ICAP server for file transfers
            request_failure: Action on request failure (error/bypass)
            response_failure: Action on response failure (error/bypass)
            file_transfer_failure: Action on file transfer failure (error/bypass)
            request_path: ICAP URI path for request processing
            response_path: ICAP URI path for response processing
            file_transfer_path: ICAP URI path for file transfer processing
            methods: HTTP methods to inspect (delete/get/head/options/post/put/trace/connect/other)
            response_req_hdr: Enable/disable req-hdr for respmod (enable/disable)
            respmod_default_action: Default respmod action (forward/bypass)
            icap_block_log: Enable/disable UTM log for infections (enable/disable)
            chunk_encap: Enable/disable chunked encapsulation (enable/disable)
            extension_feature: ICAP extension features (scan-progress)
            scan_progress_interval: Scan progress interval (5-30 seconds)
            timeout: Response timeout (30-3600 seconds)
            icap_headers: ICAP forwarded request headers list
            respmod_forward_rules: ICAP response mode forward rules list
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing creation result

        Examples:
            >>> # Create with dictionary
            >>> config = {
            ...     'name': 'web-filter',
            ...     'request': 'enable',
            ...     'request-server': 'icap-server1',
            ...     'request-path': '/reqmod',
            ...     'timeout': 60
            ... }
            >>> result = fgt.api.cmdb.icap.profile.create(data_dict=config)

            >>> # Create with keywords
            >>> result = fgt.api.cmdb.icap.profile.create(
            ...     name='email-filter',
            ...     response='enable',
            ...     response_server='icap-server2',
            ...     response_path='/respmod'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "name": name,
            "replacemsg_group": replacemsg_group,
            "comment": comment,
            "request": request,
            "response": response,
            "file_transfer": file_transfer,
            "streaming_content_bypass": streaming_content_bypass,
            "ocr_only": ocr_only,
            "size_limit_204": size_limit_204,
            "response_204": response_204,
            "preview": preview,
            "preview_data_length": preview_data_length,
            "request_server": request_server,
            "response_server": response_server,
            "file_transfer_server": file_transfer_server,
            "request_failure": request_failure,
            "response_failure": response_failure,
            "file_transfer_failure": file_transfer_failure,
            "request_path": request_path,
            "response_path": response_path,
            "file_transfer_path": file_transfer_path,
            "methods": methods,
            "response_req_hdr": response_req_hdr,
            "respmod_default_action": respmod_default_action,
            "icap_block_log": icap_block_log,
            "chunk_encap": chunk_encap,
            "extension_feature": extension_feature,
            "scan_progress_interval": scan_progress_interval,
            "timeout": timeout,
            "icap_headers": icap_headers,
            "respmod_forward_rules": respmod_forward_rules,
        }

        api_field_map = {
            "name": "name",
            "replacemsg_group": "replacemsg-group",
            "comment": "comment",
            "request": "request",
            "response": "response",
            "file_transfer": "file-transfer",
            "streaming_content_bypass": "streaming-content-bypass",
            "ocr_only": "ocr-only",
            "size_limit_204": "204-size-limit",
            "response_204": "204-response",
            "preview": "preview",
            "preview_data_length": "preview-data-length",
            "request_server": "request-server",
            "response_server": "response-server",
            "file_transfer_server": "file-transfer-server",
            "request_failure": "request-failure",
            "response_failure": "response-failure",
            "file_transfer_failure": "file-transfer-failure",
            "request_path": "request-path",
            "response_path": "response-path",
            "file_transfer_path": "file-transfer-path",
            "methods": "methods",
            "response_req_hdr": "response-req-hdr",
            "respmod_default_action": "respmod-default-action",
            "icap_block_log": "icap-block-log",
            "chunk_encap": "chunk-encap",
            "extension_feature": "extension-feature",
            "scan_progress_interval": "scan-progress-interval",
            "timeout": "timeout",
            "icap_headers": "icap-headers",
            "respmod_forward_rules": "respmod-forward-rules",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = "icap/profile"
        return self._client.post("cmdb", path, data=data, vdom=vdom)

    def update(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        replacemsg_group: Optional[str] = None,
        comment: Optional[str] = None,
        request: Optional[str] = None,
        response: Optional[str] = None,
        file_transfer: Optional[str] = None,
        streaming_content_bypass: Optional[str] = None,
        ocr_only: Optional[str] = None,
        size_limit_204: Optional[int] = None,
        response_204: Optional[str] = None,
        preview: Optional[str] = None,
        preview_data_length: Optional[int] = None,
        request_server: Optional[str] = None,
        response_server: Optional[str] = None,
        file_transfer_server: Optional[str] = None,
        request_failure: Optional[str] = None,
        response_failure: Optional[str] = None,
        file_transfer_failure: Optional[str] = None,
        request_path: Optional[str] = None,
        response_path: Optional[str] = None,
        file_transfer_path: Optional[str] = None,
        methods: Optional[str] = None,
        response_req_hdr: Optional[str] = None,
        respmod_default_action: Optional[str] = None,
        icap_block_log: Optional[str] = None,
        chunk_encap: Optional[str] = None,
        extension_feature: Optional[str] = None,
        scan_progress_interval: Optional[int] = None,
        timeout: Optional[int] = None,
        icap_headers: Optional[list[dict[str, Any]]] = None,
        respmod_forward_rules: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update ICAP profile.

        Supports three usage patterns:

        1. Dictionary pattern (template-based):
           >>> config = {'request': 'disable', 'response': 'enable'}
           >>> fgt.api.cmdb.icap.profile.update('web-filter', data_dict=config)

        2. Keyword pattern (explicit parameters):
           >>> fgt.api.cmdb.icap.profile.update(
           ...     'web-filter',
           ...     request='enable',
           ...     response_server='new-server'
           ... )

        3. Mixed pattern (template + overrides):
           >>> base = {'request': 'enable'}
           >>> fgt.api.cmdb.icap.profile.update('web-filter', data_dict=base, response='enable')

        Args:
            name: Profile name
            data_dict: Complete configuration dictionary (pattern 1 & 3)
            replacemsg_group: Replacement message group
            comment: Comment
            request: Enable/disable ICAP request modification (enable/disable)
            response: Enable/disable ICAP response modification (enable/disable)
            file_transfer: File transfer protocols (ssh/ftp)
            streaming_content_bypass: Enable/disable bypassing ICAP for streaming (enable/disable)
            ocr_only: Enable/disable OCR-only content submission (enable/disable)
            size_limit_204: 204 response size limit in MB (1-10)
            response_204: Enable/disable 204 response allowance (enable/disable)
            preview: Enable/disable preview of data (enable/disable)
            preview_data_length: Preview data length (0-4096)
            request_server: ICAP server for HTTP requests
            response_server: ICAP server for HTTP responses
            file_transfer_server: ICAP server for file transfers
            request_failure: Action on request failure (error/bypass)
            response_failure: Action on response failure (error/bypass)
            file_transfer_failure: Action on file transfer failure (error/bypass)
            request_path: ICAP URI path for request processing
            response_path: ICAP URI path for response processing
            file_transfer_path: ICAP URI path for file transfer processing
            methods: HTTP methods to inspect (delete/get/head/options/post/put/trace/connect/other)
            response_req_hdr: Enable/disable req-hdr for respmod (enable/disable)
            respmod_default_action: Default respmod action (forward/bypass)
            icap_block_log: Enable/disable UTM log for infections (enable/disable)
            chunk_encap: Enable/disable chunked encapsulation (enable/disable)
            extension_feature: ICAP extension features (scan-progress)
            scan_progress_interval: Scan progress interval (5-30 seconds)
            timeout: Response timeout (30-3600 seconds)
            icap_headers: ICAP forwarded request headers list
            respmod_forward_rules: ICAP response mode forward rules list
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Update with dictionary
            >>> config = {'request': 'enable', 'response': 'enable', 'timeout': 90}
            >>> result = fgt.api.cmdb.icap.profile.update('web-filter', data_dict=config)

            >>> # Update with keywords
            >>> result = fgt.api.cmdb.icap.profile.update(
            ...     'web-filter',
            ...     request_server='new-icap-server',
            ...     timeout=120
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "replacemsg_group": replacemsg_group,
            "comment": comment,
            "request": request,
            "response": response,
            "file_transfer": file_transfer,
            "streaming_content_bypass": streaming_content_bypass,
            "ocr_only": ocr_only,
            "size_limit_204": size_limit_204,
            "response_204": response_204,
            "preview": preview,
            "preview_data_length": preview_data_length,
            "request_server": request_server,
            "response_server": response_server,
            "file_transfer_server": file_transfer_server,
            "request_failure": request_failure,
            "response_failure": response_failure,
            "file_transfer_failure": file_transfer_failure,
            "request_path": request_path,
            "response_path": response_path,
            "file_transfer_path": file_transfer_path,
            "methods": methods,
            "response_req_hdr": response_req_hdr,
            "respmod_default_action": respmod_default_action,
            "icap_block_log": icap_block_log,
            "chunk_encap": chunk_encap,
            "extension_feature": extension_feature,
            "scan_progress_interval": scan_progress_interval,
            "timeout": timeout,
            "icap_headers": icap_headers,
            "respmod_forward_rules": respmod_forward_rules,
        }

        api_field_map = {
            "replacemsg_group": "replacemsg-group",
            "comment": "comment",
            "request": "request",
            "response": "response",
            "file_transfer": "file-transfer",
            "streaming_content_bypass": "streaming-content-bypass",
            "ocr_only": "ocr-only",
            "size_limit_204": "204-size-limit",
            "response_204": "204-response",
            "preview": "preview",
            "preview_data_length": "preview-data-length",
            "request_server": "request-server",
            "response_server": "response-server",
            "file_transfer_server": "file-transfer-server",
            "request_failure": "request-failure",
            "response_failure": "response-failure",
            "file_transfer_failure": "file-transfer-failure",
            "request_path": "request-path",
            "response_path": "response-path",
            "file_transfer_path": "file-transfer-path",
            "methods": "methods",
            "response_req_hdr": "response-req-hdr",
            "respmod_default_action": "respmod-default-action",
            "icap_block_log": "icap-block-log",
            "chunk_encap": "chunk-encap",
            "extension_feature": "extension-feature",
            "scan_progress_interval": "scan-progress-interval",
            "timeout": "timeout",
            "icap_headers": "icap-headers",
            "respmod_forward_rules": "respmod-forward-rules",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = f"icap/profile/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete ICAP profile.

        Args:
            name: Profile name
            vdom: Virtual domain name or False for global

        Returns:
            Dictionary containing deletion result

        Examples:
            >>> # Delete profile
            >>> result = fgt.api.cmdb.icap.profile.delete('old-profile')
            >>> print(result['status'])
        """
        path = f"icap/profile/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if ICAP profile exists.

        Args:
            name: Profile name
            vdom: Virtual domain name or False for global

        Returns:
            True if profile exists, False otherwise

        Examples:
            >>> # Check if profile exists
            >>> if fgt.api.cmdb.icap.profile.exists('web-filter'):
            ...     print("Profile exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
