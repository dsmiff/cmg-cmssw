import operator 
import itertools
import copy
from math import *

from ROOT import TLorentzVector, TVectorD

from CMGTools.RootTools.fwlite.Analyzer import Analyzer
from CMGTools.RootTools.fwlite.Event import Event
from CMGTools.RootTools.statistics.Counter import Counter, Counters
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle
from CMGTools.RootTools.physicsobjects.Lepton import Lepton
from CMGTools.RootTools.physicsobjects.Photon import Photon
from CMGTools.RootTools.physicsobjects.Electron import Electron
from CMGTools.RootTools.physicsobjects.Muon import Muon
from CMGTools.RootTools.physicsobjects.Jet import Jet

from CMGTools.RootTools.utils.DeltaR import * 

import ROOT

import os
        
class ttHAlphaTMetAnalyzer( Analyzer ):
    """To construct MET for AlphaT mu control sample"""

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(ttHAlphaTMetAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)

    def declareHandles(self):
        super(ttHAlphaTMetAnalyzer, self).declareHandles()
        self.handles['met'] = AutoHandle( 'slimmedMETs', 'std::vector<pat::MET>' )
        self.handles['muons'] = AutoHandle(self.cfg_ana.muons,"std::vector<pat::Muon>") 
        self.handles['nopumet'] = AutoHandle( 'slimmedMETs', 'std::vector<pat::MET>' )
        self.handles['cmgCand'] = AutoHandle( self.cfg_ana.candidates, self.cfg_ana.candidatesTypes )
        self.handles['vertices'] =  AutoHandle( "offlineSlimmedPrimaryVertices", 'std::vector<reco::Vertex>', fallbackLabel="offlinePrimaryVertices" )

    def beginLoop(self):
        super(ttHAlphaTMetAnalyzer,self).beginLoop()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')

    def makeMETNoMu(self, event):
        event.metNoMu = copy.deepcopy(self.handles['met'].product()[0])
        event.metNoMuNoPU = copy.deepcopy(self.handles['nopumet'].product()[0])

        #muons
        allmuons = self.makeAllMuons(event)
        event.selectedMuons = []
        mupx = 0.
        mupy = 0.
        for mu in allmuons:
            mupx = mupx+mu.px()
            mupy = mupy+mu.py()

        #subtract muon momentum and construct met
        if hasattr(event, 'deltaMetFromJetSmearing'):
            import ROOT
            px,py = event.metNoMu.px()+event.deltaMetFromJetSmearing[0]-mupx, event.metNoMu.py()+event.deltaMetFromJetSmearing[1]-mupy
            event.metNoMu.setP4(ROOT.reco.Particle.LorentzVector(px,py, 0, hypot(px,py)))
            px,py = event.metNoMuNoPU.px()+event.deltaMetFromJetSmearing[0]-mupx, event.metNoMuNoPU.py()+event.deltaMetFromJetSmearing[1]-mupy
            event.metNoMuNoPU.setP4(ROOT.reco.Particle.LorentzVector(px,py, 0, hypot(px,py)))
        if hasattr(event, 'deltaMetFromJEC') and event.deltaMetFromJEC[0] != 0 and event.deltaMetFromJEC[1] != 0:
            import ROOT
            px,py = event.metNoMu.px()+event.deltaMetFromJEC[0]-mupx, event.metNoMu.py()+event.deltaMetFromJEC[1]-mupy
            event.met.setP4(ROOT.reco.Particle.LorentzVector(px,py, 0, hypot(px,py)))
            px,py = event.metNoMuNoPU.px()+event.deltaMetFromJEC[0]-mupx, event.metNoMuNoPU.py()+event.deltaMetFromJEC[1]-mupy
            event.metNoMuNoPU.setP4(ROOT.reco.Particle.LorentzVector(px,py, 0, hypot(px,py)))

    def makeAllMuons(self, event):
        """
               make a list of all muons, and apply basic corrections to them
        """
        # Start from all muons
        allmuons = map( Muon, self.handles['muons'].product() )

        # Muon scale and resolution corrections (if enabled)

        # Clean up dulicate muons (note: has no effect unless the muon id is removed)

        # Attach the vertex to them, for dxy/dz calculation
        for mu in allmuons:
            mu.associatedVertex = event.goodVertices[0]

        # Compute relIso in 0.3 and 0.4 cones
        for mu in allmuons:
            mu.absIso03 = (mu.pfIsolationR03().sumChargedHadronPt + max( mu.pfIsolationR03().sumNeutralHadronEt +  mu.pfIsolationR03().sumPhotonEt -  mu.pfIsolationR03().sumPUPt/2,0.0))
            mu.absIso04 = (mu.pfIsolationR04().sumChargedHadronPt + max( mu.pfIsolationR04().sumNeutralHadronEt +  mu.pfIsolationR04().sumPhotonEt -  mu.pfIsolationR04().sumPUPt/2,0.0))
            mu.relIso03 = mu.absIso03/mu.pt()
            mu.relIso04 = mu.absIso04/mu.pt()
 
        return allmuons


    def process(self, iEvent, event):
        self.readCollections( iEvent )
        self.counters.counter('events').inc('all events')

        self.makeMETNoMu(event)

        return True
