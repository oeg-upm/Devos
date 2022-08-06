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

n6ef86b49e7144b8ebb17fec7e9257ec5b16  --> Role   :hadRole  

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

Entity  --> Entity   :wasDerivedFrom  

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

n6ef86b49e7144b8ebb17fec7e9257ec5b4  --> Location   :atLocation  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Activity   :wasInformedBy  

Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :specializationOf  

Entity  --> Entity   :hadPrimarySource  

Entity  --> Entity   :alternateOf  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Generation   :qualifiedGeneration  

n6ef86b49e7144b8ebb17fec7e9257ec5b9  --> Activity   :hadActivity  

Agent  --> Delegation   :qualifiedDelegation  

Activity  --> Entity   :generated  

Derivation  --> Generation   :hadGeneration  

Removal  --> Dictionary   :dictionary  

Insertion  --> Dictionary   :dictionary  

Entity  --> Entity   :mentionOf  

EntityInfluence  --> Entity   :entity  

Influence  --> Role   :hadRole  

Activity  --> Association   :qualifiedAssociation  

Activity  --> Usage   :qualifiedUsage  

```