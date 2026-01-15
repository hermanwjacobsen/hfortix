from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for icap/profile payload fields.
    
    Configure ICAP profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.icap.server.ServerEndpoint` (via: file-transfer-server, request-server, response-server)
        - :class:`~.icap.server-group.ServerGroupEndpoint` (via: file-transfer-server, request-server, response-server)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    name: str  # ICAP profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    request: Literal["disable", "enable"]  # Enable/disable whether an HTTP request is passed t | Default: disable
    response: Literal["disable", "enable"]  # Enable/disable whether an HTTP response is passed | Default: disable
    file_transfer: Literal["ssh", "ftp"]  # Configure the file transfer protocols to pass tran
    streaming_content_bypass: Literal["disable", "enable"]  # Enable/disable bypassing of ICAP server for stream | Default: disable
    ocr_only: Literal["disable", "enable"]  # Enable/disable this FortiGate unit to submit only | Default: disable
    size_limit_204: int  # 204 response size limit to be saved by ICAP client | Default: 1 | Min: 1 | Max: 10
    response_204: Literal["disable", "enable"]  # Enable/disable allowance of 204 response from ICAP | Default: disable
    preview: Literal["disable", "enable"]  # Enable/disable preview of data to ICAP server. | Default: disable
    preview_data_length: int  # Preview data length to be sent to ICAP server. | Default: 0 | Min: 0 | Max: 4096
    request_server: str  # ICAP server to use for an HTTP request. | MaxLen: 63
    response_server: str  # ICAP server to use for an HTTP response. | MaxLen: 63
    file_transfer_server: str  # ICAP server to use for a file transfer. | MaxLen: 63
    request_failure: Literal["error", "bypass"]  # Action to take if the ICAP server cannot be contac | Default: error
    response_failure: Literal["error", "bypass"]  # Action to take if the ICAP server cannot be contac | Default: error
    file_transfer_failure: Literal["error", "bypass"]  # Action to take if the ICAP server cannot be contac | Default: error
    request_path: str  # Path component of the ICAP URI that identifies the | MaxLen: 127
    response_path: str  # Path component of the ICAP URI that identifies the | MaxLen: 127
    file_transfer_path: str  # Path component of the ICAP URI that identifies the | MaxLen: 127
    methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"]  # The allowed HTTP methods that will be sent to ICAP | Default: delete get head options post put trace connect other
    response_req_hdr: Literal["disable", "enable"]  # Enable/disable addition of req-hdr for ICAP respon | Default: enable
    respmod_default_action: Literal["forward", "bypass"]  # Default action to ICAP response modification | Default: forward
    icap_block_log: Literal["disable", "enable"]  # Enable/disable UTM log when infection found | Default: disable
    chunk_encap: Literal["disable", "enable"]  # Enable/disable chunked encapsulation | Default: disable
    extension_feature: Literal["scan-progress"]  # Enable/disable ICAP extension features.
    scan_progress_interval: int  # Scan progress interval value. | Default: 10 | Min: 5 | Max: 30
    timeout: int  # Time (in seconds) that ICAP client waits for the r | Default: 30 | Min: 30 | Max: 3600
    icap_headers: list[dict[str, Any]]  # Configure ICAP forwarded request headers.
    respmod_forward_rules: list[dict[str, Any]]  # ICAP response mode forward rules.

# Nested TypedDicts for table field children (dict mode)

class ProfileIcapheadersItem(TypedDict):
    """Type hints for icap-headers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # HTTP forwarded header ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # HTTP forwarded header name. | MaxLen: 79
    content: str  # HTTP header content. | MaxLen: 255
    base64_encoding: Literal["disable", "enable"]  # Enable/disable use of base64 encoding of HTTP cont | Default: disable


class ProfileRespmodforwardrulesItem(TypedDict):
    """Type hints for respmod-forward-rules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 63
    host: str  # Address object for the host. | MaxLen: 79
    header_group: str  # HTTP header group.
    action: Literal["forward", "bypass"]  # Action to be taken for ICAP server. | Default: forward
    http_resp_status_code: str  # HTTP response status code.


# Nested classes for table field children (object mode)

@final
class ProfileIcapheadersObject:
    """Typed object for icap-headers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # HTTP forwarded header ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # HTTP forwarded header name. | MaxLen: 79
    name: str
    # HTTP header content. | MaxLen: 255
    content: str
    # Enable/disable use of base64 encoding of HTTP content. | Default: disable
    base64_encoding: Literal["disable", "enable"]
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class ProfileRespmodforwardrulesObject:
    """Typed object for respmod-forward-rules table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 63
    name: str
    # Address object for the host. | MaxLen: 79
    host: str
    # HTTP header group.
    header_group: str
    # Action to be taken for ICAP server. | Default: forward
    action: Literal["forward", "bypass"]
    # HTTP response status code.
    http_resp_status_code: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for icap/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    name: str  # ICAP profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    request: Literal["disable", "enable"]  # Enable/disable whether an HTTP request is passed t | Default: disable
    response: Literal["disable", "enable"]  # Enable/disable whether an HTTP response is passed | Default: disable
    file_transfer: Literal["ssh", "ftp"]  # Configure the file transfer protocols to pass tran
    streaming_content_bypass: Literal["disable", "enable"]  # Enable/disable bypassing of ICAP server for stream | Default: disable
    ocr_only: Literal["disable", "enable"]  # Enable/disable this FortiGate unit to submit only | Default: disable
    size_limit_204: int  # 204 response size limit to be saved by ICAP client | Default: 1 | Min: 1 | Max: 10
    response_204: Literal["disable", "enable"]  # Enable/disable allowance of 204 response from ICAP | Default: disable
    preview: Literal["disable", "enable"]  # Enable/disable preview of data to ICAP server. | Default: disable
    preview_data_length: int  # Preview data length to be sent to ICAP server. | Default: 0 | Min: 0 | Max: 4096
    request_server: str  # ICAP server to use for an HTTP request. | MaxLen: 63
    response_server: str  # ICAP server to use for an HTTP response. | MaxLen: 63
    file_transfer_server: str  # ICAP server to use for a file transfer. | MaxLen: 63
    request_failure: Literal["error", "bypass"]  # Action to take if the ICAP server cannot be contac | Default: error
    response_failure: Literal["error", "bypass"]  # Action to take if the ICAP server cannot be contac | Default: error
    file_transfer_failure: Literal["error", "bypass"]  # Action to take if the ICAP server cannot be contac | Default: error
    request_path: str  # Path component of the ICAP URI that identifies the | MaxLen: 127
    response_path: str  # Path component of the ICAP URI that identifies the | MaxLen: 127
    file_transfer_path: str  # Path component of the ICAP URI that identifies the | MaxLen: 127
    methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"]  # The allowed HTTP methods that will be sent to ICAP | Default: delete get head options post put trace connect other
    response_req_hdr: Literal["disable", "enable"]  # Enable/disable addition of req-hdr for ICAP respon | Default: enable
    respmod_default_action: Literal["forward", "bypass"]  # Default action to ICAP response modification | Default: forward
    icap_block_log: Literal["disable", "enable"]  # Enable/disable UTM log when infection found | Default: disable
    chunk_encap: Literal["disable", "enable"]  # Enable/disable chunked encapsulation | Default: disable
    extension_feature: Literal["scan-progress"]  # Enable/disable ICAP extension features.
    scan_progress_interval: int  # Scan progress interval value. | Default: 10 | Min: 5 | Max: 30
    timeout: int  # Time (in seconds) that ICAP client waits for the r | Default: 30 | Min: 30 | Max: 3600
    icap_headers: list[ProfileIcapheadersItem]  # Configure ICAP forwarded request headers.
    respmod_forward_rules: list[ProfileRespmodforwardrulesItem]  # ICAP response mode forward rules.


@final
class ProfileObject:
    """Typed FortiObject for icap/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Replacement message group. | MaxLen: 35
    replacemsg_group: str
    # ICAP profile name. | MaxLen: 47
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Enable/disable whether an HTTP request is passed to an ICAP | Default: disable
    request: Literal["disable", "enable"]
    # Enable/disable whether an HTTP response is passed to an ICAP | Default: disable
    response: Literal["disable", "enable"]
    # Configure the file transfer protocols to pass transferred fi
    file_transfer: Literal["ssh", "ftp"]
    # Enable/disable bypassing of ICAP server for streaming conten | Default: disable
    streaming_content_bypass: Literal["disable", "enable"]
    # Enable/disable this FortiGate unit to submit only OCR intere | Default: disable
    ocr_only: Literal["disable", "enable"]
    # 204 response size limit to be saved by ICAP client in megaby | Default: 1 | Min: 1 | Max: 10
    size_limit_204: int
    # Enable/disable allowance of 204 response from ICAP server. | Default: disable
    response_204: Literal["disable", "enable"]
    # Enable/disable preview of data to ICAP server. | Default: disable
    preview: Literal["disable", "enable"]
    # Preview data length to be sent to ICAP server. | Default: 0 | Min: 0 | Max: 4096
    preview_data_length: int
    # ICAP server to use for an HTTP request. | MaxLen: 63
    request_server: str
    # ICAP server to use for an HTTP response. | MaxLen: 63
    response_server: str
    # ICAP server to use for a file transfer. | MaxLen: 63
    file_transfer_server: str
    # Action to take if the ICAP server cannot be contacted when p | Default: error
    request_failure: Literal["error", "bypass"]
    # Action to take if the ICAP server cannot be contacted when p | Default: error
    response_failure: Literal["error", "bypass"]
    # Action to take if the ICAP server cannot be contacted when p | Default: error
    file_transfer_failure: Literal["error", "bypass"]
    # Path component of the ICAP URI that identifies the HTTP requ | MaxLen: 127
    request_path: str
    # Path component of the ICAP URI that identifies the HTTP resp | MaxLen: 127
    response_path: str
    # Path component of the ICAP URI that identifies the file tran | MaxLen: 127
    file_transfer_path: str
    # The allowed HTTP methods that will be sent to ICAP server fo | Default: delete get head options post put trace connect other
    methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"]
    # Enable/disable addition of req-hdr for ICAP response modific | Default: enable
    response_req_hdr: Literal["disable", "enable"]
    # Default action to ICAP response modification (respmod) proce | Default: forward
    respmod_default_action: Literal["forward", "bypass"]
    # Enable/disable UTM log when infection found | Default: disable
    icap_block_log: Literal["disable", "enable"]
    # Enable/disable chunked encapsulation (default = disable). | Default: disable
    chunk_encap: Literal["disable", "enable"]
    # Enable/disable ICAP extension features.
    extension_feature: Literal["scan-progress"]
    # Scan progress interval value. | Default: 10 | Min: 5 | Max: 30
    scan_progress_interval: int
    # Time (in seconds) that ICAP client waits for the response fr | Default: 30 | Min: 30 | Max: 3600
    timeout: int
    # Configure ICAP forwarded request headers.
    icap_headers: list[ProfileIcapheadersObject]
    # ICAP response mode forward rules.
    respmod_forward_rules: list[ProfileRespmodforwardrulesObject]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Configure ICAP profiles.
    
    Path: icap/profile
    Category: cmdb
    Primary Key: name
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ProfileObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ProfileObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ProfileObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProfilePayload | None = ...,
        replacemsg_group: str | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        request: Literal["disable", "enable"] | None = ...,
        response: Literal["disable", "enable"] | None = ...,
        file_transfer: Literal["ssh", "ftp"] | list[str] | None = ...,
        streaming_content_bypass: Literal["disable", "enable"] | None = ...,
        ocr_only: Literal["disable", "enable"] | None = ...,
        size_limit_204: int | None = ...,
        response_204: Literal["disable", "enable"] | None = ...,
        preview: Literal["disable", "enable"] | None = ...,
        preview_data_length: int | None = ...,
        request_server: str | None = ...,
        response_server: str | None = ...,
        file_transfer_server: str | None = ...,
        request_failure: Literal["error", "bypass"] | None = ...,
        response_failure: Literal["error", "bypass"] | None = ...,
        file_transfer_failure: Literal["error", "bypass"] | None = ...,
        request_path: str | None = ...,
        response_path: str | None = ...,
        file_transfer_path: str | None = ...,
        methods: Literal["delete", "get", "head", "options", "post", "put", "trace", "connect", "other"] | list[str] | None = ...,
        response_req_hdr: Literal["disable", "enable"] | None = ...,
        respmod_default_action: Literal["forward", "bypass"] | None = ...,
        icap_block_log: Literal["disable", "enable"] | None = ...,
        chunk_encap: Literal["disable", "enable"] | None = ...,
        extension_feature: Literal["scan-progress"] | list[str] | None = ...,
        scan_progress_interval: int | None = ...,
        timeout: int | None = ...,
        icap_headers: str | list[str] | list[dict[str, Any]] | None = ...,
        respmod_forward_rules: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Profile",
    "ProfilePayload",
    "ProfileResponse",
    "ProfileObject",
]