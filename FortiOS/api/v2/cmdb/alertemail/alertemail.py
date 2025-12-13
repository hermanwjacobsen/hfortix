"""
FortiOS CMDB - Alert Email Settings
Configure alert email settings

API Endpoints:
    GET  /alertemail/setting - Get alert email settings
    PUT  /alertemail/setting - Update alert email settings
"""


class AlertEmail:
    """Alert Email Settings endpoint"""
    
    def __init__(self, client):
        self._client = client
    
    def get(self, vdom=None):
        """
        GET /alertemail/setting
        Get alert email settings
        
        Args:
            vdom: Virtual domain (optional)
        
        Returns:
            Alert email configuration
        
        Example:
            >>> settings = fgt.cmdb.alertemail.get()
            >>> print(settings['results']['mailto1'])
        """
        return self._client.get('cmdb', 'alertemail/setting', vdom=vdom)
    
    def update(self, 
               username=None,
               mailto1=None, 
               mailto2=None, 
               mailto3=None,
               filter_mode=None,
               email_interval=None,
               severity=None,
               local_disk_usage=None,
               # Log types (enable/disable)
               ips_logs=None,
               firewall_authentication_failure_logs=None,
               ha_logs=None,
               ipsec_errors_logs=None,
               fds_update_logs=None,
               ppp_errors_logs=None,
               antivirus_logs=None,
               webfilter_logs=None,
               configuration_changes_logs=None,
               violation_traffic_logs=None,
               admin_login_logs=None,
               fds_license_expiring_warning=None,
               log_disk_usage_warning=None,
               fortiguard_log_quota_warning=None,
               amc_interface_bypass_mode=None,
               fips_cc_errors=None,
               fsso_disconnect_logs=None,
               ssh_logs=None,
               # Interval settings (minutes)
               emergency_interval=None,
               alert_interval=None,
               critical_interval=None,
               error_interval=None,
               warning_interval=None,
               notification_interval=None,
               information_interval=None,
               debug_interval=None,
               vdom=None,
               **kwargs):
        """
        PUT /alertemail/setting
        Update alert email settings
        
        Args:
            username: Sender name displayed in "From" field (max 63 chars) - NOT for authentication
            mailto1: Primary email address (max 63 chars)
            mailto2: Second email address (max 63 chars)
            mailto3: Third email address (max 63 chars)
            filter_mode: 'category' or 'threshold'
            email_interval: Interval between emails (1-99999 min)
            severity: 'emergency', 'alert', 'critical', 'error', 'warning', 
                     'notification', 'information', 'debug'
            local_disk_usage: Disk usage percentage (1-99%)
            
            Log types (enable/disable):
            ips_logs: Enable/disable IPS logs
            firewall_authentication_failure_logs: Enable/disable auth failure logs
            ha_logs: Enable/disable HA logs
            ipsec_errors_logs: Enable/disable IPsec error logs
            fds_update_logs: Enable/disable FortiGuard update logs
            ppp_errors_logs: Enable/disable PPP error logs
            antivirus_logs: Enable/disable antivirus logs
            webfilter_logs: Enable/disable web filter logs
            configuration_changes_logs: Enable/disable config change logs
            violation_traffic_logs: Enable/disable violation traffic logs
            admin_login_logs: Enable/disable admin login/logout logs
            fds_license_expiring_warning: Enable/disable license expiration warnings
            log_disk_usage_warning: Enable/disable disk usage warnings
            fortiguard_log_quota_warning: Enable/disable FortiCloud quota warnings
            amc_interface_bypass_mode: Enable/disable AMC interface bypass logs
            fips_cc_errors: Enable/disable FIPS and Common Criteria error logs
            fsso_disconnect_logs: Enable/disable FSSO disconnect logs
            ssh_logs: Enable/disable SSH logs
            
            Interval settings (1-99999 minutes):
            emergency_interval: Emergency alert interval
            alert_interval: Alert interval
            critical_interval: Critical alert interval
            error_interval: Error alert interval
            warning_interval: Warning alert interval
            notification_interval: Notification alert interval
            information_interval: Information alert interval
            debug_interval: Debug alert interval
            
            vdom: Virtual domain (optional)
            **kwargs: Any additional parameters
        
        Returns:
            Response dict with status
        
        Examples:
            >>> # Simple update
            >>> fgt.cmdb.alertemail.update(
            ...     mailto1='admin@example.com',
            ...     severity='warning'
            ... )
            
            >>> # Enable specific logs
            >>> fgt.cmdb.alertemail.update(
            ...     ips_logs='enable',
            ...     ha_logs='enable',
            ...     admin_login_logs='enable'
            ... )
            
            >>> # Set intervals
            >>> fgt.cmdb.alertemail.update(
            ...     email_interval=10,
            ...     critical_interval=5,
            ...     warning_interval=30
            ... )
        """
        # Build data dict from provided parameters
        data = {}
        
        # Map Python parameter names to API field names
        param_map = {
            'username': 'username',
            'mailto1': 'mailto1',
            'mailto2': 'mailto2',
            'mailto3': 'mailto3',
            'filter_mode': 'filter-mode',
            'email_interval': 'email-interval',
            'severity': 'severity',
            'local_disk_usage': 'local-disk-usage',
            # Log types
            'ips_logs': 'IPS-logs',
            'firewall_authentication_failure_logs': 'firewall-authentication-failure-logs',
            'ha_logs': 'HA-logs',
            'ipsec_errors_logs': 'IPsec-errors-logs',
            'fds_update_logs': 'FDS-update-logs',
            'ppp_errors_logs': 'PPP-errors-logs',
            'antivirus_logs': 'antivirus-logs',
            'webfilter_logs': 'webfilter-logs',
            'configuration_changes_logs': 'configuration-changes-logs',
            'violation_traffic_logs': 'violation-traffic-logs',
            'admin_login_logs': 'admin-login-logs',
            'fds_license_expiring_warning': 'FDS-license-expiring-warning',
            'log_disk_usage_warning': 'log-disk-usage-warning',
            'fortiguard_log_quota_warning': 'fortiguard-log-quota-warning',
            'amc_interface_bypass_mode': 'amc-interface-bypass-mode',
            'fips_cc_errors': 'FIPS-CC-errors',
            'fsso_disconnect_logs': 'FSSO-disconnect-logs',
            'ssh_logs': 'ssh-logs',
            # Intervals
            'emergency_interval': 'emergency-interval',
            'alert_interval': 'alert-interval',
            'critical_interval': 'critical-interval',
            'error_interval': 'error-interval',
            'warning_interval': 'warning-interval',
            'notification_interval': 'notification-interval',
            'information_interval': 'information-interval',
            'debug_interval': 'debug-interval',
        }
        
        # Add all non-None parameters to data dict
        for param_name, api_name in param_map.items():
            value = locals().get(param_name)
            if value is not None:
                data[api_name] = value
        
        # Add any extra kwargs
        data.update(kwargs)
        
        return self._client.put('cmdb', 'alertemail/setting', data, vdom=vdom)
    
    # Backward compatibility aliases
    get_setting = get
    update_setting = lambda self, data, vdom=None: self._client.put('cmdb', 'alertemail/setting', data, vdom=vdom)
