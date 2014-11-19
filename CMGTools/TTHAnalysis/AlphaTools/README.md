AlphaTools
==========

Extra code for the AlphaT analysis



==========
Checking a dataset

WJetsToLNu:
python ./das_client.py --query="dataset=/*WJetsToLNu*/*/*MINIAOD*"

DYJetsToLL:
python ./das_client.py --query="dataset=/*DYJetsToLL*/*/*MINIAOD*"

ZJetsToNuNu:
python ./das_client.py --query="dataset=/*ZJetsToNuNu*/*/*MINIAOD"

TTbar:
python ./das_client.py --query="dataset=/*TTbar*/*/*MINIAOD*"

TToBLNu:
python ./das_client.py --query="dataset=/*TToBLNu*/*/*MINIAOD*"

GJets:
python ./das_client.py --query="dataset=/*GJets*/*/*MINIAOD*" 

T1qqqq:
python ./das_client.py --query="dataset=/*T1qqqq*/*/*MINIAOD*"

T1tttt:
python ./das_client.py --query="dataset=/*T1tttt*/*/*MINIAOD*"


=========
AAA (Any Data, Anytime, Anywhere)
Using the Xrootd service to quickly access data.
Requirements:
	LFN

Choose xrootd.ba.infn.it as your redirector.
e.g.
TFile *f=TFile::Open("root://xrootd.ba.infn.it//store/mc/Spring14miniaod/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/004BB841-B407-E411-8908-002590AC4BF6.root");

	

