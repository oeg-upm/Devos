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



Entity  --> Entity   :wasQuotedFrom  

Activity  --> Entity   :used  

Activity  --> Entity   :wasStartedBy  

Entity  --> Entity   :mentionOf  

Activity  --> Entity   :invalidated  

Entity  --> Entity   :alternateOf  

Entity  --> Agent   :wasAttributedTo  

Activity  --> Entity   :wasEndedBy  

Activity  --> Activity   :wasInformedBy  

Agent  --> Agent   :actedOnBehalfOf  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :specializationOf  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Entity   :wasRevisionOf  

Influence  --> Activity   :hadActivity  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Entity   :generated  

Entity  --> Activity   :wasInvalidatedBy  

Entity  --> Entity   :hadPrimarySource  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

```