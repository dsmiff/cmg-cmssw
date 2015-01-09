import FWCore.ParameterSet.Config as cms
from CMGTools.Production.PFAOD.PFAOD_EventContent_cff import V5

import copy 

V5_RA1 = copy.copy( V5 )
V5_RA1.extend(
    [
        'keep recoCaloJets_ak5CaloJets__*',
        'keep double_kt6CaloJets_rho_*',
        'keep recoVertexs_offlinePrimaryVertices__*',
        'keep *AssociationVector*_ak5JetTracksAssociatorAtVertex__*',
        'keep recoTracks_generalTracks__*',
        'keep recoGenParticles_genParticles__*',
        'keep recoGenJets_ak5GenJets__*',
        'keep GenEventInfoProduct_generator__*',
        'keep *CaloTowe*_towerMaker__*',
        'keep *AssociationVector*_combinedSecondaryVertexBJetTags__*',
        'keep *AssociationVector*_combinedSecondaryVertexMVABJetTags__*',
        'keep *AssociationVector*_jetBProbabilityBJetTags__*',
        'keep *AssociationVector*_jetProbabilityBJetTags__*',
        'keep *AssociationVector*_simpleSecondaryVertexHighEffBJetTags__*',
        'keep *AssociationVector*_simpleSecondaryVertexHighPurBJetTags__*',
        'keep *AssociationVector*_softElectronByPtBJetTags__*',
        'keep *AssociationVector*_softElectronByIP3dBJetTags__*',
        'keep *AssociationVector*_softMuonBJetTags__*',
        'keep *AssociationVector*_softMuonByPtBJetTags__*',
        'keep *AssociationVector*_softMuonByIP3dBJetTags__*',
        'keep *AssociationVector*_trackCountingHighEffBJetTags__*',
        'keep *AssociationVector*_trackCountingHighPurBJetTags__*',
        'keep *recoJetID*_ak5JetID__*',
    ]
    )
