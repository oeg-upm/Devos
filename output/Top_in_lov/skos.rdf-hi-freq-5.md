```mermaid
	classDiagram

    
    class SKOSConcept {
    
    }

    class SKOSConceptScheme {
    
    }

    class SKOSOrderedCollection {
    
    }

    class SKOSCollection {
    
    }

    class RDFList {
    
    }



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```