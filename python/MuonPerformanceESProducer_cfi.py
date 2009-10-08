import FWCore.ParameterSet.Config as cms

MuonPerformanceESProducer_GlobalMuon1 = cms.ESProducer("MuonPerformanceESProducer",
                                                          # this is what it makes available
                                                          ComponentName = cms.string('GlobalMuon'),
                                                          # this is where it gets the payload from
                                                          PayloadName = cms.string('GlobalMuon'),
                                                          WorkingPointName = cms.string('GlobalMuon')
                                                          )


MuonPerformanceESProducer_TriggerMuon1 = cms.ESProducer("MuonPerformanceESProducer",
                                                          # this is what it makes available
                                                          ComponentName = cms.string('TriggerMuon'),
                                                          # this is where it gets the payload from                                                
                                                          PayloadName = cms.string('TriggerMuon'),
                                                          WorkingPointName = cms.string('TriggerMuon')
                                                          )

MuonPerformanceESProducer_TrackerTrackMuon1 = cms.ESProducer("MuonPerformanceESProducer",
                                                            # this is what it makes available
                                                            ComponentName = cms.string('TrackerTrackMuon'),
                                                            # this is where it gets the payload from
                                                            PayloadName = cms.string('TrackerTrackMuon'),
                                                            WorkingPointName = cms.string('TrackerTrackMuon')
                                                            )


MuonPerformanceESProducer_TriggerMuon1 = cms.ESProducer("MuonPerformanceESProducer",
                                                        # this is what it makes available
                                                        ComponentName = cms.string('TriggerMuon'),
                                                        # this is where it gets the payload from
                                                        PayloadName = cms.string('TriggerMuon'),
                                                        WorkingPointName = cms.string('TriggerMuon')
                                                        )

MuonPerformanceESProducer_GlobalMuon2 = cms.ESProducer("MuonPerformanceESProducer",
                                                       # this is what it makes available
                                                       ComponentName = cms.string('GlobalMuon'),
                                                       # this is where it gets the payload from
                                                       PayloadName = cms.string('GlobalMuon'),
                                                       WorkingPointName = cms.string('GlobalMuon')
                                                       )


MuonPerformanceESProducer_TriggerMuon2 = cms.ESProducer("MuonPerformanceESProducer",
                                                        # this is what it makes available
                                                        ComponentName = cms.string('TriggerMuon'),
                                                        # this is where it gets the payload from
                                                        PayloadName = cms.string('TriggerMuon'),
                                                        WorkingPointName = cms.string('TriggerMuon')
                                                        )

MuonPerformanceESProducer_TrackerTrackMuon2 = cms.ESProducer("MuonPerformanceESProducer",
                                                             # this is what it makes available
                                                             ComponentName = cms.string('TrackerTrackMuon'),
                                                             # this is where it gets the payload from
                                                             PayloadName = cms.string('TrackerTrackMuon'),
                                                             WorkingPointName = cms.string('TrackerTrackMuon')
                                                             )

MuonPerformanceESProducer_TriggerMuon2 = cms.ESProducer("MuonPerformanceESProducer",
                                                        # this is what it makes available
                                                        ComponentName = cms.string('TriggerMuon'),
                                                        # this is where it gets the payload from
                                                        PayloadName = cms.string('TriggerMuon'),
                                                        WorkingPointName = cms.string('TriggerMuon')
                                                        )
