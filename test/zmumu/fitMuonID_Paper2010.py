import FWCore.ParameterSet.Config as cms

### USAGE:
###    cmsRun fitMuonID_Paper2010.py <scenario>
### scenarios:
###   - data_all (default)  
###   - signal_mc

import sys
args = sys.argv[1:]
if (sys.argv[0] == "cmsRun"): args =sys.argv[2:]
scenario = "data_all"
if len(args) > 0: scenario = args[0]
print "Will run scenario ", scenario 

process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),

    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "70", "130", "GeV/c^{2}"),
        pt = cms.vstring("Probe p_{T}", "0", "1000", "GeV/c"),
        eta    = cms.vstring("Probe #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("Probe |#eta|", "0", "2.5", ""),
        tag_pt = cms.vstring("Tag p_{T}",    "0", "1000", "GeV/c"),
        tag_nVertices = cms.vstring("Number of vertices", "0", "999", ""),
    ),

    Categories = cms.PSet(
        Glb   = cms.vstring("Global", "dummy[pass=1,fail=0]"),
        VBTF     = cms.vstring("VBTFLike", "dummy[pass=1,fail=0]"),
        VBTFold  = cms.vstring("VBTFLike", "dummy[pass=1,fail=0]"),
        TMOST = cms.vstring("TMOneStationTight", "dummy[pass=1,fail=0]"),
        PF    = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
        Mu15  = cms.vstring("MC true", "dummy[true=1,false=0]"),
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    ),

    PDFs = cms.PSet(
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        )
    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),

    Efficiencies = cms.PSet(), # will be filled later
)

PT_ETA_BINS = cms.PSet(
    pt     = cms.vdouble(  10, 20, 30, 40, 60, 100 ),
    abseta = cms.vdouble(  0.0, 0.9, 2.4)
)
ETA_BINS = cms.PSet(
    pt  = cms.vdouble(20,100),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.1, -0.6, 0, 0.6, 1.1, 1.6, 2.1, 2.4),
)
VTX_BINS  = cms.PSet(
    pt     = cms.vdouble(  20, 120 ),
    abseta = cms.vdouble(  0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,1.5,2.5,3.5,4.5,5.5,6.5)
)

ETA_BINS_FINE = cms.PSet(
    pt  = cms.vdouble(20,100),
    eta = cms.vdouble(*[x/10. for x in xrange(-24,25,1)]),
)
OVERALL = cms.PSet(
    pt  = cms.vdouble(20,100),
    abseta = cms.vdouble(0.0, 2.4),
)
CHARGE = cms.PSet(
    pt     = cms.vdouble(20,100),
    abseta = cms.vdouble(0.0, 2.4),
    charge = cms.vdouble(-2,0,2),
)



PREFIX="/data/gpetrucc/7TeV/tnp/2011.02.17/"
process.TnP_MuonID = Template.clone(
    InputFileNames = cms.vstring(PREFIX+'tnpZ_Data_Nov4B.root'),
    InputTreeName = cms.string("fitter_tree"),
    InputDirectoryName = cms.string("tpTree"),
    OutputFileName = cms.string("TnP_Paper2010_MuonID_%s.root" % scenario),
    Efficiencies = cms.PSet(),
)

if scenario.find("signal_mc") != -1:
    process.TnP_MuonID.InputFileNames = [ PREFIX+"tnpZ_MC_DYPoweg.root" ]
if scenario.find("some_mc") != -1:
    process.TnP_MuonID.InputFileNames = [ PREFIX+"tnpZ_MC_DYPoweg_1.root" ]

IDS = [ "Glb", "TMOST", "VBTF", "PF", "VBTFold" ]
ALLBINS=[("pt_abseta",PT_ETA_BINS),("eta", ETA_BINS)]
ALLBINS += [ ("vtx",VTX_BINS)]
#if scenario.find("set2"):
ALLBINS+=[("eta_fine",ETA_BINS_FINE), ("overall",OVERALL), ("charge",CHARGE)]
#if scenario.find("set3"):
ALLBINS+=[("overall_vv",OVERALL)]

for ID in IDS:
    if len(args) > 1 and ID != args[1]: continue
    module = process.TnP_MuonID.clone(OutputFileName = cms.string("TnP_Paper2010_MuonID_%s_%s.root" % (scenario, ID)))
    for X,B in ALLBINS:
        shape = "voigtPlusExpo"
        if X.find("_vv"): shape = "vpvPlusExpo"
        setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
            EfficiencyCategoryAndState = cms.vstring(ID,"pass"),
            UnbinnedVariables = cms.vstring("mass"),
            BinnedVariables = B.clone(),
            BinToPDFmap = cms.vstring(shape)
        ))
        if scenario.find("mc") != -1:
            setattr(module.Efficiencies, ID+"_"+X+"_mcTrue", cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(ID,"pass"),
                UnbinnedVariables = cms.vstring("mass"),
                BinnedVariables = B.clone(mcTrue = cms.vstring("true"))
            ))
    setattr(process, "TnP_MuonID_"+ID, module)        
    setattr(process, "run_"+ID, cms.Path(module))
