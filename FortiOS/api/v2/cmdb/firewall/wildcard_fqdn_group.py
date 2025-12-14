"""
FortiOS API endpoint: firewall.wildcard-fqdn/group

Config global Wildcard FQDN address groups.
"""


class Group:
    """
    Manage wildcard FQDN address groups.
    
    Groups can contain multiple wildcard FQDN addresses for use in firewall policies.
    
    API Path: firewall.wildcard-fqdn/group
    """
    
    def __init__(self, client):
        """
        Initialize the Group endpoint.
        
        Args:
            client: FortiOS API client instance
        """
        self._client = client
    
    def list(self, vdom=None, **params):
        """
        Get list of wildcard FQDN groups.
        
        Args:
            vdom (str, optional): Virtual domain name
            **params: Additional query parameters (filter, format, etc.)
            
        Returns:
            dict: API response with list of groups
            
        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.list()
        """
        return self._client.get('cmdb', 'firewall.wildcard-fqdn/group', vdom=vdom, params=params)
    
    def get(self, name: str, vdom=None, **params):
        """
        Get a specific wildcard FQDN group.
        
        Args:
            name (str): Group name
            vdom (str, optional): Virtual domain name
            **params: Additional query parameters
            
        Returns:
            dict: API response with group details
            
        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.get('example-group')
        """
        return self._client.get('cmdb', f'firewall.wildcard-fqdn/group/{name}', vdom=vdom, params=params)
    
    def create(
        self,
        name: str,
        member: list = None,
        color: int = None,
        comment: str = None,
        visibility: str = None,
        uuid: str = None,
        vdom=None
    ):
        """
        Create a new wildcard FQDN group.
        
        Args:
            name (str): Group name
            member (list): List of wildcard FQDN address names (list of dicts with 'name' key)
            color (int): Color code (0-32, default 0)
            comment (str): Comment
            visibility (str): Enable/disable visibility: enable, disable
            uuid (str): Universally Unique Identifier (UUID)
            vdom (str, optional): Virtual domain name
            
        Returns:
            dict: API response
            
        Example:
            # Create group with members
            result = fgt.cmdb.firewall.wildcard_fqdn.group.create(
                'web-wildcards',
                member=[
                    {'name': '*.example.com'},
                    {'name': '*.test.com'}
                ],
                comment='Wildcard FQDN group for web domains'
            )
        """
        data = {'name': name}
        
        if member is not None:
            data['member'] = member
        if color is not None:
            data['color'] = color
        if comment is not None:
            data['comment'] = comment
        if visibility is not None:
            data['visibility'] = visibility
        if uuid is not None:
            data['uuid'] = uuid
        
        return self._client.post('cmdb', 'firewall.wildcard-fqdn/group', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        member: list = None,
        color: int = None,
        comment: str = None,
        visibility: str = None,
        uuid: str = None,
        vdom=None
    ):
        """
        Update an existing wildcard FQDN group.
        
        Args:
            name (str): Group name
            member (list): List of wildcard FQDN address names (list of dicts with 'name' key)
            color (int): Color code (0-32)
            comment (str): Comment
            visibility (str): Enable/disable visibility: enable, disable
            uuid (str): Universally Unique Identifier (UUID)
            vdom (str, optional): Virtual domain name
            
        Returns:
            dict: API response
            
        Example:
            # Update members
            result = fgt.cmdb.firewall.wildcard_fqdn.group.update(
                'web-wildcards',
                member=[
                    {'name': '*.example.com'},
                    {'name': '*.test.com'},
                    {'name': '*.newdomain.com'}
                ]
            )
        """
        data = {}
        
        if member is not None:
            data['member'] = member
        if color is not None:
            data['color'] = color
        if comment is not None:
            data['comment'] = comment
        if visibility is not None:
            data['visibility'] = visibility
        if uuid is not None:
            data['uuid'] = uuid
        
        return self._client.put('cmdb', f'firewall.wildcard-fqdn/group/{name}', data, vdom=vdom)
    
    def delete(self, name: str, vdom=None):
        """
        Delete a wildcard FQDN group.
        
        Args:
            name (str): Group name
            vdom (str, optional): Virtual domain name
            
        Returns:
            dict: API response
            
        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.delete('web-wildcards')
        """
        return self._client.delete('cmdb', f'firewall.wildcard-fqdn/group/{name}', vdom=vdom)
    
    def exists(self, name: str, vdom=None):
        """
        Check if a wildcard FQDN group exists.
        
        Args:
            name (str): Group name
            vdom (str, optional): Virtual domain name
            
        Returns:
            bool: True if group exists, False otherwise
            
        Example:
            if fgt.cmdb.firewall.wildcard_fqdn.group.exists('web-wildcards'):
                print("Group exists")
        """
        try:
            result = self.get(name, vdom=vdom)
            return result.get('status') == 'success' and len(result.get('results', [])) > 0
        except Exception:
            return False
