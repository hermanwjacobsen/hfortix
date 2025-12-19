"""
FortiOS CMDB - Firewall Sniffer

API Endpoints:
    GET    /firewall/sniffer
    POST   /firewall/sniffer
    GET    /firewall/sniffer/{id}
    PUT    /firewall/sniffer/{id}
    DELETE /firewall/sniffer/{id}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Sniffer:
    """Sniffer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Sniffer endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/firewall/sniffer/{id}"
        else:
            endpoint = "/firewall/sniffer"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        status: str | None = None,
        logtraffic: str | None = None,
        ipv6: str | None = None,
        non_ip: str | None = None,
        interface: str | None = None,
        host: str | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None,
        application_list_status: str | None = None,
        application_list: str | None = None,
        ips_sensor_status: str | None = None,
        ips_sensor: str | None = None,
        dsri: str | None = None,
        av_profile_status: str | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: str | None = None,
        webfilter_profile: str | None = None,
        emailfilter_profile_status: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: str | None = None,
        dlp_profile: str | None = None,
        ip_threatfeed_status: str | None = None,
        ip_threatfeed: list | None = None,
        file_filter_profile_status: str | None = None,
        file_filter_profile: str | None = None,
        ips_dos_status: str | None = None,
        anomaly: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            id: Sniffer ID (0 - 9999). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            status: Enable/disable the active status of the sniffer. (optional)
            logtraffic: Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy. (optional)
            ipv6: Enable/disable sniffing IPv6 packets. (optional)
            non_ip: Enable/disable sniffing non-IP packets. (optional)
            interface: Interface name that traffic sniffing will take place on. (optional)
            host: Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240). (optional)
            port: Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200). (optional)
            protocol: Integer value for the protocol type as defined by IANA (0 - 255). (optional)
            vlan: List of VLANs to sniff. (optional)
            application_list_status: Enable/disable application control profile. (optional)
            application_list: Name of an existing application list. (optional)
            ips_sensor_status: Enable/disable IPS sensor. (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            dsri: Enable/disable DSRI. (optional)
            av_profile_status: Enable/disable antivirus profile. (optional)
            av_profile: Name of an existing antivirus profile. (optional)
            webfilter_profile_status: Enable/disable web filter profile. (optional)
            webfilter_profile: Name of an existing web filter profile. (optional)
            emailfilter_profile_status: Enable/disable emailfilter. (optional)
            emailfilter_profile: Name of an existing email filter profile. (optional)
            dlp_profile_status: Enable/disable DLP profile. (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            ip_threatfeed_status: Enable/disable IP threat feed. (optional)
            ip_threatfeed: Name of an existing IP threat feed. (optional)
            file_filter_profile_status: Enable/disable file filter. (optional)
            file_filter_profile: Name of an existing file-filter profile. (optional)
            ips_dos_status: Enable/disable IPS DoS anomaly detection. (optional)
            anomaly: Configuration method to edit Denial of Service (DoS) anomaly settings. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/firewall/sniffer/{id}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if id is not None:
            data_payload['id'] = id
        if uuid is not None:
            data_payload['uuid'] = uuid
        if status is not None:
            data_payload['status'] = status
        if logtraffic is not None:
            data_payload['logtraffic'] = logtraffic
        if ipv6 is not None:
            data_payload['ipv6'] = ipv6
        if non_ip is not None:
            data_payload['non-ip'] = non_ip
        if interface is not None:
            data_payload['interface'] = interface
        if host is not None:
            data_payload['host'] = host
        if port is not None:
            data_payload['port'] = port
        if protocol is not None:
            data_payload['protocol'] = protocol
        if vlan is not None:
            data_payload['vlan'] = vlan
        if application_list_status is not None:
            data_payload['application-list-status'] = application_list_status
        if application_list is not None:
            data_payload['application-list'] = application_list
        if ips_sensor_status is not None:
            data_payload['ips-sensor-status'] = ips_sensor_status
        if ips_sensor is not None:
            data_payload['ips-sensor'] = ips_sensor
        if dsri is not None:
            data_payload['dsri'] = dsri
        if av_profile_status is not None:
            data_payload['av-profile-status'] = av_profile_status
        if av_profile is not None:
            data_payload['av-profile'] = av_profile
        if webfilter_profile_status is not None:
            data_payload['webfilter-profile-status'] = webfilter_profile_status
        if webfilter_profile is not None:
            data_payload['webfilter-profile'] = webfilter_profile
        if emailfilter_profile_status is not None:
            data_payload['emailfilter-profile-status'] = emailfilter_profile_status
        if emailfilter_profile is not None:
            data_payload['emailfilter-profile'] = emailfilter_profile
        if dlp_profile_status is not None:
            data_payload['dlp-profile-status'] = dlp_profile_status
        if dlp_profile is not None:
            data_payload['dlp-profile'] = dlp_profile
        if ip_threatfeed_status is not None:
            data_payload['ip-threatfeed-status'] = ip_threatfeed_status
        if ip_threatfeed is not None:
            data_payload['ip-threatfeed'] = ip_threatfeed
        if file_filter_profile_status is not None:
            data_payload['file-filter-profile-status'] = file_filter_profile_status
        if file_filter_profile is not None:
            data_payload['file-filter-profile'] = file_filter_profile
        if ips_dos_status is not None:
            data_payload['ips-dos-status'] = ips_dos_status
        if anomaly is not None:
            data_payload['anomaly'] = anomaly
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/firewall/sniffer/{id}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        status: str | None = None,
        logtraffic: str | None = None,
        ipv6: str | None = None,
        non_ip: str | None = None,
        interface: str | None = None,
        host: str | None = None,
        port: str | None = None,
        protocol: str | None = None,
        vlan: str | None = None,
        application_list_status: str | None = None,
        application_list: str | None = None,
        ips_sensor_status: str | None = None,
        ips_sensor: str | None = None,
        dsri: str | None = None,
        av_profile_status: str | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: str | None = None,
        webfilter_profile: str | None = None,
        emailfilter_profile_status: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: str | None = None,
        dlp_profile: str | None = None,
        ip_threatfeed_status: str | None = None,
        ip_threatfeed: list | None = None,
        file_filter_profile_status: str | None = None,
        file_filter_profile: str | None = None,
        ips_dos_status: str | None = None,
        anomaly: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            id: Sniffer ID (0 - 9999). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset). (optional)
            status: Enable/disable the active status of the sniffer. (optional)
            logtraffic: Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy. (optional)
            ipv6: Enable/disable sniffing IPv6 packets. (optional)
            non_ip: Enable/disable sniffing non-IP packets. (optional)
            interface: Interface name that traffic sniffing will take place on. (optional)
            host: Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240). (optional)
            port: Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200). (optional)
            protocol: Integer value for the protocol type as defined by IANA (0 - 255). (optional)
            vlan: List of VLANs to sniff. (optional)
            application_list_status: Enable/disable application control profile. (optional)
            application_list: Name of an existing application list. (optional)
            ips_sensor_status: Enable/disable IPS sensor. (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            dsri: Enable/disable DSRI. (optional)
            av_profile_status: Enable/disable antivirus profile. (optional)
            av_profile: Name of an existing antivirus profile. (optional)
            webfilter_profile_status: Enable/disable web filter profile. (optional)
            webfilter_profile: Name of an existing web filter profile. (optional)
            emailfilter_profile_status: Enable/disable emailfilter. (optional)
            emailfilter_profile: Name of an existing email filter profile. (optional)
            dlp_profile_status: Enable/disable DLP profile. (optional)
            dlp_profile: Name of an existing DLP profile. (optional)
            ip_threatfeed_status: Enable/disable IP threat feed. (optional)
            ip_threatfeed: Name of an existing IP threat feed. (optional)
            file_filter_profile_status: Enable/disable file filter. (optional)
            file_filter_profile: Name of an existing file-filter profile. (optional)
            ips_dos_status: Enable/disable IPS DoS anomaly detection. (optional)
            anomaly: Configuration method to edit Denial of Service (DoS) anomaly settings. (optional)
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
        endpoint = "/firewall/sniffer"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if id is not None:
            data_payload['id'] = id
        if uuid is not None:
            data_payload['uuid'] = uuid
        if status is not None:
            data_payload['status'] = status
        if logtraffic is not None:
            data_payload['logtraffic'] = logtraffic
        if ipv6 is not None:
            data_payload['ipv6'] = ipv6
        if non_ip is not None:
            data_payload['non-ip'] = non_ip
        if interface is not None:
            data_payload['interface'] = interface
        if host is not None:
            data_payload['host'] = host
        if port is not None:
            data_payload['port'] = port
        if protocol is not None:
            data_payload['protocol'] = protocol
        if vlan is not None:
            data_payload['vlan'] = vlan
        if application_list_status is not None:
            data_payload['application-list-status'] = application_list_status
        if application_list is not None:
            data_payload['application-list'] = application_list
        if ips_sensor_status is not None:
            data_payload['ips-sensor-status'] = ips_sensor_status
        if ips_sensor is not None:
            data_payload['ips-sensor'] = ips_sensor
        if dsri is not None:
            data_payload['dsri'] = dsri
        if av_profile_status is not None:
            data_payload['av-profile-status'] = av_profile_status
        if av_profile is not None:
            data_payload['av-profile'] = av_profile
        if webfilter_profile_status is not None:
            data_payload['webfilter-profile-status'] = webfilter_profile_status
        if webfilter_profile is not None:
            data_payload['webfilter-profile'] = webfilter_profile
        if emailfilter_profile_status is not None:
            data_payload['emailfilter-profile-status'] = emailfilter_profile_status
        if emailfilter_profile is not None:
            data_payload['emailfilter-profile'] = emailfilter_profile
        if dlp_profile_status is not None:
            data_payload['dlp-profile-status'] = dlp_profile_status
        if dlp_profile is not None:
            data_payload['dlp-profile'] = dlp_profile
        if ip_threatfeed_status is not None:
            data_payload['ip-threatfeed-status'] = ip_threatfeed_status
        if ip_threatfeed is not None:
            data_payload['ip-threatfeed'] = ip_threatfeed
        if file_filter_profile_status is not None:
            data_payload['file-filter-profile-status'] = file_filter_profile_status
        if file_filter_profile is not None:
            data_payload['file-filter-profile'] = file_filter_profile
        if ips_dos_status is not None:
            data_payload['ips-dos-status'] = ips_dos_status
        if anomaly is not None:
            data_payload['anomaly'] = anomaly
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
