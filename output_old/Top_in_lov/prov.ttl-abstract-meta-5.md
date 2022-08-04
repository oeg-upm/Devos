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



Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :hadPrimarySource  

Activity  --> Entity   :wasStartedBy  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Entity   :used  

Activity  --> Entity   :wasEndedBy  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Activity  --> Activity   :wasInformedBy  

Agent  --> Agent   :actedOnBehalfOf  

Entity  --> Entity   :specializationOf  

Activity  --> Entity   :invalidated  

Influence  --> Activity   :hadActivity  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Activity   :wasInvalidatedBy  

Entity  --> Entity   :wasQuotedFrom  

Entity  --> Entity   :alternateOf  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> Entity   :mentionOf  

Activity  --> Entity   :generated  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Entity   :wasRevisionOf  

```