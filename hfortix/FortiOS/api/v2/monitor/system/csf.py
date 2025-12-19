"""Monitor API - Csf operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class PendingAuthorizations:
    """PendingAuthorizations operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize PendingAuthorizations endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve fabric devices with pending authorizations for joining the Security Fabric.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.csf.pending_authorizations.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/system/csf/pending-authorizations", params=params)


class RegisterAppliance:
    """RegisterAppliance operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize RegisterAppliance endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        type: str | None = None,
        mgmt_ip: str | None = None,
        mgmt_port: int | None = None,
        mgmt_url_parameters: list | None = None,
        serial: str | None = None,
        hostname: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Register appliance to Security Fabric.
        
        Args:
            type: Appliance type (Example: 'faz'). (optional)
            mgmt_ip: Management IP or FQDN. (optional)
            mgmt_port: Management port. (optional)
            mgmt_url_parameters: Array of URL parameters. Each item is a key/value pair. If provided, the URL parameters will be included in the management IP URL. (optional)
            serial: Serial number. (optional)
            hostname: Host name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.csf.register_appliance.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if type is not None:
            data['type'] = type
        if mgmt_ip is not None:
            data['mgmt_ip'] = mgmt_ip
        if mgmt_port is not None:
            data['mgmt_port'] = mgmt_port
        if mgmt_url_parameters is not None:
            data['mgmt_url_parameters'] = mgmt_url_parameters
        if serial is not None:
            data['serial'] = serial
        if hostname is not None:
            data['hostname'] = hostname
        data.update(kwargs)
        return self._client.post("monitor", "/system/csf/register-appliance", data=data)


class Csf:
    """Csf operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Csf endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.pending_authorizations = PendingAuthorizations(client)
        self.register_appliance = RegisterAppliance(client)

    def get(
        self,
        scope: str | None = None,
        all_vdoms: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a full tree of downstream FortiGates registered to the Security Fabric.
        
        Args:
            scope: Scope from which to retrieve the Security Fabric tree [vdom*|global]. (optional)
            all_vdoms: Include information from all VDOMs that the admin can access. Only applies for scope=vdom (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.csf.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params['scope'] = scope
        if all_vdoms is not None:
            params['all_vdoms'] = all_vdoms
        params.update(kwargs)
        return self._client.get("monitor", "/system/csf", params=params)
