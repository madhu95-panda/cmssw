import FWCore.ParameterSet.Config as cms

ak5JetFlavourInfos = cms.EDProducer("JetFlavourClustering",
    jets                     = cms.InputTag("ak5PFJets"),
    bHadrons                 = cms.InputTag("selectedHadronsAndPartons","bHadrons"),
    cHadrons                 = cms.InputTag("selectedHadronsAndPartons","cHadrons"),
    partons                  = cms.InputTag("selectedHadronsAndPartons","physicsPartons"),
    leptons                  = cms.InputTag("selectedHadronsAndPartons","leptons"),
    jetAlgorithm             = cms.string("AntiKt"),
    rParam                   = cms.double(0.5),
    ghostRescaling           = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False)
)
