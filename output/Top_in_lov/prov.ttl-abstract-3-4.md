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



Entity  --> Entity   :specializationOf  

Activity  --> Entity   :used  

Entity  --> Entity   :mentionOf  

Activity  --> Entity   :wasEndedBy  

Entity  --> Entity   :wasQuotedFrom  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Entity   :generated  

Entity  --> Entity   :wasDerivedFrom  

Activity  --> Entity   :wasStartedBy  

Entity  --> Entity   :alternateOf  

Activity  --> Agent   :wasAssociatedWith  

Entity  --> Activity   :wasInvalidatedBy  

Agent  --> Agent   :actedOnBehalfOf  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> Activity   :wasGeneratedBy  

Activity  --> Activity   :wasInformedBy  

Entity  --> Entity   :wasRevisionOf  

Activity  --> Entity   :invalidated  

Entity  --> Agent   :wasAttributedTo  

Entity  --> Entity   :hadPrimarySource  

```