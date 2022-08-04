```mermaid
	classDiagram

    
    class Entity {
    
    }

    class Activity {
    
    }

    class Dictionary {
    
    }



Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :wasQuotedFrom  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Entity  --> Entity   :wasDerivedFrom  

Activity  --> Activity   :wasInformedBy  

Activity  --> Entity   :used  

Activity  --> Entity   :wasStartedBy  

Activity  --> Entity   :generated  

Entity  --> Entity   :alternateOf  

Entity  --> Entity   :specializationOf  

Entity  --> Entity   :hadPrimarySource  

Activity  --> Entity   :wasEndedBy  

Activity  --> Entity   :invalidated  

Entity  --> Entity   :mentionOf  

Entity  --> Activity   :wasInvalidatedBy  

```