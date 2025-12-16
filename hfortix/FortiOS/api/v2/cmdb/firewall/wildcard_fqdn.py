"""
FortiOS firewall.wildcard-fqdn sub-category.

Provides access to wildcard FQDN address configuration endpoints.
"""


class WildcardFqdn:
    """
    Wildcard FQDN address configuration sub-category.

    This class provides access to wildcard FQDN address endpoints through
    property methods that lazy-load the corresponding endpoint modules.

    Usage:
        fgt.cmdb.firewall.wildcard_fqdn.custom.list()
        fgt.cmdb.firewall.wildcard_fqdn.group.list()
    """

    def __init__(self, client):
        self._client = client
        self._custom = None
        self._group = None

    @property
    def custom(self):
        """
        Access the wildcard FQDN custom addresses endpoint.

        Returns:
            Custom: Wildcard FQDN custom addresses endpoint instance

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.list()
        """
        if self._custom is None:
            from .wildcard_fqdn_custom import Custom

            self._custom = Custom(self._client)
        return self._custom

    @property
    def group(self):
        """
        Access the wildcard FQDN address groups endpoint.

        Returns:
            Group: Wildcard FQDN groups endpoint instance

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.list()
        """
        if self._group is None:
            from .wildcard_fqdn_group import Group

            self._group = Group(self._client)
        return self._group
