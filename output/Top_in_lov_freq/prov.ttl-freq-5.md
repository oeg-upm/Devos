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



Entity  --> Entity   :wasDerivedFrom  

Entity  --> Entity   :hadPrimarySource  

Entity  --> Bundle   :asInBundle  

Agent  --> Delegation   :qualifiedDelegation  

Entity  --> Entity   :mentionOf  

KeyEntityPair  --> Entity   :pairEntity  

Activity  --> Activity   :wasInformedBy  

Entity  --> Activity   :wasGeneratedBy  

Activity  --> Usage   :qualifiedUsage  

Activity  --> Entity   :invalidated  

Dictionary  --> Removal   :qualifiedRemoval  

Entity  --> Activity   :wasInvalidatedBy  

Insertion  --> Dictionary   :dictionary  

Collection  --> Entity   :hadMember  

Activity  --> Entity   :wasStartedBy  

n4d96a30ff4644cb2aaae255b06433e69b9  --> Activity   :hadActivity  

Activity  --> Communication   :qualifiedCommunication  

ActivityInfluence  --> Activity   :activity  

Activity  --> Agent   :wasAssociatedWith  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Entity  --> Attribution   :qualifiedAttribution  

Entity  --> Entity   :wasRevisionOf  

Activity  --> Association   :qualifiedAssociation  

AgentInfluence  --> Agent   :agent  

Entity  --> Revision   :qualifiedRevision  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

EntityInfluence  --> Entity   :entity  

Derivation  --> Generation   :hadGeneration  

Influence  --> Activity   :hadActivity  

Entity  --> Invalidation   :qualifiedInvalidation  

Dictionary  --> Insertion   :qualifiedInsertion  

Activity  --> Entity   :used  

Removal  --> Dictionary   :dictionary  

Entity  --> Quotation   :qualifiedQuotation  

Agent  --> Agent   :actedOnBehalfOf  

Activity  --> Entity   :generated  

Entity  --> Derivation   :qualifiedDerivation  

Entity  --> Entity   :specializationOf  

Activity  --> Entity   :wasEndedBy  

Entity  --> Entity   :wasQuotedFrom  

Activity  --> End   :qualifiedEnd  

Activity  --> Start   :qualifiedStart  

Entity  --> Generation   :qualifiedGeneration  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Entity   :alternateOf  

Entity  --> PrimarySource   :qualifiedPrimarySource  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

```