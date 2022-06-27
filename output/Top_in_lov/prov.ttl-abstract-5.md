```mermaid
	classDiagram

    
    class Entity {
    
    }

    class Activity {
    
    }

    class Dictionary {
    
    }

    class Agent {
    
    }

    class Influence {
    
    }



Entity  --> Entity   :mentionOf  

Activity  --> Entity   :wasStartedBy  

Activity  --> Entity   :used  

Entity  --> Entity   :specializationOf  

Entity  --> Activity   :wasInvalidatedBy  

Activity  --> Agent   :wasAssociatedWith  

Influence  --> Activity   :hadActivity  

Entity  --> Entity   :wasQuotedFrom  

Activity  --> Activity   :wasInformedBy  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Activity   :wasGeneratedBy  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Entity   :hadPrimarySource  

Entity  --> Entity   :alternateOf  

Activity  --> Entity   :invalidated  

Activity  --> Entity   :wasEndedBy  

Activity  --> Entity   :generated  

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

```