from CMGTools.TTHAnalysis.samples.getFiles import getFiles
from CMGTools.TTHAnalysis.samples.getMyFiles import getMyFiles
import CMGTools.RootTools.fwlite.Config as cfg
import os

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

#AlphaT sample (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/AlphaT#MC_samples_for_CSA14_exercise)

#PU20bx25
WJetsToLNu_PU20bx25 = kreator.makeMCComponent("WJetsToLNu_PU20bx25","/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS" , "*.root")

DYJetsToLL_PU20bx25 = kreator.makeMCComponent("DYJetsToLL_PU20bx25","/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM", "CMS" , "*.root")
# "/DYJetsToLL_M-50_13TeV-pythia6/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# "/DYJetsToLL_M-50_13TeV-madgraph-pythia8-tauola_v2/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# "/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"

ZJetsToNuNu_HT100to200_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT100to200_PU20bx25","/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
ZJetsToNuNu_HT200to400_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT200to400_PU20bx25","/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
ZJetsToNuNu_HT400to600_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT400to600_PU20bx25","/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
ZJetsToNuNu_HT600toInf_PU20bx25 = kreator.makeMCComponent("ZJetsToNuNu_HT600toInf_PU20bx25","/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")

GJets_HT100to200_PU20bx25 = kreator.makeMCComponent("GJets_HT100to200_PU20bx25","/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
GJets_HT200to400_PU20bx25 = kreator.makeMCComponent("GJets_HT200to400_PU20bx25","/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
GJets_HT400to600_PU20bx25 = kreator.makeMCComponent("GJets_HT400to600_PU20bx25","/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
GJets_HT600toInf_PU20bx25 = kreator.makeMCComponent("GJets_HT600toInf_PU20bx25","/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")

TTbar_PU20bx25 = kreator.makeMCComponent("TTbar_PU20bx25","/TT_Tune4C_13TeV-pythia8-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")

TToBLNu_schannelEMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_schannelEMu_PU20bx25","/TToBLNu_s-channel-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
TToBLNu_tchannelEMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_tchannelEMu_PU20bx25","/TToBLNu_t-channel-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM","CMS","*.root")
TToBLNu_tWchannelDREMu_PU20bx25 = kreator.makeMCComponent("TToBLNu_tWchannelDREMu_PU20bx25","/TToBLNu_tW-channel-DR-EMu_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")

T1qqqq_mGl1000mLSP800_PU20bx25 = kreator.makeMCComponent("SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauolaLSP800_PU20bx25","/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*root")
# "/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"

T1bbbb_mGl1000mLSP900_PU20bx25 = kreator.makeMCComponent("T1bbbb_mGl1000mLSP900_PU20bx25","/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")
# "/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
# "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v3/MINIAODSIM"

T1tttt_mGl1200mLSP800_PU20bx25 = kreator.makeMCComponent("T1tttt_mGl1200mLSP800_PU20bx25","/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM","CMS","*.root")
# "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v1/MINIAODSIM"
# "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14miniaod-PU20bx25_POSTLS170_V5-v2/MINIAODSIM"
