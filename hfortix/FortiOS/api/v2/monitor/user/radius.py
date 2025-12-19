"""Monitor API - Radius operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class GetTestConnect:
    """GetTestConnect operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize GetTestConnect endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        ordinal: str | None = None,
        server: str | None = None,
        secret: str | None = None,
        auth_type: str | None = None,
        user: str | None = None,
        password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Test the connectivity of the given RADIUS server and, optionally, the validity of a username & password.
        
        Args:
            mkey: Name of FortiGate's RADIUS object whose settings to test. (optional)
            ordinal: If 'mkey' is provided, the server-secret pair to use from the object: 'primary', 'secondary' or 'tertiary'. Defaults to 'primary'. (optional)
            server: Host name or IP of a RADIUS server. If 'mkey' is provided, this overrides the 'server' value in the object. (optional)
            secret: Secret password for the RADIUS server. If 'mkey' is provided, this overrides the 'secret' value in the object. (optional)
            auth_type: Authentication protocol to use [auto|ms_chap_v2|ms_chap|chap|pap]. If 'mkey' is provided, this overrides the 'auth-type' value in the object. (optional)
            user: User name whose access to check. (optional)
            password: User's password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.radius.get_test_connect.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params['mkey'] = mkey
        if ordinal is not None:
            params['ordinal'] = ordinal
        if server is not None:
            params['server'] = server
        if secret is not None:
            params['secret'] = secret
        if auth_type is not None:
            params['auth_type'] = auth_type
        if user is not None:
            params['user'] = user
        if password is not None:
            params['password'] = password
        params.update(kwargs)
        return self._client.get("monitor", "/user/radius/get-test-connect", params=params)


class TestConnect:
    """TestConnect operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize TestConnect endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        ordinal: str | None = None,
        server: str | None = None,
        secret: str | None = None,
        auth_type: str | None = None,
        user: str | None = None,
        password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Test the connectivity of the given RADIUS server and, optionally, the validity of a username & password.
        
        Args:
            mkey: Name of FortiGate's RADIUS object whose settings to test. (optional)
            ordinal: If 'mkey' is provided, the server-secret pair to use from the object: 'primary', 'secondary' or 'tertiary'. Defaults to 'primary'. (optional)
            server: Host name or IP of a RADIUS server. If 'mkey' is provided, this overrides the 'server' value in the object. (optional)
            secret: Secret password for the RADIUS server. If 'mkey' is provided, this overrides the 'secret' value in the object. (optional)
            auth_type: Authentication protocol to use [auto|ms_chap_v2|ms_chap|chap|pap]. If 'mkey' is provided, this overrides the 'auth-type' value in the object. (optional)
            user: User name whose access to check. (optional)
            password: User's password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.radius.test_connect.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data['mkey'] = mkey
        if ordinal is not None:
            data['ordinal'] = ordinal
        if server is not None:
            data['server'] = server
        if secret is not None:
            data['secret'] = secret
        if auth_type is not None:
            data['auth_type'] = auth_type
        if user is not None:
            data['user'] = user
        if password is not None:
            data['password'] = password
        data.update(kwargs)
        return self._client.post("monitor", "/user/radius/test-connect", data=data)


class Radius:
    """Radius operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Radius endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.get_test_connect = GetTestConnect(client)
        self.test_connect = TestConnect(client)
