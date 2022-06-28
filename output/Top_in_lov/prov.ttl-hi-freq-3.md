```mermaid
	classDiagram

    
    class Entity {
    
    }

    class Activity {
    
    }

    class Dictionary {
    
    }



Entity  --> Entity   :wasQuotedFrom  

Activity  --> Entity   :used  

Activity  --> Entity   :wasStartedBy  

Entity  --> Entity   :mentionOf  

Activity  --> Entity   :invalidated  

Entity  --> Entity   :alternateOf  

Activity  --> Entity   :wasEndedBy  

Activity  --> Activity   :wasInformedBy  

Entity  --> Activity   :wasGeneratedBy  

Entity  --> Entity   :specializationOf  

Entity  --> Entity   :wasDerivedFrom  

Entity  --> Entity   :wasRevisionOf  

Dictionary  --> Dictionary   :derivedByRemovalFrom  

Activity  --> Entity   :generated  

Entity  --> Activity   :wasInvalidatedBy  

Entity  --> Entity   :hadPrimarySource  

Dictionary  --> Dictionary   :derivedByInsertionFrom  

```