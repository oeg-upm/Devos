```mermaid
	classDiagram

    
    class Entity {
    
    }

    class Activity {
    
    }

    class Agent {
    
    }

    class Dictionary {
    
    }

    class Generation {
    
    }

    class Usage {
    
    }

    class KeyEntityPair {
    
    }

    class Location {
    
    }

    class Plan {
    
    }

    class Role {
    
    }



Entity  --> Quotation   :qualifiedQuotation  

Activity  --> Agent   :wasAssociatedWith  

Activity  --> Entity   :wasEndedBy  

AgentInfluence  --> Agent   :agent  

Activity  --> Start   :qualifiedStart  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Entity  --> Agent   :wasAttributedTo  

Association  --> Plan   :hadPlan  

Entity  --> Entity   :wasRevisionOf  

Entity  --> Entity   :wasQuotedFrom  

Entity  --> Derivation   :qualifiedDerivation  

n29303b33f3a640c787ee38bcbcbe3e88b16  --> Role   :hadRole  

Entity  --> Entity   :wasDerivedFrom  

n29303b33f3a640c787ee38bcbcbe3e88b4  --> Location   :atLocation  

Activity  --> Entity   :used  

Derivation  --> Usage   :hadUsage  

Influence  --> Activity   :hadActivity  

ActivityInfluence  --> Activity   :activity  

Entity  --> Revision   :qualifiedRevision  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Entity  --> Invalidation   :qualifiedInvalidation  

Dictionary  --> Insertion   :qualifiedInsertion  

Dictionary  --> Removal   :qualifiedRemoval  

Insertion  --> KeyEntityPair   :insertedKeyEntityPair  

Collection  --> Entity   :hadMember  

Activity  --> Entity   :wasStartedBy  

Entity  --> Attribution   :qualifiedAttribution  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> Bundle   :asInBundle  

Activity  --> Entity   :invalidated  

Entity  --> Activity   :wasInvalidatedBy  

Activity  --> End   :qualifiedEnd  

Activity  --> Communication   :qualifiedCommunication  

KeyEntityPair  --> Entity   :pairEntity  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Activity   :wasInformedBy  

Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :specializationOf  

Entity  --> Entity   :hadPrimarySource  

Entity  --> Entity   :alternateOf  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Generation   :qualifiedGeneration  

Agent  --> Delegation   :qualifiedDelegation  

Activity  --> Entity   :generated  

Derivation  --> Generation   :hadGeneration  

n29303b33f3a640c787ee38bcbcbe3e88b9  --> Activity   :hadActivity  

Removal  --> Dictionary   :dictionary  

Insertion  --> Dictionary   :dictionary  

Entity  --> Entity   :mentionOf  

EntityInfluence  --> Entity   :entity  

Influence  --> Role   :hadRole  

Activity  --> Association   :qualifiedAssociation  

Activity  --> Usage   :qualifiedUsage  

```