```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class N57100002dbf0428780953b06b1db3453 {
    
    }

    class RDFList {
    
    }



SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```