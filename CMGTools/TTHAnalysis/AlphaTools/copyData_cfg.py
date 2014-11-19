import FWCore.ParameterSet.Config as cms

# Give the process a name
process = cms.Process("PickEvent")

# Tell the process which files to use as the sourdce
process.source = cms.Source ("PoolSource",
          fileNames = cms.untracked.vstring ("/store/mc/Spring14miniaod/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/00F8CFD8-2909-E411-9184-003048D439B6.root")
)

# tell the process to only run over 100 events (-1 would mean run over
#  everything
process.maxEvents = cms.untracked.PSet(
            input = cms.untracked.int32 (10)

)

# Tell the process what filename to use to save the output
process.Out = cms.OutputModule("PoolOutputModule",
         fileName = cms.untracked.string ("MyOutputFile.root")
)

# make sure everything is hooked up
process.end = cms.EndPath(process.Out)
