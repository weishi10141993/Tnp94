import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")
process.load("CondCore.DBCommon.CondDBCommon_cfi")

process.CondDBCommon.connect = 'sqlite_file:MuonPhysicsPerformance.db'


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    timetype = cms.untracked.string("runnumber"),                                          
    toPut = cms.VPSet(
    cms.PSet(
    record = cms.string('GLBMUJPSI_OCTXTEST_TABLE'),
    tag = cms.string('GLBMUJPSI_OCTXTEST_TABLE'),
    label = cms.string('GLBMUJPSI_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('GLBMUJPSI_OCTXTEST_WP'),
    tag = cms.string('GLBMUJPSI_OCTXTEST_WP'),
    label = cms.string('GLBMUJPSI_OCTXTEST_WP')
    ),
    cms.PSet(
    record = cms.string('TRKEFFMUJPSI_OCTXTEST_TABLE'),
    tag = cms.string('TRKEFFMUJPSI_OCTXTEST_TABLE'),
    label = cms.string('TRKEFFMUJPSI_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('TRKEFFMUJPSI_OCTXTEST_WP'),
    tag = cms.string('TRKEFFMUJPSI_OCTXTEST_WP'),
    label = cms.string('TRKEFFMUJPSI_OCTXTEST_WP')
    ),
    cms.PSet(
    record = cms.string('TRGMUJPSI_OCTXTEST_TABLE'),
    tag = cms.string('TRGMUJPSI_OCTXTEST_TABLE'),
    label = cms.string('TRGMUJPSI_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('TRGMUJPSI_OCTXTEST_WP'),
    tag = cms.string('TRGMUJPSI_OCTXTEST_WP'),
    label = cms.string('TRGMUJPSI_OCTXTEST_WP')
    ),    
    cms.PSet(
    record = cms.string('GLBMUJPSICAL_OCTXTEST_TABLE'),
    tag = cms.string('GLBMUJPSICAL_OCTXTEST_TABLE'),
    label = cms.string('GLBMUJPSICAL_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('GLBMUJPSICAL_OCTXTEST_WP'),
    tag = cms.string('GLBMUJPSICAL_OCTXTEST_WP'),
    label = cms.string('GLBMUJPSICAL_OCTXTEST_WP')
    ),
    cms.PSet(
    record = cms.string('GLBMUZ_OCTXTEST_TABLE'),
    tag = cms.string('GLBMUZ_OCTXTEST_TABLE'),
    label = cms.string('GLBMUZ_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('GLBMUZ_OCTXTEST_WP'),
    tag = cms.string('GLBMUZ_OCTXTEST_WP'),
    label = cms.string('GLBMUZ_OCTXTEST_WP')
    ),
    cms.PSet(
    record = cms.string('TRKEFFMUZ_OCTXTEST_TABLE'),
    tag = cms.string('TRKEFFMUZ_OCTXTEST_TABLE'),
    label = cms.string('TRKEFFMUZ_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('TRKEFFMUZ_OCTXTEST_WP'),
    tag = cms.string('TRKEFFMUZ_OCTXTEST_WP'),
    label = cms.string('TRKEFFMUZ_OCTXTEST_WP')
    ),
    cms.PSet(
    record = cms.string('TRGMUZ_OCTXTEST_TABLE'),
    tag = cms.string('TRGMUZ_OCTXTEST_TABLE'),
    label = cms.string('TRGMUZ_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('TRGMUZ_OCTXTEST_WP'),
    tag = cms.string('TRGMUZ_OCTXTEST_WP'),
    label = cms.string('TRGMUZ_OCTXTEST_WP')
    ),    
    cms.PSet(
    record = cms.string('GLBMUZCAL_OCTXTEST_TABLE'),
    tag = cms.string('GLBMUZCAL_OCTXTEST_TABLE'),
    label = cms.string('GLBMUZCAL_OCTXTEST_TABLE')
    ),
    cms.PSet(
    record = cms.string('GLBMUZCAL_OCTXTEST_WP'),
    tag = cms.string('GLBMUZCAL_OCTXTEST_WP'),
    label = cms.string('GLBMUZCAL_OCTXTEST_WP')
    )
    
    )
                                          )
                      



process.mywriter = cms.EDFilter("PhysicsPerformanceDBWriterFromTPHist",

                                # For each table to be loaded, set the name of the input T/P file, histogram, algorithm, and cut (if any)
                                inputHistoFiles = cms.vstring('fit_result_GlbFromTk_JPsi.root',
                                                              'fit_result_TkFromSta_JPsi.root',
                                                              'fit_result_HltFromGlb_JPsi.root',
                                                              'fit_result_GlbFromCal_JPsi.root',
                                                              'fit_result_GlbFromTk_Z.root',
                                                              'fit_result_TkFromSta_Z.root',
                                                              'fit_result_HltFromGlb_Z.root',
                                                              'fit_result_GlbFromCal_Z.root'
                                                              ),                                

                                inputHistogramNames = cms.vstring('fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta',
                                                                  'fit_eff_pt_eta'),
                                
                                inputAlgorithmNames = cms.vstring('GlobalMuonFromTrackerTrackJpsi',
                                                                  'TrackerTrackFromStandaloneMuonJpsi',
                                                                  'TriggerMuonFromGlobalMuonJpsi',
                                                                  'GlobalMuonFromCaloMuonJpsi',
                                                                  'GlobalMuonFromTrackerTrackZ',
                                                                  'TrackerTrackFromStandaloneMuonZ',
                                                                  'TriggerMuonFromGlobalMuonZ',
                                                                  'GlobalMuonFromCaloMuonZ'), 

                                inputDiscriminatorCuts = cms.vdouble(0.0,
                                                                     0.0,
                                                                     0.0,
                                                                     0.0,
                                                                     0.0,
                                                                     0.0,
                                                                     0.0,
                                                                     0.0),
                                
                                # For each table to be loaded, set the payload and working point record names as
                                # defined above in the PoolDBOutputService
                                RecordPayloads = cms.vstring('GLBMUJPSI_OCTXTEST_TABLE','TRKEFFMUJPSI_OCTXTEST_TABLE','TRGMUJPSI_OCTXTEST_TABLE','GLBMUJPSICAL_OCTXTEST_TABLE',
                                                             'GLBMUZ_OCTXTEST_TABLE','TRKEFFMUZ_OCTXTEST_TABLE','TRGMUZ_OCTXTEST_TABLE','GLBMUZCAL_OCTXTEST_TABLE'),
                                RecordWPs = cms.vstring('GLBMUJPSI_OCTXTEST_WP','TRKEFFMUJPSI_OCTXTEST_WP','TRGMUJPSI_OCTXTEST_WP','GLBMUJPSICAL_OCTXTEST_WP',
                                                        'GLBMUZ_OCTXTEST_WP','TRKEFFMUZ_OCTXTEST_WP','TRGMUZ_OCTXTEST_WP','GLBMUZCAL_OCTXTEST_WP'),

                                # Set the type of data to be stored, the binning variables, and the IOV
                                # These are currently assumed to be the same for all tables loaded in a single job
                                inputResultTypes = cms.vstring('efficiency','efficiency_symerr'),
                                inputBinningVariables = cms.vstring('pt','eta'),                                
                                IOVBegin = cms.uint64(1),
                                IOVEnd = cms.uint64(50)
                                )


process.p = cms.Path(process.mywriter)


