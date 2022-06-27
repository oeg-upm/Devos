```mermaid
	classDiagram

    
    class Removal {
    
    }

    class Modify {
    
    }

    class Publish {
    
    }

    class Entity {
    
    }

    class Usage {
    
    }

    class Contributor {
    
    }

    class Activity {
    
    }

    class Attribution {
    
    }

    class Association {
    
    }

    class Dictionary {
    
    }

    class nffd8d6a0ede54f81adec44ecf0bdf337b35 {
    
    }

    class Invalidation {
    
    }

    class Delegation {
    
    }

    class Revision {
    
    }

    class DirectQueryService {
    
    }

    class Insertion {
    
    }

    class Publisher {
    
    }

    class nffd8d6a0ede54f81adec44ecf0bdf337b19 {
    
    }

    class Derivation {
    
    }

    class Generation {
    
    }

    class Quotation {
    
    }

    class PrimarySource {
    
    }

    class Agent {
    
    }

    class Creator {
    
    }

    class Influence {
    
    }

    class Start {
    
    }

    class nffd8d6a0ede54f81adec44ecf0bdf337b39 {
    
    }

    class End {
    
    }

    class Communication {
    
    }



Entity  --> Entity   :mentionOf  

nffd8d6a0ede54f81adec44ecf0bdf337b9  --> Activity   :hadActivity  

Entity  --> Quotation   :qualifiedQuotation  

Insertion  --> Dictionary   :dictionary  

AgentInfluence  --> Agent   :agent  

Activity  --> Entity   :wasStartedBy  

Activity  --> Entity   :used  

Activity  --> Usage   :qualifiedUsage  

Activity  --> Association   :qualifiedAssociation  

Entity  --> Entity   :specializationOf  

Entity  --> Activity   :wasInvalidatedBy  

Activity  --> Agent   :wasAssociatedWith  

Influence  --> Activity   :hadActivity  

Entity  --> Revision   :qualifiedRevision  

Association  --> Plan   :hadPlan  

Derivation  --> Generation   :hadGeneration  

Entity  --> Entity   :wasQuotedFrom  

Activity  --> Activity   :wasInformedBy  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Invalidation   :qualifiedInvalidation  

Removal  --> Dictionary   :dictionary  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Activity   :wasGeneratedBy  

Influence  --> Thing   :influencer  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Entity   :hadPrimarySource  

Entity  --> Entity   :alternateOf  

Activity  --> End   :qualifiedEnd  

Insertion  --> KeyEntityPair   :insertedKeyEntityPair  

Entity  --> Attribution   :qualifiedAttribution  

Activity  --> Start   :qualifiedStart  

Activity  --> Entity   :invalidated  

Activity  --> Entity   :wasEndedBy  

EntityInfluence  --> Entity   :entity  

KeyEntityPair  --> Entity   :pairEntity  

Activity  --> Entity   :generated  

nffd8d6a0ede54f81adec44ecf0bdf337b19  --> Influence   :qualifiedInfluence  

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Activity  --> Communication   :qualifiedCommunication  

Agent  --> Delegation   :qualifiedDelegation  

Entity  --> Generation   :qualifiedGeneration  

Entity  --> Derivation   :qualifiedDerivation  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Dictionary  --> Insertion   :qualifiedInsertion  

Influence  --> Role   :hadRole  

Dictionary  --> Removal   :qualifiedRemoval  

Entity  --> Bundle   :asInBundle  

Collection  --> Entity   :hadMember  

ActivityInfluence  --> Activity   :activity  

Derivation  --> Usage   :hadUsage  

```