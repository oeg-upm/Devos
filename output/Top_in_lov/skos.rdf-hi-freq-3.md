```mermaid
	classDiagram

    
    class SKOSConcept {
    
    }

    class SKOSConceptScheme {
    
    }

    class SKOSOrderedCollection {
    
    }



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```