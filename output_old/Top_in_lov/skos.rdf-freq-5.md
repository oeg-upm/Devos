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



SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

```