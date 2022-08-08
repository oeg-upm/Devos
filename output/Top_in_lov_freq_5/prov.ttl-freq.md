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



Entity  --> Entity   :specializationOf  

Entity  --> Activity   :wasInvalidatedBy  

Insertion  --> Dictionary   :dictionary  

Activity  --> Agent   :wasAssociatedWith  

Influence  --> Activity   :hadActivity  

Entity  --> Activity   :wasGeneratedBy  

Activity  --> Communication   :qualifiedCommunication  

EntityInfluence  --> Entity   :entity  

Dictionary  --> Insertion   :qualifiedInsertion  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Quotation   :qualifiedQuotation  

Activity  --> Entity   :wasEndedBy  

Activity  --> Entity   :used  

Activity  --> Entity   :wasStartedBy  

Entity  --> Revision   :qualifiedRevision  

Agent  --> Agent   :actedOnBehalfOf  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Entity  --> Generation   :qualifiedGeneration  

Entity  --> Entity   :hadPrimarySource  

Derivation  --> Generation   :hadGeneration  

Activity  --> Association   :qualifiedAssociation  

Dictionary  --> Removal   :qualifiedRemoval  

Collection  --> Entity   :hadMember  

Entity  --> Entity   :wasRevisionOf  

Activity  --> Entity   :generated  

Activity  --> Usage   :qualifiedUsage  

Activity  --> Entity   :invalidated  

nee9980d51aa64b9095c1dc50353a304db9  --> Activity   :hadActivity  

KeyEntityPair  --> Entity   :pairEntity  

Entity  --> Entity   :wasQuotedFrom  

Activity  --> End   :qualifiedEnd  

Activity  --> Start   :qualifiedStart  

ActivityInfluence  --> Activity   :activity  

Agent  --> Delegation   :qualifiedDelegation  

Removal  --> Dictionary   :dictionary  

AgentInfluence  --> Agent   :agent  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> Invalidation   :qualifiedInvalidation  

Activity  --> Activity   :wasInformedBy  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Entity  --> Bundle   :asInBundle  

Entity  --> Entity   :mentionOf  

Entity  --> Attribution   :qualifiedAttribution  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Entity   :alternateOf  

Entity  --> Derivation   :qualifiedDerivation  

```