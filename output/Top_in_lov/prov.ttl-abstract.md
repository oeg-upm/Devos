```mermaid
	classDiagram

    
    class Insertion {
    
    }

    class Contributor {
    
    }

    class Communication {
    
    }

    class Entity {
    
    }

    class Start {
    
    }

    class Usage {
    
    }

    class Influence {
    
    }

    class Agent {
    
    }

    class Delegation {
    
    }

    class End {
    
    }

    class Attribution {
    
    }

    class Publisher {
    
    }

    class Modify {
    
    }

    class Publish {
    
    }

    class Removal {
    
    }

    class DirectQueryService {
    
    }

    class Activity {
    
    }

    class Association {
    
    }

    class ne5fbb81be4694f688a3d741b79e449beb39 {
    
    }

    class Quotation {
    
    }

    class Revision {
    
    }

    class Generation {
    
    }

    class Creator {
    
    }

    class ne5fbb81be4694f688a3d741b79e449beb19 {
    
    }

    class Derivation {
    
    }

    class Invalidation {
    
    }

    class Dictionary {
    
    }

    class ne5fbb81be4694f688a3d741b79e449beb35 {
    
    }

    class PrimarySource {
    
    }



Entity  --> Activity   :wasGeneratedBy  

Activity  --> Start   :qualifiedStart  

Entity  --> Entity   :hadPrimarySource  

Association  --> Plan   :hadPlan  

Entity  --> Derivation   :qualifiedDerivation  

Activity  --> Entity   :wasStartedBy  

Insertion  --> Dictionary   :dictionary  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Entity   :used  

Activity  --> Entity   :wasEndedBy  

AgentInfluence  --> Agent   :agent  

Activity  --> Communication   :qualifiedCommunication  

EntityInfluence  --> Entity   :entity  

Entity  --> Bundle   :asInBundle  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Activity  --> Activity   :wasInformedBy  

Activity  --> Usage   :qualifiedUsage  

Removal  --> Dictionary   :dictionary  

Agent  --> Agent   :actedOnBehalfOf  

Insertion  --> KeyEntityPair   :insertedKeyEntityPair  

Agent  --> Delegation   :qualifiedDelegation  

Entity  --> Revision   :qualifiedRevision  

Entity  --> Entity   :specializationOf  

Activity  --> Entity   :invalidated  

Influence  --> Role   :hadRole  

Derivation  --> Usage   :hadUsage  

Entity  --> Generation   :qualifiedGeneration  

Entity  --> PrimarySource   :qualifiedPrimarySource  

KeyEntityPair  --> Entity   :pairEntity  

Dictionary  --> Insertion   :qualifiedInsertion  

Influence  --> Activity   :hadActivity  

Activity  --> End   :qualifiedEnd  

ne5fbb81be4694f688a3d741b79e449beb9  --> Activity   :hadActivity  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Activity   :wasInvalidatedBy  

Dictionary  --> Removal   :qualifiedRemoval  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Derivation  --> Generation   :hadGeneration  

ActivityInfluence  --> Activity   :activity  

Entity  --> Entity   :wasQuotedFrom  

Entity  --> Entity   :alternateOf  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> Entity   :mentionOf  

Entity  --> Invalidation   :qualifiedInvalidation  

Entity  --> Attribution   :qualifiedAttribution  

Activity  --> Entity   :generated  

Activity  --> Association   :qualifiedAssociation  

ne5fbb81be4694f688a3d741b79e449beb19  --> Influence   :qualifiedInfluence  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Quotation   :qualifiedQuotation  

Entity  --> Entity   :wasRevisionOf  

Collection  --> Entity   :hadMember  

Influence  --> Thing   :influencer  

```