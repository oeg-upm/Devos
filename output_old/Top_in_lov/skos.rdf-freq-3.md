```mermaid
	classDiagram

    
    class SKOSConcept {
    
    }

    class SKOSConceptScheme {
    
    }

    class SKOSOrderedCollection {
    
    }



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

```