"""Firewall convenience wrappers for FortiOS API."""

from .firewallPolicy import FirewallPolicy
from .ipmacBindingSetting import IPMACBindingSetting
from .ipmacBindingTable import IPMACBindingTable
from .scheduleGroup import ScheduleGroup
from .scheduleOnetime import ScheduleOnetime
from .scheduleRecurring import ScheduleRecurring
from .serviceCategory import ServiceCategory
from .serviceCustom import ServiceCustom
from .serviceGroup import ServiceGroup

__all__ = [
    "FirewallPolicy",
    "IPMACBindingSetting",
    "IPMACBindingTable",
    "ScheduleGroup",
    "ScheduleOnetime",
    "ScheduleRecurring",
    "ServiceCategory",
    "ServiceCustom",
    "ServiceGroup",
]
