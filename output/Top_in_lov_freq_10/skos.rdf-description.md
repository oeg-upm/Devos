```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class Ne59e5efa04cd4796afc822af3f78ab92 {
    
    }

    class RDFList {
    
    }



SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```