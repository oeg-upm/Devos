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



Entity  --> Derivation   :qualifiedDerivation  

Entity  --> Attribution   :qualifiedAttribution  

Entity  --> Bundle   :asInBundle  

Entity  --> Entity   :wasDerivedFrom  

Activity  --> Usage   :qualifiedUsage  

Derivation  --> Usage   :hadUsage  

Derivation  --> Generation   :hadGeneration  

Entity  --> Entity   :wasQuotedFrom  

Entity  --> Generation   :qualifiedGeneration  

EntityInfluence  --> Entity   :entity  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Insertion  --> Dictionary   :dictionary  

Entity  --> Entity   :mentionOf  

Activity  --> Association   :qualifiedAssociation  

Dictionary  --> Removal   :qualifiedRemoval  

Activity  --> Entity   :generated  

Entity  --> Invalidation   :qualifiedInvalidation  

Entity  --> Entity   :hadPrimarySource  

Activity  --> Entity   :wasStartedBy  

Activity  --> Agent   :wasAssociatedWith  

Collection  --> Entity   :hadMember  

Activity  --> Start   :qualifiedStart  

Activity  --> Activity   :wasInformedBy  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Entity   :specializationOf  

ActivityInfluence  --> Activity   :activity  

Influence  --> Activity   :hadActivity  

Activity  --> Entity   :wasEndedBy  

Activity  --> End   :qualifiedEnd  

Entity  --> Quotation   :qualifiedQuotation  

n3d649fce557147879e66442571388555b4  --> Location   :atLocation  

Entity  --> Activity   :wasInvalidatedBy  

n3d649fce557147879e66442571388555b16  --> Role   :hadRole  

n3d649fce557147879e66442571388555b9  --> Activity   :hadActivity  

KeyEntityPair  --> Entity   :pairEntity  

Activity  --> Communication   :qualifiedCommunication  

Association  --> Plan   :hadPlan  

Insertion  --> KeyEntityPair   :insertedKeyEntityPair  

AgentInfluence  --> Agent   :agent  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Entity  --> Entity   :alternateOf  

Activity  --> Entity   :used  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> Agent   :wasAttributedTo  

Activity  --> Entity   :invalidated  

Removal  --> Dictionary   :dictionary  

Influence  --> Role   :hadRole  

Agent  --> Delegation   :qualifiedDelegation  

Dictionary  --> Insertion   :qualifiedInsertion  

Entity  --> Activity   :wasGeneratedBy  

Entity  --> Revision   :qualifiedRevision  

```