```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class N5abfcc3bd9b945a9aa2ae7525349ff54 {
    
    }

    class RDFList {
    
    }



SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```