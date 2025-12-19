"""
FortiOS CMDB - Vpn CertificateHsmLocal

API Endpoints:
    GET    /vpn.certificate/hsm-local
    POST   /vpn.certificate/hsm-local
    GET    /vpn.certificate/hsm-local/{name}
    PUT    /vpn.certificate/hsm-local/{name}
    DELETE /vpn.certificate/hsm-local/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class CertificateHsmLocal:
    """CertificateHsmLocal operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CertificateHsmLocal endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if name:
            endpoint = f"/vpn.certificate/hsm-local/{name}"
        else:
            endpoint = "/vpn.certificate/hsm-local"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        comments: str | None = None,
        vendor: str | None = None,
        api_version: str | None = None,
        certificate: str | None = None,
        range: str | None = None,
        source: str | None = None,
        gch_url: str | None = None,
        gch_project: str | None = None,
        gch_location: str | None = None,
        gch_keyring: str | None = None,
        gch_cryptokey: str | None = None,
        gch_cryptokey_version: str | None = None,
        gch_cloud_service_name: str | None = None,
        gch_cryptokey_algorithm: str | None = None,
        details: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: Name. (optional)
            comments: Comment. (optional)
            vendor: HSM vendor. (optional)
            api_version: API version for communicating with HSM. (optional)
            certificate: PEM format certificate. (optional)
            range: Either a global or VDOM IP address range for the certificate. (optional)
            source: Certificate source type. (optional)
            gch_url: Google Cloud HSM key URL (e.g. "https://cloudkms.googleapis.com/v1/projects/sampleproject/locations/samplelocation/keyRings/samplekeyring/cryptoKeys/sampleKeyName/cryptoKeyVersions/1"). (optional)
            gch_project: Google Cloud HSM project ID. (optional)
            gch_location: Google Cloud HSM location. (optional)
            gch_keyring: Google Cloud HSM keyring. (optional)
            gch_cryptokey: Google Cloud HSM cryptokey. (optional)
            gch_cryptokey_version: Google Cloud HSM cryptokey version. (optional)
            gch_cloud_service_name: Cloud service config name to generate access token. (optional)
            gch_cryptokey_algorithm: Google Cloud HSM cryptokey algorithm. (optional)
            details: Print hsm-local certificate detailed information. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/vpn.certificate/hsm-local/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if comments is not None:
            data_payload['comments'] = comments
        if vendor is not None:
            data_payload['vendor'] = vendor
        if api_version is not None:
            data_payload['api-version'] = api_version
        if certificate is not None:
            data_payload['certificate'] = certificate
        if range is not None:
            data_payload['range'] = range
        if source is not None:
            data_payload['source'] = source
        if gch_url is not None:
            data_payload['gch-url'] = gch_url
        if gch_project is not None:
            data_payload['gch-project'] = gch_project
        if gch_location is not None:
            data_payload['gch-location'] = gch_location
        if gch_keyring is not None:
            data_payload['gch-keyring'] = gch_keyring
        if gch_cryptokey is not None:
            data_payload['gch-cryptokey'] = gch_cryptokey
        if gch_cryptokey_version is not None:
            data_payload['gch-cryptokey-version'] = gch_cryptokey_version
        if gch_cloud_service_name is not None:
            data_payload['gch-cloud-service-name'] = gch_cloud_service_name
        if gch_cryptokey_algorithm is not None:
            data_payload['gch-cryptokey-algorithm'] = gch_cryptokey_algorithm
        if details is not None:
            data_payload['details'] = details
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/vpn.certificate/hsm-local/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comments: str | None = None,
        vendor: str | None = None,
        api_version: str | None = None,
        certificate: str | None = None,
        range: str | None = None,
        source: str | None = None,
        gch_url: str | None = None,
        gch_project: str | None = None,
        gch_location: str | None = None,
        gch_keyring: str | None = None,
        gch_cryptokey: str | None = None,
        gch_cryptokey_version: str | None = None,
        gch_cloud_service_name: str | None = None,
        gch_cryptokey_algorithm: str | None = None,
        details: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Name. (optional)
            comments: Comment. (optional)
            vendor: HSM vendor. (optional)
            api_version: API version for communicating with HSM. (optional)
            certificate: PEM format certificate. (optional)
            range: Either a global or VDOM IP address range for the certificate. (optional)
            source: Certificate source type. (optional)
            gch_url: Google Cloud HSM key URL (e.g. "https://cloudkms.googleapis.com/v1/projects/sampleproject/locations/samplelocation/keyRings/samplekeyring/cryptoKeys/sampleKeyName/cryptoKeyVersions/1"). (optional)
            gch_project: Google Cloud HSM project ID. (optional)
            gch_location: Google Cloud HSM location. (optional)
            gch_keyring: Google Cloud HSM keyring. (optional)
            gch_cryptokey: Google Cloud HSM cryptokey. (optional)
            gch_cryptokey_version: Google Cloud HSM cryptokey version. (optional)
            gch_cloud_service_name: Cloud service config name to generate access token. (optional)
            gch_cryptokey_algorithm: Google Cloud HSM cryptokey algorithm. (optional)
            details: Print hsm-local certificate detailed information. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/vpn.certificate/hsm-local"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if comments is not None:
            data_payload['comments'] = comments
        if vendor is not None:
            data_payload['vendor'] = vendor
        if api_version is not None:
            data_payload['api-version'] = api_version
        if certificate is not None:
            data_payload['certificate'] = certificate
        if range is not None:
            data_payload['range'] = range
        if source is not None:
            data_payload['source'] = source
        if gch_url is not None:
            data_payload['gch-url'] = gch_url
        if gch_project is not None:
            data_payload['gch-project'] = gch_project
        if gch_location is not None:
            data_payload['gch-location'] = gch_location
        if gch_keyring is not None:
            data_payload['gch-keyring'] = gch_keyring
        if gch_cryptokey is not None:
            data_payload['gch-cryptokey'] = gch_cryptokey
        if gch_cryptokey_version is not None:
            data_payload['gch-cryptokey-version'] = gch_cryptokey_version
        if gch_cloud_service_name is not None:
            data_payload['gch-cloud-service-name'] = gch_cloud_service_name
        if gch_cryptokey_algorithm is not None:
            data_payload['gch-cryptokey-algorithm'] = gch_cryptokey_algorithm
        if details is not None:
            data_payload['details'] = details
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
