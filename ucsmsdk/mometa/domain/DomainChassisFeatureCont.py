"""This module contains the general information for DomainChassisFeatureCont ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class DomainChassisFeatureContConsts:
    pass


class DomainChassisFeatureCont(ManagedObject):
    """This is DomainChassisFeatureCont class."""

    consts = DomainChassisFeatureContConsts()
    naming_props = set([])

    mo_meta = MoMeta("DomainChassisFeatureCont", "domainChassisFeatureCont", "chassis-feature-cont", None, "InputOutput", 0x1f, [], ["admin"], [u'topSystem'], [u'domainChassisFeature', u'domainEnvironmentFeature', u'domainNetworkFeature', u'domainServerFeature', u'domainStorageFeature'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", None, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.flt_aggr = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "DomainChassisFeatureCont", parent_mo_or_dn, **kwargs)
