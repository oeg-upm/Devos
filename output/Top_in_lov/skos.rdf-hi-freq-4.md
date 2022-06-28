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



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```