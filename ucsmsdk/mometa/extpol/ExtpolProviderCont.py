"""This module contains the general information for ExtpolProviderCont ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ExtpolProviderContConsts():
    pass


class ExtpolProviderCont(ManagedObject):
    """This is ExtpolProviderCont class."""

    consts = ExtpolProviderContConsts()
    naming_props = set([])

    mo_meta = MoMeta("ExtpolProviderCont", "extpolProviderCont", "providers", VersionMeta.Version211a, "InputOutput", 0x1f, [], ["admin"], [u'extpolRegistry'], [u'extpolProvider'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "gen_num": MoPropertyMeta("gen_num", "genNum", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "genNum": "gen_num", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.gen_num = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ExtpolProviderCont", parent_mo_or_dn, **kwargs)

