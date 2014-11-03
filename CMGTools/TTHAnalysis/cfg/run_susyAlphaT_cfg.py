import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.RootTools.fwlite.Config import printComps
from CMGTools.RootTools.RootTools import *

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

##------------------------------------------
## Redefine analyzer parameters
##------------------------------------------

# Muons
#------------------------------
ttHLepAna.loose_muon_pt               = 10.
ttHLepAna.loose_muon_eta              = 2.5
ttHLepAna.loose_muon_id               = "POG_ID_Tight"
ttHLepAna.loose_muon_dxy              = 0.2
ttHLepAna.loose_muon_dz               = 0.5
ttHLepAna.loose_muon_relIso           = 0.12
#
## Electrons
##------------------------------
ttHLepAna.loose_electron_id           = "POG_Cuts_ID_2012_Loose"
#ttHLepAna.loose_electron_id          = "POG_CSA14_25ns_v1_Loose"  

ttHLepAna.loose_electron_pt           = 10
ttHLepAna.loose_electron_eta          = 2.5
ttHLepAna.loose_electron_dxy          = 0.02
ttHLepAna.loose_electron_dz           = 0.2
ttHLepAna.loose_electron_relIso       = 0.15
ttHLepAna.loose_electron_lostHits     = 1 
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
ttHLepAna.ele_isoCorr                 = "rhoArea"
ttHLepAna.ele_tightId                 = "Cuts_2012"

# Photons
#------------------------------
ttHPhoAna.ptMin                       = 25,
ttHPhoAna.etaMax                      = 2.5,
ttHPhoAna.gammaID                     = "PhotonCutBasedIDLoose"

# Taus 
#------------------------------
ttHTauAna.etaMax         = 2.3
ttHTauAna.dxyMax         = 99999.
ttHTauAna.dzMax          = 99999.
ttHTauAna.vetoLeptons    = False
ttHTauAna.vetoLeptonsPOG = True


# Jets (for event variables do apply the jetID and not PUID yet)
#------------------------------
ttHJetAna.relaxJetId      = False
ttHJetAna.doPuId          = False
ttHJetAna.jetEta          = 5.
ttHJetAna.jetEtaCentral   = 3.
ttHJetAna.jetPt           = 50.
ttHJetAna.recalibrateJets = False
ttHJetAna.jetLepDR        = 0.4
ttHJetMCAna.smearJets     = False

##------------------------------------------
##  ISOLATED TRACK
##------------------------------------------

# those are the cuts for the nonEMu
ttHIsoTrackAna = cfg.Analyzer(
            'ttHIsoTrackAnalyzer',
#            candidates='cmgCandidates',
#            candidatesTypes='std::vector<cmg::Candidate>',
            candidates      ='packedPFCandidates',
            candidatesTypes ='std::vector<pat::PackedCandidate>',
            ptMin           = 10, ### for pion 
            ptMinEMU        = 10, ### for EMU
            dzMax           = 0.05,
            #####
            isoDR           = 0.3,
            ptPartMin       = 0,
            dzPartMax       = 0.1,
            maxAbsIso       = 8,
            #####
            MaxIsoSum       = 0.1, ### unused
            MaxIsoSumEMU    = 0.2, ### unused
            doSecondVeto    = False
            )


##------------------------------------------
##  ALPHAT VARIABLES
##------------------------------------------

ttHAlphaTSkim = cfg.Analyzer(
            'ttHAlphaTSkimmer',
            forwardJetVeto = True,
            alphaTCuts = [(0.65, 200, 275),   #AlphaT cut in HT region
                          (0.60, 275, 325),   #(aT, HTlow, HThigh)
                          (0.55, 325, 99999)],#Any region not specified will be vetoed
            )

##------------------------------------------
##  mT_W VARIABLE
##------------------------------------------

# Currently produced in alphaT analyzer
# Modularize in future? 


#-------------------------------------------
# CUTS AND VETOS
#-------------------------------------------
# NOTE: Currently energy sums are calculated with 40 GeV jets (ttHCoreEventAnalyzer.py)
#       However, the input collection is cleanjets which have a 50 GeV cut so this is a labeling problem

#ESums
ttHJetMETSkim.jetPtCuts   = [100,100] # require the lead two jets to be above 100GeV
ttHJetMETSkim.htCut       = ('htJet40j', 200)
ttHJetMETSkim.mhtCut      = ('mhtJet40j', 0)
ttHJetMETSkim.nBJet       = ('CSVM', 0, "jet.pt() > 50")     # require at least 0 jets passing CSVM and pt > 50

#Leptons (currently allowing none)
ttHLepSkim.maxLeptons     = 0
ttHLepSkim.minLeptons     = 0

#AlphaT Specific cuts
ttHAlphaTAna = cfg.Analyzer(
            'ttHAlphaTVarAnalyzer'
            )

##------------------------------------------
##  PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.samples.samples_8TeV_v517 import triggers_RA1_Bulk, triggers_RA1_Prompt, triggers_RA1_Parked, triggers_RA1_Single_Mu, triggers_RA1_Photon, triggers_RA1_Muon

# Tree Producer
treeProducer = cfg.Analyzer(
        'treeProducerSusyAlphaT',
        vectorTree = True,
        PDFWeights = PDFWeights,
        triggerBits = {
            'Bulk'     : triggers_RA1_Bulk,
            'Prompt'   : triggers_RA1_Prompt,
            'Parked'   : triggers_RA1_Parked,
            'SingleMu' : triggers_RA1_Single_Mu,
            'Photon'   : triggers_RA1_Photon,
            'Muon'     : triggers_RA1_Muon,
            }
        )

#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import *


# Selected samples as defined on the AlphaT twiki
WJetsToLNu   = [ WJetsToLNu_HT100to200_PU_S14_POSTLS170, WJetsToLNu_HT200to400_PU_S14_POSTLS170, WJetsToLNu_HT400to600_PU_S14_POSTLS170, WJetsToLNu_HT600toInf_PU_S14_POSTLS170]
#GJets        = [ GJets_HT100to200_PU_S14_POSTLS170, GJets_HT200to400_PU_S14_POSTLS170, GJets_HT400to600_PU_S14_POSTLS170, GJets_HT600toInf_PU_S14_POSTLS170 ]


# Currently not defined in the samples file could be added from here: https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2F*DYJetsToLL*13TeV*%2F*PU20bx25*%2F*AODSIM
#DYJetsToLL  = []
# Currently not defined in the samples file could be added from here: https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2F*ZJetsToNuNu*13TeV*%2F*PU20bx25*%2F*AODSIM
#ZJetsToNuNu = []
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2F*GJets*13TeV*%2F*PU20bx25*%2F*AODSIM
#GJets       = []

# NOT INCLUDING: /TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM
TTbar        = [ TTpythia8_PU20bx25 ]
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2FTToBLNu*13TeV*%2FSpring*PU20bx25*%2F*AODSIM
#TToBLNu     = []
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2FSMS-T1qqqq*13TeV*%2FSpring*PU20bx25*%2F*AODSIM
#T1qqqq       = []
# https://cmsweb.cern.ch/das/request?view=list&limit=100&instance=prod%2Fglobal&input=dataset%3D%2FSMS-T1bbbb*13TeV*%2FSpring*PU20bx25*%2F*AODSIM
#T1bbbb       = []
T1tttt       = [ T1tttt_PU20bx25 ]


selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsM50_PU20bx25, TTJets_PUS14 , GJets_HT100to200_PU_S14_POSTLS170 ]
selectedComponents = []
selectedComponents.extend( WJetsToLNu )
selectedComponents.extend( TTbar )




#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence + [
                        ttHIsoTrackAna,
                        ttHAlphaTAna,
                        ttHAlphaTSkim,
                        treeProducer,
                        ])


#-------- HOW TO RUN
test = 1

# Test a single component, using a single thread.
#--------------------------------------------------
if test==1:
    #comp               = TTHToWW_PUS14
    #comp 	        = T1tttt_PU20bx25
    comp               = VBFHGG_PU20bx25
    #comp               = GJets_HT100to200_PU_S14_POSTLS170
    #comp.files = ['/afs/cern.ch/work/p/pandolf/CMSSW_7_0_6_patch1_2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']
    comp.files         = comp.files[:1]
    
    selectedComponents = [comp]
    comp.splitFactor   = 1
#--------------------------------------------------

# Test a single component on GJets (Photon + Jets sample)
#--------------------------------------------------
elif test==11:
    comp               = GJets_HT100to200_PU_S14_POSTLS170
    comp.files         = comp.files[:2]

    selectedComponents = [comp]
    comp.splitFactor   = 1
#-------------------------------------------------

# Test all components (1 thread per component).
#--------------------------------------------------
elif test==2:
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files       = comp.files[:1]
#--------------------------------------------------

#--------------------------------------------------

# Test on all GJets (Photon + Jets) samples
#--------------------------------------------------
elif test==3:
    for comp in GJets:
        comp.splitFactor = 1
        comp.files       = comp.files[:1]
#--------------------------------------------------



# Run on local files
#--------------------------------------------------
elif test==4:
    comp = TTJets_PU20bx25
#    comp.name = 'TTJets'
    #    comp.files = [ '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/063013AD-9907-E411-8135-0026189438BD.root' ]

    comp.files = [ '/afs/cern.ch/user/m/mbaber/WORK/private/CSA14Samples/TT_Tune4C_13TeV-pythia8_PU20bx25.root' ]

    selectedComponents = [comp]
    comp.splitFactor = 1
#--------------------------------------------------


config = cfg.Config( components = selectedComponents,
                     sequence = sequence )

printComps(config.components, True)
        
