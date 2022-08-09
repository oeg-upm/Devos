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



Activity  --> Entity   :wasStartedBy  

Activity  --> Usage   :qualifiedUsage  

Influence  --> Role   :hadRole  

Entity  --> Invalidation   :qualifiedInvalidation  

Agent  --> Delegation   :qualifiedDelegation  

Association  --> Plan   :hadPlan  

Entity  --> Entity   :wasRevisionOf  

Entity  --> Entity   :specializationOf  

Entity  --> Activity   :wasInvalidatedBy  

Collection  --> Entity   :hadMember  

Entity  --> Derivation   :qualifiedDerivation  

Entity  --> Attribution   :qualifiedAttribution  

Activity  --> Start   :qualifiedStart  

Entity  --> Quotation   :qualifiedQuotation  

Derivation  --> Generation   :hadGeneration  

KeyEntityPair  --> Entity   :pairEntity  

Influence  --> Activity   :hadActivity  

Entity  --> Entity   :mentionOf  

Dictionary  --> Insertion   :qualifiedInsertion  

EntityInfluence  --> Entity   :entity  

Derivation  --> Usage   :hadUsage  

nf60df0426ad14108a80bb9203f5889a2b16  --> Role   :hadRole  

nf60df0426ad14108a80bb9203f5889a2b9  --> Activity   :hadActivity  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Insertion  --> KeyEntityPair   :insertedKeyEntityPair  

Entity  --> Entity   :wasQuotedFrom  

AgentInfluence  --> Agent   :agent  

Activity  --> Association   :qualifiedAssociation  

Entity  --> Bundle   :asInBundle  

Activity  --> Activity   :wasInformedBy  

Dictionary  --> Removal   :qualifiedRemoval  

Entity  --> Activity   :wasGeneratedBy  

Activity  --> Entity   :used  

Entity  --> Generation   :qualifiedGeneration  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Entity   :alternateOf  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Removal  --> Dictionary   :dictionary  

Activity  --> Entity   :wasEndedBy  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> Agent   :wasAttributedTo  

Activity  --> Communication   :qualifiedCommunication  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Entity  --> Revision   :qualifiedRevision  

Entity  --> Entity   :wasDerivedFrom  

Activity  --> Entity   :invalidated  

nf60df0426ad14108a80bb9203f5889a2b4  --> Location   :atLocation  

ActivityInfluence  --> Activity   :activity  

Insertion  --> Dictionary   :dictionary  

Activity  --> Entity   :generated  

Activity  --> End   :qualifiedEnd  

Entity  --> Entity   :hadPrimarySource  

```