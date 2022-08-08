```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class N51cf363f22e642cba1a56f8f0a0ef518 {
    
    }

    class RDFList {
    
    }



SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

```