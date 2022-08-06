```mermaid
	classDiagram

    
    class SKOSConceptScheme {
    
    }

    class SKOSConcept {
    
    }

    class Na3be12ec77ad490fb4755eeace32a69c {
    
    }

    class RDFList {
    
    }



SKOSConceptScheme  --> SKOSConcept   :SKOShasTopConcept  

SKOSConcept  --> SKOSConcept   :SKOSsemanticRelation  

SKOSOrderedCollection  --> RDFList   :SKOSmemberList  

SKOSConcept  --> SKOSConceptScheme   :SKOStopConceptOf  

```