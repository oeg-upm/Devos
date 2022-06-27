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

    class n1fe43d7349a24e3b8d5e01f1af9b52bbb35 {
    
    }

    class Activity {
    
    }

    class Attribution {
    
    }

    class Association {
    
    }

    class n1fe43d7349a24e3b8d5e01f1af9b52bbb19 {
    
    }

    class Dictionary {
    
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

    class n1fe43d7349a24e3b8d5e01f1af9b52bbb39 {
    
    }

    class End {
    
    }

    class Communication {
    
    }



Entity  --> Entity   :mentionOf  

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

n1fe43d7349a24e3b8d5e01f1af9b52bbb9  --> Activity   :hadActivity  

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

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Activity  --> Communication   :qualifiedCommunication  

Agent  --> Delegation   :qualifiedDelegation  

Entity  --> Generation   :qualifiedGeneration  

n1fe43d7349a24e3b8d5e01f1af9b52bbb19  --> Influence   :qualifiedInfluence  

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