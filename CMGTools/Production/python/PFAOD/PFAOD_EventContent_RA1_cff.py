
import FWCore.ParameterSet.Config as cms
from CMGTools.Production.PFAOD.PFAOD_EventContent_cff import V5

import copy 

V5_RA1 = copy.copy( V5 )
V5_RA1.extend(
    [
    'keep *_ak5CaloJets_*_*',
    ]
    )
