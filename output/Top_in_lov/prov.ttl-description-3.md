```mermaid
	classDiagram

    
    class Entity {
    
    }

    class Activity {
    
    }

    class Dictionary {
    
    }



Entity  --> Entity   :mentionOf  

Activity  --> Entity   :wasStartedBy  

Activity  --> Entity   :used  

Entity  --> Entity   :specializationOf  

Entity  --> Activity   :wasInvalidatedBy  

Entity  --> Entity   :wasQuotedFrom  

Activity  --> Activity   :wasInformedBy  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :hadPrimarySource  

Entity  --> Entity   :alternateOf  

Activity  --> Entity   :invalidated  

Activity  --> Entity   :wasEndedBy  

Activity  --> Entity   :generated  

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

```