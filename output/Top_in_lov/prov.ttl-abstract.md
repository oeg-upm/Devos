```mermaid
	classDiagram

    
    class n30e0c908f2d647788404a64fe435c30eb19 {
    
    }

    class n30e0c908f2d647788404a64fe435c30eb35 {
    
    }

    class Start {
    
    }

    class PrimarySource {
    
    }

    class Contributor {
    
    }

    class Revision {
    
    }

    class Publisher {
    
    }

    class Communication {
    
    }

    class Influence {
    
    }

    class DirectQueryService {
    
    }

    class End {
    
    }

    class Association {
    
    }

    class Derivation {
    
    }

    class Invalidation {
    
    }

    class Entity {
    
    }

    class Usage {
    
    }

    class Activity {
    
    }

    class Quotation {
    
    }

    class Agent {
    
    }

    class Delegation {
    
    }

    class Removal {
    
    }

    class n30e0c908f2d647788404a64fe435c30eb39 {
    
    }

    class Dictionary {
    
    }

    class Generation {
    
    }

    class Creator {
    
    }

    class Insertion {
    
    }

    class Publish {
    
    }

    class Modify {
    
    }

    class Attribution {
    
    }



Entity  --> Entity   :specializationOf  

Activity  --> Entity   :used  

Entity  --> Entity   :mentionOf  

Activity  --> Association   :qualifiedAssociation  

Entity  --> Derivation   :qualifiedDerivation  

Activity  --> Entity   :wasEndedBy  

Entity  --> Entity   :wasQuotedFrom  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Entity   :generated  

Agent  --> Delegation   :qualifiedDelegation  

n30e0c908f2d647788404a64fe435c30eb19  --> Influence   :qualifiedInfluence  

Entity  --> Revision   :qualifiedRevision  

Entity  --> Entity   :wasDerivedFrom  

Activity  --> Entity   :wasStartedBy  

Entity  --> Entity   :alternateOf  

Entity  --> Invalidation   :qualifiedInvalidation  

Association  --> Plan   :hadPlan  

Derivation  --> Generation   :hadGeneration  

Insertion  --> Dictionary   :dictionary  

Entity  --> Generation   :qualifiedGeneration  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> Bundle   :asInBundle  

Activity  --> Start   :qualifiedStart  

Activity  --> Usage   :qualifiedUsage  

KeyEntityPair  --> Entity   :pairEntity  

Entity  --> Quotation   :qualifiedQuotation  

Removal  --> Dictionary   :dictionary  

Influence  --> Role   :hadRole  

Entity  --> Activity   :wasInvalidatedBy  

Activity  --> Communication   :qualifiedCommunication  

Entity  --> Attribution   :qualifiedAttribution  

Agent  --> Agent   :actedOnBehalfOf  

AgentInfluence  --> Agent   :agent  

Dictionary  --> KeyEntityPair   :hadDictionaryMember  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> PrimarySource   :qualifiedPrimarySource  

n30e0c908f2d647788404a64fe435c30eb9  --> Activity   :hadActivity  

Entity  --> Activity   :wasGeneratedBy  

Activity  --> Activity   :wasInformedBy  

Influence  --> Thing   :influencer  

Dictionary  --> Removal   :qualifiedRemoval  

Derivation  --> Usage   :hadUsage  

Collection  --> Entity   :hadMember  

EntityInfluence  --> Entity   :entity  

Influence  --> Activity   :hadActivity  

Entity  --> Entity   :wasRevisionOf  

Activity  --> Entity   :invalidated  

Dictionary  --> Insertion   :qualifiedInsertion  

Entity  --> Agent   :wasAttributedTo  

Insertion  --> KeyEntityPair   :insertedKeyEntityPair  

ActivityInfluence  --> Activity   :activity  

Activity  --> End   :qualifiedEnd  

Entity  --> Entity   :hadPrimarySource  

```