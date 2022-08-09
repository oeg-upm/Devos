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



Removal  --> Dictionary   :dictionary  

Entity  --> Entity   :wasQuotedFrom  

Activity  --> Communication   :qualifiedCommunication  

Entity  --> Entity   :mentionOf  

Activity  --> Association   :qualifiedAssociation  

Activity  --> Entity   :used  

Entity  --> Bundle   :asInBundle  

Entity  --> Invalidation   :qualifiedInvalidation  

Entity  --> Entity   :hadPrimarySource  

Agent  --> Delegation   :qualifiedDelegation  

Activity  --> Start   :qualifiedStart  

KeyEntityPair  --> Entity   :pairEntity  

Activity  --> End   :qualifiedEnd  

Dictionary  --> Insertion   :qualifiedInsertion  

Activity  --> Activity   :wasInformedBy  

Influence  --> Activity   :hadActivity  

Entity  --> Revision   :qualifiedRevision  

Entity  --> Entity   :alternateOf  

Agent  --> Agent   :actedOnBehalfOf  

Collection  --> Entity   :hadMember  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Entity  --> Activity   :wasGeneratedBy  

n7f43746eb4f749e2ab2774032f188047b9  --> Activity   :hadActivity  

Derivation  --> Generation   :hadGeneration  

Entity  --> Entity   :specializationOf  

Entity  --> Attribution   :qualifiedAttribution  

Insertion  --> Dictionary   :dictionary  

Activity  --> Entity   :invalidated  

EntityInfluence  --> Entity   :entity  

ActivityInfluence  --> Activity   :activity  

Entity  --> Entity   :wasDerivedFrom  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> Derivation   :qualifiedDerivation  

Activity  --> Usage   :qualifiedUsage  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Entity   :wasRevisionOf  

AgentInfluence  --> Agent   :agent  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Entity  --> Activity   :wasInvalidatedBy  

Entity  --> Generation   :qualifiedGeneration  

Entity  --> Quotation   :qualifiedQuotation  

Dictionary  --> Removal   :qualifiedRemoval  

Activity  --> Entity   :generated  

Activity  --> Entity   :wasEndedBy  

Activity  --> Entity   :wasStartedBy  

```