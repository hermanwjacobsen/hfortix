"""Firewall convenience wrappers for FortiOS API."""

from .firewallPolicy import FirewallPolicy
from .ipmacBindingSetting import IPMACBindingSetting
from .ipmacBindingTable import IPMACBindingTable
from .scheduleGroup import ScheduleGroup
from .scheduleOnetime import ScheduleOnetime
from .scheduleRecurring import ScheduleRecurring

__all__ = [
    "FirewallPolicy",
    "IPMACBindingSetting",
    "IPMACBindingTable",
    "ScheduleGroup",
    "ScheduleOnetime",
    "ScheduleRecurring",
]
